.PHONY: migrations
migrations:
	python manage.py makemigrations

.PHONY: migrate
migrate:
	python manage.py migrate

.PHONY: run
run:
	python manage.py runserver 0.0.0.0:8000

