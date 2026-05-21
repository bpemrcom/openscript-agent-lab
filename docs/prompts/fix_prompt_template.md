Follow AGENTS.md.

RUN_ID: <RUN_ID>
RUN_MODE: minimal_fix

Если AGENTS.md отсутствует в корне текущего рабочего проекта — STOP.
Не продолжай работу без правил проекта.

ЗАДАЧА:
<одно минимальное исправление>

ДОКАЗАННАЯ ПРИЧИНА:
<root cause из proof-run>

SCOPE:
Разрешено менять только:
- <file/path>
- <file/path>

Запрещено менять:
- <file/path>
- unrelated files;
- runtime data;
- secrets.

ДОКУМЕНТЫ ДЛЯ ЧТЕНИЯ:
- <doc path>
- <doc path>

ПРАВИЛА FIX:
1. Один run = одна задача.
2. Исправлять только доказанную причину.
3. Не расширять scope.
4. Не делать opportunistic cleanup.
5. Не делать broad refactor.
6. Stage только файлы из scope.
7. Не использовать git add . если есть unrelated dirty files.
8. Commit делать только если prompt требует commit.
9. Push делать только если prompt требует push.
10. User-facing URL не должен быть localhost.

CHECKS:
1. git status before;
2. current root/head proof;
3. targeted tests;
4. nearest relevant regression checks;
5. git diff --check;
6. git diff --stat;
7. staged files check;
8. commit, если требуется;
9. push, если требуется;
10. git status after;
11. final safety check.

ОТЧЁТ:
Верни отчёт строго между маркерами:

CHATGPT_REPORT_BEGIN

RUN_ID:
RUN_MODE: minimal_fix
STATUS: SUCCESS / STOP / FAIL

SCOPE:
DOCS_READ:
PREFLIGHT:
CURRENT_STATE_PROOF:
ROOT_CAUSE:
WHAT_CHANGED:
FILES_CHANGED:
TESTS_RUN:
CHECKS:
GIT:
SAFETY:
NEXT:

CHATGPT_REPORT_END
