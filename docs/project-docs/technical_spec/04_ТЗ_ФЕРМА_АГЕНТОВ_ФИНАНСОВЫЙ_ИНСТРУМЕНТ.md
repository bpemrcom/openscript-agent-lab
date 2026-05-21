# 04. ТЗ: Ферма агентов с финансовым инструментом

Версия: `v0.1`  
Назначение: техническое задание для учебного проекта OpenScript Agent Lab.  
Кто читает: ChatGPT-наставник и Codex-исполнитель.  
Для кого проект: ученик без опыта программирования, который работает через ChatGPT, Codex и сервер.

---

## 1. Главная идея проекта

Проект должен научить человека не классическому программированию, а новому рабочему циклу разработки:

```text
ученик → ChatGPT-наставник → Codex-исполнитель → сервер → git → проверка результата
```

Ученик не обязан знать Python, Linux, git, SSH, API, Telegram Bot API, Hermes или устройство баз данных.  
ChatGPT объясняет всё простым русским языком по ходу работы.  
Codex выполняет технические шаги на сервере.  
Ученик копирует prompt, вставляет его в Codex, получает отчёт и возвращает отчёт в ChatGPT.

Итог первого проекта:

```text
маленькая ферма агентов + Telegram-общение + финансовый инструмент + текст/фото/голос + запись в БД
```

---

## 2. Что должно получиться в конце

К концу проекта у ученика должно быть:

1. свой сервер;
2. свой git-проект;
3. документация проекта внутри git;
4. общий публичный student-kit repo как источник учебных документов;
5. установленное/подключённое расширение с правилами для ChatGPT;
6. страница визуального просмотра структуры проекта;
7. каркас OpenScript Agent Lab;
8. Hermes как обязательный runtime для агентов;
9. формат agent package;
10. UI фабрики агентов;
11. первый агент, созданный через UI и применённый в Hermes;
12. Telegram как первый внешний канал общения с агентом;
13. tool registry;
14. финансовый инструмент как первый бизнес-инструмент;
15. текстовый расход через Telegram с записью в SQLite;
16. обработка фото чека: черновик → подтверждение → запись в БД;
17. обработка голоса: голос → текст → тот же путь, что обычное сообщение;
18. второй агент, чтобы доказать, что это ферма, а не один hardcoded bot;
19. финальная проверка;
20. обновлённая документация проекта.

---

## 3. Главные роли в учебном процессе

### 3.1. Ученик

Ученик:

- открывает браузер;
- загружает стартовые документы в ChatGPT;
- устанавливает расширение;
- копирует prompt из ChatGPT;
- вставляет prompt в Codex;
- ждёт отчёт Codex;
- присылает отчёт обратно в ChatGPT;
- иногда вставляет документы агента через UI;
- проверяет результат глазами.

Ученик не должен:

- самостоятельно редактировать код;
- сам разбираться в логах;
- сам писать команды;
- сам искать, какой файл менять;
- сам решать архитектуру;
- открывать `localhost`, если проект живёт на сервере.

---

### 3.2. ChatGPT-наставник

ChatGPT:

- читает стартовые документы;
- объясняет ученику следующий шаг простыми словами;
- критически проверяет предложения ученика;
- не соглашается автоматически;
- пишет один полный prompt для Codex;
- проверяет отчёт Codex;
- решает, можно ли идти дальше;
- следит за документацией;
- следит, чтобы не было `localhost`;
- следит, чтобы агент работал через Hermes;
- не допускает fake/template успех.

ChatGPT не должен:

- давать много шагов сразу;
- говорить сложным языком без объяснения;
- просить ученика “самому разобраться”;
- пропускать проверку отчёта;
- начинать разработку без git и документации;
- путать общий student-kit repo и личный проект ученика.

---

### 3.3. Codex-исполнитель

Codex:

- работает на сервере;
- получает точный prompt от ChatGPT;
- выполняет одну задачу за run;
- не проектирует архитектуру сам;
- не читает и не печатает секреты;
- возвращает отчёт между `CHATGPT_REPORT_BEGIN` и `CHATGPT_REPORT_END`;
- делает commit/push, если это разрешено задачей;
- останавливается со `STOP`, если не хватает фактов.

Codex не должен:

- делать несколько задач сразу;
- обходить Hermes;
- делать fake/template reply и называть это агентом;
- читать `.env`, токены, приватные ключи, auth files;
- менять runtime как source of truth;
- пушить unrelated dirty files.

---

## 4. Общий student-kit repo

### 4.1. Назначение

Общий публичный repo нужен, чтобы все ученики брали один и тот же учебный комплект.

Repo:

