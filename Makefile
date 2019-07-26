export MARKOV_MODEL_PATH=api/model/data/serialized/markov.json
export MARKOV_MODEL_CORPUS_DIR=api/model/data/corpus/
export TWEETS_OUTPUT_DIR=api/model/data/corpus/
export SHAKESPEARE_OUTPUT_PATH=api/model/data/corpus/shakespeare.txt

setup:
	@(make setup_webapp)
	@(make setup_backend)

setup_webapp:
	yarn --cwd app

setup_backend:
	pyenv local 3.7.2
	pipenv install
	pipenv run python -m spacy download en
	mkdir -p api/model/data/corpus
	mkdir -p api/model/data/serialized


run_webapp_dev:
	yarn --cwd app start

run_backend_dev:
	FLASK_ENV=development FLASK_APP=./api/app.py pipenv run flask run

run_etla:
	@(make parse_cardi_tweets)
	@(make parse_shakespeare)
	@(make train_model)	

train_model:
	pipenv run python api/model/train.py --corpus-dir ${MARKOV_MODEL_CORPUS_DIR} --output ${MARKOV_MODEL_PATH}

parse_cardi_tweets:
	pipenv run python scrapers/twitter.py --num-tweets 1000 --accounts iamcardib --output-dir ${TWEETS_OUTPUT_DIR}

parse_shakespeare:
	pipenv run python scrapers/shakespeare.py --output ${SHAKESPEARE_OUTPUT_PATH}