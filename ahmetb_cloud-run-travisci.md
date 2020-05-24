ahmetb/cloud-run-travisci

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='137'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='897' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#google-cloud-run--travis-ci)Google Cloud Run + Travis CI

This repository shows how to use [Travis CI](https://www.travis-ci.com/) to build a container image and deploy it to [Google Cloud Run](https://cloud.google.com/run) when you push a new commit.

[![logo.png](../_resources/3355a6ab694d4a2330504c87426a2540.png)](https://github.com/ahmetb/cloud-run-travisci/blob/master/logo.png)

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='138'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='901' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#table-of-contents)Table of Contents

- [Step 0: Fork this repository](https://github.com/ahmetb/cloud-run-travisci/#step-0-fork-this-repository)
- [Step 1: Sign up to Travis CI](https://github.com/ahmetb/cloud-run-travisci/#step-1-sign-up-to-travis-ci)
- [Step 1: Install required tools](https://github.com/ahmetb/cloud-run-travisci/#step-1-install-required-tools)
- [Step 2: Create a service account for deploying](https://github.com/ahmetb/cloud-run-travisci/#step-2-create-a-service-account-for-deploying)
- [Step 3: Assign permissions to the service account](https://github.com/ahmetb/cloud-run-travisci/#step-3-assign-permissions-to-the-service-account)
- [Step 4: Encrypt the service account key](https://github.com/ahmetb/cloud-run-travisci/#step-4-encrypt-the-service-account-key)
- [Step 5: Configure your project ID](https://github.com/ahmetb/cloud-run-travisci/#step-5-configure-your-project-id)
- [Step 6: Commit the changes to your fork](https://github.com/ahmetb/cloud-run-travisci/#step-6-commit-the-changes-to-your-fork)
- [Step 7: View build result](https://github.com/ahmetb/cloud-run-travisci/#step-7-view-build-result)
- [Step 8: Clean up](https://github.com/ahmetb/cloud-run-travisci/#step-8-clean-up)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='139'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='914' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-0-fork-this-repository)Step 0: Fork this repository

1. Scroll up and click **"Fork"** so you can try pushing commits and testing builds.

2. **Clone** the repository on your machine.
3. Go to the `cloud-run-travisci` directory you cloned.

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='140'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='920' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-1-sign-up-to-travis-ci)Step 1: Sign up to Travis CI

Sign up at [www.travis-ci.com](https://www.travis-ci.com/) and enable **Travis CI** app on your forked`cloud-run-travisci` repository athttps://www.travis-ci.com/account/repositories.

> Note: If you have an travis-ci**> .org**>  account instead of .com, replace`--pro`>  arguments in this tutorial with `--org`> .

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='141'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='925' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-1-install-required-tools)Step 1: Install required tools

- Google Cloud SDK (`gcloud`): https://cloud.google.com/sdk
- `travis` command-line tool:

sudo gem install travis
travis login --pro # (use --org if you're on travis-ci.ORG and not .COM)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='142'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='934' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-2-create-a-service-account-for-deploying)Step 2: Create a service account for deploying

To authenticate to GCP APIs from Travis CI build environment you will need a[service account](https://cloud.google.com/iam/docs/understanding-service-accounts).

PROJECT_ID="$(gcloud config get-value project -q)"  # fetch current GCP project ID

SVCACCT_NAME=travisci-deployer # choose name for service account
Create a service account:
gcloud iam service-accounts create "${SVCACCT_NAME?}"
Find the email address of this account:

SVCACCT_EMAIL="$(gcloud iam service-accounts list \ --filter="name:${SVCACCT_NAME?}@" \ --format=value\(email\))"

Create a JSON key to authenticate as this service account, and save it as`google-key.json`:

gcloud iam service-accounts keys create "google-key.json" \
--iam-account="${SVCACCT_EMAIL?}"

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='143'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='947' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-3-assign-permissions-to-the-service-account)Step 3: Assign permissions to the service account

You need to give these IAM roles to the service account created:

1. **Storage Admin:** Used for pushing docker images to Google Container Registry (GCR).

2. **Cloud Run Admin:** Used for deploying services to Cloud Run.

3. **IAM Service Account user:** Required by Cloud Run to be able to "act as" the runtime identity of the Cloud Run application (in this case, our deployer service account needs to able to "act as" the GCE default service account).

gcloud projects add-iam-policy-binding "${PROJECT_ID?}" \
--member="serviceAccount:${SVCACCT_EMAIL?}" \
--role="roles/storage.admin"
gcloud projects add-iam-policy-binding "${PROJECT_ID?}" \
--member="serviceAccount:${SVCACCT_EMAIL?}" \
--role="roles/run.admin"
gcloud projects add-iam-policy-binding "${PROJECT_ID?}" \
--member="serviceAccount:${SVCACCT_EMAIL?}" \
--role="roles/iam.serviceAccountUser"

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='144'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='957' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-4-encrypt-the-service-account-key)Step 4: Encrypt the service account key

Run the following command
travis encrypt-file --pro google-key.json
This command will print an `openssl [...]` command, **don’t lose it!**

Edit the `.travis.yml` file, and add this commmand to the `before_install` step:

before_install:-- echo REMOVE_ME # replace with the openssl command from "travis encrypt-file"+- openssl aes-256-cbc -K $encrypted_fbfaf42b268c_key -iv $encrypted_fbfaf42b268c_iv -in google-key.json.enc -out google-key.json -d - curl https://sdk.cloud.google.com | bash > /dev/null

...

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='145'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='964' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-5-configure-your-project-id)Step 5: Configure your project ID

Edit the `.travis.yml` and configure the environment variables under the `env:`key (such as `GCP_PROJECT_ID`, `IMAGE`, and `CLOUD_RUN_SERVICE`).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='146'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='967' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-6-commit-the-changes-to-your-fork)Step 6: Commit the changes to your fork

⚠️ Do not add `google-key.json` file to your repository as it can be reached by others.

Make a commit, and push the changes to your fork:
git add google-key.json.enc .travis.yml
git commit -m "Enable Travis CI"
git push -u origin master

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='147'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='975' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-7-view-build-result)Step 7: View build result

Go to [www.travis-ci.com](https://www.travis-ci.com/) and view your build results.

There might be errors that require you to fix.

If the build succeeds, the output of `gcloud run beta deploy` command will show you the URL your app is deployed on! Visit the URL to see if the application works!

	[...]
	Deploying container to Cloud Run service [example-app] in project [...] region [us-central1]
	Deploying new service...
	Setting IAM Policy.....done
	Creating Revision......done
	Routing traffic........done
	Done.
	Service [example-app] revision [example-app-00001] has been deployed
	and is serving traffic at https://example-app-pwfuv4g72q-uc.a.run.app

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='148'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='980' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/ahmetb/cloud-run-travisci/#step-8-clean-up)Step 8: Clean up

Delete the service account you created:
gcloud iam service-accounts delete "${SVCACCT_EMAIL?}"
Delete the Cloud Run application you deployed:
gcloud beta run services delete "YOUR-APP-NAME"

* * *

**Did this tutorial work for you?** Click "✭Star" on the top right of this page and let me know!