```text
https://github.com/MaksimUnimax/openscript-agent-lab-student-kit.git
```

SSH alias для записи с нашего сервера:

```text
git@github.com-student-kit:MaksimUnimax/openscript-agent-lab-student-kit.git
```

Этот repo не является личным проектом ученика.  
Это общий комплект учебных документов.

---

### 4.2. Что лежит в student-kit repo

Ожидаемая структура:

```text
README.md
START_HERE.md

chatgpt/
  README.md
  01_ИНСТРУКЦИЯ_ДЛЯ_CHATGPT.md
  02_СТАРТ_ПРОЕКТА_GIT_ДОКУМЕНТАЦИЯ_СТРУКТУРА.md

roadmap/
  README.md
  03_ROADMAP_ФЕРМА_АГЕНТОВ_ФИНАНСОВЫЙ_ИНСТРУМЕНТ.md

project-docs/
  README.md
  technical_spec/
    04_ТЗ_ФЕРМА_АГЕНТОВ_ФИНАНСОВЫЙ_ИНСТРУМЕНТ.md
  module_map/
    README.md
  project_snapshot/
    README.md
  source_runtime/
    README.md
  current_status/
    README.md
  student_dialogue_context/
    README.md

rules/
  README.md
  chatgpt/
    README.md
    01_ПРАВИЛА_ДЛЯ_CHATGPT.md
    02_СТИЛЬ_ОБЪЯСНЕНИЙ.md
    03_ПРАВИЛО_БЕЗ_LOCALHOST.md
    04_ПРАВИЛО_ОДНОГО_ШАГА.md
    05_ПРАВИЛО_ПРОВЕРКИ_ОТЧЁТОВ.md
  codex/
    README.md
    AGENTS.md

prompts/
  README.md
  proof_prompt_template.md
  fix_prompt_template.md
  docs_update_prompt_template.md
  codex_report_contract.md

extension/
  README_УСТАНОВКА_РАСШИРЕНИЯ.md
  prefix/
    README.md
    openscript_student_prefix.md
  zip/
    README.md

vendor-notes/
  README.md
  hermes/
    README.md
  telegram/
    README.md

student-project-seed/
  README.md
  docs/
    README.md
  agent-packages/
    README.md
  tools/
    README.md
  tests/
    README.md
```

---

### 4.3. Что нельзя класть в student-kit repo

Запрещено:

```text
.env
auth.json
tokens
API keys
Telegram bot token
private SSH keys
runtime DB
personal student files
production runtime state
secret logs
```

---

## 5. GitHub write access через SSH deploy key

Для записи в student-kit repo используется отдельный deploy key.

Процесс для клиента:

1. ChatGPT даёт Codex prompt на создание SSH keypair.
2. Codex создаёт отдельный ключ только для student-kit repo.
3. Codex печатает только публичный ключ одной строкой.
4. Клиент открывает GitHub repo.
5. GitHub → Settings → Deploy keys → Add deploy key.
6. Вставляет публичный ключ.
7. Обязательно включает `Allow write access`.
8. Сохраняет.
9. ChatGPT даёт Codex второй prompt.
10. Codex настраивает SSH alias, проверяет доступ и делает push.

Важно:

```text
Приватный ключ никогда не печатать.
Приватный ключ никогда не вставлять в GitHub.
В GitHub вставляется только публичная строка, начинающаяся с ssh-ed25519.
```

---

## 6. Расширение для ChatGPT

### 6.1. Назначение расширения

Расширение нужно не для ученика как учебник.  
Расширение нужно, чтобы ChatGPT не забывал правила.

Оно должно вставлять prefix с учебными правилами:

- ученик нулевой;
- объяснять простым русским языком;
- один шаг за раз;
- не давать `localhost`;
- если Codex вернул отчёт — сначала проверить отчёт;
- каждый N-й шаг думать об обновлении документации;
- не соглашаться автоматически;
- критиковать по делу;
- агент работает только через Hermes.

---

### 6.2. Что должно быть в extension/

```text
extension/
  README_УСТАНОВКА_РАСШИРЕНИЯ.md
  prefix/
    openscript_student_prefix.md
  zip/
    архив расширения
```

Позже можно добавить:

```text
extension/profile/
  openscript_student_profile.json
```

---

## 7. Личный проект ученика

### 7.1. Назначение

Личный проект ученика создаётся отдельно на его сервере.

Пример пути:

```text
/opt/openscript-agent-lab
```

Но путь может отличаться.

Главное:

```text
student-kit repo = общий учебный комплект
student project repo = личный проект ученика
```

---

### 7.2. Базовые папки личного проекта

