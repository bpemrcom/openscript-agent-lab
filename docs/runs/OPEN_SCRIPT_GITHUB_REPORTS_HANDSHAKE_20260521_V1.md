# GitHub Reports Handshake

Codex принимает протокол GitHub-отчётов как основной порядок работы.

ChatGPT будет читать отчёты из repo и использовать их как вход для следующего self-contained prompt.

До добавления deploy key push может быть невозможен.

Следующий человеческий шаг: добавить public deploy key в GitHub repo Settings → Deploy keys → Add deploy key и включить Allow write access.

Codex подтверждает, что будет:

- писать отчёты в `docs/runs/`;
- выполнять только разрешённые изменения;
- не печатать приватные ключи, токены и секреты;
- возвращать STOP при риске или нехватке данных.
