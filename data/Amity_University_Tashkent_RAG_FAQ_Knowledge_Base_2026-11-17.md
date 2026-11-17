# Amity University Tashkent — RAG-ready FAQ Knowledge Base

**Project:** RAG Chatbot for University FAQs (B.Sc. IT Minor Project)
**Scope:** Amity University in Tashkent (AUT), Uzbekistan, NOT every institution in the international Amity group.
**Research cut-off:** 2026-11-17 (Asia/Tashkent). **Language:** Answers in English with Russian query variants; LLM may translate grounded answers to Uzbek or Russian.
**Data sources:** Official AUT website pages; the separately marked NTCC section is based on user-provided university guideline files and requires local confirmation.
**Update policy:** Fees, admissions, staff, calendars, partner universities, visas and scholarship rules require fresh verification when used in future years.

## How the RAG chatbot must use this file

1. Retrieve the FAQ record and cite its `Source URL` when answering. If not supported, say information is unavailable and direct the student to the university.
2. Never invent exam dates, admission deadlines, tuition for a new academic year, dorm charges, academic timetables, GPAs, credentials, grades, scholarship eligibility decisions or government visa rules.
3. Distinguish **2025–26 full-year fees** from **programme-page per-semester figures whose effective year is not explicitly labeled**. Do not silently reconcile contradictions.
4. Treat the NTCC G-32 appendix as **uploaded guidance**, not proof that every rule automatically applies to AUT. Request supervisor confirmation for student-specific requirements.
5. Do not reveal, request or store passwords or other sensitive student records. This knowledge base contains only general information.
6. For questions asked in Russian or Uzbek, answer in that language if the retrieved source supports the answer. The `Question (RU)` alias helps multilingual retrieval.
7. Use the earliest `Source URL` as the primary citation; all links are research provenance, not a live guarantee of unchanged site content.

## Snapshot warnings and cross-source discrepancies

- **Tuition:** https://amity.uz/en/pages/view/fees explicitly labels prices as **2025–26**. The programme pages display fee-per-semester figures but do not always state an academic year. The BBA programme page lists 19.5 million UZS/semester while the 2025–26 annual table shows 35 million UZS; a new applicant should rely on their formal offer letter.
- **Admissions:** The main B.Tech CSE programme page describes Math 60% plus Aptitude 40%; the generic entry-requirements page mentions Math, Physics and Chemistry. Treat exact CSE exam subjects as **needing admissions confirmation**.
- **English equivalents:** Pages display inconsistent TOEFL ranges and CEFR labels for the same IELTS thresholds. The knowledge base intentionally uses IELTS where consistently listed and refers to an admissions officer for equivalent tests.
- **Accreditation:** Some official accreditation information refers to Amity University Uttar Pradesh/the broader Amity group. Do not interpret group accreditation as a separate verified accreditation of AUT without checking scope.
- **Counts:** Different AUT pages have shown different student-enrolment totals. No precise current student count is asserted in the FAQs.
- **Visas and dates:** Official pages and historical posts may become outdated. Do not promise legal immigration outcomes or use past exam dates as upcoming events.

## Quick reference — official 2025–26 tuition table (historical)

| Programme | Full fee UZS, 2025–26 | Source |
|---|---:|---|
| B.Sc. IT | 35,000,000 | https://amity.uz/en/pages/view/fees |
| B.Sc. Cyber Security & Blockchain | 35,000,000 | same source |
| B.Sc. AI & Data Science | 35,000,000 | same source |
| B.Tech CSE | 39,000,000 | same source |
| BBA | 35,000,000 | same source |
| BA Tourism Administration | 35,000,000 | same source |
| BA Economics | 35,000,000 | same source |
| M.Sc. IT | 30,000,000 | same source |
| International Foundation Studies | 29,000,000 | same source |

**Official programme-page semester amounts (effective academic year not shown alongside these figures):** B.Sc. IT, Cybersecurity, AI & Data Science, BA Tourism and BA Economics: 17,500,000 UZS; B.Tech CSE and BBA: 19,500,000 UZS; M.Sc. IT: 15,000,000 UZS; IFS: 14,500,000 UZS. Each is sourced in its programme FAQ record. A semester figure is not automatically a binding quote for 2026–27.

---


## 01 University identity and contacts

### FAQ-001 — What is Amity University Tashkent?

- **Question (EN):** What is Amity University Tashkent?
- **Question (RU):** Что такое Amity University Tashkent?
- **Answer (EN):** Amity University in Tashkent (AUT) is a university established in Uzbekistan in cooperation with Amity University in Noida, India. It offers career-oriented foundation, undergraduate, and postgraduate education.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/about_us

### FAQ-002 — When was Amity University Tashkent founded?

- **Question (EN):** When was Amity University Tashkent founded?
- **Question (RU):** Когда был основан Amity University Tashkent?
- **Answer (EN):** AUT was founded under Uzbekistan Presidential Resolution No. PP-4097 dated 7 January 2019; its first academic year began in 2019.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/about_us

### FAQ-003 — Where is Amity University Tashkent located?

- **Question (EN):** Where is Amity University Tashkent located?
- **Question (RU):** Где находится университет Амити в Ташкенте?
- **Answer (EN):** The campus is at 70 Labzak Street, Shaykhontohur District, Tashkent 100128, Uzbekistan.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-004 — What is the official website?

- **Question (EN):** What is the official website?
- **Question (RU):** Какой официальный сайт университета?
- **Answer (EN):** The official university website is https://amity.uz.
- **Status:** official
- **Source URL / file:** https://amity.uz/en

### FAQ-005 — What is the university email address?

- **Question (EN):** What is the university email address?
- **Question (RU):** Какой электронный адрес университета?
- **Answer (EN):** For general enquiries use info@amity.uz.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-006 — What are the main university phone numbers?

- **Question (EN):** What are the main university phone numbers?
- **Question (RU):** Какие номера телефона университета?
- **Answer (EN):** The official site lists +998 71 207 90 06 and +998 71 207 90 07. The contact page prominently lists the first number.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/site/contact ; https://amity.uz/en

### FAQ-007 — Is the Amity Tashkent diploma recognized in Uzbekistan?

- **Question (EN):** Is the Amity Tashkent diploma recognized in Uzbekistan?
- **Question (RU):** Признаётся ли диплом Amity в Узбекистане?
- **Answer (EN):** AUT says graduates receive a diploma from Amity University (India/Noida) that is recognized as a higher-education credential in Uzbekistan. Ask admissions about recognition for a specific destination country or profession.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/about_us

### FAQ-008 — What language can admissions counsellors speak?

- **Question (EN):** What language can admissions counsellors speak?
- **Question (RU):** На каких языках говорят сотрудники приёмной комиссии?
- **Answer (EN):** The admissions information describes advisers who can communicate in Uzbek, Russian, and English.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/entry_requirements

### FAQ-009 — Does AUT cooperate with employers?

- **Question (EN):** Does AUT cooperate with employers?
- **Question (RU):** Есть ли у университета партнёры среди компаний?
- **Answer (EN):** AUT describes industry-oriented curricula and partnerships with organizations; it reports more than 80 memoranda of understanding with partner organizations.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/about_us

### FAQ-010 — What is the university mission?

- **Question (EN):** What is the university mission?
- **Question (RU):** Какова миссия университета?
- **Answer (EN):** Its published mission emphasizes education, research, professional excellence, personal development, cultural awareness, and ethical values.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/mission

