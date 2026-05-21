# Windows VM Deployment

Текущая целевая среда проекта OpenScript Agent Lab - Windows VM.

Linux-specific путь через `nginx`, `systemd` и `ufw` не является обязательным target для этого этапа.

## Текущий viewer

`project-structure` viewer запускается через Python standard library и не требует npm.

## Ближайший практический путь

1. Сначала проверить `localhost` на той же Windows VM.
2. Если пользователь работает не на самой VM, проверить LAN IP.
3. Если нужен доступ извне, выбрать tunnel, port forwarding или domain path.

## Базовый запуск

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/start_project_structure.ps1 -Host 127.0.0.1 -Port 8765
```

## Локальная проверка

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/check_project_structure.ps1 -Port 8765
```

## Варианты инструментов

Для Windows VM допустимы разные безопасные варианты, если они подходят фактической среде и правам:

- PowerShell scripts;
- Windows Firewall rule;
- Scheduled Task;
- NSSM;
- Cloudflare Tunnel;
- ngrok;
- IIS;
- nginx;
- другой reverse proxy.

Это опции, а не обязательный стек.

## Правило изменения инфраструктуры

Новый софт, firewall, service, Scheduled Task, tunnel или port forwarding можно менять только отдельным prompt с явным разрешением пользователя.

## URL

Пока публичный адрес не доказан, пользовательский URL остаётся `not_proven_yet`.

Для локальной проверки допустимы:

- `http://127.0.0.1:<PORT>/project-structure/`
- `http://<WINDOWS_VM_LAN_IP>:<PORT>/project-structure/`

Для внешнего доступа нужен отдельно доказанный адрес.
