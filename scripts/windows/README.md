# Windows helper scripts

Эти скрипты помогают запускать и проверять `project-structure` viewer на Windows VM.

## Запуск viewer

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/start_project_structure.ps1 -Host 127.0.0.1 -Port 8765
```

Локальный URL для той же Windows VM:

`http://127.0.0.1:8765/project-structure/`

## Локальная проверка

```powershell
powershell -ExecutionPolicy Bypass -File scripts/windows/check_project_structure.ps1 -Port 8765
```

## LAN URL

Если браузер открыт не на самой VM, но в той же локальной сети, можно использовать:

`http://<WINDOWS_VM_LAN_IP>:8765/project-structure/`

## Про внешний доступ

Если нужен доступ извне, позже можно выбрать один из вариантов:

- public IP или domain;
- port forwarding;
- Windows Firewall inbound rule;
- Scheduled Task;
- Windows Service;
- NSSM;
- Cloudflare Tunnel;
- ngrok;
- IIS;
- nginx;
- другой безопасный reverse proxy.

Выбор инструментов делается по фактической среде и отдельному prompt. Пока такие настройки не были отдельно разрешены, менять их не нужно.