### FAQ-011 — What are Amity University’s core values?

- **Question (EN):** What are Amity University’s core values?
- **Question (RU):** Какие основные ценности университета?
- **Answer (EN):** The mission page names academic excellence, integrity and ethics, diversity, and mutual respect among the university’s stated values.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/mission

### FAQ-012 — Who is the Director of Amity University Tashkent?

- **Question (EN):** Who is the Director of Amity University Tashkent?
- **Question (RU):** Кто директор Amity University Tashkent?
- **Answer (EN):** The university’s leadership page lists Mr. Shukhrat Sattorov as Director. Leadership positions can change; check the current leadership page.
- **Status:** time-sensitive
- **Source URL / file:** https://amity.uz/en/lists/guides

### FAQ-013 — Is Amity accredited by WASC or QAA?

- **Question (EN):** Is Amity accredited by WASC or QAA?
- **Question (RU):** Есть ли аккредитация WASC и QAA?
- **Answer (EN):** AUT’s accreditation page references WASC and QAA. The accreditation documents concern the broader Amity institutions; do not assume this means AUT has a separate campus-specific accreditation without checking the underlying scope.
- **Status:** scope-warning
- **Source URL / file:** https://amity.uz/en/pages/view/accreditation


## 02 Programmes and degrees

### FAQ-014 — What programmes does Amity University Tashkent offer?

- **Question (EN):** What programmes does Amity University Tashkent offer?
- **Question (RU):** Какие направления есть в Amity Tashkent?
- **Answer (EN):** The official catalogue lists International Foundation Studies; B.Sc. in Information Technology; B.Sc. in Cyber Security and Blockchain; B.Sc. in Artificial Intelligence and Data Science; B.Tech. in Computer Science and Engineering; B.A. Economics; B.A. Tourism Administration; BBA; and M.Sc. in Information Technology.
- **Status:** official
- **Source URL / file:** https://amity.uz/en

### FAQ-015 — Does the university offer a foundation programme?

- **Question (EN):** Does the university offer a foundation programme?
- **Question (RU):** Есть ли Foundation программа?
- **Answer (EN):** Yes. International Foundation Studies (IFS) is a preparatory programme designed to help students develop academic and English-language skills for bachelor’s programmes.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/71

### FAQ-016 — How long is the foundation programme?

- **Question (EN):** How long is the foundation programme?
- **Question (RU):** Сколько длится Foundation?
- **Answer (EN):** IFS is shown as a one-year programme consisting of two semesters.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/71

### FAQ-017 — What is B.Sc. (IT)?

- **Question (EN):** What is B.Sc. (IT)?
- **Question (RU):** Что изучают на BSc IT?
- **Answer (EN):** B.Sc. in Information Technology covers software development and testing, programming, information databases, and networks, alongside the social and professional aspects of IT.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91

### FAQ-018 — How long is B.Sc. IT?

- **Question (EN):** How long is B.Sc. IT?
- **Question (RU):** Сколько длится бакалавриат IT?
- **Answer (EN):** The standard on-campus B.Sc. IT degree is shown as three years over six semesters. A separate international dual-degree route is also promoted.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91 ; https://amity.uz/en/pages/programme/719

### FAQ-019 — What is B.Sc. Cyber Security and Blockchain?

- **Question (EN):** What is B.Sc. Cyber Security and Blockchain?
- **Question (RU):** Что изучают на Cyber Security and Blockchain?
- **Answer (EN):** The programme covers network security, digital forensics, cryptography, ethical hacking, blockchain development and smart contracts.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/673

### FAQ-020 — How long is Cyber Security and Blockchain?

- **Question (EN):** How long is Cyber Security and Blockchain?
- **Question (RU):** Сколько учиться на Cybersecurity and Blockchain?
- **Answer (EN):** The standard campus degree is listed as three years (six semesters). There is also a dual-degree pathway.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/673 ; https://amity.uz/en/pages/programme/664

### FAQ-021 — What is B.Sc. Artificial Intelligence and Data Science?

- **Question (EN):** What is B.Sc. Artificial Intelligence and Data Science?
- **Question (RU):** Что изучают на AI & Data Science?
- **Answer (EN):** This bachelor’s programme covers programming, statistics, machine learning, deep learning, data visualization and natural-language processing.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/677

### FAQ-022 — How long is B.Sc. Artificial Intelligence and Data Science?

- **Question (EN):** How long is B.Sc. Artificial Intelligence and Data Science?
- **Question (RU):** Сколько лет длится AI & DS?
- **Answer (EN):** The regular B.Sc. AI & Data Science programme is listed as three years, or six semesters.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/677

### FAQ-023 — What is B.Tech. Computer Science and Engineering?

- **Question (EN):** What is B.Tech. Computer Science and Engineering?
- **Question (RU):** Что такое B.Tech CSE?
- **Answer (EN):** B.Tech. CSE is a four-year computer science and engineering bachelor’s programme. The university also advertises an international 2+2 route.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/696

### FAQ-024 — How long is the B.Tech CSE programme?

- **Question (EN):** How long is the B.Tech CSE programme?
- **Question (RU):** Сколько длится B.Tech CSE?
- **Answer (EN):** The on-campus degree is described as four years. The dual-degree option is presented as two years at AUT plus two abroad.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/696

### FAQ-025 — What does BA Economics teach?

- **Question (EN):** What does BA Economics teach?
- **Question (RU):** Что изучают на Economics?
- **Answer (EN):** BA Economics includes economic theory, policy, quantitative and statistical tools, analysis, and preparation for careers or further study in economics.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/97

### FAQ-026 — How long is BA Economics?

- **Question (EN):** How long is BA Economics?
- **Question (RU):** Сколько учиться на Economics?
- **Answer (EN):** The programme page lists three years and six semesters.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/97

### FAQ-027 — What does BA Tourism Administration teach?

- **Question (EN):** What does BA Tourism Administration teach?
- **Question (RU):** Что изучают на Tourism Administration?
- **Answer (EN):** The programme focuses on the tourism sector, tourism management and related professional skills. The official site describes it as a three-year undergraduate degree.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/102

### FAQ-028 — How long is the Tourism Administration degree?

- **Question (EN):** How long is the Tourism Administration degree?
- **Question (RU):** Сколько длится Tourism Administration?
- **Answer (EN):** BA Tourism Administration is listed as a three-year programme over six semesters.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/102

### FAQ-029 — Does Amity offer BBA?

- **Question (EN):** Does Amity offer BBA?
- **Question (RU):** Есть ли BBA?
- **Answer (EN):** Yes. AUT offers a Bachelor of Business Administration with a standard three-year on-campus route and advertised international dual-degree pathways.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/699

### FAQ-030 — Is there a master’s degree in information technology?

- **Question (EN):** Is there a master’s degree in information technology?
- **Question (RU):** Есть ли магистратура по IT?
- **Answer (EN):** Yes. AUT offers a Master of Science in Information Technology (M.Sc. IT).
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/112

### FAQ-031 — How long is M.Sc. IT?

- **Question (EN):** How long is M.Sc. IT?
- **Question (RU):** Сколько длится MSc IT?
- **Answer (EN):** The master’s programme is listed as two years, or four semesters.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/112

### FAQ-032 — What can I do after graduating with B.Sc. IT?

