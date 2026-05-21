Follow AGENTS.md.

RUN_ID: <RUN_ID>
RUN_MODE: docs_update

Если AGENTS.md отсутствует в корне текущего рабочего проекта — STOP.
Не продолжай работу без правил проекта.

ЗАДАЧА:
Обновить только явно указанные документы.

ОБНОВИТЬ:
- <doc path>
- <doc path>

НЕ ТРОГАТЬ:
- документы вне списка;
- source code;
- runtime;
- secrets;
- unrelated files.

ФАКТЫ ДЛЯ ОБНОВЛЕНИЯ:
Использовать только:
- отчёты Codex;
- git status;
- текущие файлы;
- доказанный source/runtime state.

НЕ ИСПОЛЬЗОВАТЬ:
- память;
- догадки;
- устаревшие выводы;
- неподтверждённые предположения.

ПРАВИЛА DOCS-UPDATE:
1. Codex сам не решает, что пора обновлять docs.
2. Обновлять только документы из списка ОБНОВИТЬ.
3. Не переписывать историю задним числом.
4. Если документ имеет раздел истории — добавить новую запись.
5. Если фактов не хватает — STOP.
6. Не hardcode IP тестового сервера.
7. Не добавлять localhost как user-facing URL.
8. Commit делать только если prompt требует commit.
9. Push делать только если prompt требует push.

ВОЗМОЖНЫЕ ДОКУМЕНТЫ СОСТОЯНИЯ:
Это справка. Не обновлять все сразу без прямого указания.
- roadmap;
- ТЗ;
- module map;
- project snapshot;
- dialogue context;
- current status, если есть.

ОТЧЁТ:
Верни отчёт строго между маркерами:

CHATGPT_REPORT_BEGIN

RUN_ID:
RUN_MODE: docs_update
STATUS: SUCCESS / STOP / FAIL

DOCS_REQUESTED:
DOCS_UPDATED:
DOCS_NOT_TOUCHED:
FACTS_USED:
FILES_CHANGED:
CHECKS:
GIT:
SAFETY:
NEXT:

CHATGPT_REPORT_END
