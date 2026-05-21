# Project Structure Viewer

Страница структуры проекта нужна, чтобы быстро и безопасно показать карту папок и файлов, не открывая содержимое файлов и не подключая основной UI Agent Lab.

## Что показывает

- только имена папок и файлов;
- вложенность;
- безопасное дерево проекта из repo root.

## Что не показывает

- содержимое файлов;
- редактирование;
- скачивание;
- абсолютные пути;
- секретные имена и опасные служебные каталоги.

## Что скрывается

Страница и API скрывают такие имена и зоны, как:

- `.git`
- `.env`
- `.env.*`
- `node_modules`
- `__pycache__`
- `*.pyc`
- `token`
- `tokens`
- `secret`
- `secrets`
- `key`
- `keys`
- `auth`
- `password`
- `credential`
- `credentials`

## Access policy

Для текущей Windows VM допустимы несколько режимов доступа:

- Local VM URL:
  `http://127.0.0.1:<PORT>/project-structure/`
  Используется, если пользователь открывает браузер на той же Windows VM.

- LAN URL:
  `http://<WINDOWS_VM_LAN_IP>:<PORT>/project-structure/`
  Используется, если пользователь открывает страницу с другого устройства в той же локальной сети.

- Public/tunnel/domain URL:
  `http://<PUBLIC_IP_OR_DOMAIN>:<PORT>/project-structure/`
  или tunnel/domain URL.
  Используется только если нужен доступ извне.

Текущий доказанный режим должен фиксироваться в отчётах.

current_access_url: not_verified_yet
software_policy: tool_agnostic

## Локальная проверка

Для технической проверки можно запустить stdlib HTTP server и проверить:

- `GET /healthz`
- `GET /api/project-tree`
- `GET /project-structure/`

Локальный check допускает `localhost` или `127.0.0.1`, если пользователь работает на той же Windows VM.

## Будущий user-facing URL

Когда адрес будет доказан, пользователь должен открывать один из вариантов:

- `http://127.0.0.1:<PORT>/project-structure/`
- `http://<WINDOWS_VM_LAN_IP>:<PORT>/project-structure/`
- `http://<PUBLIC_IP_OR_DOMAIN>:<PORT>/project-structure/`

## Примечание

Страница не использует основной UI Agent Lab и не требует сборки или npm.

## Windows VM

- Локальная проверка на Windows VM выполняется через PowerShell scripts из `scripts/windows/`.
- Linux nginx/systemd сейчас не target для этого этапа.