- **Question (EN):** What can I do after graduating with B.Sc. IT?
- **Question (RU):** Какая карьера после BSc IT?
- **Answer (EN):** The IT programme highlights software development, programming, web design, software testing and related freelance or business opportunities. These are career directions, not guaranteed placements.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91

### FAQ-033 — What jobs does M.Sc. IT prepare students for?

- **Question (EN):** What jobs does M.Sc. IT prepare students for?
- **Question (RU):** Где можно работать после MSc IT?
- **Answer (EN):** The M.Sc. IT page lists possible fields such as software development, systems analysis, IT project management, cloud architecture, machine learning and data analysis. These are examples rather than placement guarantees.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/112

### FAQ-034 — Where can I see the official programme structure?

- **Question (EN):** Where can I see the official programme structure?
- **Question (RU):** Где посмотреть учебный план программы?
- **Answer (EN):** Each programme’s official webpage contains a link to download its detailed programme structure. Choose your programme on amity.uz and open the corresponding download link.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91 ; https://amity.uz/en/pages/programme/696 ; https://amity.uz/en/pages/programme/112


## 03 Admissions and eligibility

### FAQ-035 — How do I apply to AUT?

- **Question (EN):** How do I apply to AUT?
- **Question (RU):** Как поступить в Amity Tashkent?
- **Answer (EN):** Create a profile in the official admission portal, complete the application, upload scanned documents and follow admission-test/interview instructions. The Admissions Committee reviews completed applications and tests.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process

### FAQ-036 — What is the domestic applicant portal?

- **Question (EN):** What is the domestic applicant portal?
- **Question (RU):** Где подать заявку гражданам Узбекистана?
- **Answer (EN):** The university links domestic applicants to https://abiturient.amity.uz.
- **Status:** official
- **Source URL / file:** https://amity.uz/en ; https://amity.uz/en/pages/view/application_process

### FAQ-037 — What is the international applicant portal?

- **Question (EN):** What is the international applicant portal?
- **Question (RU):** Куда подавать заявку иностранцам?
- **Answer (EN):** The official website links international applicants to https://admission.amity.uz.
- **Status:** official
- **Source URL / file:** https://amity.uz/en

### FAQ-038 — How do I receive admission updates?

- **Question (EN):** How do I receive admission updates?
- **Question (RU):** Где смотреть статус заявки?
- **Answer (EN):** Check the admission-system personal account regularly. The university says applicant status messages and important notices are sent through that account.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process

### FAQ-039 — What happens after the entrance tests?

- **Question (EN):** What happens after the entrance tests?
- **Question (RU):** Что происходит после вступительных экзаменов?
- **Answer (EN):** The Admissions Committee evaluates the application and assessments. Successful applicants receive an offer letter setting out the programme, start date, fees and relevant payment and refund details.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process

### FAQ-040 — How is an admission offer accepted?

- **Question (EN):** How is an admission offer accepted?
- **Question (RU):** Как принять приглашение на обучение?
- **Answer (EN):** The admission process page states that an offer can be accepted by paying the registration fee and tuition in accordance with the offer letter.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process

### FAQ-041 — What documents are required for a foundation application?

- **Question (EN):** What documents are required for a foundation application?
- **Question (RU):** Какие документы нужны для Foundation?
- **Answer (EN):** The published list includes proof of 11 or 12 years of secondary education, passport copy, 3×4 photograph and an optional IELTS certificate.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process

### FAQ-042 — What documents are required for a bachelor’s application?

- **Question (EN):** What documents are required for a bachelor’s application?
- **Question (RU):** Какие документы нужны на бакалавриат?
- **Answer (EN):** The listed documents include proof of 12 years of secondary education, passport copy, 3×4 photograph and evidence of English proficiency appropriate to the chosen programme.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process

### FAQ-043 — Can a student apply after 11 years of school?

- **Question (EN):** Can a student apply after 11 years of school?
- **Question (RU):** Можно ли поступить после 11 класса?
- **Answer (EN):** The IFS foundation page accepts completion of 11 years of secondary education; the direct bachelor’s entry pages generally specify 12 years. Ask admissions to assess individual qualifications.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/71 ; https://amity.uz/en/pages/view/entry_requirements

### FAQ-044 — What English proficiency is needed for B.Sc. IT?

- **Question (EN):** What English proficiency is needed for B.Sc. IT?
- **Question (RU):** Какой IELTS нужен для BSc IT?
- **Answer (EN):** The programme page lists IELTS 5.5 or higher (or accepted equivalent). The English requirement may be waived if the qualifying examination’s main teaching language was English.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91

### FAQ-045 — What IELTS is needed for AI & Data Science?

- **Question (EN):** What IELTS is needed for AI & Data Science?
- **Question (RU):** Какой IELTS нужен для AI & DS?
- **Answer (EN):** The official programme page lists IELTS 5.5 or higher (or accepted equivalent), with a potential English-medium exemption.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/677

### FAQ-046 — What IELTS is needed for Cyber Security and Blockchain?

- **Question (EN):** What IELTS is needed for Cyber Security and Blockchain?
- **Question (RU):** Какой IELTS нужен для Cybersecurity?
- **Answer (EN):** The programme page lists IELTS 5.5 or higher (or accepted equivalent), with possible exemption for eligible English-medium education.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/673

### FAQ-047 — What IELTS is needed for B.Tech CSE?

- **Question (EN):** What IELTS is needed for B.Tech CSE?
- **Question (RU):** Какой IELTS нужен для CSE?
- **Answer (EN):** The programme page specifies IELTS 5.5 or higher or equivalent English evidence, with a possible exemption for English-medium qualifying education.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/696

### FAQ-048 — What IELTS is needed for BBA, Economics or Tourism?

- **Question (EN):** What IELTS is needed for BBA, Economics or Tourism?
- **Question (RU):** Какой IELTS нужен для BBA, Economics и Tourism?
- **Answer (EN):** BBA, BA Economics and BA Tourism Administration programme pages list IELTS 6 or higher or accepted equivalent, with possible English-medium exemption.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/699 ; https://amity.uz/en/pages/programme/97 ; https://amity.uz/en/pages/programme/102

### FAQ-049 — What IELTS is needed for M.Sc. IT?

- **Question (EN):** What IELTS is needed for M.Sc. IT?
- **Question (RU):** Какой IELTS нужен для MSc IT?
- **Answer (EN):** The M.Sc. IT programme page lists IELTS 5.5 or higher or an accepted equivalent.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/112

### FAQ-050 — Is IELTS mandatory for Foundation Studies?

- **Question (EN):** Is IELTS mandatory for Foundation Studies?
- **Question (RU):** Нужен ли IELTS на Foundation?
- **Answer (EN):** The application document list calls IELTS optional for IFS. The IFS programme page describes an English entrance examination for applicants without an English qualification; verify the current selection process with admissions.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process ; https://amity.uz/en/pages/programme/71

### FAQ-051 — Which entrance tests are required for B.Sc. IT?

- **Question (EN):** Which entrance tests are required for B.Sc. IT?
- **Question (RU):** Какие вступительные экзамены на BSc IT?
- **Answer (EN):** The B.Sc. IT programme page describes a mathematics test (60%) and aptitude test (40%), followed by an interview.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91

### FAQ-052 — Which entrance tests are required for AI, Cybersecurity, or CSE?

