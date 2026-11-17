"""Local speech-to-text with Whisper (Hugging Face transformers), no API key needed."""

from __future__ import annotations

import io
import wave
from functools import lru_cache

import numpy as np
import torch
from transformers import pipeline

import config

# Whisper language names for the UI languages.
WHISPER_LANG = {"en": "english", "ru": "russian", "uz": "uzbek"}


@lru_cache(maxsize=1)
def get_transcriber():
    device = "mps" if torch.backends.mps.is_available() else "cpu"
    return pipeline(
        "automatic-speech-recognition",
        model=config.STT_MODEL,
        device=device,
        dtype=torch.float16 if device == "mps" else torch.float32,
    )


def read_wav(data: bytes) -> tuple[np.ndarray, int]:
    """Decode 16-bit PCM WAV (what Streamlit's recorder produces) to mono float32."""
    with wave.open(io.BytesIO(data)) as w:
        rate, channels, width = w.getframerate(), w.getnchannels(), w.getsampwidth()
        frames = w.readframes(w.getnframes())
    if width != 2:
        raise ValueError(f"Unsupported WAV sample width: {width * 8} bit")
    audio = np.frombuffer(frames, dtype=np.int16).astype(np.float32) / 32768.0
    if channels > 1:
        audio = audio.reshape(-1, channels).mean(axis=1)
    return audio, rate


def transcribe(data: bytes, lang: str | None = None) -> str:
    """Transcribe WAV bytes. `lang` ("en"/"ru"/"uz") hints Whisper; None = auto-detect."""
    audio, rate = read_wav(data)
    if audio.size < rate * 0.3:  # under 0.3 s — nothing said
        return ""
    gen = {"task": "transcribe"}
    if lang in WHISPER_LANG:
        gen["language"] = WHISPER_LANG[lang]
    out = get_transcriber()(
        {"raw": audio, "sampling_rate": rate}, generate_kwargs=gen, return_timestamps=True
    )
    return out["text"].strip()
