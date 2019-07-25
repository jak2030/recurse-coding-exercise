run_webapp_dev:
	cd app && yarn start

run_backend_dev:
	FLASK_ENV=development FLASK_APP=./api/app.py flask run