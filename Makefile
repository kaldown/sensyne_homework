
install:
	docker-compose up -d
	./sensyne/manage.py migrate

test:
	python tests/runner.py

run:
	docker-compose up -d
	./sensyne/manage.py runserver

