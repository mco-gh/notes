jamesward/cloud-run-button

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='47'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='658' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/jamesward/cloud-run-button#cloud-run-button)Cloud Run Button

Your own fancy button that uses Cloud Shell to deploy a git repo to Cloud Run in two clicks.

Like this:

[![68747470733a2f2f73746f726167652e676f6f676c65617069732e636f6d2f636c6f756472756e2f627574746f6e2e706e67](../_resources/f64454b03ac2ead234462307d0830cf2.png)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=https://github.com/jamesward/cloud-run-button.git)

To add a Cloud Run deploy button to your project's readme:
1. Copy & paste this markdown:

	[![Run on Google Cloud](https://storage.googleapis.com/cloudrun/button.png)](https://console.cloud.google.com/cloudshell/editor?shellonly=true&cloudshell_image=gcr.io/cloudrun/button&cloudshell_git_repo=YOUR_HTTP_GIT_URL)

2. Replace `YOUR_HTTP_GIT_URL` with your HTTP git URL, like: `https://github.com/jamesward/hello-kotlin-ktor.git`

3. Make sure the repo is buildable on Google Cloud Build and its build config publishes a container to the Google Container Repository. If you use a `cloudbuild.yaml` file, the publishing config must use `PROJECT_ID` and `REPO_NAME` parameters.