GoogleCloudPlatform/django-demo-app-unicodex

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='70'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1019' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#unicodex)Unicodex

Let's build a demo application, using a whole bunch o' Google Cloud components. Let's make it just like [emojipedia](https://emojipedia.org/), but let's call it...

✨  [unicodex](https://unicodex.gl.asnt.app/)  ✨
Unicodex uses:

- [Django 3.0](https://docs.djangoproject.com/en/3.0/) as the web framework
- [Google Cloud Run](https://cloud.google.com/run/) as the hosting platform
- [Google Cloud SQL](https://cloud.google.com/sql/) as the managed database, via [django-environ](https://django-environ.readthedocs.io/en/latest/)
- [Google Cloud Storage](https://cloud.google.com/storage/) as the media storage platform, via [django-storages](https://django-storages.readthedocs.io/en/latest/)
- [Google Cloud Build](https://cloud.google.com/cloud-build/) for build and deployment automation
- [Google Secret Manager](https://cloud.google.com/secret-manager/) for managing encrypted values

*This repo serves as a proof of concept of showing how you can piece all the above technologies together into a working project.*

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='71'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1035' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#steps)Steps

[Try the application locally](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/00-test-local.md)  *optional*

Manual deployment:

1. [Setup Google Cloud Platform environment](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/10-setup-gcp.md)

2. [Create a Cloud SQL Instance](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/20-setup-sql.md)

3. [Create a Cloud Storage Bucket](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/30-setup-bucket.md)

4. [Create some Secrets](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/40-setup-secrets.md)

5. [First Deployment](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/50-first-deployment.md)

6. [Ongoing Deployments](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/60-ongoing-deployments.md)

Automated deployment:

- [Deploy with Terraform](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/80-automation.md)

Cleanup:

- [Cleanup your project resources](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/docs/90-cleanup.md)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='72'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1053' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#application-design)Application Design

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='73'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1055' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#unicodex-itself)Unicodex itself

[Emojipedia](https://emojipedia.org/) curates information about emoji and how they are represented on different platforms. E.g. the [Sparkles emoji](https://emojipedia.org/sparkles/) (✨) is mostly represented by three golden stars in a cluster, but this has changed over the years (click the sparkle image marked "Google" and you'll see how Sparkles has appeared in every version of Android over the years. It used to look *very* different!)

In Unicodex, these relations are represented by a **codepoint** (Sparkles) having multiple **designs** (images). Each image represents a **version** from a **vendor** (e.g. Google Android 9.0, Twitter Twemoji 1.0, ...). These relations are represented by four models: `Codepoint`, `Design`, `VendorVersion` and `Vendor`, respectively. Designs have a FileField which stores the image.

In the django admin, an admin action has been setup so that you can select a Codepoint, and run the "Generate designs" actions. This will -- for all configured vendors and vendor versions -- scrape Emojipedia for the information. Alternatively, you can enter this information manually from the django admin.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='74'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1062' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#service-design---111)Service design - 1:1:1

Unicodex runs as a Cloud Run service. Using the Python package `django-storages`, it's been configured to take a `GS_BUCKET_NAME` as a storage place for its media. Using the Python package `django-environ` it takes a complex `DATABASE_URL`, which will point to a Cloud SQL PostgreSQL database. The `settings.py` is also designed to pull specifically named secrets into the environment. These are all designed to live in the same Google Cloud Project.

In this way, Unicodex runs 1:1:1 -- one Cloud Run Service, one Cloud SQL Database, one Google Storage bucket. It also assumes that there is *only* one service/database/bucket.

This implementation is live at https://unicodex.gl.asnt.app/

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='75'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1068' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#other-service-designs)Other service designs

It is possible to host multiple instances of Unicodex on the one project (where the service name, bucket name, and database name, and django database username have different appended 'slugs', and all share one instance), but this configuration is out of scope for this project.

You can host multiple versions of Unicodex using project isolation (one Google Cloud account can have multiple projects) without any code editing, but this may not work for your own project. [Read more about project organisation considerations](https://cloud.google.com/docs/enterprise/best-practices-for-enterprise-organizations#project-structure)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='76'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1072' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#contributions)Contributions

Please see the [contributing guidelines](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/CONTRIBUTING.md)

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='77'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1075' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex#license)License

This library is licensed under Apache 2.0. Full license text is available in [LICENSE](https://github.com/GoogleCloudPlatform/django-demo-app-unicodex/blob/master/LICENSE).