- **Question (EN):** Which entrance tests are required for AI, Cybersecurity, or CSE?
- **Question (RU):** Какие экзамены на AI, Cybersecurity и CSE?
- **Answer (EN):** Their individual programme pages list mathematics (60%) and aptitude (40%) plus a personal interview. The general requirements page contains different wording for CSE, so applicants should confirm the current test syllabus with admissions.
- **Status:** conflicting-sources
- **Source URL / file:** https://amity.uz/en/pages/programme/677 ; https://amity.uz/en/pages/programme/673 ; https://amity.uz/en/pages/programme/696 ; https://amity.uz/en/pages/view/entry_requirements

### FAQ-053 — Which entrance tests are required for BBA and BA programmes?

- **Question (EN):** Which entrance tests are required for BBA and BA programmes?
- **Question (RU):** Какие экзамены на BBA, Economics, Tourism?
- **Answer (EN):** The university lists an aptitude entrance examination and personal interview for business, economics and tourism programmes.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/699 ; https://amity.uz/en/pages/programme/97 ; https://amity.uz/en/pages/programme/102

### FAQ-054 — What degrees qualify for admission to M.Sc. IT?

- **Question (EN):** What degrees qualify for admission to M.Sc. IT?
- **Question (RU):** Какой диплом нужен для MSc IT?
- **Answer (EN):** The master’s programme requires an undergraduate qualification in a relevant area such as computer science, information technology, electronics or telecommunications, with assessment and interview requirements.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/112 ; https://amity.uz/en/pages/view/application_process

### FAQ-055 — Can an English-medium student receive an IELTS exemption?

- **Question (EN):** Can an English-medium student receive an IELTS exemption?
- **Question (RU):** Можно ли поступить без IELTS после англоязычной школы?
- **Answer (EN):** Several programme pages note that an English-language condition may be waived if English was the primary language of the qualifying examination. Admission staff must determine eligibility in each case.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/programme/91 ; https://amity.uz/en/pages/programme/699

### FAQ-056 — When is the next entrance exam?

- **Question (EN):** When is the next entrance exam?
- **Question (RU):** Когда следующий вступительный экзамен?
- **Answer (EN):** No verified future entrance-test date is available in this knowledge base. The 2026 admissions announcements on the university’s official Telegram channel show historical rounds. Check the admission portal or contact the university for the next test date.
- **Status:** needs-live-confirmation
- **Source URL / file:** https://amity.uz/en ; https://t.me/s/AmityUniversityTashkent

### FAQ-057 — What is the application deadline?

- **Question (EN):** What is the application deadline?
- **Question (RU):** Какой последний срок подачи заявки?
- **Answer (EN):** A current universal application deadline is not verified here. Check your programme’s admission portal or ask the admission office; do not assume previous 2026 exam dates still apply.
- **Status:** needs-live-confirmation
- **Source URL / file:** https://amity.uz/en ; https://amity.uz/en/pages/view/application_process

### FAQ-058 — Is admission guaranteed if I meet the IELTS requirement?

- **Question (EN):** Is admission guaranteed if I meet the IELTS requirement?
- **Question (RU):** Гарантирует ли IELTS поступление?
- **Answer (EN):** No guarantee is stated. Application documents, entrance assessments, interviews and the Admissions Committee decision are part of the published process.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/application_process


## 04 Tuition, payment and refunds

### FAQ-059 — What were the annual tuition fees for 2025–26?

- **Question (EN):** What were the annual tuition fees for 2025–26?
- **Question (RU):** Какая стоимость обучения в 2025–26 году?
- **Answer (EN):** The official 2025–26 domestic-fee table lists: B.Sc. IT, Cybersecurity, AI & Data Science, BBA, BA Tourism and BA Economics — UZS 35 million; B.Tech CSE — UZS 39 million; M.Sc. IT — UZS 30 million; Foundation — UZS 29 million. These are explicitly 2025–26 figures, not verified 2026–27 quotations.
- **Status:** historical-fee
- **Source URL / file:** https://amity.uz/en/pages/view/fees

### FAQ-060 — How much does B.Sc. IT cost per semester?

- **Question (EN):** How much does B.Sc. IT cost per semester?
- **Question (RU):** Сколько стоит семестр BSc IT?
- **Answer (EN):** The B.Sc. IT programme page lists UZS 17,500,000 per semester. Confirm the amount and contract year in your offer letter.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/91

### FAQ-061 — How much does AI & Data Science cost per semester?

- **Question (EN):** How much does AI & Data Science cost per semester?
- **Question (RU):** Сколько стоит семестр AI & Data Science?
- **Answer (EN):** The AI & Data Science programme page lists UZS 17,500,000 per semester; the year of applicability is not explicitly shown beside that figure.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/677

### FAQ-062 — How much does Cyber Security and Blockchain cost per semester?

- **Question (EN):** How much does Cyber Security and Blockchain cost per semester?
- **Question (RU):** Сколько стоит семестр Cybersecurity?
- **Answer (EN):** The Cyber Security and Blockchain programme page lists UZS 17,500,000 per semester.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/673

### FAQ-063 — How much does B.Tech CSE cost per semester?

- **Question (EN):** How much does B.Tech CSE cost per semester?
- **Question (RU):** Сколько стоит семестр B.Tech CSE?
- **Answer (EN):** The B.Tech CSE programme page lists UZS 19,500,000 per semester for the Tashkent campus.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/696

### FAQ-064 — How much does BBA cost per semester?

- **Question (EN):** How much does BBA cost per semester?
- **Question (RU):** Сколько стоит семестр BBA?
- **Answer (EN):** The BBA programme page lists UZS 19,500,000 per semester, whereas the separate annual table for 2025–26 lists UZS 35 million per year. Confirm the price in the current written offer.
- **Status:** conflicting-sources
- **Source URL / file:** https://amity.uz/en/pages/programme/699 ; https://amity.uz/en/pages/view/fees

### FAQ-065 — How much does BA Economics cost per semester?

- **Question (EN):** How much does BA Economics cost per semester?
- **Question (RU):** Сколько стоит семестр Economics?
- **Answer (EN):** The BA Economics programme page lists UZS 17,500,000 per semester.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/97

### FAQ-066 — How much does BA Tourism Administration cost per semester?

- **Question (EN):** How much does BA Tourism Administration cost per semester?
- **Question (RU):** Сколько стоит семестр Tourism Administration?
- **Answer (EN):** The Tourism Administration page lists UZS 17,500,000 per semester.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/102

### FAQ-067 — How much does M.Sc. IT cost per semester?

- **Question (EN):** How much does M.Sc. IT cost per semester?
- **Question (RU):** Сколько стоит семестр MSc IT?
- **Answer (EN):** The M.Sc. IT programme page lists UZS 15,000,000 per semester.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/112

### FAQ-068 — How much does Foundation cost per semester?

- **Question (EN):** How much does Foundation cost per semester?
- **Question (RU):** Сколько стоит семестр Foundation?
- **Answer (EN):** The IFS programme page lists UZS 14,500,000 per semester.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/programme/71

### FAQ-069 — What were international fees in 2025–26?

- **Question (EN):** What were international fees in 2025–26?
- **Question (RU):** Сколько стоило обучение для иностранных студентов в 2025–26?
- **Answer (EN):** The international 2025–26 fee table lists USD 4,200 for B.Sc. IT, BBA, BA Tourism and BA Economics; USD 4,000 for Cybersecurity, AI & Data Science and M.Sc. IT; USD 4,600 for B.Tech CSE; and USD 3,700 for Foundation. Verify the applicant category and current year before payment.
- **Status:** historical-fee
- **Source URL / file:** https://amity.uz/en/pages/view/fees_int

