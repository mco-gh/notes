GPUs on Compute Engine  |  Compute Engine Documentation       |  Google Cloud Platform

star_border
star_border
star_border
star_border
star_border

- [Compute Engine](https://cloud.google.com/compute/)

- chevron_right

 [Documentation](https://cloud.google.com/compute/docs/)

#  GPUs on Compute Engine

- [Contents](https://cloud.google.com/compute/docs/gpus/#top_of_page)
- [Introduction](https://cloud.google.com/compute/docs/gpus/#introduction)
- [Restrictions](https://cloud.google.com/compute/docs/gpus/#restrictions)
- [What's next?](https://cloud.google.com/compute/docs/gpus/#whats_next)

star  **Beta**

This is a Beta release of Google Compute Engine GPUs. This feature is not covered by any SLA or deprecation policy and may be subject to backward-incompatible changes.

Google Compute Engine provides graphics processing units (GPUs) that you can attach to your virtual machine instances. You can use these GPUs to accelerate specific workloads on your instances such as machine learning and data processing.

To learn how to add GPUs to your instances, read[Attaching GPUs to Instances](https://cloud.google.com/compute/docs/gpus/add-gpus).

## [arrow_upward](https://cloud.google.com/compute/docs/gpus/#top_of_page)Introduction

Compute Engine provides NVIDIA® Tesla® K80 GPUs for your instances in passthrough mode so that your virtual machine instances have direct control over the GPUs and their associated memory. You can attach GPUs to any non-shared-core[predefined machine type](https://cloud.google.com/compute/docs/machine-types#predefined_machine_types)or [custom machine type](https://cloud.google.com/compute/docs/machine-types#custom_machine_types)that you are able to create in a zone. However, instances with lower numbers of GPUs are limited to a maximum number of vCPUs. In general, higher numbers of GPUs allow you to create instances with higher numbers of vCPUs and system memory.

| GPU model | GPUs | GPU boards | GPU memory | Available vCPUs | Available memory | Available zones |
| --- | --- | --- | --- | --- | --- | --- |
| [NVIDIA® Tesla® K80](http://www.nvidia.com/object/tesla-k80.html) | 1 GPU | 1/2 board | 12 GB GDDR5 | 1 - 8 vCPUs | 1 - 52 GB | - us-west1-b<br>- us-east1-d<br>- europe-west1-b<br>- asia-east1-a |
| 2 GPUs | 1 board | 24 GB GDDR5 | 1 - 16 vCPUs | 1 - 104 GB |
| 4 GPUs | 2 boards | 48 GB GDDR5 | 1 - 32 vCPUs | 1 - 208 GB |
| 8 GPUs | 4 boards | 96 GB GDDR5 | 1 - 64 vCPUs | 1 - 416 GB |

For GPU pricing, see the[Compute Engine pricing page](https://cloud.google.com/compute/pricing#gpus).

## [arrow_upward](https://cloud.google.com/compute/docs/gpus/#top_of_page)Restrictions

Instances with GPUs have specific restrictions that make them behave differently than other instance types.

- You must have GPU quota before you can create instances with GPUs. Check the [quotas page](https://console.cloud.google.com/compute/quotas) to ensure that you have enough GPUs available in your project. Free Trial accounts do not receive GPU quota by default.
- Instances with one or more GPUs have a maximum number of vCPUs for each GPU that you attach to the instance. For example, each NVIDIA® Tesla® K80 GPU allows you to have up to eight vCPUs in your instance machine type. To see the available vCPU ranges for different GPU configurations, see the [GPUs list](https://cloud.google.com/compute/docs/machine-types).
- You cannot attach GPUs to instances with [shared-core machine types](https://cloud.google.com/compute/docs/machine-types#sharedcore).
- You cannot attach GPUs to [preemptible instances](https://cloud.google.com/compute/docs/instances/preemptible).
- GPU instances cannot [live migrate](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#live_migrate) for host maintenance events because the VM instance is directly attached to a specific hardware device. When you create GPU instances, you must [set your instances to terminate for host maintenance events](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#settingoptions) and optionally, [set the instance to restart](https://cloud.google.com/compute/docs/instances/setting-instance-scheduling-options#autorestart) on a different host system after the VM instance terminates. Learn how to [handle host maintenance events](https://cloud.google.com/compute/docs/gpus/add-gpus#host-maintenance) on instances with GPUs.
- GPUs require device drivers in order to function properly. You can use any driver that you like, but you must ensure that these drivers are installed and configured properly. For example, some drivers install kernel modules that you must reconfigure every time you update the kernel for your instance. You can avoid this issue by installing drivers using dynamic kernel module support system (DKMS). For instructions on how to install drivers for instances with GPUs, see [installing GPU drivers](https://cloud.google.com/compute/docs/gpus/add-gpus#install-gpu-driver).

## [arrow_upward](https://cloud.google.com/compute/docs/gpus/#top_of_page)What's next?

- [Create instances with GPUs](https://cloud.google.com/compute/docs/gpus/add-gpus#create-new-gpu-instance)
- Read the [Compute Engine pricing page](https://cloud.google.com/compute/pricing#gpus) to learn about GPU pricing.

Was this page helpful? Let us know how we did:
star_border
star_border
star_border
star_border
star_border

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated May 12, 2017.