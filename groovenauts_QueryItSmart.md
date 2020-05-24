groovenauts/QueryItSmart

# [(L)](https://github.com/groovenauts/QueryItSmart#queryit-smart)QueryIt Smart

QueryIt Smart is the demonstration application where it combines [BigQuery](http://cloud.google.com/bigquery) for large scale data analytics and [Cloud Machine Learning Engine](http://cloud.google.com/ml) for scalable machine learning analytics. See [What is it?](https://github.com/groovenauts/QueryItSmart/blob/master/whatisit.md) page for details of the technology.

## [(L)](https://github.com/groovenauts/QueryItSmart#preparation)Preparation

### [(L)](https://github.com/groovenauts/QueryItSmart#service-account-json-key)Service Account JSON key

You need to have a Google Cloud Platform project and get service account's JSON key. Pleace it to ` config/service_account.json `.

### [(L)](https://github.com/groovenauts/QueryItSmart#api-key)API Key

For Map API used in demand forecast, you should generate API key from Google Cloud Developers Console.

## [(L)](https://github.com/groovenauts/QueryItSmart#build-docker-image)Build Docker Image

	docker build -t queryit-smart:latest .

## [(L)](https://github.com/groovenauts/QueryItSmart#run)Run

At the top directory of this project, run the following command. Please replace ` MY_API_KEY ` with your API Key generated in Setup section. Replace ` MY_USER ` and ` MY_PASS ` with your user/password for HTTP basic authentication.

	docker run -d -v $PWD/config:/usr/app/config -p 8080:8080 -e BASIC_USER=MY_USER -e BASIC_PASSWORD=MY_PASS -e API_KEY=MY_API_KEY queryit-smart:latest

Open ` http://localhost:8080 ` (if you use Virtual Machine or CCE to run docker container, replace ` localhost ` with your VM address) in browser.

## [(L)](https://github.com/groovenauts/QueryItSmart#modify-datasets)Modify datasets

See [models/README.md](https://github.com/groovenauts/QueryItSmart/blob/master/models/README.md) to know how to customize datasets for Image search and Document search.