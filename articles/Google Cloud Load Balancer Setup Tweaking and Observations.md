Google Cloud Load Balancer Setup Tweaking and Observations

# Google Cloud Load Balancer Setup Tweaking and Observations

## Overview and testing the most robust cloud load balancer available today

The Google Cloud Load Balancer (GCLB) is a software defined globally distributed load balancing service. It enables GCP users to distribute applications across the world and scale compute up and down with very little configuration and cost. It allows for 0 to 1 million requests per second (rps) with no pre-warming. Pricing starts at $.025/hr or $0.6/day or $18/month for global anycast (single IP) with autoscaling. It’s low cost and insanely powerful technology available for anyone to test today [for free](https://cloud.google.com/free/).

In this article I will test and demonstrate some of the product features highlighted on https://cloud.google.com/load-balancing/

### **Overview and Setup**

There are a few deployment types for the GCP load balancer service.
Global external:**
**1. HTTP(S) — Public only, single or multi-region
2. SSL proxy, TCP Proxy — Public only, single or multi-region
Regional external:**
**3. Network — Public, TCP/UDP, single region
Regional internal:**

**4. Network — Internal only, TCP/UDP. Can be used in-conjunction with #1 HTTP GCLB.

In this article we will test #1 HTTP public load balancing.

The GCLB can help improve end user latency with the power of Google’s huge network. Check this article [here](https://cloud.google.com/compute/docs/load-balancing/optimize-app-latency) for more detail measuring and comparing latency with different GCLB deployment types.

> Health checks, backends, and front ends are the core elements of the GCLB. Focus on these if you are looking to setup load balancing quickly.

**Health checks**

There are 2 types of health checks you should be aware of. #1 is required by the load balancer and #2 is extra to ensure health of instance groups (autohealing).

1. Used by the load balancer that ensures that requests are only sent to instances that are up and running

2. Used by instance groups to recreate instances that are unhealthy by your set criteria. Ex: HTTP health check port 80; if webserver fails, instance is terminated and recreated.

Health checks are setup within the Compute Engine of the UI as they are used in more than one place in GCP. You can run health checks on instance groups without the load balancer as well. If the healthcheck notices an instance is not healthy it will terminate and recreate.

The GCLB will manage instance health for you and the instance group will manage autoscaling so make sure you have both configured and tuned per your requirements. You can keep them basic; HTTP port 80, if the web server or instance fails the instance group will terminate and recreate a new one.

![](../_resources/1a57c2f86bba29f9fcb4ca562d409906.png)

A basic health check making sure the web server is up and responding on instances

**Backend Services

** These are the services that direct incoming traffic to instance groups. The backend service for a single load balancer can contain a number of backends or buckets. You can have 1 backend service going to multiple instance groups. Each backend is a really a link to the instance groups you wish to distribute traffic between.

So say you plan to have 3 instance groups (US, EMEA, ASIA) setup behind the HTTP(S) load balancer, they are configured 1 backend service. Here is how the back end service looks configured with 3 instance groups (backends) using the health TCP health check we created earlier.

![](../_resources/649f720d6b2c312597fe3194a308f10b.png)
Load balancer edit backend service
**Host and path rules**

This is where you can send subdomains or different hosts to different back ends. Example, if I had eu.mydomain.com I could send those requests directly to my autocomplete-demo-eu instance group. Host and path rules are automatically configured for * to send to the backend service you create so you do not have to worry about configuring these if you are doing basic http load balancing.

![](../_resources/2028ecd144418d87987461bd78497dd6.png)
**Frontends

**The front end is your virtual IP (VIP) or called anycast IP in GCP. One front end can service multiple regions (backends). In most cases you would want a static or reserved IP and not the default ephemeral. This way you can easily point an a-record on your Cloud DNS zone file to your load balancer IP.

![](:/9dfd6ac3b2b0f15f6cb9c9cdd937ddd5)
Load balancer frontend configuration

That’s it for configuration of the GCP load balancer. Easy huh? After you review and update configuration in a few minutes you’ll have traffic going through your front end to your instance groups.

### Tweaking the GCLB

**Health checks

**The portal provides a ⚠️ suggestion after a health check is added to an instance group. The warning provided is that you may want to increase the check interval and unhealthy threshold as shown below. This is working to help you reduce the amount of false positives that may come with services under heavy load. Consider changing your check interval from 2s to 10s, and unhealthy threshold from 2 attempts to 6 attempts if you are just getting started.

![](:/21edd25bc741e48e54bd685a248b8e03)
Default health check value warning

![](../_resources/aedfbe0d02cb784778fd6b873f7b8956.png)
Listen to the portals advice!
**Initial delay

**This is a setting on the instance groups configuration that specifies the delay after an instance has been replaced for the health check to run again. Default is 300 sec which is 5 minutes. Hopefully your instances are light enough to boot in or around a 1 minute. If you think you may need more time for your application to come online after initial boot by the instance group autoscale action, then increase the initial delay.

**Routing

**Incoming client requests are sent to to the region closest to the use assuming the region has capacity. If more than one zone is configured with backends, traffic is distributed across each zone. Check my behavior observations below for more details. Within the zone requests are distributed via round robin. You can override round robin in zone by configuring affinity.

**Affinity

**Typically the LB is going to route new requests to any instance and traffic from one connection is going to route to the same instance. Say you want to set stickiness to make sure all connections from one client go to the same instance. Configure session affinity to client IP. You can also set by cookie. The GCLB sends a cookie on the first client request and future incoming requests with that cookie will be sent to the same instance.

**Scaling instances back or maintenance

**Easy, just drop an instance group’s number of instances. GCE takes all instances in that group offline and you are no longer charged. Now you can scale back or perform maintenance, maybe change an instance template to a new version of software in a region. Take a region out of service by removing the instance group from the load balancer back end to perform maintenance, test, or upgrade software. Then re-add that group and push changes across other regions.

![](../_resources/ee2d5f32b008bc763210ac4cb4827b38.png)

Quickly took my europe-west1- instance group out of service by dropping number of instances to 0.

**Minimum sizing

**I noticed the GCLB performed best with 3–4 minimum instances if using a single instance group as a backend. There is a slight lag for the LB to pickup the new instance information so its probably not the best idea to run a backend with 1 instance group with 2 instances at a very minimum. Multiple instance groups should be fine with 1–2 instances, just be aware and test the slight lag with the GCLB to pickup new instances added to groups. Tweak the initial delay threshold if you need to run a small amount of instances.

**IPv6 Support

**You an attach a IPv6 Ip to a GCLB and have the same type of routing globally as you would with IPv4. One strategy would be to configure the GCLB with an IPv6 address to handle all IPv6 traffic. Just create an additional forwarding rule with the IPv6 address. Then you can associate both IPv6 and IPv4 with the same load balancer and back end instances. More on IPv6 support [here](https://cloud.google.com/compute/docs/load-balancing/ipv6).

### Observations

The GCLB is a managed service and intended to make intelligent decisions on routing and traffic shaping for you. Below are a few specific service behaviors observed for basic http load balancing.

I used Apache Bench for connection testing from a US and EU instance. Apache Bench (ab) is included in the apache2 package. More info on Apache Bench testing [here](https://www.petefreitag.com/item/689.cfm).

**Location based routing and traffic load distribution

**First test was sending 10,000 requests with 100 concurrent from an ab-tester US instance and the GCLB routed directly to my us-east1 instance group. So the GCLB routing works great ✔️.

![](:/ce55c7478704ee2415e8e253753a153c)
US east Apache Bench tester instance traffic going to US instance Group

Increasing the requests from 10,000 to 100,000 from an ab-tester in EU this time, initially routed to the europe-west1 instance group (blue), then distributed across all 3 instance groups to better handle the load. At the same time my instance group in EU scaled up to 7 instances to accept the bulk of the traffic. Intelligent load balancing with minimal configuration and seamless autoscaling works great ✔️.

![](:/2e765f1f6a89d3c815efdce8338d8491)
EU Apache bench tester instance going to EU instance group

![](../_resources/e29ab994f1269ed3526c1b2efd0e98d7.png)

100,000 requests from an EU instance initially flows to my Europe instance group (blue) and as requests spike is spread across all 3 available instance groups.

About 30 minutes after the 100,000 query spike had long passed and the instance group started to stabilize and scale down gracefully.

![](../_resources/989a03c8c362dafa50d01e3528228410.png)
At the peak of the traffic the EU instance group was 7 instances

![](:/f971d4ccd7a65d69e99d806e33bc3f46)
After the event the EU instance group scaled down
Scale resources up and down with intelligent autoscaling ✔️.

I was going to stress test the GCLB up to 1 million rps just to see it perform with my own eyes. After doing more testing in excess of 500,000 rps instances I found the same behavior was demonstrated: flawlessly routing and balancing of traffic across regions. I had quickly gained trust in the service and saved myself the testing costs. Saved money by trusting the platform. ✔️