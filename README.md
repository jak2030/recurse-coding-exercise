# Recurse Interview

A single page web page that spits out sweet nothings penned by the Bard filtered through a certain Twitter account.

## Setup

The project uses Python for backend and data scripting and Javascript for the web app.

Anything above [Node](https://nodejs.org/en/download/) 4.0 should work for running the web app. I use [Yarn](https://yarnpkg.com/lang/en/docs/install/#mac-stable) for package management.

I developed the Python in version **3.7.2**. I used [pyenv](https://github.com/pyenv/pyenv) to manage my Python installations and [pipenv](https://docs.pipenv.org/en/latest/install/) to manage project dependencies. (I like [this guide](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c) on how to get this setup.)


If you also set the app up in this way, you should be able to run:

```
make setup
```

Which takes care of installing dependencies for the React web app, the Python Flask API, as well as the parsing and model training Python scripts.

## Run the ETLA pipeline

To run the 'extract transform load analyze' pipeline that parses data from various Shakespeare and Twitter sources, trains the raw text into a Markov model and writes a JSON-serialized version to a file, you'll need your own [Twitter API credentials](https://developer.twitter.com/en/apply-for-access.html).

Environment variables are stored or passed at runtime as: 

```
TWITTER_RECURSE_API_KEY
TWITTER_RECURSE_API_SECRET
TWITTER_RECURSE_ACCESS_TOKEN
TWITTER_RECURSE_ACCESS_TOKEN_SECRET
```


The command expects two pipeline-specific environment variables: the Twitter account to parse and the number of tweets to take.

Running:

```
NUM_TWEETS=100 TWITTER_ACCOUNTS=realdonaldtrump make run_etla
```

will generate a model located at `api/model/data/serialized/`.

If you want to include more than one Twitter account, pass a space-delimited string for the `TWITTER_ACCOUNTS`:

```
NUM_TWEETS=100 TWITTER_ACCOUNTS="Rihanna TheEllenShow" make run_etla
```

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

You should be able to see a working example of the site in your favorite browser on localhost at port 3000.

## What's in the repo?

### `/app`
A React web app that `GET`s a single `/texts` endpoint.

### `/api`
A Flask app that serves a single `GET` request and returns a single "tweet".

### `/api/model`
* A `train.py` script for reading in a list of sentences and writing a new Markov model.
* A `./data` directory to store a corpus and a trained model.


### `/scrapers`

#### `/scrapers/shakespeare.py`
The script we'll fill out in the interview that will parse http://shakespeare.mit.edu/ and write it to a format readible by the Markov trainer.

#### `/scrapers/twitter.py`
A Python script that reads in the last N tweets of users in a given list of Twitter accounts and writes it to a format readible by the Markov trainer.