```text
agent_lab/
agent-packages/
docs/codex_source/
tests/
tools/
vendor/
```

Назначение:

- `agent_lab/` — код системы;
- `agent-packages/` — пакеты агентов;
- `docs/codex_source/` — документация проекта;
- `tests/` — проверки;
- `tools/` — служебные скрипты;
- `vendor/` — внешние компоненты, например Hermes;
- runtime state — отдельно, не как source.

---

## 8. Source и runtime

Это один из главных принципов.

```text
source = то, что хранится в git
runtime = рабочее состояние на сервере
```

Примеры source:

```text
agent_lab/
agent-packages/
docs/
tests/
tools/
```

Примеры runtime:

```text
/var/lib/openscript-agent-lab/**
Hermes profiles
Telegram state
SQLite DB
sessions
logs
```

Правило:

```text
Source — источник правды.
Runtime — результат применения source.
```

Нельзя:

- править runtime как будто это source;
- считать runtime-only fix финальным решением;
- применять agent changes вручную в Hermes profile без controlled apply-flow.

---

## 9. Ранняя страница структуры проекта

### 9.1. Назначение

Страница нужна, чтобы ученик сразу увидел проект в браузере.

Универсальный адрес:

```text
http://<SERVER_PUBLIC_IP>/project-structure/
```

Если используется порт:

```text
http://<SERVER_PUBLIC_IP>:<PORT>/project-structure/
```

Нельзя использовать:

```text
localhost
127.0.0.1
IP тестового сервера другого человека
```

---

### 9.2. Требования к странице

Страница должна быть:

- отдельной от основного Agent Lab UI;
- read-only;
- минималистичной;
- похожей на файловый менеджер;
- на русском языке;
- без редактирования;
- без скачивания;
- без просмотра содержимого файлов;
- с раскрытием папок;
- со скрытием secret-like имён.

Скрывать:

```text
.git
.env
token
auth
secret
key
password
__pycache__
.venv
node_modules
tmp
runtime cache/scratch/temp
```

---

## 10. Общий каркас проекта

До агентов, Telegram и финансов должен быть создан базовый каркас:

- backend;
- health check;
- static UI foundation;
- tests;
- nginx/systemd route при необходимости;
- source/runtime boundary;
- docs baseline.

Минимальный health endpoint:

```text
/healthz
```

Готовность:

```text
service active
health ok
public route works
git commit created
```

---

## 11. Hermes foundation

### 11.1. Главный инвариант

Агент считается рабочим только если его ответ проходит через Hermes.

Правильная цепочка:

```text
agent package → validate → apply в Hermes runtime profile → reply через Hermes
```

Запрещённые ложные успехи:

```text
backend сам ответил за агента
template/fake reply считается успехом
provider вызван напрямую мимо Hermes
agent package сохранён, но Hermes profile не создан
UI показывает “готов”, но apply не выполнен
```

---

### 11.2. Что должен уметь Hermes foundation

- найти Hermes binary или описать установку;
- проверить Hermes status;
- создать/проверить runtime profile;
- проверить auth metadata без чтения секретов;
- выполнить dry/smoke path без live model call;
- отделить source package от runtime profile;
- вернуть понятный статус.

---

### 11.3. Codex/OpenAI и Hermes

Нельзя объяснять ученику “Hermes сидит на Codex” как точную архитектуру.

Правильнее:

```text
Hermes — runtime-слой агента.
Provider/model — источник ответа для Hermes.
Codex/OpenAI может быть одним из provider/resource режимов.
Codex-исполнитель разработки и Codex/provider для Hermes — разные роли.
```

---

## 12. Agent package foundation

### 12.1. Формат agent package

Agent package обязан включать:

```text
manifest.json
SOUL.md
rules.md
examples.md
README.md
provider.defaults.json
skills/
tools.json
```

Агент — это не один prompt.  
Агент — это пакет документов, навыков, настроек и будущих инструментов.

---

### 12.2. Обязательные документы агента

- `SOUL.md` — кто агент;
- `rules.md` — правила поведения;
- `examples.md` — примеры ответов;
- `README.md` — описание агента;
- `provider.defaults.json` — настройки provider по умолчанию;
- `skills/` — навыки;
- `tools.json` — разрешённые tools.

---

### 12.3. Validator

Validator должен проверять:

- обязательные файлы существуют;
- package не пустой;
- slug корректен;
- нет запрещённых имён;
- `tools.json` существует;
- `skills/` существует;
- package можно применить в Hermes.

---

### 12.4. Smoke package

До первого настоящего агента можно использовать технический smoke package.

Ограничения:

