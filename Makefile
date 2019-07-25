export MARKOV_MODEL_PATH=api/model/data/serialized/markov.json
export MARKOV_MODEL_CORPUS_DIR=api/model/data/corpus/
export TWEETS_OUTPUT_PATH=api/model/data/corpus/tweets.txt
export SHAKESPEARE_OUTPUT_PATH=api/model/data/corpus/hamlet.txt

setup:
	@(make setup_webapp)
	@(make setup_backend)

setup_webapp:
	yarn --cwd app

setup_backend:
	pyenv local 3.7.2
	pipenv install
	python -m spacy download en
	pipenv shell

run_webapp_dev:
	yarn --cwd app start

run_backend_dev:
	FLASK_ENV=development FLASK_APP=./api/app.py flask run

run_etla:
	@(make parse_tweets)
	@(make parse_shakespeare)
	@(make train_model)	

train_model:
	python api/model/train.py --corpus_dir ${MARKOV_MODEL_CORPUS_DIR} --output ${MARKOV_MODEL_PATH}

parse_tweets:
	python scrapers/twitter.py --num_tweets ${NUM_TWEETS} --accounts ${TWITTER_ACCOUNTS} --output ${TWEETS_OUTPUT_PATH}

parse_shakespeare:
	python scrapers/shakespeare.py --output ${SHAKESPEARE_OUTPUT_PATH}