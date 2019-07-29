# Bardi B

This project parses Shakespeare and mashes it up with tweets by Cardi B.

## Setting up your environment

The project uses Javascript for the web app and Python for the backend API, data extraction, and model generation.

Anything above [Node](https://nodejs.org/en/download/) 4.0 should work for running the web app. I use [Yarn](https://yarnpkg.com/lang/en/docs/install/#mac-stable) for package management.

I developed the Python in version 3.7.2. I used [pyenv](https://github.com/pyenv/pyenv) to manage my Python installations and [pipenv](https://docs.pipenv.org/en/latest/install/) to manage project dependencies. (I like [this guide](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c) on how to get this setup.)


If you also set the app up in this way, you should be able to run:

```
make setup
```

which takes care of installing dependencies for the React web app, the Python Flask API, and the data extraction and model training Python scripts.

## Running the ETLA pipeline

The ETLA ('extract transform load analyze') pipeline parses data from various Shakespeare and Twitter sources, writes the output to files, and calls a Markov library to train the raw text into a model and write it to a JSON-serialized version to a file.

You'll need your own [Twitter API credentials](https://developer.twitter.com/en/apply-for-access.html) to run this portion.

Environment variables for these creds are stored or passed at runtime as: 

```
TWITTER_API_KEY
TWITTER_API_SECRET
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET
```


The command expects two pipeline-specific environment variables: the Twitter account to parse and the number of tweets to take.

Running:

```
make run_etla
```

will generate a model located at `api/model/data/serialized/`.

## Run the app

Run two separate windows in your terminal of choice:

Development web app:
```
make run_webapp_dev
```

Development backend api:

```
make run_backend_dev
```

You should be able to see a working example of the site in your favorite browser at `localhost:3000`.

## What's in the repo?

### `/app`
A React web app that `GET`s a single `/texts` endpoint.

### `/backend`
A Flask app that serves a single `GET` `/texts` request and returns a single "tweet".

### `/backend/model`
* A `train.py` script for reading in a list of sentences and writing a new Markov model.
* A `./data` directory to store a corpus and a trained model.


### `/backend/scrapers`

* A `shakespeare.py` script we'll fill out in the interview that will parse content from http://shakespeare.mit.edu/ and write it to a format readible by the model trainer.

* A `twitter.py`script that reads in the latest tweets from the specified user and writes them to a format readible by the model trainer.
