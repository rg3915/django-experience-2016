install:
	pip install -r requirements.txt

delete_migrations:
	rm db.sqlite3
	rm -rf djexperience/bookstore/migrations
	rm -rf djexperience/crm/migrations
	rm -rf djexperience/sale/migrations

migrate:
	./manage.py makemigrations bookstore crm sale
	./manage.py migrate

test:
	python manage.py test -n


mer:
	./manage.py graph_models -a -g -o dev/dj-exp${n}.png
	# usage: make mer n="02"

createuser:
	./manage.py createsuperuser --username='admin' --email=''

shell_person:
	./manage.py shell < shell/shell_person.py

backup:
	./manage.py dumpdata --format=json --indent=2 > fixtures.json

load:
	./manage.py loaddata fixtures.json

run:
	./manage.py runserver

initial: install migrate createuser
