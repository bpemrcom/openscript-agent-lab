Follow AGENTS.md.

RUN_ID: <RUN_ID>
RUN_MODE: proof_only

Если AGENTS.md отсутствует в корне текущего рабочего проекта — STOP.
Не продолжай работу без правил проекта.

ЗАДАЧА:
<описать, какие факты нужно собрать>

Это proof-only run.
Ничего не менять.
Ничего не коммитить.
Ничего не пушить.

SCOPE:
Проверить только:
- <path or subsystem>
- <path or subsystem>

НЕ ТРОГАТЬ:
- source files;
- runtime data;
- secrets;
- unrelated files.

ДОКУМЕНТЫ ДЛЯ ЧТЕНИЯ:
- <doc path>
- <doc path>

Если нужный документ отсутствует, stub или противоречит source/runtime — STOP.

ЧТО ПРОВЕРИТЬ:
1. repo root;
2. current branch/head;
3. git status;
4. relevant docs;
5. relevant source files;
6. relevant runtime state, только если это безопасно и разрешено;
7. current behavior proof;
8. contradictions;
9. risks;
10. recommended next step.

ЗАПРЕТЫ:
- не менять файлы;
- не делать commit;
- не делать push;
- не перезапускать сервисы без явного разрешения;
- не менять runtime;
- не читать и не печатать секреты;
- не выполнять external API/model calls без явного разрешения;
- не писать в production DB;
- не давать localhost как user-facing URL.

ОТЧЁТ:
Верни отчёт строго между маркерами:

CHATGPT_REPORT_BEGIN

RUN_ID:
RUN_MODE: proof_only
STATUS: SUCCESS / STOP / FAIL

SCOPE:
DOCS_READ:
DOCS_MISSING:
PREFLIGHT:
CURRENT_STATE_PROOF:
FINDINGS:
RISKS:
SAFETY:
NEXT:

CHATGPT_REPORT_END
