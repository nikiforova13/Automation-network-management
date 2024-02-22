PYTHONPATH= PYTHONPATH=src
PATH = src
run:
	gunicorn

format:
	black $(PATH)