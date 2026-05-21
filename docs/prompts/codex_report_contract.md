# Контракт отчёта Codex

Каждый Codex run должен завершаться отчётом между маркерами:

CHATGPT_REPORT_BEGIN
...
CHATGPT_REPORT_END

## STATUS

SUCCESS — задача выполнена и проверена.

STOP — не хватает фактов, есть риск или prompt противоречит правилам.

FAIL — попытка была, но команда, проверка или изменение не прошли.

## Базовые поля

RUN_ID:
RUN_MODE:
STATUS:

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

Если поле неприменимо, писать:

not_applicable

или:

not_run_<reason>

## SAFETY block

secrets_read:
secrets_printed:
private_key_printed:
env_values_printed:
localhost_given_to_user:
hardcoded_test_ip_found:
unrelated_files_changed:
runtime_only_fix:

## GIT block

branch:
start_head:
final_head:
commit:
pushed:
remote_head:
git_status_after:

## STOP report

Если STATUS = STOP, указать:

what_was_proven:
exact_blocker:
files_inspected:
data_or_decision_needed:
git_status:

## FAIL report

Если STATUS = FAIL, указать:

failed_step:
error_summary:
files_changed_before_fail:
rollback_or_cleanup_status:
git_status:
recommended_next_step:

## SUCCESS report

Если STATUS = SUCCESS, указать:

acceptance_passed:
checks_passed:
remaining_risks:
next_recommended_step:

## Дополнительные поля

Не добавлять domain-specific поля в общий контракт как обязательные.

Если prompt требует дополнительные поля для конкретной подсистемы, Codex должен включить их точно в том виде, как попросил prompt.
