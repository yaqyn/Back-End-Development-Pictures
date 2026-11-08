# Back-End-Development-Pictures

Flask REST service that stores picture metadata for past band events.

## Environment setup

This repository is based on the official IBM Developer Skills Network
`luggb-Back-End-Development-Pictures` course template. The IBM lab setup uses
Python 3.9.x and provides `bin/setup.sh`. In this workspace, the project was
also tested using Python 3.9.25 in the named `backend-pics-venv` environment.
That named environment is separate from the course script's default `~/venv`.

```bash
bash bin/setup.sh  # IBM course-lab setup
# In a fresh terminal, activate the course-created environment:
source ~/venv/bin/activate
python3.9 --version
# Or use the separately named local environment:
python3.9 -m venv ~/backend-pics-venv
source ~/backend-pics-venv/bin/activate
python --version  # Python 3.9.25 in this workspace
pip install -r requirements.txt pytest
pytest
```

`bin/setup.sh` is the provided course setup script. It uses `sudo apt-get`,
appends environment settings to `~/.bashrc`, and calls `make db`; run it only in
the IBM course lab where those prerequisites are configured. The `backend-pics-venv`
environment and the Pictures tests were verified locally with Python 3.9.25.

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
