Uncovering the Magic of Click-to-Deploy for Cloud Run

# **Uncovering the Magic of Click-to-Deploy for Cloud Run**

[![0*xwPS49PrXvGYvJG8.jpeg](../_resources/5ba3d619c81a68f6836c602193733865.jpg)](https://medium.com/@_jamesward?source=post_page-----52d6ac79f6e1----------------------)

[James Ward](https://medium.com/@_jamesward?source=post_page-----52d6ac79f6e1----------------------)

[Jan 21](https://medium.com/google-cloud/uncovering-the-magic-of-click-to-deploy-for-cloud-run-52d6ac79f6e1?source=post_page-----52d6ac79f6e1----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='193'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='194' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/52d6ac79f6e1/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='197'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='198' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/52d6ac79f6e1/share/facebook?source=post_actions_header---------------------------)

I love using a command line but when I want to give something a quick spin I don’t always want to install tools and then copy & paste a bunch of commands. I’d rather just click a button. That is exactly what Cloud Run Button does for deploying GitHub repos on Cloud Run. Check it out:

![1*GviiWQyuNoDjd0hSwIAqHQ.gif](../_resources/ad3ae5e82bf7156b4f6b10f565f190ba.jpg)
![1*GviiWQyuNoDjd0hSwIAqHQ.gif](../_resources/f533a0330372925c5a2d20120cfa7f91.gif)

Any GitHub repo containing a serverless app can enable the Cloud Run Button simply by adding the following markdown to the `README.md` file:

`[![Run on Google Cloud](https://deploy.cloud.run/button.svg)](https://deploy.cloud.run)`

When a user clicks the button it will launch Cloud Shell and do a bunch of magic to make those “quick spins” easier. To skip right to the actual docs, check out the [GitHub repo for Cloud Run Button](https://github.com/GoogleCloudPlatform/cloud-run-button). If you are still reading, let’s walk through all the stuff that Cloud Run Button does.

**1. Git Clone**

The repo the button was clicked from is cloned into a temporary Cloud Shell environment. A branch and subdirectory can be manually specified, or it will be automatically detected based on the referrer URL.

**2. Parse app.json**

Sometimes a repo needs to configure some things about how the Button will build and deploy the project. Following the [Heroku Button’s app settings style](https://devcenter.heroku.com/articles/app-json-schema), those settings are specified in an `app.json` file in the project directory. There are a bunch of settings we will walk through in a minute, but the one to point out here is that the Cloud Run service name and Container Registry image name can be set using a `name` field. ([Check out the full docs for Cloud Run Button’s app.json settings](https://github.com/GoogleCloudPlatform/cloud-run-button#customizing-deployment-parameters).)

**3. Project Setup / Selection**

Everything in Google Cloud Platform is part of a “project” thus users need to select a project. There is a nice project selector if the user already has a bunch. If the user doesn’t have a project, the Button helps them do that.

**4. Billing Account Verification**

To deploy apps on Cloud Run you need to have a billing account setup, even if you won’t actually get charged anything because you are in the [Cloud Run free tier](https://cloud.google.com/run/pricing#pricing_table), or using some of your [free trial credits](https://cloud.google.com/free/docs/gcp-free-tier). Cloud Run Button verifies that you have a billing account associated with your project and if not, it helps you set one up.

**5. Cloud Run API**

For Cloud Run Button to deploy an app on Cloud Run, it needs to enable the Cloud Run API. So it does that if needed.

**6. Region Selection**

Google Cloud Platform is organized into regions which are made up of zones delineating network segments and Service Level Agreements. Cloud Run is regional as it is automatically redundant across the underlying zones of a given region. You can [select from a number of regions](https://cloud.google.com/run/docs/locations) to deploy your app in, so the Button prompts the user for the region.

**7. Environment Variables**

Cloud Run uses environment variables for configuration and so a project’s `app.json` file can specify those. The values can either be generated randomly or the Button will prompt the user for the values. ([Check out the full docs for Cloud Run Button’s app.json settings](https://github.com/GoogleCloudPlatform/cloud-run-button#customizing-deployment-parameters).)

**8. Build the project**

The Button will now build the project from source into a container image since that is the format needed for Cloud Run. First the Button checks for a `Dockerfile` and if it finds one it builds it with Docker. If there wasn’t a `Dockerfile` then the Button checks for a Maven (Java build tool) project that has the Jib plugin (Java build tool plugin for creating container images) setup. In that case it runs the Maven Jib build task to build the container image. If there wasn’t a Maven Jib-enabled project, then the final thing the Button tries is to build the project using the [Cloud Native Buildpacks](https://buildpacks.io/) via the Heroku Buildpacks which can build most Java, Python, Node, Ruby, Go, and PHP projects.

**9. Push Container Image**

Cloud Run needs the container image to be in the Google Container Registry so unless the build step did the push, the Button pushes it from the local docker daemon (i.e. it uploads it from Cloud Shell to GCR).

**10. Run Pre-Deployment Hook Commands**

A project’s `app.json` file can specify commands that will be run before the Cloud Run service is created. Those scripts are run if the service does not yet exist (Note: The Button can deploy a new version of an existing service too.)

**11. Deploy Cloud Run Service**

The project is now deployed to Cloud Run using the container image in GCR! This sets the environment variables and options (currently just whether or not to allow unauthenticated requests) on the new service.

**12. Run Post-Deployment Hook Commands**

Just like the precreate commands, if postcreate commands are specified in `app.json` then those are run. This can be used for provisioning other resources like storage buckets, Cloud SQL instances, service accounts, etc. These commands can use the gcloud command to add new env vars or change other settings on the newly deployed service.