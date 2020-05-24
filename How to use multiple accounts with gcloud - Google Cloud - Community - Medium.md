How to use multiple accounts with gcloud - Google Cloud - Community - Medium

## GCP TIPS

# How to use multiple accounts with gcloud

## Learn how to easily switch contexts with gcloud.

[![2*C974eIQCY1Fx2XhIWaSpZg.jpeg](../_resources/e5a80ae65ee9228be4583168982dc1cb.jpg)](https://medium.com/@mfsilv?source=post_page-----848fdb53a39a----------------------)

[Fatima Silveira](https://medium.com/@mfsilv?source=post_page-----848fdb53a39a----------------------)

[Apr 17](https://medium.com/google-cloud/how-to-use-multiple-accounts-with-gcloud-848fdb53a39a?source=post_page-----848fdb53a39a----------------------) · 2 min read

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='199'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='200' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/848fdb53a39a/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='208'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='209' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/848fdb53a39a/share/facebook?source=post_actions_header---------------------------)

![1*r-81XZzfTZCe1Is2s2JA7A.png](../_resources/ddb762a8e0af2b87d1f5b6077845555d.png)
![1*r-81XZzfTZCe1Is2s2JA7A.png](../_resources/a25fcdf7f3ab44a4c70b0a1cacd96e54.png)

Do you want to know how to work with multiple accounts and organizations in *gcloud* while keeping your sanity? Let me share with you a little known feature in *gcloud* that does just that.

# gcloud config configurations

There is a sub-module in *gcloud config *that allows you to group a set of *configurations* and give it a name. You can then activate it on-demand! This means it becomes super easy to switch between different accounts or organizations whenever you need. In other words, context switching.

This is how you use it:
gcloud config configurations activate config-name

Switching between configurations is very simple and it carries all the information you set when you created it — this means that you don’t have to login again even if you are using different credentials. Simply type the command above *et voilà.*

* * *

*...*

Before we get into details on how to create them, let me give you a few examples when this is useful:

- Switching between environments with distinct regions and zones.
- Switching between different credentials, especially for testing.
- Switching between completely different organizations.

![1*5HD9BrDFGx846sLDL7wtAg.png](../_resources/faceed4135aa76cff46e29d423952cf6.png)
![1*5HD9BrDFGx846sLDL7wtAg.png](../_resources/cb7d8a3b626603883e52a513b0d878c7.png)
gcloud configurations example. Source: my terminal

Notice on the screenshot above that I have accounts for different organizations, projects, compute zone, and compute region — and these are only a subset of [possible settings](https://cloud.google.com/sdk/gcloud/reference/config/set).

* * *

*...*

Of course to use a *configuration* you must first create it. This step requires a bit of typing but it’s a one-time effort, and will save a lot of time in the long run. This is how you create a new configuration:

|     |     |
| --- | --- |
| 1   | $ gcloud config configurations create config-name |
| 2   | Created [demo-config]. |
| 3   | Activated [demo-config]. |
| 4   |     |
| 5   | $ gcloud config set project my-project-id |
| 6   | Updated property [core/project]. |
| 7   |     |
| 8   | $ gcloud config set account my-account@example.com |
| 9   | Updated property [core/account]. |
| 10  |     |
| 11  | $ gcloud config set compute/region us-east1 |
| 12  | Updated property [compute/region]. |
| 13  |     |
| 14  | $ gcloud config set compute/zone us-east1-b |
| 15  | Updated property [compute/zone]. |

 [view raw](https://gist.github.com/fawix/8ea183fce91eddbd9e1d73939d28bef8/raw/fc13f0821e47e9a2086e35a6b3858595408f045d/gcloud_config.sh)  [gcloud_config.sh](https://gist.github.com/fawix/8ea183fce91eddbd9e1d73939d28bef8#file-gcloud_config-sh) hosted with ❤ by [GitHub](https://github.com/)

Give the config a memorable name, then add the *project id* and the *account *at a minimum. I typically also set the compute region and zone since I work with these a lot. For development, you may also want to add a service account.

By the way, did you notice I didn’t have to log in when creating the config above? That is because that account was already in use by another configuration. Yes, that easy!

If you do need to add a new account just invoke the following:
gcloud auth login

Using this trick will save you a lot of time and make your experience in *gcloud* better! It’s well worth to learn and configure if you work with multiple contexts;

Ready to create your first configuration? [Let me know how it goes!](https://twitter.com/fawix)