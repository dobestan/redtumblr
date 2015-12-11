# target: help - Display callable targets
help:
	@egrep "^# target:" [Mm]akefile


# target: clean - Clean all ".pyc" files
clean:
	find . -name "*.pyc" -exec rm -rf {} \;


# target: migrate - Migrate all django applications considering app dependencies
migrate:
	python redtumblr/manage.py makemigrations
	python redtumblr/manage.py migrate


# target: clean_migration - folders in all django apps
clean_migrations:
	ls redtumblr/ | grep -v -e 'manage.py' | xargs -I{} rm -rf redtumblr/{}/migrations/


# target: test - execute project related tests including coding convention and unittest
test:
	flake8 redtumblr/
	redtumblr/manage.py test redtumblr/ -v 2