### FAQ-070 — Are tuition fees paid each semester or each year?

- **Question (EN):** Are tuition fees paid each semester or each year?
- **Question (RU):** Оплата обучения посеместровая или годовая?
- **Answer (EN):** The official fee overview shows a 2025–26 full-fee table, while individual programme pages display per-semester figures. The offer letter defines the actual payment method and schedule for the applicant.
- **Status:** time-sensitive-fee
- **Source URL / file:** https://amity.uz/en/pages/view/fees ; https://amity.uz/en/pages/view/application_process

### FAQ-071 — What is the refund policy before the semester starts?

- **Question (EN):** What is the refund policy before the semester starts?
- **Question (RU):** Можно ли вернуть деньги до начала семестра?
- **Answer (EN):** The published refund policy states that tuition paid in advance can be refunded before semester commencement, except for the registration fee.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/fees

### FAQ-072 — What refund is available in the first 14 days?

- **Question (EN):** What refund is available in the first 14 days?
- **Question (RU):** Какой возврат оплаты в первые 14 дней?
- **Answer (EN):** According to the listed policy, a student withdrawing during the first 14 days of a semester is eligible for a 50% refund of tuition paid for that semester.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/fees

### FAQ-073 — Can tuition be refunded after the first 14 days?

- **Question (EN):** Can tuition be refunded after the first 14 days?
- **Question (RU):** Можно ли вернуть контракт после двух недель?
- **Answer (EN):** The university’s published policy says tuition and registration fees for that semester are nonrefundable after the first 14 days.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/fees

### FAQ-074 — Can tuition be fully refunded when a student visa is refused?

- **Question (EN):** Can tuition be fully refunded when a student visa is refused?
- **Question (RU):** Вернут ли деньги при отказе в визе?
- **Answer (EN):** The published policy includes unsuccessful student-visa issuance among the circumstances for a total refund. Confirm documentation and conditions directly with admissions.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/fees

### FAQ-075 — Where can I find my current tuition invoice and payment deadline?

- **Question (EN):** Where can I find my current tuition invoice and payment deadline?
- **Question (RU):** Где найти счёт и дедлайн оплаты?
- **Answer (EN):** The admission offer letter contains the programme fee, payment method and related terms. For an enrolled student, check the student-facing official channels and contact the finance or admissions office; this public corpus does not contain personal invoices.
- **Status:** personal-account-required
- **Source URL / file:** https://amity.uz/en/pages/view/application_process


## 05 Scholarships

### FAQ-076 — Does AUT offer scholarships?

- **Question (EN):** Does AUT offer scholarships?
- **Question (RU):** Есть ли стипендии в Amity?
- **Answer (EN):** Yes. AUT publishes merit-based, graduate and sibling scholarship schemes. Places are limited and criteria must be verified for the relevant year.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-077 — How much is the admission merit scholarship?

- **Question (EN):** How much is the admission merit scholarship?
- **Question (RU):** Какой размер merit scholarship?
- **Answer (EN):** The university lists a 10% admission merit scholarship for qualifying bachelor’s and master’s applicants based on high entrance-test and interview performance.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-078 — How is a merit scholarship renewed?

- **Question (EN):** How is a merit scholarship renewed?
- **Question (RU):** Как продлить академическую скидку?
- **Answer (EN):** The university says scholarships are awarded annually and then reassessed by academic performance and CGPA. The merit information references students in the top 5% by CGPA.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-079 — Can Amity graduates receive a postgraduate discount?

- **Question (EN):** Can Amity graduates receive a postgraduate discount?
- **Question (RU):** Есть ли скидка выпускникам Amity на магистратуру?
- **Answer (EN):** The Amity Graduate Awards description states that Amity undergraduate alumni may receive a 20% scholarship for postgraduate study.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-080 — Is there a sibling scholarship?

- **Question (EN):** Is there a sibling scholarship?
- **Question (RU):** Есть ли семейная скидка для братьев или сестёр?
- **Answer (EN):** The site describes a 10% scholarship for a second sibling enrolling at AUT.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-081 — Where are the detailed scholarship rules?

- **Question (EN):** Where are the detailed scholarship rules?
- **Question (RU):** Где найти правила scholarship?
- **Answer (EN):** The scholarship page directs students to the “Scholarships, Award & Medals” guidelines section in AMIZONE for detailed rules.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-082 — Is every qualified applicant automatically given a scholarship?

- **Question (EN):** Is every qualified applicant automatically given a scholarship?
- **Question (RU):** Получает ли каждый абитуриент scholarship?
- **Answer (EN):** No. The university states that scholarship places are limited and eligibility depends on performance and programme conditions.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships


## 06 Campus facilities and student life

### FAQ-083 — Does AUT have a library?

- **Question (EN):** Does AUT have a library?
- **Question (RU):** Есть ли библиотека в университете?
- **Answer (EN):** Yes. AUT has a campus library described as supporting about 200 readers at once, with a collection exceeding 10,000 books and other resources.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/library

### FAQ-084 — Can I study quietly in the library?

- **Question (EN):** Can I study quietly in the library?
- **Question (RU):** Можно ли учиться в читальном зале?
- **Answer (EN):** The library is described as offering quiet reading and study space for students.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/library

### FAQ-085 — Does AUT have a dormitory?

- **Question (EN):** Does AUT have a dormitory?
- **Question (RU):** Есть ли общежитие у Amity?
- **Answer (EN):** Yes. The university describes a furnished student dormitory on its campus with rooms designed for two students and indoor fitness facilities.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/hostel

### FAQ-086 — How many students share a dormitory room?

- **Question (EN):** How many students share a dormitory room?
- **Question (RU):** На сколько человек комнаты в общежитии?
- **Answer (EN):** The campus housing page describes rooms for two students.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/hostel

### FAQ-087 — How much is the dormitory?

- **Question (EN):** How much is the dormitory?
- **Question (RU):** Сколько стоит общежитие Amity?
- **Answer (EN):** A verified dormitory price is not published in the checked official dormitory page. Please ask the housing office or main university contact for current rates and availability.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/pages/view/hostel ; https://amity.uz/en/site/contact

### FAQ-088 — Does the campus have a cafeteria?

- **Question (EN):** Does the campus have a cafeteria?
- **Question (RU):** Есть ли столовая?
- **Answer (EN):** Yes. The official site describes a modern 200-seat cafeteria serving Uzbek/ethnic, Indian and continental food options.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/cafeteria

### FAQ-089 — What are the cafeteria prices and hours?

- **Question (EN):** What are the cafeteria prices and hours?
- **Question (RU):** Какие цены и часы работы столовой?
- **Answer (EN):** The university calls its cafeteria student-affordable and describes broad access, but this corpus does not verify a current menu, price list, or daily operating schedule.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/pages/view/cafeteria

### FAQ-090 — Are sports facilities available?

- **Question (EN):** Are sports facilities available?
- **Question (RU):** Есть ли спортзал и спортивные площадки?
- **Answer (EN):** Yes. The university describes basketball, football, volleyball and tennis facilities, plus table-tennis halls.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/sports_facilities

### FAQ-091 — Are sports facilities free?

- **Question (EN):** Are sports facilities free?
- **Question (RU):** Бесплатные ли спортивные секции?
- **Answer (EN):** The university states that students can use its sports sections free of charge.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/sports_facilities

### FAQ-092 — Does the university have a medical station?

