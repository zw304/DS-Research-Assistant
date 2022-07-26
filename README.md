# Bots, Disinformation, and the (First) Trump Impeachment

## Introduction
This is a A research project by Dr.Michael Rossetti and Dr.Tauhid Zaman

"We collect tweets about the (First) Trump Impeachment, identify automated accounts known as "bots", analyze their behavior, and assess their impact on the conversation.

We study the role of automated accounts known as ''bots'' in manipulating the social media discussion surrounding the first Impeachment of U.S. President Donald Trump. Our dataset includes 67 million posts from 3.6 million Twitter users, covering a 60 day period from Impeachment to acquittal. Despite comprising less than 1% of users in our dataset, we find the bots are around 70 times more active in the Impeachment discussion on average than normal users, and they produce around one third of all Impeachment-related content. We find Pro-Trump bots are more numerous and active than Anti-Trump bots, and more persuasive on most days. Content analysis shows Pro-Trump bots promoting topics related to the Q-Anon conspiracy theory. News quality analysis shows bots, Q-Anon promoters, and Pro-Trump users (including Pro-Trump bots) are each more likely to spread disinformation and fake news than their counterparts."

**For more detailed info, please check Dr.Michael Rossetti's website: https://impeachment-tweet-analysis-web.herokuapp.com





#---------------------------------------------


# disinfo-research-group-template


## Installation

### Repo Setup

Make a copy of this template repo. Clone / download your copy of the repo.

And navigate there from the command-line.

```sh
cd ~/path/to/disinfo-research-group-template
```

### Environment Setup

> If you use conda environments, follow this section


Setup a virtual environment:

```sh
conda create -n research-env python=3.8
```

```sh
conda activate research-env
```

### Package Installation

Install packages:

```sh
pip install -r requirements.txt
```


## Setup

### Google Credentials

Gain access to the shared drive.

Locate the JSON credentials file in the "credentials" directory, and download it to the root directory of this repo, naming it specifically "google-credentials.json".

### Environment Variables

Create a new local ".env" file and set the following environment variable (`GOOGLE_APPLICATION_CREDENTIALS`):

```sh
# this is the ".env" file..

GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/disinfo-research-group-template/google-credentials.json"
```

## Usage


Demonstrate ability to fetch data from BigQuery:

```sh
python -m app.bq_service
```
