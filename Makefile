CONTAINER_NAME = simple_event_logging

.PHONY build:
build:
	docker build -t $(CONTAINER_NAME) .

.PHONY run:
run:
	docker compose up

.PHONY: migrations
migrations:
	python src/manage.py makemigrations

.PHONY: migrate
migrate:
	python src/manage.py migrate

.PHONY: run-local
run-local:
	python src/manage.py runserver 0.0.0.0:8000

