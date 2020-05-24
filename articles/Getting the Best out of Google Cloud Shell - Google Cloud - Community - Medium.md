Getting the Best out of Google Cloud Shell - Google Cloud - Community - Medium

# Getting the Best out of Google Cloud Shell

[![1*r7hrULSjglXP2M63J8Txug.png](../_resources/62f1fbf3ec4682d09ffb814e26839e8d.png)](https://medium.com/@dwdraju?source=post_page-----3d6ca64bc741----------------------)

[Raju Dawadi](https://medium.com/@dwdraju?source=post_page-----3d6ca64bc741----------------------)

[Feb 8](https://medium.com/google-cloud/getting-the-best-out-of-google-cloud-shell-3d6ca64bc741?source=post_page-----3d6ca64bc741----------------------) · 4 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='192'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='193' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/3d6ca64bc741/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='196'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/3d6ca64bc741/share/facebook?source=post_actions_header---------------------------)

When it comes to accessing google cloud resources or giving ssh access or doing some actions on cloud, we think of creating a standalone VM aka jump server. Running dedicated instance or getting full access to local system could also be option. And what about mobile when we need quick access? All these hurdles can be avoided by one solution: [Google Cloud Shell](https://cloud.google.com/shell/).

![1*XxWTGiDhIvoUQCJmo1Ullg.png](../_resources/a95089819543a460267a63152927978c.png)
![1*XxWTGiDhIvoUQCJmo1Ullg.png](../_resources/a488a2031c2416a4f7732922a421a6b5.png)

Google Cloud Shell is a command line machine which is available for every google cloud account user for free and provides shell access from browser from where we can access and manage cloud resources and projects. This secured shell with 5GB storage is pre-installed with favorite tools like: MySql client, Kubernetes, and Docker. The shell is account wide so by staying on same shell, we can connect to cloud resources of multiple project with access.

Let’s see how you can make life easier by getting the best of Google Cloud Shell.

## 1. Start the shell in few seconds by one click

The machine pre-loaded with debian starts in few seconds in the same browser by clicking on “Activate Cloud Shell” icon on top right of the google cloud console. If you haven’t been using the shell since long time or trying out for first time, it might take half a minute or so. The shell has built-in authorization with gcloud credential, so you can access any cloud resources for which you have IAM access in any project.

![1*8ptAD1YARne_q48MnRfQNA.png](../_resources/75e5e8e1cdd37b60818437a9f8953ddb.png)
![1*SjZx6S4RQvMCwvKJepiCMQ.png](../_resources/2bebc163d790ce7ec7dcb65c4e366123.png)
starting google cloud shell

## 2. Connect to cloud shell from local

Google Cloud Shell is not limited to browser access but from any gcloud sdk installed and account activated terminal. Authenticate your local system with gcloud IAM and access the google cloud shell:

$ gcloud auth login$ gcloud alpha cloud-shell ssh

## 3. Easy SSH access to compute engine instances

From the Cloud Shell, one with [SSH access](https://cloud.google.com/compute/docs/access/#granting_users_ssh_access_to_vm_instances) can easily connect to compute engine instance using gcloud command.

gcloud compute ssh [instance-name] --project [project-name] --zone [zone]

Even if the compute instance is not assigned with public ip, the instance can be accessed through cloud shell.

## 4. Web preview on of running service

Its not only shell but is a real tool for debugging. We can start any service or run docker and preview the output on nice url with “Web Preview”.

![1*wE7z7Du9fUIxww3Y7SgMuw.jpeg](../_resources/4c1a84b286ae234f56ef8352cec0a375.png)
Cloud Shell web preview

By running multiple service on background or on different tab of the shell, we can preview them on different port.

## 5. Boost power of cloud shell for higher performance

By default, cloud shell runs on *g1-small* machine type which provides 1 vCPU short periods of bursting and 1.70 GB memory. Sometimes, this isn’t enough if you have to work with multiple tabs and run few services.

The newly introduced power boosting feature of cloud shell allows upgrade of the shell *n1-standard-1* VM instance which offers 1vCPU and 3.75GB memory for 24 hours.

To activate the boost mode, click ‘Enable Boost Mode’ option under the ‘More’ menu of the cloud shell.

## 6. Its more than shell — Code Editor and run VS Code

Google Cloud Shell’s integrated code editor based on [Theia IDE](https://theia-ide.org/) makes it easy to edit files and folders in the shell from browser.

![1*i_vZMETXnqe8jmwlN-RQoQ.png](../_resources/2aaa0ca4de0fcb7ab12c31600628e86e.png)
Cloud Shell integrated code editor

Clicking on *Launch Editor*(edit icon) on the top of the cloud shell opens a new tab on browser with all access to files and folder in the root of shell.

Also, we can run VS Code with Cloud shell. By simply running [cdr/code-server](https://github.com/cdr/code-server/) through docker or [shell](https://medium.com/google-cloud/how-to-run-visual-studio-code-in-google-cloud-shell-354d125d5748) inside cloud shell, we can preview nice VS code UI on http port.

## 7. Easy connect to Cloud SQL

Whether it be creating mysql user, database or any operation on Cloud SQL instance, using Cloud Shell makes it easier.

$ gcloud sql connect myinstance --user=root

## 8. Shell access from mobile app with advanced key

The cloud shell access is not limited from web browser and computer but also from mobile device. We can connect to shell from [Cloud Console Mobile App](https://cloud.google.com/console-app/) apart from getting alert notification, manage GCP resources and access compute engine instances.

![1*kW_xXIeCZ3hOvMqblDGg9A.png](../_resources/888b4efcefd4b29cedf1d96ad3981639.jpg)
Cloud Shell access from mobile

## 9. Deploy to Cloud Run in single click

Deploying containerized serverless application to Google Cloud Run button is possible with cloud shell. The newly introduced “Run on Google Cloud” button makes it super easy to deploy new image to cloud run service.

![1*SjZx6S4RQvMCwvKJepiCMQ.png](../_resources/39160c081d28b3dcd765fb03081120eb.png)

Read more about the application structure for the setup from [GoogleCloudPlatform/cloud-run-button](https://github.com/GoogleCloudPlatform/cloud-run-button) repo.