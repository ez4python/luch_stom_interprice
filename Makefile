migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

admin:
	python3 manage.py createsuperuser

language:
	python3 manage.py makemessages -l en -l ru -l uz
	python3 manage.py compilemessages --ignore=.venv

celery:
	celery -A root worker --loglevel=info

run:
	docker start pg_data luch_redis
