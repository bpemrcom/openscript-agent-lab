# Prompt templates

Эта папка содержит шаблоны prompt’ов для ChatGPT.

Шаблоны не являются готовыми задачами.

ChatGPT должен заполнить:
- RUN_ID;
- RUN_MODE;
- цель;
- scope;
- forbidden scope;
- нужные документы;
- checks;
- acceptance;
- формат отчёта.

Все prompt’ы должны начинаться с:

Follow AGENTS.md.

Если AGENTS.md отсутствует в корне рабочего проекта, Codex должен вернуть STOP.

Файлы:

- proof_prompt_template.md — для проверки фактов без изменений;
- fix_prompt_template.md — для одного минимального исправления;
- docs_update_prompt_template.md — для обновления явно указанных документов;
- codex_report_contract.md — общий формат отчёта Codex.
