Configuring Cloud Run with Terraform | Seth Vargo

# [Configuring Cloud Run with Terraform](https://www.sethvargo.com/configuring-cloud-run-with-terraform/)

 [Cloud Run](https://www.sethvargo.com/tag/cloud-run), [Serverless](https://www.sethvargo.com/tag/serverless), [Terraform](https://www.sethvargo.com/tag/terraform)  ![configuring-cloud-run-with-terraform.jpg](../_resources/4b318b1037abf54c2a52ca53ad73f3f0.jpg)  * Posted on December 4, 2019*

[Terraform](https://www.terraform.io/) is a popular tool for managing infrastructure configurations as code, but what if that infrastructure is serverless? Google's [Cloud Run](https://cloud.google.com/run) is a fully-managed serverless offering that leverages the power and flexibility of containers as a deployment primitive. This post explores **how to setup and configure a Cloud Run service using Terraform**.

The full sample code for this post is [available on GitHub](https://github.com/sethvargo/terraform-cloud-run-demo).

## Setup

To get started, [create a Google Cloud account](https://console.cloud.google.com/freetrial), [install the Cloud SDK](https://cloud.google.com/sdk/install), and install [Terraform](https://www.terraform.io/) for your device. If you have not already done so, authenticate to the Cloud SDK:

	$ gcloud auth application-default login

This will open a browser and prompt a sign in for your Google account. This only needs to be done once per device.

Create a new folder in which to create your Terraform configurations. All future commands will be run from this folder and files will be created in this folder.

	$ mkdir terraform-cloud-run-demo

	$ cd terraform-cloud-run-demo

## Configurations

Create a file named `versions.tf` that define the version constraints.

	terraform {
	  required_version = ">= 0.12"

	  required_providers {
	    google = ">= 3.3"
	  }
	}

This file creates two constraints:

- `terraform` - This is the actual Terraform binary version. We require version 12.0+.

- `google` - This is the Google *provider* for Terraform. We require 3.3+ because Cloud Run support was added in version 3.3.0.

Create a file named `main.tf` and configure the Google provider stanza:

	provider "google" {
	  project = "YOUR_PROJECT_ID" *# replace with your project ID*
	}

Enable the Cloud Run API. This only needs to be done once per project, but it is an idempotent operation.

	resource "google_project_service" "run" {
	  service = "run.googleapis.com"
	}

Create a Cloud Run service named `"my_service"` in the `"us-central1"` region. This service deploys a basic hello world container and directs 100% of traffic to this container.

	resource "google_cloud_run_service" "my_service" {
	  name     = "my_service"
	  location = "us-central1"

	  template {
	    spec {
	      containers {
	        image = "gcr.io/cloudrun/hello"
	      }
	    }
	  }

	  traffic {
	    percent         = 100
	    latest_revision = true
	  }

	  depends_on = [google_project_service.run]
	}

Make the deployed service publicly accessible. Without this configuration, the endpoint will require authentication. For demo purposes, give "allUsers" the ability to invoke the service.

	resource "google_cloud_run_service_iam_member" "allUsers" {
	  service  = google_cloud_run_service.my_service.name
	  location = google_cloud_run_service.my_service.location
	  role     = "roles/run.invoker"
	  member   = "allUsers"
	}

Finally, output the URL where the service can be accessed.

	output "url" {
	  value = "${google_cloud_run_service.my_service.status[0].url}"
	}

## Execute Terraform

Now that the configurations are written, initialize Terraform.

	$ terraform init

Next, plan the changes.

	$ terraform plan

The output will show the actions Terraform is going to take.

	Plan: 3 to add, 0 to change, 0 to destroy.

Now apply the changes. Terraform will automatically handle the order of operations.

	$ terraform apply

The output will show the progress and eventually the URL.

	google_project_service.run: Creating...
	google_project_service.run: Still creating... [10s elapsed]
	google_project_service.run: Still creating... [20s elapsed]
	google_project_service.run: Still creating... [30s elapsed]
	google_project_service.run: Creation complete after 38s [id=sethvargo-gcloud-secrets/run.googleapis.com]
	google_cloud_run_service.my-service: Creating...
	google_cloud_run_service.my-service: Still creating... [10s elapsed]
	google_cloud_run_service.my-service: Creation complete after 16s [id=locations/us-central1/namespaces/sethvargo-gcloud-secrets/services/my-service]
	google_cloud_run_service_iam_member.allUsers: Creating...
	google_cloud_run_service_iam_member.allUsers: Creation complete after 6s [id=v1/projects/sethvargo-gcloud-secrets/locations/us-central1/services/my-service/roles/run.invoker/allusers]

	Apply complete! Resources: 3 added, 0 changed, 0 destroyed.

	Outputs:

	url = https://my-service-3vyvs7utmq-uc.a.run.app

## Invoke the service

Use Terraform outputs to invoke the service.

	# In the terminal
	$ curl $(terraform output url)

	# In the default browser
	$ open $(terraform output url)

## Tearing it down

One of the beauties of Terraform is its self-contained nature. Even though Cloud Run has a generours free tier and [you only pay when your service is running], some folks want to cleanup things when they are done.

When you are done experimenting, tear everything down with a single Terraform command!

	$ terraform destroy

Confirm "yes" at the prompt.

## Next steps

This post only beings to scratch the surface of the functionality offered by the `google_cloud_run_service` resource in Terraform. Check out the [Cloud Run Terraform resource documentation](https://www.terraform.io/docs/providers/google/r/cloud_run_service.html) for a full list of all arguments and attributes available. You can also [learn more about Cloud Run](https://cloud.google.com/run) and [Cloud Run pricing](https://cloud.google.com/run/pricing) on the Google Cloud website.

## About Seth

Seth Vargo is an engineer at [Google Cloud](https://cloud.google.com/). Previously he worked at HashiCorp, Chef Software, CustomInk, and some Pittsburgh-based startups. He is the author of [Learning Chef](https://www.amazon.com/Learning-Chef-Configuration-Management-Automation/dp/1491944935) and is passionate about reducing inequality in technology. When he is not writing, working on open source, teaching, or speaking at conferences, Seth advises non-profits.

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1792 1792' data-evernote-id='76' class='js-evernote-checked'%3e%3cpath d='M1684 408q-67 98-162 167 1 14 1 42 0 130-38 259.5T1369.5 1125 1185 1335.5t-258 146-323 54.5q-271 0-496-145 35 4 78 4 225 0 401-138-105-2-188-64.5T285 1033q33 5 61 5 43 0 85-11-112-23-185.5-111.5T172 710v-4q68 38 146 41-66-44-105-115t-39-154q0-88 44-163 121 149 294.5 238.5T884 653q-8-38-8-74 0-134 94.5-228.5T1199 256q140 0 236 102 109-21 205-78-37 115-142 178 93-10 186-50z'%3e%3c/path%3e%3c/svg%3e)](https://twitter.com/sethvargo)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1792 1792' data-evernote-id='77' class='js-evernote-checked'%3e%3cpath d='M1343 12v264h-157q-86 0-116 36t-30 108v189h293l-39 296h-254v759H734V905H479V609h255V391q0-186 104-288.5T1115 0q147 0 228 12z'%3e%3c/path%3e%3c/svg%3e)](https://facebook.com/sethvargo)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1792 1792' data-evernote-id='78' class='js-evernote-checked'%3e%3cpath d='M704 1216q0 40-12.5 82t-43 76-72.5 34-72.5-34-43-76-12.5-82 12.5-82 43-76 72.5-34 72.5 34 43 76 12.5 82zm640 0q0 40-12.5 82t-43 76-72.5 34-72.5-34-43-76-12.5-82 12.5-82 43-76 72.5-34 72.5 34 43 76 12.5 82zm160 0q0-120-69-204t-187-84q-41 0-195 21-71 11-157 11t-157-11q-152-21-195-21-118 0-187 84t-69 204q0 88 32 153.5t81 103 122 60 140 29.5 149 7h168q82 0 149-7t140-29.5 122-60 81-103 32-153.5zm224-176q0 207-61 331-38 77-105.5 133t-141 86-170 47.5-171.5 22-167 4.5q-78 0-142-3t-147.5-12.5-152.5-30-137-51.5-121-81-86-115q-62-123-62-331 0-237 136-396-27-82-27-170 0-116 51-218 108 0 190 39.5T603 419q147-35 309-35 148 0 280 32 105-82 187-121t189-39q51 102 51 218 0 87-27 168 136 160 136 398z'%3e%3c/path%3e%3c/svg%3e)](https://github.com/sethvargo)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1792 1792' data-evernote-id='79' class='js-evernote-checked'%3e%3cpath d='M576 1344q0 80-56 136t-136 56-136-56-56-136 56-136 136-56 136 56 56 136zm512 123q2 28-17 48-18 21-47 21H889q-25 0-43-16.5t-20-41.5q-22-229-184.5-391.5T250 902q-25-2-41.5-20T192 839V704q0-29 21-47 17-17 43-17h5q160 13 306 80.5T826 902q114 113 181.5 259t80.5 306zm512 2q2 27-18 47-18 20-46 20h-143q-26 0-44.5-17.5T1329 1476q-12-215-101-408.5t-231.5-336-336-231.5T252 398q-25-1-42.5-19.5T192 335V192q0-28 20-46 18-18 44-18h3q262 13 501.5 120T1186 542q187 186 294 425.5t120 501.5z'%3e%3c/path%3e%3c/svg%3e)](https://www.sethvargo.com/feed.xml)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1792 1792' data-evernote-id='80' class='js-evernote-checked'%3e%3cpath d='M711 1128l484-250-484-253v503zm185-862q168 0 324.5 4.5T1450 280l73 4q1 0 17 1.5t23 3 23.5 4.5 28.5 8 28 13 31 19.5 29 26.5q6 6 15.5 18.5t29 58.5 26.5 101q8 64 12.5 136.5T1792 788v176q1 145-18 290-7 55-25 99.5t-32 61.5l-14 17q-14 15-29 26.5t-31 19-28 12.5-28.5 8-24 4.5-23 3-16.5 1.5q-251 19-627 19-207-2-359.5-6.5T336 1512l-49-4-36-4q-36-5-54.5-10t-51-21-56.5-41q-6-6-15.5-18.5t-29-58.5T18 1254q-8-64-12.5-136.5T0 1004V828q-1-145 18-290 7-55 25-99.5T75 377l14-17q14-15 29-26.5t31-19.5 28-13 28.5-8 23.5-4.5 23-3 17-1.5q251-18 627-18z'%3e%3c/path%3e%3c/svg%3e)](https://youtube.com/sethvargo)

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1792 1792' data-evernote-id='81' class='js-evernote-checked'%3e%3cpath d='M477 625v991H147V625h330zm21-306q1 73-50.5 122T312 490h-2q-82 0-132-49t-50-122q0-74 51.5-122.5T314 148t133 48.5T498 319zm1166 729v568h-329v-530q0-105-40.5-164.5T1168 862q-63 0-105.5 34.5T999 982q-11 30-11 81v553H659q2-399 2-647t-1-296l-1-48h329v144h-2q20-32 41-56t56.5-52 87-43.5T1285 602q171 0 275 113.5t104 332.5z'%3e%3c/path%3e%3c/svg%3e)](https://linkedin.com/in/sethvargo)