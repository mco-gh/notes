The Littlest JupyterHub — The Littlest JupyterHub v0.1 documentation

# The Littlest JupyterHub[¶](https://tljh.jupyter.org/en/latest/index.html#the-littlest-jupyterhub)

A simple [JupyterHub](https://github.com/jupyterhub/jupyterhub) distribution for a small (0-100) number of users on a single server. We recommend reading[When to use The Littlest JupyterHub](https://tljh.jupyter.org/en/latest/topic/whentouse.html#topic-whentouse) to determine if this is the right tool for you.

## Development Status[¶](https://tljh.jupyter.org/en/latest/index.html#development-status)

This project is currently in **beta** state. Folks have been using installations of TLJH for more than a year now to great success. While we try hard not to, we might still make breaking changes that have no clear upgrade pathway.

## Installation[¶](https://tljh.jupyter.org/en/latest/index.html#installation)

The Littlest JupyterHub (TLJH) can run on any server that is running at least**Ubuntu 18.04**. Earlier versions of Ubuntu are not supported. We have a bunch of tutorials to get you started.

- Tutorials to create a new server from scratch on a cloud provider & run TLJH on it. These are **recommended** if you do not have much experience setting up servers.
    - [Installing on Digital Ocean](https://tljh.jupyter.org/en/latest/install/digitalocean.html)
    - [Installing on Jetstream](https://tljh.jupyter.org/en/latest/install/jetstream.html)
    - [Installing on Google Cloud](https://tljh.jupyter.org/en/latest/install/google.html)
    - [Installing on Amazon Web Services](https://tljh.jupyter.org/en/latest/install/amazon.html)
    - [Installing on Azure](https://tljh.jupyter.org/en/latest/install/azure.html)
    - [Installing on your own server](https://tljh.jupyter.org/en/latest/install/custom-server.html)

Once you are ready to run your server for real, it’s a good idea to proceed directly to [Enable HTTPS](https://tljh.jupyter.org/en/latest/howto/admin/https.html).

## How-To Guides[¶](https://tljh.jupyter.org/en/latest/index.html#how-to-guides)

How-To guides answer the question ‘How do I…?’ for a lot of topics.

### Content and Data[¶](https://tljh.jupyter.org/en/latest/index.html#content-and-data)

- [Distributing materials to users with nbgitpuller](https://tljh.jupyter.org/en/latest/howto/content/nbgitpuller.html)
- [Adding data to the JupyterHub](https://tljh.jupyter.org/en/latest/howto/content/add-data.html)
- [Share data with your users](https://tljh.jupyter.org/en/latest/howto/content/share-data.html)

### The user environment[¶](https://tljh.jupyter.org/en/latest/index.html#the-user-environment)

- [Install conda, pip or apt packages](https://tljh.jupyter.org/en/latest/howto/env/user-environment.html)
- [Change default User Interface for users](https://tljh.jupyter.org/en/latest/howto/env/notebook-interfaces.html)
- [Configure resources available to users](https://tljh.jupyter.org/en/latest/howto/env/server-resources.html)

### Authentication[¶](https://tljh.jupyter.org/en/latest/index.html#authentication)

We have a special set of How-To Guides on using various forms of authentication with your JupyterHub. For more information on Authentication, see[Configuring JupyterHub authenticators](https://tljh.jupyter.org/en/latest/topic/authenticator-configuration.html#topic-authenticator-configuration)

- [Authenticate *any* user with a single shared password](https://tljh.jupyter.org/en/latest/howto/auth/dummy.html)
- [Authenticate using GitHub Usernames](https://tljh.jupyter.org/en/latest/howto/auth/github.html)
- [Let users choose a password when they first log in](https://tljh.jupyter.org/en/latest/howto/auth/firstuse.html)
- [Let users sign up with a username and password](https://tljh.jupyter.org/en/latest/howto/auth/nativeauth.html)

### Administration and security[¶](https://tljh.jupyter.org/en/latest/index.html#administration-and-security)

- [Add / Remove admin users](https://tljh.jupyter.org/en/latest/howto/admin/admin-users.html)
- [Estimate Memory / CPU / Disk needed](https://tljh.jupyter.org/en/latest/howto/admin/resource-estimation.html)
- [Resize the resources available to your JupyterHub](https://tljh.jupyter.org/en/latest/howto/admin/resize.html)
- [Check your memory usage](https://tljh.jupyter.org/en/latest/howto/admin/nbresuse.html)
- [Enable HTTPS](https://tljh.jupyter.org/en/latest/howto/admin/https.html)
- [Enabling Jupyter Notebook extensions](https://tljh.jupyter.org/en/latest/howto/admin/enable-extensions.html)

### Cloud provider configuration[¶](https://tljh.jupyter.org/en/latest/index.html#cloud-provider-configuration)

- [Perform common Digital Ocean configuration tasks](https://tljh.jupyter.org/en/latest/howto/providers/digitalocean.html)
- [Perform common Microsoft Azure configuration tasks](https://tljh.jupyter.org/en/latest/howto/providers/azure.html)

## Topic Guides[¶](https://tljh.jupyter.org/en/latest/index.html#topic-guides)

Topic guides provide in-depth explanations of specific topics.

- [When to use The Littlest JupyterHub](https://tljh.jupyter.org/en/latest/topic/whentouse.html)
- [Server Requirements](https://tljh.jupyter.org/en/latest/topic/requirements.html)
- [Security Considerations](https://tljh.jupyter.org/en/latest/topic/security.html)
- [Customizing the Installer](https://tljh.jupyter.org/en/latest/topic/customizing-installer.html)
- [What does the installer do?](https://tljh.jupyter.org/en/latest/topic/installer-actions.html)
- [Configuring TLJH with `tljh-config`](https://tljh.jupyter.org/en/latest/topic/tljh-config.html)
- [Configuring JupyterHub authenticators](https://tljh.jupyter.org/en/latest/topic/authenticator-configuration.html)
- [Custom `jupyterhub_config.py` snippets](https://tljh.jupyter.org/en/latest/topic/escape-hatch.html)

## Troubleshooting[¶](https://tljh.jupyter.org/en/latest/index.html#troubleshooting)

In time, all systems have issues that need to be debugged. Troubleshooting guides help you find what is broken & hopefully fix it.

- [Looking at Logs](https://tljh.jupyter.org/en/latest/troubleshooting/logs.html)

Often, your issues are not related to TLJH itself but to the cloud provider your server is running on. We have some documentation on common issues you might run into with various providers and how to fix them. We welcome contributions here to better support your favorite provider!

- [Troubleshooting issues on Google Cloud](https://tljh.jupyter.org/en/latest/troubleshooting/providers/google.html)
- [Troubleshooting issues on Amazon Web Services](https://tljh.jupyter.org/en/latest/troubleshooting/providers/amazon.html)
- [Troubleshooting issues on your own server](https://tljh.jupyter.org/en/latest/troubleshooting/providers/custom.html)

## Contributing[¶](https://tljh.jupyter.org/en/latest/index.html#contributing)

We want you to contribute to TLJH in the ways that are most useful and exciting to you. This section contains documentation helpful to people contributing in various ways.

- [Writing documentation](https://tljh.jupyter.org/en/latest/contributing/docs.html)
- [Code Review guidelines](https://tljh.jupyter.org/en/latest/contributing/code-review.html)
- [Setting up Development Environment](https://tljh.jupyter.org/en/latest/contributing/dev-setup.html)
- [Testing TLJH](https://tljh.jupyter.org/en/latest/contributing/tests.html)
- [TLJH Plugins](https://tljh.jupyter.org/en/latest/contributing/plugins.html)
- [Environments & Packages](https://tljh.jupyter.org/en/latest/contributing/packages.html)