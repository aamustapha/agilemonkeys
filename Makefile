all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

# target: help - Display callable targets.
help:
	@egrep "^# target:" [Mm]akefile

# target: install-dev - setup project on new machine
install:
	pip install pre-commit;
	pre-commit install;
	docker-compose build;
	make migrations;

# target: start - start django server
start:
	docker-compose up

# target: migrations - Run migrations
migrations:
	docker-compose run app sh -c "python manage.py makemigrations && python manage.py migrate"

# target: test - Run tesst
test:
	docker-compose run app sh -c "python manage.py test"
