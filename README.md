# Back-End-Development-Pictures

Flask REST service that stores picture metadata for past band events.

## Endpoints

| Method | Endpoint | Result |
|---|---|---|
| GET | `/health` | `{"status":"OK"}` |
| GET | `/count` | `{"length":10}` |
| GET | `/picture` | All pictures |
| GET | `/picture/<id>` | One picture or 404 |
| POST | `/picture` | Create a picture, 201 |
| PUT | `/picture/<id>` | Replace a picture, 200 |
| DELETE | `/picture/<id>` | Delete a picture, 204 |

## Run and test

```bash
python3.11 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
flask --app app run --debug
```
