# Протокол взаимодействия ChatGPT ↔ Codex

- ChatGPT даёт Codex self-contained prompt.
- Codex выполняет только prompt.
- Codex пишет отчёт в `docs/runs/`.
- Codex делает commit только разрешённых изменений.
- Codex делает push только если prompt явно разрешает push и GitHub-доступ настроен.
- ChatGPT читает отчёты из GitHub и даёт следующий prompt.
- Приватные ключи, токены и секреты никогда не печатаются.
- Если есть риск или нехватка данных, Codex возвращает STOP.
- Один run = одна задача.
