# AGENTS.md — Codex Run Contract

Этот файл содержит постоянные правила выполнения Codex run.

Prompt конкретной задачи должен задавать:
- цель;
- allowed scope;
- forbidden scope;
- нужные документы;
- проверки;
- acceptance;
- формат отчёта.

Codex не планирует следующий этап сам.
Codex не выбирает архитектуру сам.
Codex выполняет только prompt.

## 1. Entrypoint

Для каждого нетривиального run начать из корня текущего рабочего репозитория.

Перед изменениями:
- проверить repo root;
- проверить git status;
- определить текущий HEAD;
- определить scope из prompt;
- прочитать документы, явно указанные в prompt.

Не придумывать поведение проекта.
Если docs/source/runtime не доказывают нужное поведение — STOP.

## 2. Task-specific docs

Если prompt указывает точные документы — читать их.

Не заменять точные документы общими предположениями.

Если задача зависит от subsystem/vendor/runtime/tool/API/protocol, читать только документы, указанные в prompt, и проверять факты по source/runtime.

Если документов не хватает или они противоречат source/runtime — STOP.

## 3. Standard run order

Использовать порядок, если prompt не говорит иначе:

1. Documentation gate, если задача зависит от docs.
2. Preflight.
3. Read-only proof/current state.
4. Root cause, если есть ошибка.
5. Design/impact только в рамках prompt.
6. Minimal source change, только если безопасно.
7. Targeted tests.
8. Relevant regression checks.
9. Service restart/health only if required.
10. Commit/push only if prompt requires it.
11. Final report.

One run = one task.
Do not mix unrelated work.
Do not do broad refactors unless prompt explicitly asks.

## 4. Preflight

Перед изменениями выполнить или эквивалентно проверить:

- `git rev-parse HEAD`
- `git status -sb`
- `git status --short`
- `git diff --stat`
- `git diff --cached --stat`

Если есть unexplained dirty state вне scope — STOP.
Никогда не stage/overwrite unrelated dirty files.

## 5. Source vs runtime

Git-tracked source is source of truth.

Runtime отдельно.

Не делать runtime-only fix как финальное решение.
Не коммитить runtime data.

Никогда не коммитить:
- secrets;
- tokens;
- logs;
- sessions;
- runtime profiles;
- memories;
- generated caches;
- backups;
- temp files;
- editor swap files;
- production data.

Если классификация файла неоднозначна — STOP.

## 6. Safety boundaries

Не делать без явного разрешения prompt:

- external API calls;
- provider/model calls;
- real tool execution;
- production DB writes;
- auth/login/provider changes;
- token/secret reads or prints;
- runtime profile mutation;
- public network calls outside required checks.

Read-only inspection allowed only when safe and when it does not expose secrets.

Never print:
- secrets;
- tokens;
- private credentials;
- private keys;
- raw sensitive payloads.

Public deploy key можно печатать только если prompt явно просит создать public deploy key.
Private key никогда не печатать.

## 7. User-facing URLs

localhost / 127.0.0.1 можно использовать только для внутренней технической проверки.

Нельзя давать localhost / 127.0.0.1 как user-facing URL.

User-facing URL должен быть шаблонным или фактически доказанным публичным адресом:

- `http://<SERVER_PUBLIC_IP>/<PATH>`
- `http://<SERVER_PUBLIC_IP>:<PORT>/<PATH>`
- `https://<STUDENT_DOMAIN>/<PATH>`

Не hardcode IP тестового сервера.

## 8. UI tasks

Для UI tasks делать source/local/API/test proof.

Не требовать browser screenshots или Playwright, если prompt этого не просит.

Если user manually verifies UI, report:
`browser_rendered_proof: not_required_user_will_verify_ui_manually`

Основной UI не превращать в diagnostic wall.
Diagnostics держать в secondary/collapsed sections, если это требуется.

## 9. Tool and integration semantics

Не считать все integrations одинаковыми.

Различать:
- executable tools;
- service integrations/channels;
- diagnostic-only entries;
- unavailable placeholders;
- future/blocked capabilities.

