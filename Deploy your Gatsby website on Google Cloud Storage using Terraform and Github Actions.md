Deploy your Gatsby website on Google Cloud Storage using Terraform and Github Actions

![0*m6qtFNz9quc_drA3](../_resources/9e728214c8635a573f908b16b4193c65.jpg)
![0*m6qtFNz9quc_drA3](../_resources/61213aaf463044b86238a7478ec1e4b4.jpg)

Photo by [JJ Ying](https://unsplash.com/@jjying?utm_source=medium&utm_medium=referral) on [Unsplash](https://unsplash.com/?utm_source=medium&utm_medium=referral)

# Deploy your Gatsby website on Google Cloud Storage using Terraform and Github Actions

[![1*jb2CM5k6BrtfI8GOWjdaXA.jpeg](../_resources/f5b199e3ebf7fda3c2cc9cd700d7e272.jpg)](https://medium.com/@julienfouilhe?source=post_page-----fcf4b8f516ff----------------------)

[Julien Fouilhé](https://medium.com/@julienfouilhe?source=post_page-----fcf4b8f516ff----------------------)

[Mar 18](https://medium.com/inato/deploy-your-gatsby-website-on-google-cloud-storage-using-terraform-and-github-actions-fcf4b8f516ff?source=post_page-----fcf4b8f516ff----------------------) · 6 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='187'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='188' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='193'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='194' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/fcf4b8f516ff/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='202'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='203' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/fcf4b8f516ff/share/facebook?source=post_actions_header---------------------------)

# Context

![1*B6Cr60iN9fmPjZw_hD2cbg.png](../_resources/2693aafe6df103f2ce7891e44a56a5bd.png)
![1*B6Cr60iN9fmPjZw_hD2cbg.png](../_resources/d559f0abff888a2a10ee28a108eb722c.png)
[https://inato.com](https://inato.com/) Before/after

At Inato, we decided to revamp our website two months ago and to do this, we decided to go with Gatsby for several reasons.

Firstly, because it **uses a stack we are familiar with** since GraphQL and React are tools we use on a regular basis.

Secondly, because it unbelievably **enhances the performance** of the website, by optimizing everything it can, from image sizes to lazy loading out of the box.

Thirdly, because it **allows for easy integration with various CMS**, and we needed the website to be fully customizable by our marketing team.

With that settled, we still needed to decide how we would deploy our website.

Gatsby builds static webpages, so we didn’t need anything too complex, and certainly didn’t need to deploy it inside our Kubernetes cluster. Our **requirements** were:

- Easy deployment of new versions.
- Our assets needed to be served via a CDN for speed.
- Browsing the website should not be interrupted when a new version is deployed.

That third one was actually decisive in how we chose our solution, because Gatsby, even though it builds static pages that can be loaded without any javascript, then hydrates those pages with javascript that enhances the whole user experience. That javascript is split in a lot of chunks of code, that are each loaded lazily when needed (for instance, when clicking a link to another page of the website).

Those chunk files are named with a hash of their content so that if you’ve visited the website and you return on it after a new version has been deployed, the cache control rules you’ve applied to the chunks of the former version do not apply and you get the new version.

That’s great! But what happens if a new version is deployed **while **you’re browsing the website? Well, if you use a tool such as Amplify or Firebase Hosting, chunks for the version you’re browsing are erased, and even though some nodes of your CDN may have cached it, they also may not have, and therefore you may get a blank page and have to reload, leading to bad user experience.

# Solution

The solution to this is not that complicated in theory: it requires you **not to erase the assets of the former versions**. Remember, your file names contain the hash of their content, so if they change, their filename changes also. That means that you can keep all the versions of your javascript available!

The problem is: most tools designed to deploy a static website do not allow that. When you deploy a new version, the old files are erased completely.

Hence why we decided to go with **Google Cloud Storage**.

The concept is simple: you store your files in a Google Cloud Storage bucket, then Cloud CDN serves those files. Nothing more complicated.

Now, it also has disadvantages compared to other solutions, so this may not be for everyone. Here are some of the disadvantages compared to, for instance, Amplify:

- **You have to set up your own CI/CD.** Where Amplify connects to your Git repository and launches automatically a CI/CD pipeline on every new commit, you will have to set this up yourself with Google Cloud Storage.
- **It only offers limited URL rewriting/forwarding. **

Want a 301 redirect from HTTP to HTTPS? Really hard to do, and you would have to use a Google Cloud Engine instance, [there are plans for this though](https://googlecloudplatform.uservoice.com/forums/302616-load-balancing/suggestions/31951531-allow-http-to-redirect-to-https-automatically).

Want a 301 redirect from [www.inato.com](http://www.inato.com/) to inato.com? Not possible, you’ll have to do it using your DNS records if your provider allows it. *You can only define a 404 page and an index page with GCS.*

# Let’s dig in!

Now that we know what we’re in for, let’s dig in and actually get it done.

## Terraform

At Inato, we already use Terraform to describe our infrastructure. Thus, it appeared natural to us that we would also use it for our website. **If you don’t already use Terraform** and are not familiar with it, you can just skip this and **setup everything using only the console or the CLI**. But if you do use this already, here’s what you’ll need.

First, set up your basic information:

Then, add your bucket. We set the project id in its name because it needs to be unique among all existing projects in GCP, not just yours. We set our main page suffix to be the `index.html`, and the not found page to be our `404.html` page.

Then we need to add public read rights:

We will want to add a load balancer on top and enable Cloud CDN. We will need an SSL certificate to handle HTTPS requests. *Note: *the certificate will only become active ~10 minutes after you have redirected your domain to the new load balancer IP.

Once you’ve run `terraform apply` , you’ll be able to manually upload a build to your newly created bucket, and once you’ve changed your DNS records to point to your load balancer, you’ll be able to access your website!

Now let’s add a `github-actions` service account, which will allow Github Actions to perform the required actions:

Run `terraform apply` again to apply those changes and you’re done!
**Github Actions**
![1*0KJ_sUrHqtDW_7cCzISKzg.png](../_resources/ac2d7f76611cb5b9884ea1fad8080bd3.png)
![1*0KJ_sUrHqtDW_7cCzISKzg.png](../_resources/4d8eff5035abb87a0e3f55b31fcbb7a7.png)
Our Github Actions pipeline

Obviously, if you don’t use Github, you can just do the same thing with other CI solutions such as Gitlab CI or CircleCI.

Our CI/CD pipeline needs to:

- Build the gatsby website.
- Upload our build to our Google Cloud Storage bucket. During this step, we will need to gzip our text files and to set our cache control policy.

First let’s step up our workflow, stored under `.github/workflows/main.yml`

Now that we have our basic setup, let’s install dependencies, build the site and run our different tests. Note that since we use Cypress for our end-to-end tests, we used its Github Action to install our dependencies. If you don’t use it, you can just run `yarn install --frozen-lockfile` and use the `actions/cache` to cache your dependencies.

Now, we have our build directory ready, and we can upload our files to GCS.

For this you’ll need to go to your GCloud console, go to “IAM > Service Accounts”, select the `github-actions` service account that you previously created with Terraform, and create a JSON key that you can download. Encode it to Base 64 (for example by using `base64 -i /path/to/your/file.json` in your terminal).

Then go to your Github repository secrets and add the base64-encoded string as a new secret named `GOOGLE_APPLICATION_CREDENTIALS` . Then we can upload the files:

Let’s examine the above step of our workflow. It is just as if you were running `gsutil -m cp -z html,css,js,json,txt,xml,svg -r ./public/* gs://{bucket-id}/` in your terminal.

The option`-m` allows for concurrent requests and will make the whole command faster.

`cp` means we want to copy files.

`-z html,css,js,json,txt,xml,svg` is interesting because it means that you want to gzip those files. It will take less space in your bucket and, more interestingly, will send the files gzipped and set the correct HTTP headers whenever a request is made.

`-r ./public/* gs://{bucket-id}/` will recursively copy the files and directory in public (your gatsby build directory) to the root of your bucket.

That’s it, you can now access your website! But **we’re not finished**! We want to set our cache control rules! You can change them if they do not fit your needs.

Now that we have our assets cached for 1 year (only 1 day for HTML files and JSON files), we need to invalidate the CDN cache in the CI, so that our new version can be available directly to new users, without waiting for our files to be expired on CDN nodes.

And now we’re done!

# Conclusion

For now, Google Cloud Storage is perfect for deploying static assets to a CDN but still misses some functionalities if you want to deploy a whole website. Other solutions are also faster and easier. But it is stable, has blazing fast performances, and it feels safer.

*Drug discovery is a challenging, intellectually complex, and rewarding endeavor: we help develop effective and safe cures to diseases affecting millions of people. If you’re looking to have a massive impact, join us!*  [*https://inato.com/careers/*](https://inato.com/careers/)