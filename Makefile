export MARKOV_MODEL_PATH=api/model/data/serialized/markov.json
export TWEETS_OUTPUT_PATH=api/model/data/corpus/tweets.txt
export LIB_CONGRESS_OUTPUT_PATH=api/model/data/corpus/laws.txt


run_webapp_dev:
	cd app && yarn start

run_backend_dev:
	FLASK_ENV=development FLASK_APP=./api/app.py flask run

train_model:
	python api/model/train.py --corpus ${TWEETS_OUTPUT_PATH} ${LIB_CONGRESS_OUTPUT_PATH} --output ${MARKOV_MODEL_PATH}

parse_tweets:
	python scrapers/twitter.py --num_tweets ${NUM_TWEETS} --account ${TWITTER_ACCOUNT} --output ${TWEETS_OUTPUT_PATH}

parse_lib_congress:
	python scrapers/lib_congress.py --output ${LIB_CONGRESS_OUTPUT_PATH}