- **Question (EN):** Does the university have a medical station?
- **Question (RU):** Есть ли медпункт в университете?
- **Answer (EN):** Yes. AUT describes an on-campus medical station for basic first-line student health support.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/medical_center

### FAQ-093 — What student clubs exist?

- **Question (EN):** What student clubs exist?
- **Question (RU):** Какие есть студенческие клубы?
- **Answer (EN):** The official club list includes Zakovat, Literature, Sports, Amity Computer & Science, Press, Movie, Cybersports, Art & Culture, Helping Hands, Travel & Adventure and Business.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/clubs

### FAQ-094 — Is there a computer science club?

- **Question (EN):** Is there a computer science club?
- **Question (RU):** Есть ли Computer Science Club?
- **Answer (EN):** Yes. The Amity Computer & Science Club describes seminars, coding competitions, research projects, hackathons and links with professionals.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/clubs

### FAQ-095 — Can students participate in volunteering?

- **Question (EN):** Can students participate in volunteering?
- **Question (RU):** Есть ли волонтёрский клуб?
- **Answer (EN):** The Helping Hands Club supports volunteering, community assistance and charity activities.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/clubs

### FAQ-096 — Does AUT have esports activities?

- **Question (EN):** Does AUT have esports activities?
- **Question (RU):** Есть ли киберспорт в Amity?
- **Answer (EN):** The published clubs directory lists a Cybersports Club that aims to organize tournaments and develop competitive gaming.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/clubs

### FAQ-097 — How do I join a student club?

- **Question (EN):** How do I join a student club?
- **Question (RU):** Как вступить в студенческий клуб?
- **Answer (EN):** Review the university club directory and contact the club’s representative or published Telegram link if available. The page does not describe one universal registration procedure.
- **Status:** procedural-details-not-public
- **Source URL / file:** https://amity.uz/en/pages/view/clubs

### FAQ-098 — What is the Incubation Centre?

- **Question (EN):** What is the Incubation Centre?
- **Question (RU):** Что такое Incubation Centre?
- **Answer (EN):** It is a university facility intended to help student entrepreneurs develop businesses through mentoring, training, networking and assistance locating funding opportunities.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/incubation_centre

### FAQ-099 — Who can apply to the Incubation Centre?

- **Question (EN):** Who can apply to the Incubation Centre?
- **Question (RU):** Кто может подать заявку в инкубатор?
- **Answer (EN):** The centre states that AUT students with a business idea can apply through a competitive selection process.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/incubation_centre


## 07 Careers and international opportunities

### FAQ-100 — Does AUT have a Career Center?

- **Question (EN):** Does AUT have a Career Center?
- **Question (RU):** Есть ли карьерный центр?
- **Answer (EN):** Yes. The Career Centre provides career advice and helps students prepare for job searches and internships.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/career_center

### FAQ-101 — What services does the Career Center provide?

- **Question (EN):** What services does the Career Center provide?
- **Question (RU):** Какие услуги оказывает Career Center?
- **Answer (EN):** Its published services include career counselling, job and internship search assistance, career events, CV preparation, interview training and networking.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/career_center

### FAQ-102 — How can I contact the Career Center?

- **Question (EN):** How can I contact the Career Center?
- **Question (RU):** Как связаться с Career Center?
- **Answer (EN):** The official Career Centre page lists +998 71 207 9005 and partnership@amity.uz.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/career_center

### FAQ-103 — Are internships and jobs guaranteed?

- **Question (EN):** Are internships and jobs guaranteed?
- **Question (RU):** Гарантируется ли стажировка или работа после выпуска?
- **Answer (EN):** The Career Center advertises assistance, employer connections and events; the checked page does not promise a job or internship to every student.
- **Status:** not-a-guarantee
- **Source URL / file:** https://amity.uz/en/pages/view/career_center

### FAQ-104 — What is the Study Abroad Program?

- **Question (EN):** What is the Study Abroad Program?
- **Question (RU):** Что такое Study Abroad Program?
- **Answer (EN):** The university describes a short Study Abroad Program that provides selected students with approximately two weeks of learning and cultural exposure at Amity’s overseas campuses.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/study_abroad_program

### FAQ-105 — What is the Semester Abroad Programme?

- **Question (EN):** What is the Semester Abroad Programme?
- **Question (RU):** Что такое Semester Abroad Programme?
- **Answer (EN):** The Semester Abroad Programme is an option for a semester of overseas academic experience. The university says it is offered in the third semester of bachelor’s studies, subject to programme announcements.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/semester_abroad_program

### FAQ-106 — Which destinations are mentioned for Semester Abroad?

- **Question (EN):** Which destinations are mentioned for Semester Abroad?
- **Question (RU):** В какие страны можно поехать по Semester Abroad?
- **Answer (EN):** The university lists destinations such as Dubai, Singapore, London, Australia, Canada and France. Locations and availability are announced for each semester.
- **Status:** time-sensitive
- **Source URL / file:** https://amity.uz/en/pages/view/semester_abroad_program

### FAQ-107 — Can I complete part of a bachelor’s degree abroad?

- **Question (EN):** Can I complete part of a bachelor’s degree abroad?
- **Question (RU):** Можно ли часть бакалавриата учиться за границей?
- **Answer (EN):** Yes. AUT advertises dual-degree international pathways for selected degrees, including B.Sc. IT, Cyber Security, AI & Data Science, B.Tech CSE and BBA. Conditions depend on the partner university.
- **Status:** official
- **Source URL / file:** https://amity.uz/en ; https://amity.uz/en/pages/programme/719 ; https://amity.uz/en/pages/programme/696 ; https://amity.uz/en/pages/programme/699

### FAQ-108 — What is the dual-degree route for B.Sc IT?

- **Question (EN):** What is the dual-degree route for B.Sc IT?
- **Question (RU):** Как работает двойной диплом BSc IT?
- **Answer (EN):** The dual-degree IT page describes a 2+2 route, with study in Tashkent and at a foreign partner institution. Exact admission, visa, transfer, degree-award and partner costs must be confirmed with AUT.
- **Status:** time-sensitive
- **Source URL / file:** https://amity.uz/en/pages/programme/719

### FAQ-109 — What foreign partners are named for IT dual degree?

- **Question (EN):** What foreign partners are named for IT dual degree?
- **Question (RU):** Какой зарубежный партнёр у IT dual degree?
- **Answer (EN):** The B.Sc. IT dual-degree page names the University of Melbourne in Australia as a partner option. Confirm current availability, entry conditions and fees before applying.
- **Status:** time-sensitive
- **Source URL / file:** https://amity.uz/en/pages/programme/719

### FAQ-110 — What is the international route for B.Tech CSE?

- **Question (EN):** What is the international route for B.Tech CSE?
- **Question (RU):** Есть ли зарубежная программа для B.Tech CSE?
- **Answer (EN):** The university advertises a 2+2 model with international options including Illinois Institute of Technology (USA) and University of Birmingham (UK). Separate foreign tuition rates may apply.
- **Status:** time-sensitive
- **Source URL / file:** https://amity.uz/en/pages/programme/696

### FAQ-111 — What international route is listed for BBA?

- **Question (EN):** What international route is listed for BBA?
- **Question (RU):** Есть ли двойной диплом BBA?
- **Answer (EN):** The BBA page advertises 1+2, 1+3 and 2+2 pathway formats, with options in the USA and UK. The correct duration, partner and tuition must be confirmed with admissions.
- **Status:** time-sensitive
- **Source URL / file:** https://amity.uz/en/pages/programme/699

