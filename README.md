# Bardi B

This project parses Shakespeare and mashes it up with tweets by Cardi B or any other Twitter user requested by the client app. It builds a model on the fly if it doesn't already have the requested model. Furthermore, you can request the Shakespearean style from "villain", "jester", or "dreamer".

## Setting up your environment

The project uses Javascript for the web app and Python for the backend API, data extraction, and model generation.

Anything above [Node](https://nodejs.org/en/download/) 4.0 should work for running the web app. I use [Yarn](https://yarnpkg.com/lang/en/docs/install/#mac-stable) for package management.

I developed the Python in version 3.7.2. I used [pyenv](https://github.com/pyenv/pyenv) to manage my Python installations and [pipenv](https://docs.pipenv.org/en/latest/install/) to manage project dependencies. (I like [this guide](https://hackernoon.com/reaching-python-development-nirvana-bb5692adf30c) on how to get this setup.)


If you also set the app up in this way, you should be able to run:

```
make setup
```

which takes care of installing dependencies for the React web app, the Python Flask API, and the data extraction and model training Python scripts.

## Running pre-processing

This script needs to be run before starting up the app. It builds four Shakespeare-specific models: one for villainous characters, another for jesters, a third for dreamers, and another that combines those three archetypes.

The script parses the complete works, pulls pre-defined characters by archetyep and combines their text into these aforementioned models. Each model is written to a JSON-serialized file.

To run preprocessing, enter:

```
make preprocess
```

## Running the app

Run two separate windows in your terminal of choice:

Development web app:
```
make run_webapp_dev
```

Development backend api:

```
make run_backend_dev
```

To see the app in action, you'll need your own [Twitter API credentials](https://developer.twitter.com/en/apply-for-access.html).

Environment variables for these creds are stored or passed at runtime as: 

```
TWITTER_API_KEY
TWITTER_API_SECRET
TWITTER_ACCESS_TOKEN
TWITTER_ACCESS_TOKEN_SECRET
```

This is because every time a new permutation of Twitter account user + archetype is requested by the client a server executes a backend task to parse Twitter and build a new model that combines those tweets with the given archetypal Shakespeare model, if it doesn't already exist.

You should be able to see a working example of the site in your favorite browser at `localhost:3000`.

## What's in the repo?

### `/app`
A React web app that `GET`s a single `/lines` endpoint.

### `/backend`
A Flask app that serves a single `GET` `/lines` request and returns a single "tweet".

### `/backend/model`
* A `spacy_markovify.py` script that handles model tasks including loading, writing, and combining.

### `/backend/shakespeare`

* Scripts for various ETLA (extract, transform, load, analyze) tasks related to Shakespeare data pulled from http://shakespeare.mit.edu/.

### `/backend/twitter`
* Scripts for various ETLA tasks related to Twitter data.
