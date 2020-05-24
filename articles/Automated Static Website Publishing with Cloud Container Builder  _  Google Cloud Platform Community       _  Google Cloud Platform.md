Automated Static Website Publishing with Cloud Container Builder  |  Google Cloud Platform Community       |  Google Cloud Platform

 [Edit on GitHub](https://github.com/GoogleCloudPlatform/community/edit/master/tutorials/automated-publishing-container-builder/index.md)

 [Report issue](https://github.com/GoogleCloudPlatform/community/issues/new?title=Issue%20with%20automated-publishing-container-builder&body=Issue%20Description)

 [Page history](https://github.com/GoogleCloudPlatform/community/commits/master/tutorials/automated-publishing-container-builder/index.md)

# Automated Static Website Publishing with Cloud Container Builder

  Submitted by [@ahmetb](https://github.com/ahmetb) Mar 13, 2017

- [Contents](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#top_of_page)
- [Objectives](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#objectives)
- [Before you begin](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#before-you-begin)
- [Set up a storage bucket](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#set-up-a-storage-bucket)
- [Set up automated builds](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#set-up-automated-builds)
    - [Trigger the first build](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#trigger-the-first-build)
- [Try it out](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#try-it-out)
- [Clean up](https://cloud.google.com/community/tutorials/automated-publishing-container-builder#clean-up)

star Google Cloud Platform Community tutorials submitted from the community do not represent official Google Cloud Platform product documentation.

This tutorial shows how to automate publishing a static HTML website using a custom domain name to Google Cloud Storage using the [Google Cloud Container Builder](https://cloud.google.com/container-builder/).

## Objectives

- Automatically publish changes to your static website from the source control repository.

## Before you begin

1. Make sure you have a custom domain name (e.g. example.com).

2. Make sure the source code for your static website is hosted on a GitHub or BitBucket repository.

3. Make sure you verified ownership of your domain on [Google Webmaster Central](https://www.google.com/webmasters/verification/). (Do not include `http://` or `https://` in the URL for the purposes of this demo.)

4. Make sure you have a Project on Google Cloud Platform Console to host your website.

## Set up a storage bucket

By uploading your website contents as files to Google Cloud Storage, you can[host your static website](https://cloud.google.com/storage/docs/hosting-static-website) on buckets. First, you need to create a bucket. Head to the [Storage](https://console.cloud.google.com/storage/browser) section of Google Cloud Platform Console and type in your domain name (e.g. `www.example.com`) and create the bucket:

![Create a bucket named as your domain name](../_resources/0f89716fefab6981d066e1c9ad14df04.png)

After the bucket is created, you need to make it readable by everyone. Go to the[Storage Browser](https://console.cloud.google.com/storage/browser) on Cloud Platform Console and click the menu icon to the right of the bucket, then select “Edit Object Default Permissions”:

![Change object default permissions of the bucket](../_resources/26ef1cae5fa62fe7b97da678af0d009a.png)

Then add the user `allUsers` with “Reader” role and click “Save”:
![Add allUsers as HeReader](../_resources/652fbb26d1042197b3498635b958d2ba.png)

Now, you need to configure the storage bucket to serve a static website. Click the “Edit Website Configuration” button on the list of buckets:

![Edit Website Configuration](../_resources/11d8c9866848e16ba718a3a138517c38.png)
Specify the main page as "index.html" and click “Save”:
![Specify main page](../_resources/deef4d3f716d5397c938142f8e8495d0.png)

Now, configure your domain name’s DNS records to [create a CNAME record](https://cloud.google.com/storage/docs/hosting-static-website) that points to Google Cloud Storage. This makes clients requesting your website point to Cloud Storage APIs.

## Set up automated builds

You will use [Google Cloud Container Builder](https://cloud.google.com/container-builder/) and the [Build Triggers](https://cloud.google.com/container-builder/docs/creating-build-triggers)feature to upload your website automatically every time you push a new git commit to the source repository.

**> Note:**>  If you do not have a repository on GitHub, you can fork > [> this sample repository](https://github.com/GoogleCloudPlatform/web-docs-samples)>  for the purposes of this tutorial.

Head over to the Container Registry → [Build Triggers](https://console.cloud.google.com/gcr/triggers)section on Google Cloud Platform Console and click “Add trigger”:

![Add build trigger on Container Registry section](../_resources/d3a5bcd5a70ecee8b7c6020287ff20f8.png)

Then select GitHub as the source of your repository. In the next screen you may be asked to authorize access to your GitHub account and repositories. This is needed for Google Cloud Source Repositories to mirror and create commit hooks on your GitHub repositories.

![Select GitHub as the source](../_resources/7dc0c5b16f5725904480891d3e0bf40b.png)

Then, pick your repository from the list. If you forked the sample repository above, pick it here:

![Select the Git repository](../_resources/1cb743fcc1c3b32befce04826bea6dc1.png)
In the next screen

- give this Build Trigger a name (e.g. publish-website)
- choose Build Configuration "cloudbuild.yaml"
- choose Trigger Type ”Branch”
- Set the file location to `cloudbuild.yaml`

![Create build trigger](../_resources/b30fabc88d8ee31a8ee9a799e55c464a.png)

Now, create a `cloudbuild.yaml` file with the following contents in your repository. Note that you can add files to your repository on GitHub’s website, or by cloning the repository on your development machine:

hdr_strong

	steps:

	  - name: gcr.io/cloud-builders/gsutil

	    args: ["-m", "rsync", "-r", "-c", "-d", "./vision/explore-api", "gs://hello.alp.im"]

This YAML file declares a build step with the `gsutil -m rsync` command and makes sure that the website is uploaded to the storage bucket. The `-m` flag accelerates upload by processing multiple files in parallel and the `-c` flag avoids re-uploading unchanged files.

If you are using the sample repository, you should upload the`./vision/explore-api/` directory. If you would like to upload your entire repository to the storage bucket, make sure to change this value to `.` in the YAML file.

The last command in the `args` is the name of your storage bucket prefixed with`gs://`. Be sure to change this argument to the correct value.

After saving the file, commit and push the changes:
hdr_strong

	git add cloudbuild.yaml
	git commit -m 'Add build configuration'
	git push

### Trigger the first build

Once you push the `cloudbuild.yaml` file to your repository and create the Build Trigger, you can kick off the first build manually. Head over to the Google Cloud Platform Console [Build Triggers](https://console.cloud.google.com/gcr/triggers) section, click “Run Trigger” and choose the the branch (i.e. master) to build.

![Trigger the first build manually](../_resources/fb1bfc300fd29504519d527b2e5b72e0.png)

Now click the “Build history” on the left and watch the build job execute and succeed:

![Build history shows the executing or completed builds](../_resources/388ab41c1fe59eb07d1e40ddec5e82c3.png)

Remember that after now, every commit pushed to any branch of your GitHub repository will trigger a new build and publish contents to your website. If you need to change which git branches or tags you use for publishing, you can update the Build Trigger configuration.

## Try it out

Point your browser to your website URL and see if it works:
![See if your website works](../_resources/3855a34811c8d571f9777677bbd5232d.png)

## Clean up

After you no longer need the artifacts of this tutorial, you can clean up the following resources on the Google Cloud Platform Console to prevent incurring additional charges:

- Storage: delete bucket named as your website
- Container Registry → Build Triggers: delete build trigger
- Development → Repositories: delete mirrored repository

  See more by [@ahmetb](https://cloud.google.com/community/tutorials?q=ahmetb) and more tagged [Cloud Container Builder](https://cloud.google.com/community/tutorials?q=%22Cloud%20Container%20Builder%22), [Hosting](https://cloud.google.com/community/tutorials?q=%22Hosting%22), [Cloud Storage](https://cloud.google.com/community/tutorials?q=%22Cloud%20Storage%22)