### FAQ-112 — Does Amity hold sports competitions?

- **Question (EN):** Does Amity hold sports competitions?
- **Question (RU):** Проводятся ли спортивные соревнования?
- **Answer (EN):** The university describes student sports competitions and Sangathan, an Amity-wide annual sporting and cultural event.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/sports_facilities ; https://amity.uz/en/pages/view/study_abroad_program


## 08 Transfers and international students

### FAQ-113 — Can I transfer to AUT from another university?

- **Question (EN):** Can I transfer to AUT from another university?
- **Question (RU):** Можно ли перевестись из другого университета?
- **Answer (EN):** The university publishes a credit-transfer process for applicants from other recognized institutions. Equivalence depends on programme fit, accreditation, grades and committee review.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/transfer_to_amity

### FAQ-114 — Which grades are considered for transfer credit?

- **Question (EN):** Which grades are considered for transfer credit?
- **Question (RU):** Какие оценки нужны для перевода кредитов?
- **Answer (EN):** The stated transfer policy normally considers comparable courses completed with a satisfactory grade of C or better at an accredited institution.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/transfer_to_amity

### FAQ-115 — Are unofficial transcripts accepted for credit transfer?

- **Question (EN):** Are unofficial transcripts accepted for credit transfer?
- **Question (RU):** Можно ли перевестись по неофициальной выписке?
- **Answer (EN):** The policy requires official transcripts from the previous institution and says copies/facsimiles are not accepted for the formal credit-transfer decision.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/transfer_to_amity

### FAQ-116 — Who approves transfer-credit equivalence?

- **Question (EN):** Who approves transfer-credit equivalence?
- **Question (RU):** Кто подтверждает предметы при переводе?
- **Answer (EN):** AUT describes evaluation by admissions/academic officials and its Equivalence Committee, based on comparability of course work.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/transfer_to_amity

### FAQ-117 — Can online courses automatically be transferred for credit?

- **Question (EN):** Can online courses automatically be transferred for credit?
- **Question (RU):** Засчитываются ли онлайн курсы автоматически?
- **Answer (EN):** The published transfer policy lists categories of online, correspondence and independent-study courses among examples that may not receive non-resident credit. Ask the Equivalence Committee about a specific course.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/transfer_to_amity

### FAQ-118 — Does AUT accept international students?

- **Question (EN):** Does AUT accept international students?
- **Question (RU):** Могут ли иностранцы поступить в Amity?
- **Answer (EN):** Yes. AUT has an international application path and publishes visa/arrival guidance for international applicants.
- **Status:** official
- **Source URL / file:** https://amity.uz/en ; https://amity.uz/en/pages/view/visa_and_arrival

### FAQ-119 — Do international students need a visa?

- **Question (EN):** Do international students need a visa?
- **Question (RU):** Нужна ли виза иностранным студентам?
- **Answer (EN):** Visa requirements depend on citizenship and current Uzbek rules. AUT publishes a visa guidance page and application steps, but students should confirm current requirements with the Uzbekistan embassy/consulate and AUT before travel.
- **Status:** immigration-live-verification
- **Source URL / file:** https://amity.uz/en/pages/view/visa_and_arrival

### FAQ-120 — Where can I read about student visa and arrival?

- **Question (EN):** Where can I read about student visa and arrival?
- **Question (RU):** Где узнать о визе и приезде?
- **Answer (EN):** Start with AUT’s Visa and Arrival page and confirm the latest requirements using Uzbek government or consular sources. AUT also links a visa application form.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/visa_and_arrival

### FAQ-121 — Does AUT assist newly arrived international students?

- **Question (EN):** Does AUT assist newly arrived international students?
- **Question (RU):** Помогает ли Amity иностранным студентам адаптироваться?
- **Answer (EN):** The university describes student mentorship and a Student Services Centre that can guide international students settling in Tashkent.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/visa_and_arrival


## 09 Student administration and information gaps

### FAQ-122 — What is AMIZONE?

- **Question (EN):** What is AMIZONE?
- **Question (RU):** Что такое AMIZONE?
- **Answer (EN):** The AUT scholarship page identifies AMIZONE as the student intranet portal where detailed scholarship guidelines are available. For account-specific services, follow instructions from the university; this corpus does not contain private student credentials.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-123 — Where can I see the academic calendar?

- **Question (EN):** Where can I see the academic calendar?
- **Question (RU):** Где найти академический календарь?
- **Answer (EN):** A current official academic-calendar schedule for each AUT programme has not been verified in this public corpus. Ask your programme office or check authenticated university student resources.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-124 — When does my semester start or end?

- **Question (EN):** When does my semester start or end?
- **Question (RU):** Когда начинается и заканчивается семестр?
- **Answer (EN):** Semester dates depend on programme and academic year. This corpus cannot verify an individual student’s start/end dates; use an official academic calendar or ask your programme office.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-125 — What is my classroom or timetable?

- **Question (EN):** What is my classroom or timetable?
- **Question (RU):** Как узнать расписание и аудиторию?
- **Answer (EN):** Class and room schedules are student-specific and are not part of this public FAQ corpus. Use the university’s approved student timetable resource or contact your faculty office.
- **Status:** personal-account-required
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-126 — How many absences are permitted?

- **Question (EN):** How many absences are permitted?
- **Question (RU):** Сколько занятий можно пропустить?
- **Answer (EN):** A confirmed attendance threshold for AUT is not documented in the checked local public pages. Do not apply thresholds from other Amity campuses automatically. Verify the current AUT course handbook and faculty guidance.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-127 — How do I check grades or CGPA?

- **Question (EN):** How do I check grades or CGPA?
- **Question (RU):** Где смотреть оценки и CGPA?
- **Answer (EN):** Grades and CGPA are individual academic records. Use the university’s official authenticated student service or contact the programme administration; this knowledge base contains no student data.
- **Status:** personal-account-required
- **Source URL / file:** https://amity.uz/en/pages/view/scholarships

### FAQ-128 — What is the passing grade?

- **Question (EN):** What is the passing grade?
- **Question (RU):** Какой минимальный балл для зачёта?
- **Answer (EN):** This corpus does not verify a universal AUT passing mark across programmes and batches. Check your course’s official assessment scheme or ask the responsible faculty member.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-129 — How can I get an academic transcript?

- **Question (EN):** How can I get an academic transcript?
- **Question (RU):** Как получить транскрипт?
- **Answer (EN):** The public sources checked do not specify the current transcript request procedure for AUT. Contact the academic/registrar office through the official university channels.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-130 — How can I reset my university password?

- **Question (EN):** How can I reset my university password?
- **Question (RU):** Как восстановить пароль AMIZONE?
- **Answer (EN):** Password-reset instructions were not verified in the public corpus. Use the official sign-in help service or the university IT support team; never share your password with the FAQ chatbot.
- **Status:** not-publicly-confirmed
- **Source URL / file:** https://amity.uz/en/site/contact

### FAQ-131 — Who should I contact for an official policy clarification?

- **Question (EN):** Who should I contact for an official policy clarification?
- **Question (RU):** К кому обратиться за подтверждением правил?
- **Answer (EN):** Contact AUT through info@amity.uz or the official call centre, or ask the relevant faculty/administrative office for a written policy applicable to your programme and academic year.
- **Status:** official
- **Source URL / file:** https://amity.uz/en/site/contact


