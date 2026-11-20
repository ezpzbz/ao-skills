# tasklist

A tiny command-line task tracker. Python 3.10+, standard library only.

```bash
python3 -m tasklist.cli add "buy milk"
python3 -m tasklist.cli list
python3 -m unittest        # run tests
```

Tasks are stored in `tasks.json` in the current directory (override with `TASKLIST_FILE`).

Planned work is in [docs/plans/](docs/plans/).
