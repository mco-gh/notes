Making requests to Cloud Run with the Service account

# Making requests to Cloud Run with the Service Account

[![2*1SPuBB83vjwqBHL5mNzcuQ.jpeg](../_resources/701f2a216fa221489fa9dd6f49a486d5.jpg)](https://medium.com/@zdenulo?source=post_header_lockup)

[Zdenko Hrcek](https://medium.com/@zdenulo)
Apr 26·4 min read

Cloud Run is a new compute serverless solution on Google Cloud Platform. It can run any web app deployed as Docker image. One of the nice features it has is built in automatic authentication, i.e. you can hide service from public internet and control access via IAM. With this, you grant access to concrete users or groups. Since one of the primary uses of Cloud Run are microservices and with access control functionality it’s convenient to use it for internal microservices (which you want to be private), one of the ways how to do it is using Service Accounts.

In the [official documentation](https://cloud.google.com/run/docs/securing/authenticating#service-to-service), there is a description of how to use service to service authentication with code sample of making requests from Google Cloud where authentication credentials are obtained from metadata server thus no service accounts are required. Service Accounts are needed if you want to make requests to Cloud Run service outside of GCP. Now in the documentation, there are described steps how to do it, but with no code sample.

So in this article, I wanna describe how to set up Cloud Run service which is private and how to make requests using a service account. As an application, I created Docx to PDF converter, similar as it was presented in Cloud Next ’19 keynote. Service can be used also as Pub Sub HTTP target and used for asynchronous processing which I will describe in the next articles.

The full code of this example is in Github repository https://github.com/zdenulo/gcp-docx2pdf/tree/master/cloud_run_pubsub.

Regarding web service, there is nothing special about it, it’s cool that Libreoffice can be installed and used thanks to using Docker. Web service is tailored to accept json messages from Pub Sub, minimal POST request needs to be in the following format:

{
"message":{
"attributes":{
"bucketId":"BUCKET-ID",
"objectId":"FILE-PATH"
}
}
}

Service expects a Docx file that needs to be converted to be stored in Cloud Storage thus bucket and filename (path) are necessary as inputs.

To build and deploy service Cloud Build is used with configuration file cloudbuild.yaml

steps:

# build the container image

- name: 'gcr.io/cloud-builders/docker'

args: ['build', '-t', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${TAG_NAME}', '.']

# push the container image to Container Registry

- name: 'gcr.io/cloud-builders/docker'

args: ['push', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}']

# Deploy container image to Cloud Run

- name: 'gcr.io/cloud-builders/gcloud'

args: ['beta', 'run', 'deploy', '${_SERVICE_NAME}', '--image', 'gcr.io/$PROJECT_ID/${_SERVICE_NAME}:${TAG_NAME}', '--region', 'us-central1', '--memory', '1Gi', '--update-env-vars', '${_ENV_VARIABLES}']

images:

- gcr.io/$PROJECT_ID/${_SERVICE_NAME}

Service expects that environmental variable OUTPUT_BUCKET (which is the name of the bucket where PDF will be saved) to be set, which is done during deployment. Also, the name of Cloud Run service needs to be defined.

Build and deployment are initiated with the command:

gcloud builds submit --config=cloudbuild.yaml --substitutions=_SERVICE_NAME="<service name>",TAG_NAME="v0.1",_ENV_VARIABLES="OUTPUT_BUCKET=<name of output bucket>"

Cloud Run service is by default deployed as private.

Next step is to create a service account and assign a specific role. To create a service account with name cr-test I’ll execute the command:

~>gcloud iam service-accounts create cr-test --display-name="Cloud Run Test"
Created service account [cr-test].

Then as official documentation says, I’ll add to service account role Cloud Run Invoker which is necessary to make requests to Cloud Run service:

~> gcloud beta run services add-iam-policy-binding sa-run --member=serviceAccount:cr-test@adventures-on-gcp.iam.gserviceaccount.com --role=roles/run.invoker

Updated IAM policy for service [sa-run].
bindings:

- members:
- serviceAccount:cr-test@adventures-on-gcp.iam.gserviceaccount.com

role: roles/run.invoker
etag: BwWHWbhxA2c=

Another way is to add IAM policy binding to that Service Account. With this, Service Account will be displayed in the IAM section and you can assign it multiple roles if necessary.

gcloud projects add-iam-policy-binding <PROJECT-ID> --member=serviceAccount:cr-test@adventures-on-gcp.iam.gserviceaccount.com --role=roles/run.invoker

The last step is to create a private key file (in my case I called it cr-test-secret.json) and download it locally to make a request from local computer to Cloud Run service:

gcloud iam service-accounts keys create cr-test-secret.json --iam-account=cr-test@adventures-on-gcp.iam.gserviceaccount.com

The code to make a request in Python using service account credentials is in file api_request.py and has few lines, BUCKET_NAME and API_URL need to be set appropriately.

from google.oauth2 import service_account
from google.auth.transport.requests import AuthorizedSession

SERVICE_FILENAME = 'cr-test-secret.json'
BUCKET_NAME = '' # name of the bucket where Docx file is saved
API_URL = '' # change to url of you Cloud Run service

audience = API_URL

credentials = service_account.IDTokenCredentials.from_service_account_file(SERVICE_FILENAME, target_audience=audience)

session = AuthorizedSession(credentials)

data = {"message": {"attributes": {"bucketId": BUCKET_NAME, "objectId": "demo.docx"}}}

r = session.post(API_URL, json=data)
print(r.text)

The most important thing here is to be careful which class to use from the service_accounts module. I usually use **Credentials.from_service_account()** but in this case, **IDTokenCredentials** class is required. Difference between the two as written in documentation is “These credentials are largely similar to Credentials class, but instead of using an OAuth 2.0 Access Token as the bearer token, they use an Open ID Connect ID Token as the bearer token. These credentials are useful when communicating to services that require ID Tokens and cannot accept access tokens.”

AuthorizedSession is basically a wrapper around “request” library to make requests with correct headers.