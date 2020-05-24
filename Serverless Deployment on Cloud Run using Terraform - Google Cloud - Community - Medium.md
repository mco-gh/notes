Serverless Deployment on Cloud Run using Terraform - Google Cloud - Community - Medium

# Serverless Deployment on Cloud Run using Terraform

[![1*ofUGmTB2JSCklJzdWAZppA.jpeg](../_resources/c98574a3f75f3663226ee85b9e293482.jpg)](https://medium.com/@timtech4u?source=post_page-----ee8ae4ecb72e----------------------)

[Timothy](https://medium.com/@timtech4u?source=post_page-----ee8ae4ecb72e----------------------)

[Jan 23](https://medium.com/google-cloud/deploying-docker-images-to-cloud-run-using-terraform-ee8ae4ecb72e?source=post_page-----ee8ae4ecb72e----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='192'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/ee8ae4ecb72e/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='196'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/ee8ae4ecb72e/share/facebook?source=post_actions_header---------------------------)

![1*RMCKkdd6bbPT5LctVVv5dw.png](../_resources/f5fafe7e89cc6b3e10e53e7d9f6520ec.png)
![1*RMCKkdd6bbPT5LctVVv5dw.png](../_resources/c3a20b6a1c606171dfbb1b55780d9212.png)

> In this article, we’ll deploy a serverless Flask web application to Cloud Run by building its > [> Docker image](https://github.com/Timtech4u/ghost3-docker)>  into Container Registry and use Terraform to provision our deployment as code.

> [> Terraform](https://www.terraform.io/)>  is a infrastructure as code tool for building, changing, and versioning infrastructure safely and efficiently across various cloud providers.

> [> Cloud Run](https://cloud.google.com/run/)>  is a managed compute platform that enables you to run stateless serverless containers that automatically scales.

> [> Container Registry](https://cloud.google.com/container-registry)>  is a private container image registry that runs on Google Cloud.

> [> Flask](https://github.com/pallets/flask)>  is a micro web framework written in Python.

# Prerequisites

- Create a [Google Cloud Platform (GCP) project](https://console.cloud.google.com/project), or use an existing one.
- Setup [Cloud SDK](https://cloud.google.com/sdk/), or use [Cloud Shell](https://cloud.google.com/shell/).
- Enable the [Cloud Run API](https://console.developers.google.com/apis/api/run.googleapis.com/overview).
- Enable the [Container Registry API](https://console.developers.google.com/apis/api/containerregistry.googleapis.com/overview).
- Clone the [sample codes](https://github.com/Timtech4u/flask-docker) or setup your own codes with a *Dockerfile*.

For this guide, I would stick to using Cloud Shell which has Terraform enabled by default.

If you are using the Cloud SDK on your local PC, you need a service account to use Terraform, do create one [here](https://console.cloud.google.com/apis/credentials/serviceaccountkey).

*Note that ****terraform-cr ****is my GCP project ID and you should replace that with yours.*

# Pushing Docker Image to Container Registry

We need to build the Docker image and push it to the project’s container registry so Terraform can access it.

You can clone the source codes into Cloud Shell and execute the following commands within it’s directory.

$ docker build -t gcr.io/terraform-cr/webapp .
$ docker push gcr.io/terraform-cr/webapp
![1*Hc8Qc_Xv4W7RqMP-CtCI1A.png](../_resources/b5fe0bbd73e35c79f2a48d142a3dafe5.png)
![1*Hc8Qc_Xv4W7RqMP-CtCI1A.png](../_resources/02d1a51f2d1eb7492b1d1e143b9e7811.png)
Output

If this didn’t work for you, do check out other steps on the official documentation [here](https://cloud.google.com/container-registry/docs/pushing-and-pulling).

Cloud Run will only retrieve containers hosted in Container Registry and not from other sources.

If your Docker Image is on [Docker Hub](http://hub.docker.com/), I made a short video that narrates how to push a Docker Image to Container Registry. Do subscribe

Deploying Docker Images to Google Cloud Run

# Deploying to Cloud Run using Terraform

Terraform is enabled on Cloud Shell, you can verify by executing the ***terraform -v ***command. The version of Terraform installed is v0.12.9.

![1*SZLjZpScDhwaGdQQPA0p4g.png](../_resources/095ece6171ffbf2f6ebf88fcc12911fc.png)
![1*TgCaXl1nVkw99ARRjWLG6g.png](../_resources/73182d4acb0fcbae4fd51f88b1b5863b.png)
Terraform version

If you want to find out more details on this section, do checkout [Cloud Run - Terraform resource documentation](https://www.terraform.io/docs/providers/google/r/cloud_run_service.html).

Next step is to create a **main.tf** file which is a Terraform configuration file, you can find mine here:

# Filename: main.tf# Configure GCP project

provider "google" {
project = "terraform-cr"
}# Deploy image to Cloud Run
resource "google_cloud_run_service" "mywebapp" {
name = "mywebapp"
location = "us-central1"
template {
spec {
containers {
image = "gcr.io/terraform-cr/webapp"
}
}
}
traffic {
percent = 100
latest_revision = true
}
}# Create public access
data "google_iam_policy" "noauth" {
binding {
role = "roles/run.invoker"
members = [
"allUsers",
]
}
}# Enable public access on Cloud Run service
resource "google_cloud_run_service_iam_policy" "noauth" {
location = google_cloud_run_service.mywebapp.location
project = google_cloud_run_service.mywebapp.project
service = google_cloud_run_service.mywebapp.name
policy_data = data.google_iam_policy.noauth.policy_data
}# Return service URL
output "url" {
value = "${google_cloud_run_service.mywebapp.status[0].url}"
}
Now let’s initialize Terraform on Google Cloud Shell.
$ terraform init
![1*gqPXlWuvIpabg26YdMS_dg.png](../_resources/ee5db57b73fccea4b8524af57d04663a.png)
![1*gqPXlWuvIpabg26YdMS_dg.png](../_resources/19dce5ea82a85c525ff3a23bb817f9f2.png)
Output

Then let’s plan the code in our **main.tf **file and see what the infrastructure looks like:

$ terraform plan
![1*TgCaXl1nVkw99ARRjWLG6g.png](../_resources/d83abae4b473256280d76c1dd02ecea8.png)
![1*SZLjZpScDhwaGdQQPA0p4g.png](../_resources/2928f0d7dc7ef1a98e92d515ae6da73d.png)
Truncated Output
Finally, we can apply to execute, make sure to enter ‘**yes**’ to approve.
$ terraform apply
![1*tj5Xuj8JymgyStzP1nE6lw.png](../_resources/bc0e60c4c19b15d29cde8b0c8b84df3f.png)
![1*tj5Xuj8JymgyStzP1nE6lw.png](../_resources/a6a99ce5fa0463b2a9e771e9c12504ee.png)
Truncated Output

Outputs:url = [https://mywebapp-mxxduub7tq-uc.a.run.app](https://mywebapp-mxxduub7tq-uc.a.run.app/)

# Next Steps

Terraform allows you delete every resource used (including the GCP project), to do this, execute the following command, make sure to enter ‘**yes**’ to approve.

$ terraform destroy

So far we have been able to use Terraform to provision our deployment to Cloud Run as code. This could help you deploy applications much faster.

If you’re looking to automate more of your workflow on Google Cloud, the following resources would come in handy.

- [Terraform Google Cloud Provider documentation](https://www.terraform.io/docs/providers/google/index.html)
- [Google Cloud Build documentation](https://cloud.google.com/cloud-build/docs/)
- [Automation Tips on my blog.](https://fullstackgcp.com/)