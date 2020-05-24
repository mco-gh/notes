onejgordon/flow-dashboard

# [(L)](https://github.com/onejgordon/flow-dashboard#flow-dashboard)Flow Dashboard

[[Build Status](../_resources/af3359b6a330e8be6d21e0274c77bc30.bin)](https://travis-ci.org/onejgordon/flow-dashboard)[[Code Climate](../_resources/9708145ceeb7540e760d9d15553d7307.bin)](https://lima.codeclimate.com/github/onejgordon/flow-dashboard)[[Coverage Status](../_resources/b0236bbfe669e0f248df31c80339c965.bin)](https://coveralls.io/github/onejgordon/flow-dashboard?branch=master)[[License: MIT](../_resources/65217ab2f7626cf0d4cb417d28b23598.bin)](https://jeremy.mit-license.org/)

## [(L)](https://github.com/onejgordon/flow-dashboard#purpose)Purpose

Flow is a habit tracker and personal data analytics app that lets you keep focus on what matters. Flow owns none of your data. That's yours.

If you just want look around or get started with Flow, you can create a free account at [http://flowdash.co](http://flowdash.co/).

To spin up your own instance, or start contributing to this repo, see below.

## [(L)](https://github.com/onejgordon/flow-dashboard#setup)Setup

To deploy a new instance of Flow, use the following instructions.

### [(L)](https://github.com/onejgordon/flow-dashboard#obtain-google-app-engine-sdk)Obtain Google App Engine SDK

Download the Cloud SDK from Google.` https://cloud.google.com/appengine/downloads `

### [(L)](https://github.com/onejgordon/flow-dashboard#setup-a-new-google-cloud-project)Setup a new Google Cloud project

Visit the Google developer's console: https://console.developers.google.com/Create a new project and choose a unique project ID. You will not need a billing account if usage remains within Google's free tier, which should support low-mid volume use cases.

### [(L)](https://github.com/onejgordon/flow-dashboard#set-up-a-gcloud-config)Set up a gcloud config

	gcloud config configurations create [my-flow-config-name]
	gcloud config set project [project-id]
	gcloud config set account [my email]

### [(L)](https://github.com/onejgordon/flow-dashboard#fork-the-repo)Fork the repo

Branch or fork this repository into a project directory.
Ensure you have npm and gulp installed.

	npm install -g gulp
	npm install

### [(L)](https://github.com/onejgordon/flow-dashboard#update-code-configuration)Update code configuration

Update the APP_OWNER variable in constants.py. Owner should match the Google account you logged into the console with. This will enable the application to send emails.

Create secrets.py, client_secrets.js from the templates.

### [(L)](https://github.com/onejgordon/flow-dashboard#run-the-dev-server-locally)Run the dev server locally

To avoid conflicts sometimes seen with gcloud and google.cloud python libs it is often helpful to run the dev server in a virtualenv.

- ` virtualenv env `
- ` source env/bin/activate `
- ` pip install -t lib -r requirements.txt `
- ` pip install -r local.requirements.txt `
- ` gcloud components update `
- ` ./scripts/server.sh `

Make sure dev_appserver.py is in your path, and run ` ./scripts/server.sh ` to start the dev server locally, and ` gulp ` in another terminal to build JS etc.

### [(L)](https://github.com/onejgordon/flow-dashboard#deploy)Deploy

` ./scripts/deploy.sh 0-1 ` to deploy a new version 0-1 and set is as default
Visit ` https://[project-id].appspot.com ` to see the app live.

## [(L)](https://github.com/onejgordon/flow-dashboard#features)Features

- Daily journal / survey
    - Configurable questions
    - Optional location pickup & mapping
    - Extract @mentions and #tags from configured open-ended responses (auto-suggest)
- Habit tracking ala habits app
    - With weekly targets
    - Commitments
- Tracking top tasks for each day (submitted with journal)
- Monthly/year goals & assessments
- Ongoing Projects tracking
    - Track time of each progress increment
    - View 'burn-up' chart of completion progress over time
- Analysis
    - Show summary charts of all data reported to platform
    - Segment analysis of journals by tag (highlight journal days with/without + show averages)
- Google Assitant / Home / Facebook Messenger integration for actions like:
    - "How am I doing"
    - "What are my goals for this month"
    - "Mark 'run' as complete"
    - "Daily report"
- Reading widget
    - Show currently-reading articles / books
- Flash card widget for spreadsheet access (e.g. random quotes, excerpts)
- Export all data to CSV

## [(L)](https://github.com/onejgordon/flow-dashboard#integrations)Integrations

### [(L)](https://github.com/onejgordon/flow-dashboard#data-source-integrations)Data source integrations

- Public Github commits
- Google Fit - track any activity durations by keyword
- Evernote - pull excerpts from specified notebooks
- Pocket - Sync stored articles & add notes
- Goodreads - Sync currently reading shelf
- Track any abstract data via REST API

### [(L)](https://github.com/onejgordon/flow-dashboard#setup-for-separate-instance)Setup (for separate instance)

All integrations work out of the box on flowdash.co, but if you're spinning up your own instance, you'll need to set up each integration you need. See below for specific instructions.

#### [(L)](https://github.com/onejgordon/flow-dashboard#pocket)Pocket

Create an app at https://getpocket.com/developer/ and update settings.secrets.POCKET_CONSUMER_KEY

#### [(L)](https://github.com/onejgordon/flow-dashboard#evernote)Evernote

1. Request an API Key at [https://dev.evernote.com](https://dev.evernote.com/)

2. Request a webhook at https://dev.evernote.com/support/ pointing to [Your Domain]/api/integrations/evernote/webhook

#### [(L)](https://github.com/onejgordon/flow-dashboard#google-home)Google Home

We've used API.AI to create an agent that integrates with Google Actions / Assistant / Home. To connect Assistant with a new instance of Flow:

1. Visit [https://api.ai](https://api.ai/)
2. Update the agent.json configuration file in static/flow-agent

3. Fill in config params in [Brackets] with your configuration / webhook URLs, etc

4. Import the agent.json to API.AI
5. Go to integrations and add and authorize 'Actions on Google'
6. Preview the integration using the web preview

#### [(L)](https://github.com/onejgordon/flow-dashboard#facebook-messenger)Facebook Messenger

The messenger bot lives at https://www.facebook.com/FlowDashboard/

To create a new messenger bot for your own instance of Flow, see the Facebook quickstart: https://developers.facebook.com/docs/messenger-platform/guides/quick-start

#### [(L)](https://github.com/onejgordon/flow-dashboard#bigquery)BigQuery

(Beta / admin only currently) Push daily panel data to BigQuery for additional analysis, e.g. run regressions with TensorFlow, etc.

## [(L)](https://github.com/onejgordon/flow-dashboard#contributing)Contributing

Contributions are welcome! See [CONTRIBUTING.md](https://github.com/onejgordon/flow-dashboard/blob/develop/.github/CONTRIBUTING.md)