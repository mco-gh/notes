How Amazon's EC2 Container Service is Growing in the Public Cloud

# How Amazon's EC2 Container Service is Growing in the Public Cloud

By:     [Sean Michael Kerner](http://www.eweek.com/Authors/sean-michael-kerner)     |  June 15, 2017

-

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |

|     |     |     |     |
| --- | --- | --- | --- |
|     |     |     |     |

General Manager of Amazon's public cloud container service explains how the platform has evolved and where it's headed.

Three and a half years ago, Deepak Singh was a principal product product manager for Amazon Web Services (AWS) Elastic Compute Cloud (EC2) and customers were asking him about enabling capabilities to run Docker containers.

While it was possible to run Docker on EC2 just like any other type of software, it became clear to Singh and AWS that a broader service was required. That broader service is the Amazon EC2 Container Service (ECS), which Singh now oversee as General Manager.

"People realized that while they could run Docker on an EC2 instance, they wanted to run multiple container applications potentially across different teams and business units," Singh told *eWEEK*.

ECS provides the automated services needed to manage, run and deploy container applications at scale. Singh said that ECS also provides a familiar interface for existing AWS users, providing an integrated approach for containers to use the broader array of cloud services offered by Amazon.

#### Further reading

- [AWS Releases Bevy of New Dev Tools](http://www.eweek.com/development/aws-releases-bevy-of-new-ai-container-devops-development-tools)

- [AWS Rounds Out re:Invent News with 13 More Features](http://www.eweek.com/cloud/aws-rounds-out-re-invent-news-with-13-more-features)

- [AWS Pushes 'Serverless' App Development at Its New...](http://www.eweek.com/cloud/aws-pushes-serverless-app-development-at-its-new-york-summit)

ECS has evolved over the years to include container application level Identity and Access Management (IAM) and application load balancing capabilities. The overall AWS platform adds features on a regular basis and Singh noted that his job is to bring a container viewpoint to the product development teams. As such, when new AWS features are announced, there is an understanding that end-users customer will run those features inside of containers on ECS.

### Docker

Docker Inc. also has a working relationship with AWS that enables Docker for AWS, as well as the commercially supported Docker Enterprise Edition (EE) product platforms.

Singh explained that Docker EE and Docker for AWS provide the Docker Inc full stack view of how to run containers. In contrast, what ECS provides is an AWS viewpoint, with a style and APIs that are consistent with AWS' approach to management.

"We work with companies like Docker Inc as a partner, to provide whatever they want to provide," Singh said.

Singh added that the model enables an existing Docker customer that is already running with Docker EE on-premises, to run with the same Docker approach in AWS as well.

The ECS service can use any distribution of Linux, but requires that organizations use the AWS agent, which is small piece of code written in Go. Singh noted that many leading Linux distributions are already available with the pre-configured Go code.

From a Docker Engine perspective, Singh said that ECS simply runs 'vanilla' upstream open-source Docker images.

### Container Orchestration

Container orchestration is a robust area of technology today with multiple choices in the market including Docker Swarm, Apache Mesos and the Kubernetes open-source efforts. EC2 uses it's own approach to container orchestration.

"The approach we have take is to provide our way of handling container orchestration," Singh said. "But we always listen to our customers, so if you want to run Kubernetes, you could run your own, or use one from an AWS partner, like CoreOS Tectonic."

### Security

Security is another hot topic in the container market and AWS also has its own viewpoint on security best practises.

Containers can run on bare-metal, or directly on host operating systems, but that's not what AWS provides. Instead the ECS approach is that containers must run inside of a Virtual Machine (VM), to provide a layer of isolation and control.

"The isolation boundary that we trust is a VM," Singh said. "Our customers wanted more, so we added the ability to do Role Based Access Control at the container level."

Going a step further, AWS is building out the capability on the networking side to enable cloud security groups at the container level. With that feature AWS users will be able to filter traffic at the container-level.

"So you could have two containers, running on the same host and you can attach a different networking interface to each of them, with their own policies," Singh said. "We're basically bringing some of the features of our Virtual Private Cloud (VPC) networking capability to containers."

Singh noted that that while there is a class of organizations that has already decided to make the jump to containers, there are many other organizations that are still trying to make sense of how to use containers for their applications. He added that helping organizations to understand how to migrate to containers is an ongoing conversation.

"Organizations are now also starting to run workloads that need to be PCI-DSS or HIPAA compliant and we're working to support those customers," Singh said.

- [](http://www.eweek.com/cloud/ibm-integrates-with-bmw-cardata-to-enable-new-services-for-drivers)

- Previous  [IBM Integrates with BMW CarData to Enable New Services...](http://www.eweek.com/cloud/ibm-integrates-with-bmw-cardata-to-enable-new-services-for-drivers)

-

- Next  [AWS Introduces New Auto Scaling Feature for DynamoDB...](http://www.eweek.com/cloud/aws-introduces-new-auto-scaling-feature-for-dynamodb-cloud-database)

- [](http://www.eweek.com/cloud/aws-introduces-new-auto-scaling-feature-for-dynamodb-cloud-database)

 ![Sean Michael Kerner](../_resources/8e8946dc9e45745a91442b400ff20b6c.gif)

### Sean Michael Kerner

Sean Michael Kerner is an Internet consultant, strategist, and contributor to several leading IT business web sites.

     [View full bio](http://www.eweek.com/Authors/sean-michael-kerner)

 Connect with Sean:

-

    - [![](../_resources/99b2846d660604eaa276c8e064f94753.png)](https://twitter.com/TechJournalist)

 [+Follow on my eWEEK](http://www.eweek.com/cloud/how-amazon-s-ec2-container-service-is-growing-in-the-public-cloud#)

Login

![Avatar_empty_x1.png](../_resources/abb96b39ad25bccf80519e7a038ea0f2.png)
Write a comment

0 Comments

- Subscribe
- [RSS](http://comments.us1.gigya.com/comments/rss/6067152/B2BTech/1030159)