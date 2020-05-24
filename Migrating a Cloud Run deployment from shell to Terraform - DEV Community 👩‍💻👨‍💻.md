Migrating a Cloud Run deployment from shell to Terraform - DEV Community 👩‍💻👨‍💻

 [

 [c7814399-cf4a-4dc9-9f12-d0a97ed21bf6.webp](../_resources/882287536aafabdde3e930658e35e311.webp) Google Cloud](https://dev.to/googlecloud)

#  Migrating a Cloud Run deployment from shell to Terraform

###     [  [078c6167-7b77-47d5-bc3a-eed0cf2e89e2.webp](../_resources/d7cbee094c367e9fcd0ef1ce1c22b226.webp)  Katie McLaughlin](https://dev.to/glasnt)    [![twitter-logo-fe34f4c4c24dabe47c2b59aeb1397d6ae56b0501a1320f20ac523dd84230d789.png](../_resources/ed42b3b97be139bb18e7cdaa03aa9471.png)](http://twitter.com/glasnt)  [![github-logo-28d89282e0daa1e2496205e2f218a44c755b0dd6536bbadf5ed5a44a7ca54716.png](../_resources/f6d80f2bef7c541958d040b7f06e290c.png)](http://github.com/glasnt)  Apr 20  *Updated on Apr 27, 2020*  ・9 min read

 [#googlecloud](https://dev.to/t/googlecloud)  [#terraform](https://dev.to/t/terraform)

There are many ways you can automate deployment of your infrastructure. It's perfectly valid to have a shell script that runs a series of create commands, but those commands themselves may not work too well when the entities they are trying to create already exist. So you could update that script to first check that the item already exists, and if not, create it. But then it won't work if you have any attribute updates you want to make. When you start including variables and preconditions into the mix, you end up with a script that is complicated and hard to debug.

This is where infrastructure automation comes in, and Infrastructure as Code (IaC). Using one of the many IaC tools available, you can make configurations that allow you to ensure your infrastructure is deployed reliably and cleanly, asserting configuration changes as required, in a way that is repeatable across your project.

In this post we'll show you how we can convert a shell script deployed Cloud Run service to a Terraform manifest, with all the considerations that involves.

* * *

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#the-demo-application) The demo application

Today's demo application is going to be a base Hello World in Flask, which greets the value of 'TARGET', along with a Dockerfile to containerise it.

|     |     |
| --- | --- |
| 1   | import  os |
| 2   |     |
| 3   | from  flask  import  Flask |
| 4   |     |
| 5   | app  =  Flask(__name__) |
| 6   |     |
| 7   | @app.route('/') |
| 8   | def  hello_world(): |
| 9   |  target  =  os.environ.get('TARGET', 'World') |
| 10  |  return  'Hello {}!\n'.format(target) |
| 11  |     |
| 12  | if  __name__  ==  "__main__": |
| 13  |  app.run(debug=True,host='0.0.0.0',port=int(os.environ.get('PORT', 8080))) |

 [view raw](https://gist.github.com/glasnt/4db553e7f680784e8b910ca6de67c85b/raw/85b3688f90ad00f2f6f7ac9d20d8c32270b96f9b/app.py)  [app.py](https://gist.github.com/glasnt/4db553e7f680784e8b910ca6de67c85b#file-app-py) hosted with ❤ by [GitHub](https://github.com/)

|     |     |
| --- | --- |
| 1   | # Use the official lightweight Python image. |
| 2   | # https://hub.docker.com/_/python |
| 3   | FROM python:3.7-slim |
| 4   |     |
| 5   | # Copy local code to the container image. |
| 6   | ENV APP_HOME /app |
| 7   | WORKDIR $APP_HOME |
| 8   | COPY . ./ |
| 9   |     |
| 10  | # Install production dependencies. |
| 11  | RUN pip install Flask gunicorn |
| 12  |     |
| 13  | # Run the web service on container startup. Here we use the gunicorn |
| 14  | # webserver, with one worker process and 8 threads. |
| 15  | # For environments with multiple CPU cores, increase the number of workers |
| 16  | # to be equal to the cores available. |
| 17  | CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app |

 [view raw](https://gist.github.com/glasnt/4db553e7f680784e8b910ca6de67c85b/raw/85b3688f90ad00f2f6f7ac9d20d8c32270b96f9b/Dockerfile)  [Dockerfile](https://gist.github.com/glasnt/4db553e7f680784e8b910ca6de67c85b#file-dockerfile) hosted with ❤ by [GitHub](https://github.com/)

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#the-original-shell-script) The original shell script

To start, here's a shell script we prepared earlier -- using `[gcloud](https://cloud.google.com/sdk/install)`, it configures and deploys a Cloud Run service to a project [we've already set up](https://cloud.google.com/run/docs/quickstarts/build-and-deploy#before-you-begin) with [billing enabled](https://cloud.google.com/billing/docs/how-to/modify-project), and the script works! ...mostly.

	#!/bin/bash
	export PROJECT_ID=glasnt-playground
	gcloud config set project $PROJECT_ID

	gcloud services enable run.googleapis.com

	git clone https://gist.github.com/4db553e7f680784e8b910ca6de67c85b.git helloworld

	cd helloworld

	gcloud builds submit --tag gcr.io/${PROJECT_ID}/helloworld .

	gcloud run deploy helloworld \
	   --platform managed \
	   --image gcr.io/${PROJECT_ID}/helloworld \
	   --update-env-vars TARGET=gcloud \
	   --allow-unauthenticated

Once deployed the service displays a hello message to the value of TARGET. We can get the service URL by describing the service, then using `curl`:

	$ SERVICE_URL=$(gcloud run services describe helloworld --format "value(status.url)")
	$ curl $SERVICE_URL
	Hello gcloud!

There are a few non-obvious problems with this script:

- it only enables the Cloud Run API; this script also needs the Cloud Build API to be enabled, which is interactively asked for if it's not enabled when you run `gcloud builds submit` commands, thus breaking the automation by requiring human feedback.
- it doesn't check if the Cloud Run API has already been enabled, wasting time asking for it to be re-enabled.
- there are no checks if the service already exists, and it automatically forces the service to be public (which is a problem if it already exists and is private)
- it doesn't define a region for the service, which if a region hasn't already been defined in the `gcloud config`, will cause the script to interactively ask for a region, which will break the automation loop by requiring human feedback.

We can work around some of these issues, and generally make our provisioning more robust, by converting this shell script into a Terraform manifest.

The rest of the post will explore that process. Some of the Terraform output assumes the original service already exists, so if you don't get the errors I get, then don't worry ✨

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#setup-terraform) Setup Terraform

Before we begin, we need to install and configure Terraform. Follow the [installation instructions for your platform](https://learn.hashicorp.com/terraform/getting-started/install.html) (macOS users can `brew install terraform`). Check that it's all installed by checking the Terraform version:

	$ terraform version
	Terraform v0.12.24

For authentication, it's [recommended](https://www.terraform.io/docs/providers/google/guides/provider_reference.html#credentials-1) that we use a service account, so let's create one, then export a private key that Terraform can then use to act as this service account:

	# Set the project ID
	export PROJECT_ID=glasnt_playground
	gcloud config set project $PROJECT_ID

	# Create the service account
	gcloud iam service-accounts create terraform \
	    --display-name "Terraform Service Account"

	# Grant role
	gcloud projects add-iam-policy-binding ${PROJECT_ID} \
	  --member serviceAccount:terraform@${PROJECT_ID}.iam.gserviceaccount.com \
	  --role roles/editor

	# create and save a local private key
	gcloud iam service-accounts keys create ~/terraform-key.json \
	  --iam-account terraform@${PROJECT_ID}.iam.gserviceaccount.com

	# store location of private key in environment that terraform can use
	export GOOGLE_APPLICATION_CREDENTIALS=~/terraform-key.json

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#build-the-image) Build the image

There are some things that Terraform can't do natively. One of those is building images.

So before we can define our service, we'll have to make sure we have an image ready. If you are following along and haven't got an image yet, you'd run:

	$ git clone https://gist.github.com/4db553e7f680784e8b910ca6de67c85b.git helloworld

	$ cd helloworld
	$ gcloud builds submit --tag gcr.io/${PROJECT_ID}/helloworld

Once this completes, we can confirm we have an image ready for use:

	$ gcloud builds list --filter "images ~ hello" --sort-by "~create_time" --limit 1 \
	 --format "table[no-heading](images[0])"
	gcr.io/glasnt-playground/helloworld

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#create-the-manifest) Create the manifest

We now need to define our Terraform manifest. Google Cloud resources are provided using the [Google Cloud Terraform provider](https://www.terraform.io/docs/providers/google/), where we'll define our [Cloud Run service](https://www.terraform.io/docs/providers/google/r/cloud_run_service.html). The sample code for the resource types is very helpful to understand how to define resources.

In our example, we take the sample service, and substitute in the values from our original shell, including the explicit definition for the Terraform provider we need, and our environment variables.

|     |     |
| --- | --- |
| 1   | # local variables |
| 2   | locals { |
| 3   | project =  "YOUR_PROJECT_ID" |
| 4   | region =  "us-central1" |
| 5   | }   |
| 6   |     |
| 7   | # setting the google cloud provider version |
| 8   | terraform { |
| 9   |  required_providers { |
| 10  | google =  "~> 3.16.0" |
| 11  | }   |
| 12  | }   |
| 13  |     |
| 14  | # setting the project value cross the different resources |
| 15  | provider  google { |
| 16  | project =  local.project |
| 17  | }   |
| 18  |     |
| 19  | # the service itself |
| 20  | resource  google_cloud_run_service  helloworld { |
| 21  | name =  "helloworld"  # useful to match the resource name, but doesn't have to match. |
| 22  | location =  local.region  # location is the region, in this context |
| 23  |     |
| 24  |  # allows for automatic incrementing |
| 25  | autogenerate_revision_name =  "true" |
| 26  |     |
| 27  |  template { |
| 28  |  spec { |
| 29  |  containers { |
| 30  |  # the image we prepared earlier |
| 31  | image =  "gcr.io/${local.project}/helloworld" |
| 32  | }   |
| 33  | }   |
| 34  | }   |
| 35  | }   |
| 36  |     |
| 37  | # the permissions required to replicate "Allow unauthenticated" |
| 38  | data  "google_iam_policy"  "noauth" { |
| 39  |  binding { |
| 40  | role =  "roles/run.invoker" |
| 41  | members = [ |
| 42  |  "allUsers", |
| 43  | ]   |
| 44  | }   |
| 45  | }   |
| 46  |     |
| 47  | # actually applying the policy to the service |
| 48  | resource  "google_cloud_run_service_iam_policy"  "noauth" { |
| 49  | location = google_cloud_run_service.helloworld.location |
| 50  | project = google_cloud_run_service.helloworld.project |
| 51  | service = google_cloud_run_service.helloworld.name |
| 52  |     |
| 53  | policy_data =  data.google_iam_policy.noauth.policy_data |
| 54  | }   |

 [view raw](https://gist.github.com/glasnt/fd42d19502d30965954115f38ba270de/raw/516418c8feaf131ca59c645d4f0eea6b85324b83/main.tf)  [main.tf](https://gist.github.com/glasnt/fd42d19502d30965954115f38ba270de#file-main-tf) hosted with ❤ by [GitHub](https://github.com/)

Take a copy of this `main.tf` file into a new folder on your machine to follow along in the following steps. **Make sure you edit the file to use your project ID!**

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#deploy-the-service) Deploy the service

First time you run Terraform against a new manifest, you need to run the `init` command.

	$ terraform init

This will initialise Terraform for this particular manifest. Exactly what it does is output for us each time:

	Initializing the backend...

	Initializing provider plugins...

	- Checking for available provider plugins...
	- Downloading plugin for provider "google" (hashicorp/google) 3.16.0...

	Terraform has been successfully initialized!

	You may now begin working with Terraform. Try running "terraform plan" to see
	any changes that are required for your infrastructure. All Terraform commands
	should now work.

	If you ever set or change modules or backend configuration for Terraform,
	rerun this command to reinitialize your working directory. If you forget, other
	commands will detect it and remind you to do so if necessary.

The first time you run Terraform, this level of output may seem over the top, or even overwhelming. But take a moment to read what it's doing.

From here, we can plan what Terraform will do:

	$ terraform plan
	Refreshing Terraform state in-memory prior to plan...
	The refreshed state will be used to calculate this plan, but will not be
	persisted to local or remote state storage.

	data.google_iam_policy.noauth: Refreshing state...

	------------------------------------------------------------------------

	An execution plan has been generated and is shown below.
	Resource actions are indicated with the following symbols:
	  + create

	Terraform will perform the following actions:

	  # google_cloud_run_service.helloworld will be created
	  + resource "google_cloud_run_service" "helloworld" {

	...

	  # google_cloud_run_service_iam_policy.noauth will be created
	  + resource "google_cloud_run_service_iam_policy" "noauth" {

	...

	Plan: 2 to add, 0 to change, 0 to destroy.

	------------------------------------------------------------------------

	Note: You didn't specify an "-out" parameter to save this plan, so Terraform
	can't guarantee that exactly these actions will be performed if
	"terraform apply" is subsequently run.

This will show us exactly what Terraform plans to do. You should check to see what it expects to do. You can also see what properties will be made available after it exists.

We can now apply the manifest, as we tried to before:

	$ terraform apply
	...

	Plan: 2 to add, 0 to change, 0 to destroy.

	Do you want to perform these actions?
	  Terraform will perform the actions described above.
	  Only 'yes' will be accepted to approve.

	  Enter a value:

Terraform will only continue if we enter in exactly `yes`. The output before the confirmation will be the same as the `terraform plan`, so you don't need to re-run `plan` to see this output.

We can also skip this manual confirmation step by adding "`[-auto-approve](https://www.terraform.io/docs/commands/apply.html#auto-approve)`" to our `terraform apply` command.

But for now, we should tell Terraform we're sure:

	Do you want to perform these actions?
	  Terraform will perform the actions described above.
	  Only 'yes' will be accepted to approve.

	  Enter a value: yes▊

	google_cloud_run_service.helloworld: Creating...

	Error: Error creating Service: googleapi: Error 409: Resource 'helloworld' already exists.

	  on main.tf line 11, in resource "google_cloud_run_service" "helloworld":
	  11: resource "google_cloud_run_service" "helloworld" {

Uh oh.

Well, this is to be expected. We created our service with a shell script; Terraform wasn't to know it already existed until it tried to recreate it.

From here we have two options:

- delete the service and get Terraform to re-create it
- tell Terraform about the service, and then have it reconcile any differences.

The first method would be a case of running `gcloud run service delete helloworld`, but let's do it the smarter way.

When Terraform returns an `Error 409: Resource already exists`, it means that Terraform's local state doesn't match the project state. We can fix this by importing the state of our resource.

We want to make sure that Terraform is aware that the resource `google_cloud_run_service helloworld` maps to the real world Cloud Run service `helloworld` in region `us-central1` under our project.

To do that, we can follow the hints from the [import](https://www.terraform.io/docs/providers/google/r/cloud_run_service.html#import) section of the documentation. Some gotchas here:

- They define their only Cloud Run service as `default`; we named ours `helloworld`.
- We both defined a location as being the region, `us-central1`.

Therefore, we can import our existing state by running:

	$ terraform import google_cloud_run_service.helloworld us-central1/helloworld

	google_cloud_run_service.helloworld: Importing from ID "us-central1/helloworld"...
	google_cloud_run_service.helloworld: Import prepared!
	  Prepared google_cloud_run_service for import
	google_cloud_run_service.helloworld: Refreshing state... [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld]

	Import successful!

	The resources that were imported are shown above. These resources are now in
	your Terraform state and will henceforth be managed by Terraform.

So now we can try that manifest again:

	$ terraform apply

	Plan: 1 to add, 1 to change, 0 to destroy.

	Do you want to perform these actions?
	  Terraform will perform the actions described above.
	  Only 'yes' will be accepted to approve.

	  Enter a value: yes

	google_cloud_run_service.helloworld: Modifying... [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld]
	google_cloud_run_service.helloworld: Modifications complete after 6s [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld]
	google_cloud_run_service_iam_policy.noauth: Creating...
	google_cloud_run_service_iam_policy.noauth: Creation complete after 4s [id=v1/projects/glasnt-playground/locations/us-central1/services/helloworld]

	Apply complete! Resources: 1 added, 1 changed, 0 destroyed.

We can check the service with `curl`:

	$ curl $SERVICE_URL
	Hello World!

Hello... world? Ah, we didn't add a `TARGET`, so it no longer displays `gcloud`, so we know the service was re-deployed!

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#deploy-the-service) Deploy the service

Yes, we're doing this again.

Because one of the brilliant things about this setup is that you can re-apply the configurations to return the state (if changed), even if the items already exist.

You should be able to run `terraform apply` at any point, which will re-assert our configurations.

	$ terraform apply

	...
	Apply complete! Resources: 0 added, 0 changed, 0 destroyed.

There are no modifications required, so there was no change to be made!

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#update-the-service) Update the service

In order to make changes, we need to change the manifest. Let's set a value for `TARGET`:

	     spec {ye
	       containers {
	         image = "gcr.io/${local.project}/helloworld"
	+        env {
	+          name = "TARGET"
	+          value = "terraform"
	+        }
	       }
	     }
	   }

We can then run Terraform again and see the pending change:

	$ terraform apply

	google_cloud_run_service.helloworld: Refreshing state... [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld]

	An execution plan has been generated and is shown below.
	Resource actions are indicated with the following symbols:
	  ~ update in-place

	Terraform will perform the following actions:

	...
	          ~ spec {
	                container_concurrency = 80

	              ~ containers {
	                    args    = []
	                    command = []
	                    image   = "gcr.io/glasnt-playground/helloworld"

	                  + env {
	                      + name  = "TARGET"
	                      + value = "terraform"
	                    }
	...

and apply the change:

	  Enter a value: yes

	google_cloud_run_service.helloworld: Modifying... [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld]
	google_cloud_run_service.helloworld: Still modifying... [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld, 10s elapsed]
	google_cloud_run_service.helloworld: Modifications complete after 19s [id=locations/us-central1/namespaces/glasnt-playground/services/helloworld]

	Apply complete! Resources: 0 added, 1 changed, 0 destroyed.

Yay! ✨
We can see that the service deployed successfully by checking the URL:

	$ curl $SERVICE_URL
	Hello terraform!

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#automatically-deploying-the-service) Automatically deploying the service

One of the added benefits is that we can use this configuration in our deployment pipeline. Your project may not require this step, but it's always an option if that suits your deployment strategy.

Instead of manually running Terraform, we can replace the `gcloud run deploy` step of a standard [Cloud Run deployment in Cloud Build configuration](https://cloud.google.com/cloud-build/docs/deploying-builds/deploy-cloud-run#building_and_deploying_a_container) with a call to terraform. The configurations required for that are explained in the [Terraform Cloud Builder documentation](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/terraform), along with using [Google Storage as a Terraform backend](https://github.com/GoogleCloudPlatform/cloud-builders-community/tree/master/terraform/examples/gcs_backend).

###   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#caveats) Caveats

Terraform within Cloud Build is more complex, especially around the roles that need to be granted to the service account. In this example, `helloworld` was deployed with the default compute service account, which would not have been able to be edited without granting the Terraform service account the `role/editor` role, a permissions set too great for most applications.

Implementing Terraform within Cloud Build, and determining the minimum required permissions required, is outside the scope of this post.

##   [(L)](https://dev.to/googlecloud/migrating-a-shell-script-deployed-cloud-run-service-to-use-terraform-3ako#learn-more) Learn More

- [Terraform Google Provider Configuration Reference](https://www.terraform.io/docs/providers/google/guides/provider_reference.html)
- [google_cloud_run_service Terraform reference](https://www.terraform.io/docs/providers/google/r/cloud_run_service.html)
- [Service identity in Cloud Run](https://cloud.google.com/run/docs/securing/service-identity)
- [Service accounts on Cloud Run (fully managed)](https://cloud.google.com/run/docs/configuring/service-accounts)