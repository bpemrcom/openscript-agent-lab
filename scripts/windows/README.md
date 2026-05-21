# Windows helper scripts

Эти скрипты помогают запускать и проверять `project-structure` viewer на Windows VM.

## Запуск viewer

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/start_project_structure.ps1 -Host 127.0.0.1 -Port 8765
```

Скрипт запускает Python backend без admin-доступа, без firewall-изменений и без service-установки.

## Локальная проверка

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/check_project_structure.ps1 -Port 8765
```

Проверка использует `localhost` только как internal proof.

## Про внешний доступ

Для доступа извне позже понадобятся:

- публичный IP или домен;
- port forwarding;
- Windows Firewall inbound rule;
- решение о постоянном запуске через Scheduled Task, Windows Service или NSSM.

Пока публичный адрес не доказан, user-facing URL остаётся `not_proven_yet`.