- не показывать как первого агента;
- не использовать как Telegram-агента;
- не hardcode;
- использовать только для проверки validate/apply/status.

---

## 13. UI фабрики агентов

UI нужен для того, чтобы ученик руками вставлял документы агента.

Функции:

- список agent packages;
- создать package;
- редактировать SOUL.md;
- редактировать rules.md;
- редактировать examples.md;
- редактировать README.md;
- редактировать skills;
- редактировать tools.json;
- видеть provider defaults;
- видеть статус “сохранён, но не применён”;
- видеть статус “применён в Hermes”;
- применить package в Hermes.

Важно:

```text
Документы сохранены ≠ агент работает.
Агент работает только после apply в Hermes и reply proof через Hermes.
```

---

## 14. Первый агент

Первый настоящий агент появляется только после:

1. Hermes foundation;
2. agent package foundation;
3. UI фабрики агентов;
4. возможности apply в Hermes;
5. возможности проверить reply через Hermes.

Порядок:

1. ChatGPT генерирует документы агента.
2. Ученик вставляет их через UI.
3. Package сохраняется.
4. Package проверяется validator.
5. Package применяется в Hermes.
6. Создаётся/обновляется Hermes runtime profile.
7. Выполняется reply proof через Hermes.
8. Только после этого агент считается рабочим.

---

## 15. Telegram как первый внешний канал

### 15.1. Назначение

Telegram даёт ученику первый вау-эффект:

```text
Я написал агенту в Telegram — агент ответил.
```

Telegram — это канал общения, не бизнес-tool.

---

### 15.2. Telegram requirements

Система должна уметь:

- хранить Telegram config без печати токена;
- проверять статус connector;
- управлять polling;
- проверять allowlist;
- отличать `from.id / user_id` от `chat.id`;
- выбирать активного агента;
- передавать сообщение в Hermes reply path;
- отправлять ответ в Telegram;
- после live proof оставлять бот в рабочем состоянии.

---

### 15.3. Правило user_id vs chat_id

Доступ проверяется по:

```text
from.id / user_id
```

Доставка ответа идёт по:

```text
chat.id
```

Нельзя использовать `chat.id` как identity allowlist.

---

## 16. Tool registry

### 16.1. Назначение

Tool registry определяет, какие инструменты существуют, какие готовы, какие заблокированы, и какие инструменты разрешены конкретному агенту.

---

### 16.2. Tool states

Инструмент может быть:

```text
ready
blocked
disabled
not_configured
missing_dependency
experimental
```

Опасные tools по умолчанию заблокированы:

```text
browser
web
files
terminal
mcp
```

---

### 16.3. Tool binding

Инструменты привязываются к agent package через:

```text
tools.json
```

После сохранения `tools.json` нужно применить package в Hermes, чтобы Hermes увидел tool schemas.

---

### 16.4. Provider-safe tool names

Внутренние tool IDs могут содержать точки:

```text
fin.expense_add
fin.receipt
```

Provider-visible names должны быть безопасными.

Нужна связь:

```text
internal tool id → provider-safe name → internal tool id
```

---

## 17. Финансовый инструмент

### 17.1. Назначение

Финансовый инструмент — первый бизнес-tool.

Он показывает ученику главное:

```text
Агент не просто болтает.
Агент вызывает инструмент.
Инструмент делает действие.
Результат возвращается агенту.
```

---

### 17.2. Главный принцип

LLM/Hermes не пишет финансовые данные напрямую.

Правильно:

```text
Hermes ведёт диалог
агент вызывает tool
детерминированный financial handler пишет в БД
handler возвращает structured result
агент объясняет результат пользователю
```

---

### 17.3. Основные функции

Финансовый инструмент должен уметь:

- создать runtime storage;
- создать SQLite schema;
- добавить расход;
- показать последние расходы;
- показать месячную сводку;
- создать черновик чека;
- показать строки чека;
- подтвердить чек;
- записать подтверждённый чек в БД;
- вернуть structured result агенту.

---

### 17.4. SQLite schema

Ожидаемые таблицы:

```text
schema_version
schema_migrations
categories
payment_sources
expense_records
receipt_drafts
receipt_item_lines
operation_log
audit_events
```

---

### 17.5. Text expense flow

Поток:

```text
Telegram text
→ selected agent
→ Hermes reply path
→ financial tool call
→ validate request
→ normalize amount/category/payment source
→ write expense_records
→ write operation_log/audit_events
→ structured result
→ agent reply
→ Telegram answer
```

---

## 18. Фото чека

### 18.1. Назначение

Фото чека должно создавать черновик, а не сразу расход.

Поток:

