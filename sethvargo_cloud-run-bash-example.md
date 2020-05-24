sethvargo/cloud-run-bash-example

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='85'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='754' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/sethvargo/cloud-run-bash-example#cloud-run-server-in-bash)Cloud Run Server in Bash

[![68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f636c6f756472756e2f627574746f6e2e737667](../_resources/fe343745601fd209569bc0775e2e29aa.png)](https://deploy.cloud.run/)

This is a sample repository that runs a "server" in bash that can be deployed on Google Cloud Run.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='86'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='758' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/sethvargo/cloud-run-bash-example#setup)Setup

1. Enable Cloud Build and Cloud Run:
gcloud services enable --project "${PROJECT_ID}" \
cloudbuild.googleapis.com \
run.googleapis.com
2. Build the container:
gcloud builds submit \
--project "${PROJECT_ID}" \
--tag "gcr.io/${PROJECT_ID}/hello-world-bash" \ .
3. Deploy the container:
gcloud beta run deploy "hello-world-bash" \
--project "${PROJECT_ID}" \
--platform "managed" \
--region "us-central1" \
--image "gcr.io/${PROJECT_ID}/hello-world-bash"
4. That's it!