# Windows VM Deployment

Текущая целевая среда проекта OpenScript Agent Lab теперь Windows VM.

Linux-specific путь через `nginx`, `systemd` и `ufw` не является текущим target для этого шага.

## Текущий viewer

`project-structure` viewer запускается через Python standard library и не требует npm.

## Базовый запуск

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/start_project_structure.ps1 -Host 127.0.0.1 -Port 8765
```

## Локальная проверка

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/check_project_structure.ps1 -Port 8765
```

## Что нужно для внешнего доступа

Для доступа извне нужен отдельный infrastructure run:

- определить public IP или domain;
- проверить port forwarding;
- при необходимости создать Windows Firewall inbound rule;
- решить постоянный запуск.

## URL

Пока публичный адрес не доказан, пользовательский URL остаётся `not_proven_yet`.

Не давать `localhost` как user-facing URL.
