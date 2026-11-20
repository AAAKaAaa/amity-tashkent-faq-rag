# Как запустить чатбот Amity Tashkent FAQ

Нужны: Python 3.10+ и ключ Anthropic API (https://console.anthropic.com → API Keys).

1. Распакуйте архив и откройте Terminal в папке проекта:
   ```bash
   cd путь/к/папке/NTCC
   ```
2. Установите зависимости (один раз, ~2 ГБ):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. Создайте файл с ключом:
   ```bash
   cp .env.example .env
   ```
   Откройте `.env` и замените `sk-ant-...` на свой ключ.
4. Запустите:
   ```bash
   streamlit run app.py
   ```
   Откроется http://localhost:8501. Остановить — Ctrl + C.

При первом запуске скачиваются модели: эмбеддинги (~470 МБ) и, при первом голосовом
вопросе, Whisper (~1,6 ГБ). Индекс FAISS уже лежит в архиве; после изменения файлов в
`data/` пересоберите его командой `python ingest.py`.

Проверка качества поиска: `python eval/run_eval.py`.
