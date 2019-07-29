export MODEL_DIR=backend/model/data/serialized/
export MARKOV_MODEL_CORPUS_DIR=backend/model/data/corpus/
export TWEETS_OUTPUT_DIR=backend/model/data/corpus/
export SHAKESPEARE_OUTPUT_PATH=backend/model/data/corpus/shakespeare.txt

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

run_etla:
	@(make parse_cardi_tweets)
	@(make parse_shakespeare)
	@(make train_model)	

train_model:
	pipenv run python backend/model/train.py --corpus-dir ${MARKOV_MODEL_CORPUS_DIR} --output ${MODEL_DIR}

parse_cardi_tweets:
	pipenv run python backend/scrapers/twitter.py --num-tweets 1000 --accounts iamcardib --output-dir ${TWEETS_OUTPUT_DIR}

parse_shakespeare:
	pipenv run python backend/scrapers/shakespeare.py --output ${SHAKESPEARE_OUTPUT_PATH}