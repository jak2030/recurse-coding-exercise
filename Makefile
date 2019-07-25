export MARKOV_MODEL_PATH=api/model/data/serialized/markov.json
export MARKOV_MODEL_CORPUS=api/model/data/corpus/full.txt

run_webapp_dev:
	cd app && yarn start

run_backend_dev:
	FLASK_ENV=development FLASK_APP=./api/app.py flask run

train_model:
	python api/model/train.py --corpus ${MARKOV_MODEL_CORPUS} --output ${MARKOV_MODEL_PATH}