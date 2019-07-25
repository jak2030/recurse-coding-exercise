# Recurse Interview

A simple web page that spits out legislation as if written by a particular Twitter account.

## Setup and run the app

Run two separate windows in your terminal of choice:

Development web app:
```
make run_webapp_dev
```

Development backend api:

```
make run_backend_dev
```

## Repo Structure

### `/app`
A React web app that `GET`s a single "new legislation" endpoint.

### `/api`
A Flask app that serves a single `GET` request and returns a single piece of "new legislation"

### `/scrapers`

#### Library of Congress Scraper
A Python web scraper that pulls legislation from the Library of Congress and writes it to a format readible by the Markov trainer.

#### Twitter Scraper
A Python script that reads in the last N tweets of a given Twitter accounts and writes it to a format readible by the Markov trainer.


### `/markov-trainer`
A simple script for reading in a list of sentences and writing a new Markov model.


## Requirements

- Python 3.7.2