## 10 NTCC guidance (uploaded G-32; verify local applicability)

### FAQ-132 — What is an NTCC or SIL course?

- **Question (EN):** What is an NTCC or SIL course?
- **Question (RU):** Что такое NTCC или SIL?
- **Answer (EN):** In the supplied G-32 guidelines, Non-Teaching Credit Courses / Supervised Independent Learning are independent, application-oriented, supervised learning activities rather than standard lectures. Local course details should be confirmed with the AUT faculty guide.
- **Status:** uploaded-guideline-confirm-local
- **Source URL / file:** User-uploaded document: NTCC guidelines.pdf (G-32; esp. pp. 5, 8, 12, 14)

### FAQ-133 — What is a Minor Project?

- **Question (EN):** What is a Minor Project?
- **Question (RU):** Что такое Minor Project в NTCC?
- **Answer (EN):** The supplied G-32 schedule groups Minor Projects under 2–6 credit units, depending on course-specific allocation. This range does not determine the exact credit count for an individual AUT student.
- **Status:** uploaded-guideline-confirm-local
- **Source URL / file:** User-uploaded document: NTCC guidelines.pdf (G-32; esp. pp. 5, 8, 12, 14)

### FAQ-134 — What is WPR?

- **Question (EN):** What is WPR?
- **Question (RU):** Что такое WPR?
- **Answer (EN):** WPR means Weekly Progress Report. The provided AUT 2026–27 WPR form asks for Target of Week, Achievement of Week and Future Work Plan, along with programme and student fields and signatures.
- **Status:** user-uploaded-template
- **Source URL / file:** User-uploaded document: WPR Format.docx (AUT NTCC Fall 2026–27 form)

### FAQ-135 — What should an NTCC final report contain?

- **Question (EN):** What should an NTCC final report contain?
- **Question (RU):** Что входит в Final Project Report?
- **Answer (EN):** The supplied G-32 report-writing excerpt calls for preliminary pages (title, declaration, supervisor approval, acknowledgements, contents and abstract), main chapters, references and appendices. The precise report length depends on credit units and local instructions.
- **Status:** uploaded-guideline-confirm-local
- **Source URL / file:** User-uploaded document: project writing.pdf (G-32 report format)

### FAQ-136 — What does the G-32 report format say about language and layout?

- **Question (EN):** What does the G-32 report format say about language and layout?
- **Question (RU):** Какие требования к оформлению NTCC отчёта?
- **Answer (EN):** The supplied excerpt specifies English by default, A4 paper, justified paragraphs, 1.5 line spacing, 1.25-inch left/right margins and 1-inch top/bottom margins. Confirm local AUT requirements.
- **Status:** uploaded-guideline-confirm-local
- **Source URL / file:** User-uploaded document: project writing.pdf (G-32 report format)

### FAQ-137 — What similarity index is stated in the supplied NTCC guideline?

- **Question (EN):** What similarity index is stated in the supplied NTCC guideline?
- **Question (RU):** Какой допустимый процент плагиата в NTCC?
- **Answer (EN):** The supplied G-32 guideline calls for a plagiarism check and a similarity index not exceeding 15%, alongside proper citations. Confirm which system and local policy your AUT supervisor applies.
- **Status:** uploaded-guideline-confirm-local
- **Source URL / file:** User-uploaded document: NTCC guidelines.pdf (G-32; esp. pp. 5, 8, 12, 14)

### FAQ-138 — Do I have to submit WPRs regularly?

- **Question (EN):** Do I have to submit WPRs regularly?
- **Question (RU):** Нужно ли сдавать WPR каждую неделю?
- **Answer (EN):** The supplied G-32 guidance requires regular Weekly Progress Reports and a work diary under faculty supervision. Confirm the exact submission day and deadline for your AUT class.
- **Status:** uploaded-guideline-confirm-local
- **Source URL / file:** User-uploaded document: NTCC guidelines.pdf (G-32; esp. pp. 5, 8, 12, 14)


---

## Complete official source directory

- **ABOUT:** https://amity.uz/en/pages/view/about_us
- **HOME:** https://amity.uz/en
- **CONTACT:** https://amity.uz/en/site/contact
- **APPLY:** https://amity.uz/en/pages/view/application_process
- **ENTRY:** https://amity.uz/en/pages/view/entry_requirements
- **FOUNDATION:** https://amity.uz/en/pages/programme/71
- **IT:** https://amity.uz/en/pages/programme/91
- **CYBER:** https://amity.uz/en/pages/programme/673
- **AI:** https://amity.uz/en/pages/programme/677
- **CSE:** https://amity.uz/en/pages/programme/696
- **BBA:** https://amity.uz/en/pages/programme/699
- **ECON:** https://amity.uz/en/pages/programme/97
- **TOURISM:** https://amity.uz/en/pages/programme/102
- **MSC:** https://amity.uz/en/pages/programme/112
- **FEES:** https://amity.uz/en/pages/view/fees
- **FEES_INT:** https://amity.uz/en/pages/view/fees_int
- **SCHOLAR:** https://amity.uz/en/pages/view/scholarships
- **TRANSFER:** https://amity.uz/en/pages/view/transfer_to_amity
- **VISA:** https://amity.uz/en/pages/view/visa_and_arrival
- **LIBRARY:** https://amity.uz/en/pages/view/library
- **DORM:** https://amity.uz/en/pages/view/hostel
- **CAFE:** https://amity.uz/en/pages/view/cafeteria
- **SPORT:** https://amity.uz/en/pages/view/sports_facilities
- **MEDICAL:** https://amity.uz/en/pages/view/medical_center
- **CLUBS:** https://amity.uz/en/pages/view/clubs
- **CAREER:** https://amity.uz/en/pages/view/career_center
- **INCUB:** https://amity.uz/en/pages/view/incubation_centre
- **SAP:** https://amity.uz/en/pages/view/study_abroad_program
- **SEM_ABROAD:** https://amity.uz/en/pages/view/semester_abroad_program
- **MISSION:** https://amity.uz/en/pages/mission
- **ACCRED:** https://amity.uz/en/pages/view/accreditation
- **LEAD:** https://amity.uz/en/lists/guides
- **DUAL_IT:** https://amity.uz/en/pages/programme/719
- **DUAL_CYBER:** https://amity.uz/en/pages/programme/664
- **DUAL_AI:** https://amity.uz/en/pages/programme/716
- **PORTAL_DOM:** https://abiturient.amity.uz
- **PORTAL_INT:** https://admission.amity.uz
- **TELEGRAM:** https://t.me/s/AmityUniversityTashkent

## Out-of-scope, private or currently unverified requests

- Exact personal class schedule, attendance, grades, tuition invoices, payment status, exam marks, transcript access and account passwords require a secure student portal or authorised staff. This file cannot access them.
- Current admission deadlines, the next entrance test, 2026–27 tuition confirmation, visa/immigration rules, dormitory price and availability, student ID issuance, exact attendance minimum and pass marks must be verified through official university channels.
- When evidence conflicts, reply with both source-specific versions and recommend checking the latest official offer or academic office, rather than presenting one as certain.

**University contact:** info@amity.uz | +998 71 207 90 06 | +998 71 207 90 07 | 70 Labzak Street, Tashkent, Uzbekistan.

**Maintainer note:** This is a curated, non-exhaustive public knowledge base for educational demonstration. Update it before production deployment; it is not an official university publication.