Не показывать disabled/future/blocked placeholders как available tools.

Точное поведение брать из prompt, docs, source and runtime proof.

## 10. Context/session work

Для context/session tasks сначала доказать actual handoff path.

Map:
input source
-> selected runtime/context identity
-> model/runtime boundary
-> structured state
-> action/result state

Не решать universal context problem hardcoded local parser patch.
Не использовать model memory as source of truth for structured state.

Domain examples are test cases, not whole architecture.

## 11. Minimal domain guardrails

Не тащить stage-specific details в каждый run.

Если prompt касается agent/model reply:
- не обходить declared runtime/model boundary;
- fake/template reply не считать success;
- direct backend reply вместо declared agent runtime запрещён, если prompt требует agent runtime.

Если prompt касается business DB writes:
- model не должен писать DB напрямую;
- запись должна идти через deterministic handler/tool, если это указано в prompt.

Если prompt касается media input:
- не смешивать transport/transcription/parsing/business write в один fix без явного scope.

Детальные acceptance fields должны быть в конкретном prompt, а не в AGENTS.md.

## 12. Checks

Run targeted tests first.
Then smallest relevant regression suite.

Не запускать unrelated expensive checks unless risk justifies them.

Если test module из prompt не существует — report it and run nearest relevant existing tests.

## 13. Git discipline

For any source change:

1. `git diff --check`
2. `git diff --stat`
3. stage only allowed files
4. do not use `git add .` when unrelated dirty files exist
5. `git diff --cached --name-only`
6. `git diff --cached --stat`
7. STOP if staged files include forbidden/unrelated scope
8. commit with clear message, only if prompt requires commit
9. push only if prompt requires push
10. prove remote/head only if push was required
11. end with clean git status or explain known unrelated dirty files

For proof-only:
- do not commit;
- do not push;
- final git status must be clean or unchanged with known unrelated files.

## 14. Minimal change policy

Change only files required by prompt.
No opportunistic cleanup.
No unrelated module rewrites.
No behavior changes outside scope.
No hidden source-of-truth changes.
No invented docs/source/runtime behavior.

## 15. Docs update runs

Docs-update выполняется только если prompt явно просит.

Codex сам не решает, что пора обновлять docs.

Обновлять только явно указанные документы.

Не обновлять docs по памяти.
Использовать:
- Codex reports;
- git status;
- current files;
- verified runtime/source facts.

Do not rewrite history silently.
Add update history/append blocks when document format requires it.

## 16. Standard report

Every run must end with:

CHATGPT_REPORT_BEGIN

RUN_ID:
RUN_MODE:
STATUS: SUCCESS / STOP / FAIL

SCOPE:
DOCS_READ:
DOCS_MISSING:
PREFLIGHT:
CURRENT_STATE_PROOF:
ROOT_CAUSE:
WHAT_CHANGED:
FILES_CHANGED:
TESTS_RUN:
CHECKS:
SERVICE_RESTART:
GIT:
SAFETY:
NEXT:

CHATGPT_REPORT_END

STATUS:
- SUCCESS: task completed and checked.
- STOP: missing facts/risk/conflict; no unsafe continuation.
- FAIL: attempted execution/check failed.

Safety block:
- secrets_read:
- secrets_printed:
- private_key_printed:
- env_values_printed:
- localhost_given_to_user:
- hardcoded_test_ip_found:
- unrelated_files_changed:
- runtime_only_fix:

If prompt requires domain-specific fields, include them exactly as prompt requested.

## 17. Stop rules

STOP instead of guessing when:
- docs/source do not prove required behavior;
- source/runtime truth contradicts;
- scope requires secrets/production data/live external calls not allowed by prompt;
- staged files include forbidden scope;
- current state cannot be proven safely;
- task would require broader design than requested;
- prompt conflicts with AGENTS.md or is ambiguous.

When stopping, report:
- what was proven;
- exact blocker;
- files inspected;
- what data/decision is needed next;
- git status.
