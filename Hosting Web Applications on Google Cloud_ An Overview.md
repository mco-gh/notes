Hosting Web Applications on Google Cloud: An Overview

![1*iN7dQ1eMsAyXF6fzaqFvXQ.png](../_resources/94e8cc8d592c7f6eb43b8ed881147b2e.png)
![1*iN7dQ1eMsAyXF6fzaqFvXQ.png](../_resources/110758ed122bf1783a07c6fd9899b94c.png)

# Hosting Web Applications on Google Cloud: An Overview

## Get Cooking in Cloud

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='52' height='58' viewBox='0 0 52 58' class='cl cm mq mr ms mt cr js-evernote-checked' data-evernote-id='174'%3e%3cpath d='M1.49 16.25A27.53 27.53 0 0 1 26 1.55V.45A28.63 28.63 0 0 0 .51 15.75l.98.5zM26 1.55a27.53 27.53 0 0 1 24.51 14.7l.98-.5A28.63 28.63 0 0 0 26 .45v1.1zm24.51 40.2A27.53 27.53 0 0 1 26 56.45v1.1a28.63 28.63 0 0 0 25.49-15.3l-.98-.5zM26 56.45a27.53 27.53 0 0 1-24.51-14.7l-.98.5A28.63 28.63 0 0 0 26 57.55v-1.1z' data-evernote-id='175' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)![0*pPeZ4hKE7KR07g89.](../_resources/e34503ce6d2eb29f877734d28b03abaa.jpg)](https://medium.com/@pvergadia?source=post_page-----46f5605eb3a6----------------------)

[Priyanka Vergadia](https://medium.com/@pvergadia?source=post_page-----46f5605eb3a6----------------------)

[Aug 17](https://medium.com/google-cloud/hosting-web-applications-on-google-cloud-an-overview-46f5605eb3a6?source=post_page-----46f5605eb3a6----------------------) · 5 min read

# Introduction

***“Get Cooking in Cloud”*** is a blog and video series to help enterprises and developers build business solutions on Google Cloud. In this series we plan on identifying specific topics that developers are looking to architect on Google cloud. Once identified we will create a mini series on that topic.

In this first mini series we will cover, how to create websites on Google Cloud. If your business revenue and customer satisfaction depends on the availability and scalability of your website, then you are at the right place. In the next few blogs, we will elaborate on creating websites:

1. Hosting web apps on Google Cloud: An Overview (This article)

2. [Hosting a web app on Google Cloud using Google Cloud Storage](https://medium.com/@pvergadia/hosting-a-static-website-on-google-cloud-using-google-cloud-storage-ddebcdcc8d5b)

3. [Hosting a web app on Google Cloud using Cloud Run](https://medium.com/google-cloud/hosting-a-website-on-google-cloud-using-cloud-run-a65343a98fce)

4. [5 Steps to deploy websites on Google Cloud using Google Compute Engine](https://medium.com/p/c6fe84d76f51)

5. [Scaling web app on Google Compute Engine](https://medium.com/p/d21d6ce3e837/)

6. [Case Study](https://medium.com/faun/case-study-hosting-scalable-web-apps-on-google-cloud-c0bb675812c8)

In this article, we will see four tools that help you scale from small to large website, depending on the needs. So, read on!

# What you’ll learn

- Overview of different ways to create websites on Google Cloud

# Prerequisites

- Basic concepts and constructs of Google Cloud so you can recognize the names of the products.
- This picture (by Greg Wilson) is a good place to start and learn about all the products in less than four words:

![1*T1r2U3OIJnouB2VRvLASDA.png](../_resources/7e09dffc0bd6fbad288bafd7b5b7c3a7.png)
![1*T1r2U3OIJnouB2VRvLASDA.png](../_resources/8936d66ec9cc72298d28d7ce4d433b33.png)
Google Cloud Developers Cheat Sheet

# Check out the video

# How to create websites on Google Cloud

At a high level, there are four recipes to build a website or an application on Google Cloud. Depending on where you are in your Google Cloud journey, your business needs, and the maturity of the development and infrastructure team, one of these options should fit your needs.

![0*Pkrb_tleSfNpMlAC](../_resources/9c05f26c7ba12a831b9cee090cec77e7.png)
![0*Pkrb_tleSfNpMlAC](../_resources/318801c0241ae85bace1ef0072c5c3a4.png)
Google Cloud Storage

Static websites**  **are a good option for sites like blogs — where the page rarely changes after it has been published, or where there isn’t any dynamically-generated content. All you need to set up a static website on Google Cloud is a [cloud storage bucket](https://cloud.google.com/storage/) connected to your domain name and that’s it!!

As your business starts to mature and customers are interested in buying things from your website, you might need to generate dynamic content and enable payments. But if your company is still small, you want to be able to grow your website without worrying about scaling the website based on the increase in demand.

![0*38aeBg5nEkROZL8e](../_resources/013c58aba830c3ef5d59009064d58023.png)
![0*38aeBg5nEkROZL8e](../_resources/4ec8387154db0ffd49491103a8cf0590.png)
App Engine

In such a scenario, Google Cloud’s managed and serverless offerings like [App Engin](https://cloud.google.com/appengine/)e or [Cloud Run](https://cloud.google.com/run/) would be apt, this allows you to focus on delivering features and let Google worry about operating and managing the infrastructure.This provides a wide range of features that make scalability, load balancing, logging, monitoring, and security much easier than if you had to build and manage the website yourself.

![0*38aeBg5nEkROZL8e](../_resources/013c58aba830c3ef5d59009064d58023.png)
![0*38aeBg5nEkROZL8e](../_resources/4ec8387154db0ffd49491103a8cf0590.png)
Cloud Run

When you use Cloud Run, you can code in any programming language, because your application is deployed as a container, and Google will seamlessly launch and scale your application for you. So give it a try!

For websites with higher complexity, you probably want more options and control than a managed platform offers. Whether it’s configuring your servers or virtual machines, or if it’s a need for specific memory, SSDs, and GPUs, it makes sense to use Compute Engine.

![0*bEHgJIVKfPlXkC_m](../_resources/21798241c67a5a95038c23be70319e37.png)
![0*bEHgJIVKfPlXkC_m](../_resources/21729c3d9d0d0ee3cd2968e82467c72a.png)
Compute Engine

[Compute Engine](https://cloud.google.com/compute/) provides a robust computing infrastructure, but you must choose and configure the platform components that you want to use. Google ensures that resources are available, reliable, and ready for you to use, but it’s up to you to provision and manage them.

The advantage of using compute engine is that you have complete control of the systems and unlimited flexibility. The easiest way to deploy a complete web-serving stack on Compute engine is by using [Google Cloud Marketplace](https://cloud.google.com/marketplace/). With just a few clicks, you can deploy any of over 100 fully-realized solutions.

![0*xVn8HXClG4WdbNSM](../_resources/ac70be674aa88f06377ed6aeb5442e69.png)
![0*xVn8HXClG4WdbNSM](../_resources/17da4a2589ae6e0e1653eb79f42927a1.png)
Google Cloud Marketplace

For a more detailed explanation of how to set up Compute engine to serve scalable and resilient websites, stay tuned for upcoming articles.

![0*i3WLIH3mzB9H3jN0](../_resources/643efd26ebbeab98e86729fadfd28c20.png)
![0*i3WLIH3mzB9H3jN0](../_resources/d3e8bd513bf7bcad2cae0afba74800c2.png)
Kubernetes Engine

Finally, for a larger business with more developers and more complicated problems, it makes sense to containerize your application. You will notice that it becomes really hard to manage feature roll outs if the website is one big monolith, which makes it difficult to keep up with the increase in demand and pace of business.

Containerizing web applications provides three key advantages:

- **Componentization:** As your app’s design becomes more complex, containers are a good fit for a [service-oriented architecture](https://wikipedia.org/wiki/Service-oriented_architecture), including [microservices](https://wikipedia.org/wiki/Microservices). This supports scalability.
- **Portability:** A container has everything it needs to run — your app and its dependencies are bundled together. this facilitates portability and fixes the “it-works-on-my-machine” problem that many developers have.
- **Rapid deployment: **When it’s time to deploy, your system is built from a set of definitions and images, so the parts can be deployed quickly, reliably, and automatically. Compared to virtual machines, Containers are typically smaller and deploy much more quickly.

Using Container to deploy web apps on GKE has further advantages because:
1. Container orchestration is built in.

2. Google Cloud offers container registry which is a private storage for container images

3. You can easily use the other components of the Google Cloud platform in this architecture.

Using Kubernetes Engine makes sense in following situations:

- If you have a complicated website with multiple different pieces which are better off in separate services for easy management.
- If there are separate development teams for each service so teams can work independently at their own pace.
- If you need to ship changes quickly and easily.

# Conclusion

Whether you are a small blogger looking to grow your community, or a huge, multi-scale eCommerce site, hopefully this has been helpful in identifying which tools within the Google Cloud Platform are right for your specific web use case.

# Next steps

- Follow this blog series on [Google Cloud Platform Medium](https://medium.com/google-cloud).
- Follow [Get Cooking in Cloud](https://www.youtube.com/watch?v=pxp7uYUjH_M) video series and subscribe to Google cloud platform YouTube channel
- Want more stories? Check my [Medium](https://medium.com/@pvergadia/), [follow me on twitter](https://twitter.com/pvergadia).
- Enjoy the ride with us though this series and learn more about Google Cloud :)