Zero to JupyterHub — Zero to JupyterHub with Kubernetes 0.4 documentation

# Zero to JupyterHub[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#zero-to-jupyterhub)

[JupyterHub](https://github.com/jupyterhub/jupyterhub) is a tool that allows you to quickly utilize cloud computing infrastructure to manage a hub that enables your users to interact remotely with a computing environment that you specify. JupyterHub offers a useful way to standardize the computing environment of a group of people (e.g., for a class of students or an analytics team), as well as allowing people to access the hub remotely.

This growing collection of information will help you set up your own JupyterHub instance. It is in an early stage, so the information and tools may change quickly.

If you have tips or deployments that you would like to share, see[Resources from the community](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#community-resources). If you see anything that is incorrect or have any questions, feel free to reach out at the [issues page](https://github.com/jupyterhub/zero-to-jupyterhub-k8s/issues).

## Getting to Step Zero: your Kubernetes cluster[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#getting-to-step-zero-your-kubernetes-cluster)

This section describes a Kubernetes cluster and outlines how to complete *Step Zero: your Kubernetes cluster* for different cloud providers and infrastructure.

*Step Zero: your Kubernetes cluster*

- [Creating a Kubernetes Cluster](http://zero-to-jupyterhub.readthedocs.io/en/latest/create-k8s-cluster.html)
- [Step Zero: Kubernetes on Google Cloud](http://zero-to-jupyterhub.readthedocs.io/en/latest/google/step-zero-gcp.html)
- [Step Zero: Kubernetes on Microsoft Azure Container Service (AKS)](http://zero-to-jupyterhub.readthedocs.io/en/latest/microsoft/step-zero-azure.html)
- [Step Zero: Kubernetes on Amazon Web Services (AWS)](http://zero-to-jupyterhub.readthedocs.io/en/latest/amazon/step-zero-aws.html)
- [JupyterHub on Red Hat OpenShift](http://zero-to-jupyterhub.readthedocs.io/en/latest/redhat/step-zero-openshift.html)

## Creating your JupyterHub[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#creating-your-jupyterhub)

This tutorial starts from *Step Zero: your Kubernetes cluster* and describes the steps needed for you to create a complete initial JupyterHub deployment. This will use the JupyterHub Helm chart which provides sensible defaults for an initial deployment.

To begin, go to [Setting up Helm](http://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html#setup-helm).

*Creating your JupyterHub*

- [Getting started with JupyterHub](http://zero-to-jupyterhub.readthedocs.io/en/latest/getting-started.html)
- [Setting up Helm](http://zero-to-jupyterhub.readthedocs.io/en/latest/setup-helm.html)
- [Setting up JupyterHub](http://zero-to-jupyterhub.readthedocs.io/en/latest/setup-jupyterhub.html)
- [Turning Off JupyterHub and Computational Resources](http://zero-to-jupyterhub.readthedocs.io/en/latest/turn-off.html)

## Customization Guide[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#customization-guide)

JupyterHub can be configured and customized to fit a variety of deployment requirements. If you would like to expand JupyterHub, customize its setup, increase the computational resources available for users, or change authentication services, this guide will walk you through the steps. See the [Helm Chart Configuration Reference](http://zero-to-jupyterhub.readthedocs.io/en/latest/reference.html#id1) for a list of frequently used configurable helm chart fields.

*Customization Guide*

- [Extending your JupyterHub setup](http://zero-to-jupyterhub.readthedocs.io/en/latest/extending-jupyterhub.html)
    - [Applying configuration changes](http://zero-to-jupyterhub.readthedocs.io/en/latest/extending-jupyterhub.html#applying-configuration-changes)
- [Customizing the User Environment](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-environment.html)
    - [Use an existing Docker image](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-environment.html#use-an-existing-docker-image)
    - [Build a custom Docker image with `repo2docker`](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-environment.html#build-a-custom-docker-image-with-repo2docker)
    - [Use JupyterLab by default](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-environment.html#use-jupyterlab-by-default)
    - [Set environment variables](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-environment.html#set-environment-variables)
    - [Pre-populating user’s `$HOME` directory with files](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-environment.html#pre-populating-user-s-home-directory-with-files)
- [User Resources](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-resources.html)
    - [Set user memory and CPU guarantees / limits](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-resources.html#set-user-memory-and-cpu-guarantees-limits)
    - [Modifying user storage type and size](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-resources.html#modifying-user-storage-type-and-size)
    - [Expanding and contracting the size of your cluster](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-resources.html#expanding-and-contracting-the-size-of-your-cluster)
- [User storage in JupyterHub](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-storage.html)
    - [How can this process break down?](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-storage.html#how-can-this-process-break-down)
    - [Configuration](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-storage.html#configuration)
    - [Turn off per-user persistent storage](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-storage.html#turn-off-per-user-persistent-storage)
- [User Management](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-management.html)
    - [Culling user pods](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-management.html#culling-user-pods)
    - [Admin Users](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-management.html#admin-users)
    - [Authenticating Users](http://zero-to-jupyterhub.readthedocs.io/en/latest/user-management.html#authenticating-users)

## Administrator Guide[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#administrator-guide)

This section provides information on managing and maintaining a staging or production deployment of JupyterHub. It has considerations for managing cloud-based deployments and tips for maintaining your deployment.

*Administrator Guide*

- [The JupyterHub Architecture](http://zero-to-jupyterhub.readthedocs.io/en/latest/architecture.html)
- [Debugging Kubernetes](http://zero-to-jupyterhub.readthedocs.io/en/latest/debug.html)
    - [Debugging commands](http://zero-to-jupyterhub.readthedocs.io/en/latest/debug.html#debugging-commands)
    - [Troubleshooting Examples](http://zero-to-jupyterhub.readthedocs.io/en/latest/debug.html#troubleshooting-examples)
- [Authentication](http://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html)
    - [Authenticating with OAuth2](http://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html#authenticating-with-oauth2)
    - [Full Example of Google OAuth2](http://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html#full-example-of-google-oauth2)
    - [Adding a Whitelist](http://zero-to-jupyterhub.readthedocs.io/en/latest/authentication.html#adding-a-whitelist)
- [Speed and Optimization](http://zero-to-jupyterhub.readthedocs.io/en/latest/optimization.html)
    - [Picking a Scheduler Strategy](http://zero-to-jupyterhub.readthedocs.io/en/latest/optimization.html#picking-a-scheduler-strategy)
    - [Pre-pulling](http://zero-to-jupyterhub.readthedocs.io/en/latest/optimization.html#pre-pulling)
- [Security](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html)
    - [HTTPS](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#https)
    - [Secure access to Helm](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#secure-access-to-helm)
    - [Audit Cloud Metadata server access](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#audit-cloud-metadata-server-access)
    - [Delete the Kubernetes Dashboard](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#delete-the-kubernetes-dashboard)
    - [Use Role Based Access Control (RBAC)](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#use-role-based-access-control-rbac)
    - [Kubernetes API Access](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#kubernetes-api-access)
    - [Kubernetes Network Policies](http://zero-to-jupyterhub.readthedocs.io/en/latest/security.html#kubernetes-network-policies)
- [Upgrading your JupyterHub Kubernetes deployment](http://zero-to-jupyterhub.readthedocs.io/en/latest/upgrading.html)
    - [Major helm-chart upgrades](http://zero-to-jupyterhub.readthedocs.io/en/latest/upgrading.html#major-helm-chart-upgrades)
    - [Subtopics](http://zero-to-jupyterhub.readthedocs.io/en/latest/upgrading.html#subtopics)
    - [Troubleshooting](http://zero-to-jupyterhub.readthedocs.io/en/latest/upgrading.html#troubleshooting)
- [FAQ](http://zero-to-jupyterhub.readthedocs.io/en/latest/troubleshooting.html)
    - [I thought I had deleted my cloud resources, but they still show up. Why?](http://zero-to-jupyterhub.readthedocs.io/en/latest/troubleshooting.html#i-thought-i-had-deleted-my-cloud-resources-but-they-still-show-up-why)
    - [How does billing for this work?](http://zero-to-jupyterhub.readthedocs.io/en/latest/troubleshooting.html#how-does-billing-for-this-work)
- [Advanced Topics](http://zero-to-jupyterhub.readthedocs.io/en/latest/advanced.html)
    - [Ingress](http://zero-to-jupyterhub.readthedocs.io/en/latest/advanced.html#ingress)
    - [Arbitrary extra code and configuration in `jupyterhub_config.py`](http://zero-to-jupyterhub.readthedocs.io/en/latest/advanced.html#arbitrary-extra-code-and-configuration-in-jupyterhub-config-py)
    - [Picking a Scheduler Strategy](http://zero-to-jupyterhub.readthedocs.io/en/latest/advanced.html#picking-a-scheduler-strategy)
    - [Pre-pulling Images for Faster Startup](http://zero-to-jupyterhub.readthedocs.io/en/latest/advanced.html#pre-pulling-images-for-faster-startup)
- [Appendix: Projecting deployment costs](http://zero-to-jupyterhub.readthedocs.io/en/latest/cost.html)
    - [Factors influencing costs](http://zero-to-jupyterhub.readthedocs.io/en/latest/cost.html#factors-influencing-costs)
    - [Interactive Cost Estimator](http://zero-to-jupyterhub.readthedocs.io/en/latest/cost.html#interactive-cost-estimator)
    - [Examples](http://zero-to-jupyterhub.readthedocs.io/en/latest/cost.html#examples)

## Resources from the community[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#resources-from-the-community)

This section gives the community a space to provide information on setting up, managing, and maintaining JupyterHub.

Important:

We recognize that Kubernetes has many deployment options. As a project team with limited resources to provide end user support, we rely on community members to share their collective Kubernetes knowledge and JupyterHub experiences.

We hope that you will use this section to share deployments with on a variety of infrastructure and for different use cases. There is also a [community maintained list](http://zero-to-jupyterhub.readthedocs.io/en/latest/users-list.html) of users of this Guide and the JupyterHub Helm Chart.

Please submit a pull request to add to this section. Thanks.
*Resources from the community*

- [Community-authored documentation](http://zero-to-jupyterhub.readthedocs.io/en/latest/additional-resources.html)
- [Zero to JupyterHub Gallery of Deployments](http://zero-to-jupyterhub.readthedocs.io/en/latest/users-list.html)

## Reference[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#reference)

*Reference*

- [Helm Chart Configuration Reference](http://zero-to-jupyterhub.readthedocs.io/en/latest/reference.html)
- [Official JupyterHub and Project Jupyter Documentation](http://zero-to-jupyterhub.readthedocs.io/en/latest/reference-docs.html)
- [Tools used in a JupyterHub Deployment](http://zero-to-jupyterhub.readthedocs.io/en/latest/tools.html)
- [Glossary](http://zero-to-jupyterhub.readthedocs.io/en/latest/glossary.html)

## Institutional support[¶](http://zero-to-jupyterhub.readthedocs.io/en/latest/index.html#institutional-support)

This guide and the associated helm chart would not be possible without the amazing institutional support from the following organizations (and the organizations that support them!)

- [UC Berkeley Data Science Division](https://data.berkeley.edu/)
- [Berkeley Institute for Data Science](https://bids.berkeley.edu/)
- [Cal Poly, San Luis Obispo](https://www.calpoly.edu/)
- [Simula Research Institute](https://www.simula.no/)