```text
Telegram photo
→ attachment metadata
→ receipt_photo_draft
→ OCR/parser
→ receipt_drafts
→ receipt_item_lines
→ агент спрашивает подтверждение
→ пользователь подтверждает
→ expense_records
```

---

### 18.2. OCR requirements

OCR должен:

- извлекать текст;
- находить сумму;
- находить дату;
- находить магазин;
- находить строки товаров;
- честно сообщать missing fields;
- не hardcode под один чек;
- не подтверждать без пользователя.

Текущий риск проекта: OCR может не найти видимую сумму и может выбрать неверную дату. Поэтому этот блок должен идти после текстового расхода и тестироваться отдельно.

---

## 19. Голос

### 19.1. Назначение

Голос — это только другой способ ввода.

Правило:

```text
voice → transcript → тот же путь, что обычный text
```

Голос не должен иметь отдельную бизнес-логику.

---

### 19.2. Voice flow

```text
Telegram voice
→ voice detection
→ safe download/preparation
→ STT
→ transcript
→ selected agent
→ Hermes
→ tools if needed
→ reply
```

---

## 20. Второй агент

Второй агент нужен, чтобы доказать:

```text
это ферма агентов, а не один hardcoded bot
```

Требования:

- второй agent package;
- свои документы;
- свой Hermes runtime profile;
- отдельные permissions;
- отсутствие hardcode одного slug;
- возможность выбора/маршрутизации.

---

## 21. Документация проекта

Документация должна обновляться по ходу работы.

Минимальные документы в проекте ученика:

```text
current_status.md
roadmap_progress.md
module_map.md
source_runtime.md
student_dialogue_context.md
known_problems.md
```

Правило:

```text
не обновлять docs по памяти
не переписывать историю
использовать append-only там, где нужно
обновлять после крупных этапов
примерно каждый N-й run проверять, нужно ли обновление
```

---

## 22. Тесты и проверки

Каждый этап должен иметь проверки.

Типы проверок:

- git status;
- health check;
- public route check;
- UI check;
- unit tests;
- API tests;
- no secret files check;
- no localhost in user URL;
- Hermes dry/status proof;
- Hermes live reply proof;
- Telegram delivery proof;
- DB row proof;
- tool permission proof.

Нельзя считать готовым шаг, если Codex написал `SUCCESS`, но не доказал результат.

---

## 23. Финальный acceptance проекта

Проект считается завершённым, если:

1. student-kit repo подключён;
2. личный проект ученика создан;
3. git используется;
4. docs лежат в проекте;
5. расширение подключено;
6. `/project-structure/` открывается по IP ученика;
7. Hermes foundation работает;
8. agent package создаётся и применяется в Hermes;
9. первый агент отвечает через Hermes;
10. ученик общается с агентом в Telegram;
11. tool registry работает;
12. financial tool подключён;
13. текстовый расход через Telegram пишет в БД;
14. фото чека создаёт draft;
15. чек подтверждается и пишет в БД;
16. голос распознаётся и идёт в тот же путь, что текст;
17. второй агент создан отдельно;
18. tools не протекают между агентами;
19. документация обновлена;
20. ученик понимает цикл ChatGPT + Codex + сервер + git.

---

## 24. Главные запреты

Запрещено:

```text
создавать агента без Hermes
считать fake/template reply успехом
обходить Hermes прямым backend reply
называть Telegram бизнес-tool
путать user_id и chat_id
давать localhost как адрес ученику
подставлять IP тестового сервера в методичку
писать в БД напрямую из LLM
подтверждать чек без пользователя
hardcode одного агента
hardcode одного provider
hardcode один чек/сумму/дату
смешивать voice/text/photo/DB в одном fix
делать runtime-only fixes как финал
читать/печатать секреты
обновлять docs по памяти
```

---

## 25. Что не входит в первый проект

В первый проект не входит:

- полноценная коммерческая CRM;
- мультиарендность;
- биллинг;
- сложная авторизация пользователей;
- публичный marketplace инструментов;
- production-grade accounting;
- банковские интеграции;
- сложная аналитика;
- автоматическое принятие финансовых решений;
- любые действия без подтверждения пользователя;
- обучение классическому программированию как основная цель.

---

## 26. Связь с roadmap

Этот документ описывает, что должно быть построено.

Подробный порядок прохождения находится в:

```text
roadmap/03_ROADMAP_ФЕРМА_АГЕНТОВ_ФИНАНСОВЫЙ_ИНСТРУМЕНТ.md
```

Следующий логический документ после ТЗ:

```text
project-docs/module_map/
```

Он должен описать модули проекта, их ответственность и границы.

