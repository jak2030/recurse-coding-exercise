export BARDI_B_DATA_DIR=data

setup:
	@(make setup_webapp)
	@(make setup_backend)

setup_webapp:
	yarn --cwd app

setup_backend:
	pyenv local 3.7.2
	pipenv install	
	pipenv run python -m spacy download en
	mkdir -p backend/model/data/corpus
	mkdir -p backend/model/data/serialized

run_webapp_dev:
	yarn --cwd app start

run_backend_dev:
	FLASK_ENV=development FLASK_APP=./backend/app.py pipenv run flask run

build_model:
	pipenv run python backend/task.py --build-model iamcardib jester

preprocess:
	pipenv run python backend/preprocess.py