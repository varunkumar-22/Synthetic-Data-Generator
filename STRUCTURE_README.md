# Project Structure

The project has three parts that sit side by side: a Python package that does the actual data generation, a Node + Express server that exposes it over HTTP, and a React app that talks to the server.

```
Synthetic-Data-Generator/
│
├── structured_data_generator/     # Python package: the engine and its CLI
│   ├── templates/                 # One file per template
│   │   ├── __init__.py            # TEMPLATES registry
│   │   ├── base.py                # Shared Faker instance
│   │   ├── user.py
│   │   ├── ecommerce.py
│   │   └── ...
│   ├── engine/                    # Generation logic
│   │   ├── generator.py           # generate_from_template
│   │   ├── constraints.py         # Ranges, uniqueness, correlations
│   │   └── utils.py               # Seeding, template validation
│   ├── io/                        # CSV and JSON read/write
│   ├── profiling/                 # Dataset profiles and summary stats
│   ├── cli/                       # The sdg command
│   │   ├── __init__.py            # Subcommand wiring
│   │   ├── generate.py            # sdg generate
│   │   └── profile.py             # sdg profile <file>
│   ├── bridge.py                  # JSON over stdin/stdout, called by the server
│   └── config.py                  # Default settings
│
├── server/                        # Node + Express API
│   └── src/
│       ├── index.js               # Starts the server
│       ├── app.js                 # Builds the app and mounts routes
│       ├── config.js              # PORT, PYTHON, repo root
│       ├── routes/                # One file per resource
│       │   ├── health.js
│       │   ├── templates.js
│       │   └── generate.js
│       ├── services/
│       │   └── pythonBridge.js    # Spawns bridge.py and parses its reply
│       └── middleware/
│           ├── validate.js        # Request validation
│           └── errorHandler.js    # Turns thrown errors into JSON responses
│
├── web/                           # React + Vite app
│   └── src/
│       ├── App.jsx                # Routes
│       ├── features/              # One folder per feature
│       │   ├── home/
│       │   ├── templates/         # Page, TemplateCard, useTemplates, api
│       │   ├── generate/          # Page, ConfigForm, PreviewTable, api
│       │   └── docs/
│       ├── components/            # UI shared across features
│       │   ├── Alert/
│       │   ├── PageHeader/
│       │   └── Sidebar/
│       └── lib/                   # Helpers shared across features
│           └── download.js
│
├── tests/                         # Python unit tests
├── examples/                      # Example notebooks
├── pyproject.toml
└── requirements.txt
```

## How a request flows

```
web (React)  →  server (Express)  →  bridge.py  →  engine + templates
```

The web app only ever calls `/api/...`. The server validates the request and passes it to `bridge.py` as JSON. The bridge calls the same Python functions the CLI uses, so the CLI and the web app always produce the same data.

## Setup

```bash
# Python package and the sdg command
pip install -e .

# Server
cd server && npm install

# Web app
cd web && npm install
```

## Running

```bash
# CLI
sdg generate
sdg profile my_data.csv

# Server, on http://localhost:4000
cd server && npm run dev

# Web app, proxies /api to the server
cd web && npm run dev
```

If the server should use a virtualenv, point it at that interpreter:

```bash
PYTHON=../venv/bin/python npm run dev
```

## Running tests

```bash
python -m unittest discover tests
```

## Adding a new feature

Work from the inside out: Python first, then the server, then the web app. Each layer has one obvious place for new code.

### A feature that goes all the way to the web app

Say you want to profile a dataset from the browser.

1. **Python logic.** Put the function in the package folder it belongs to, here `structured_data_generator/profiling/`. Add a test in `tests/`.
2. **Bridge action.** Add a new `action` branch in `structured_data_generator/bridge.py` that reads the payload, calls your function and returns JSON.
3. **Server route.** Create `server/src/routes/profile.js`, call `callPython({ action: "profile", ... })` inside it, and mount it with one line in `server/src/app.js`. If the request needs checking, add a validator to `server/src/middleware/validate.js`.
4. **Web feature.** Create `web/src/features/profile/` with the page, its components and an `api.js` that calls the new endpoint. Add the route in `web/src/App.jsx` and a link in `web/src/components/Sidebar/Sidebar.jsx`.

If the feature should also work in the terminal, add `structured_data_generator/cli/<name>.py` and register the subcommand in `structured_data_generator/cli/__init__.py`.

### Smaller additions

**A new template.** Create `structured_data_generator/templates/<name>.py`, following an existing one such as `user.py`. Register it in the `TEMPLATES` dict in `templates/__init__.py`. The CLI and the web app pick it up from there, so nothing else changes.

**A new output format.** Add `structured_data_generator/io/<format>_handler.py` with a save and a load function, next to the CSV and JSON ones.

**A new API endpoint for an existing feature.** Add it to that feature's file in `server/src/routes/`.

**A new UI component.** If only one feature uses it, keep it in that feature's folder. Move it to `web/src/components/` once a second feature needs it.

### Rules of thumb

Generation logic lives in Python only. The server should not reimplement it, only pass requests through.

Features in `web/src/features/` should not import from each other. Shared code goes in `components/` or `lib/`.

Routes stay thin: validate, call the bridge, return the result.

## License

MIT License. See the LICENSE file for details.
