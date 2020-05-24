How to Debug an Unresponsive app on GCP - Google Cloud - Community - Medium

# How to Debug an Unresponsive app on GCP

[![0*-zgiz-OyLh98si0V.](../_resources/bad3634492029e3fcb800fae870034a7.jpg)](https://medium.com/@alexamies?source=post_page-----a1c00499e2cb----------------------)

[Alex Amies](https://medium.com/@alexamies?source=post_page-----a1c00499e2cb----------------------)

[Mar 28](https://medium.com/google-cloud/how-to-debug-an-unresponsive-app-on-gcp-a1c00499e2cb?source=post_page-----a1c00499e2cb----------------------) · 8 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='star-15px_svg__svgIcon-use js-evernote-checked' width='15' height='15' viewBox='0 0 15 15' style='margin-top:-2px' data-evernote-id='196'%3e%3cpath d='M7.44 2.32c.03-.1.09-.1.12 0l1.2 3.53a.29.29 0 0 0 .26.2h3.88c.11 0 .13.04.04.1L9.8 8.33a.27.27 0 0 0-.1.29l1.2 3.53c.03.1-.01.13-.1.07l-3.14-2.18a.3.3 0 0 0-.32 0L4.2 12.22c-.1.06-.14.03-.1-.07l1.2-3.53a.27.27 0 0 0-.1-.3L2.06 6.16c-.1-.06-.07-.12.03-.12h3.89a.29.29 0 0 0 .26-.19l1.2-3.52z' data-evernote-id='197' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='202'%3e%3cpath d='M22.05 7.54a4.47 4.47 0 0 0-3.3-1.46 4.53 4.53 0 0 0-4.53 4.53c0 .35.04.7.08 1.05A12.9 12.9 0 0 1 5 6.89a5.1 5.1 0 0 0-.65 2.26c.03 1.6.83 2.99 2.02 3.79a4.3 4.3 0 0 1-2.02-.57v.08a4.55 4.55 0 0 0 3.63 4.44c-.4.08-.8.13-1.21.16l-.81-.08a4.54 4.54 0 0 0 4.2 3.15 9.56 9.56 0 0 1-5.66 1.94l-1.05-.08c2 1.27 4.38 2.02 6.94 2.02 8.3 0 12.86-6.9 12.84-12.85.02-.24 0-.43 0-.65a8.68 8.68 0 0 0 2.26-2.34c-.82.38-1.7.62-2.6.72a4.37 4.37 0 0 0 1.95-2.51c-.84.53-1.81.9-2.83 1.13z' data-evernote-id='203' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/a1c00499e2cb/share/twitter?source=post_actions_header---------------------------)

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='29' height='29' class='q js-evernote-checked' data-evernote-id='211'%3e%3cpath d='M23.2 5H5.8a.8.8 0 0 0-.8.8V23.2c0 .44.35.8.8.8h9.3v-7.13h-2.38V13.9h2.38v-2.38c0-2.45 1.55-3.66 3.74-3.66 1.05 0 1.95.08 2.2.11v2.57h-1.5c-1.2 0-1.48.57-1.48 1.4v1.96h2.97l-.6 2.97h-2.37l.05 7.12h5.1a.8.8 0 0 0 .79-.8V5.8a.8.8 0 0 0-.8-.79' data-evernote-id='212' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/p/a1c00499e2cb/share/facebook?source=post_actions_header---------------------------)

**TL;DR**: You can debug an unhealthy app using Google Cloud Logging and other GCP tools even if the app has become unresponsive. A test app is provided that simulates the problem in an experiment for the purpose of explaining the debugging process with App Engine Flex. Similar debugging tools and methods are broadly available on other Google Cloud compute environments.

**Background**

App Engine Flex and other serverless offerings on Google Cloud Platform are very convenient, leaving Google to manage the app for you. If a virtual machine crashes, App Engine will reboot or create a new instance for you so that your app is still available to users. However, it is also possible that your app may become unhealthy while the virtual machine is still healthy. Conditions that may lead to this include out of memory, deadlocks in the app, and I/O problems. Rebooting the app and / or the instance may be helpful for the availability of your app. However, there may be something systemic in your app that is causing the problem then you can get to the bottom of that using the methods described here.

**Test app**

The test app is a Python Flask application that serves a few requests successfully but then randomly goes into a simulated unhealthy state when it then takes 90 seconds on all subsequent requests, including health checks. The main handler is shown below. Full code is in this [gist](https://gist.github.com/alexamies/b24f99cbeaf2cd50b2642bc182a91aa8).

@app.route('/')def home(): """1 out of 10 requests change the app to an unhealthy state""" msg = 'Welcome to the home page!\n' if not get_app_healthy(): msg = 'Changing to an unhealthy state' logging.error(msg) time.sleep(90) # seconds return msg r = random.uniform(0.0, 1.0) if r > 0.9: msg = 'App is unhealthy' logging.error(msg) set_app_healthy(False) time.sleep(90) # seconds return msg

The handler for the [readiness health check](https://cloud.google.com/appengine/docs/flexible/custom-runtimes/configuring-your-app-with-app-yaml#readiness_checks) is shown below.

@app.route('/readiness_check')def readiness_check(): """Respond to the load balancer's readiness check""" msg = 'OK' if not get_app_healthy(): msg = 'App is unhealthy' logging.error(msg) time.sleep(90) # seconds return msg

**Deploying the app**

A deployment descriptor app.yaml is provided for App engine Flex. The timeout for the readiness health check in App Engine Flex is set to 4 seconds, which is performed every 5 seconds.

readiness_check: path: "/readiness_check" check_interval_sec: 5 timeout_sec: 4 failure_threshold: 2

Deploy the app to Flex with the commands below.
Set your project as the default in gcloud

GOOGLE_CLOUD_PROJECT=[Your project]gcloud config set project $GOOGLE_CLOUD_PROJECT

Enable App Engine
gcloud app create
Deploy the app
gcloud app deploy
Browse to the app
gcloud app browse

You should see a successful response in your browser, unless you got unlucky. In that case you can try again.

Set up Apache Bench In the Cloud Shell or Linux command line to use for sending HTTP requests. You can use the [Google Cloud Shell](https://console.cloud.google.com/home/dashboard?cloudshell=true) if you local development environment is not Debian.

sudo apt-get install apache2-utils
Send some requests to your app
ab -n 1000 -c 5 https://${GOOGLE_CLOUD_PROJECT}.appspot.com/

We expect that this will overload the app. Navigate to the [App Engine dashboard](https://console.cloud.google.com/appengine) to see how the app is performing. You should see high latency, as in the chart below although it may take a few minutes for the monitoring data to appear.

![0*61lUzFVPPowqen7w](../_resources/31152f8d9ef0394df04f029ebb2e9984.png)
![0*61lUzFVPPowqen7w](../_resources/ddb917f5654b98d1d5dbf6107e24bd02.png)
**App Engine Flex Latency**

Suppose we did not know that our app had an intentionally injected problem to simulate bad health? How would you debug the problem? After noticing a general problem in the monitoring dashboard you should check the logs. Navigate to the [Cloud Logs Viewer](https://console.cloud.google.com/logs/viewer?resource=gae_app) and select App Engine | stderr, as shown below

![0*VRnpzcVtF9G9u5GV](../_resources/e5508f42da7a0bffa57cf5fdc9b6b91b.png)
![0*VRnpzcVtF9G9u5GV](../_resources/b25ab37820125e260dedeca08ac4bb6f.png)
**Screenshot: App Engine Standard Error Logs**

Notice that the latency for the app suddenly jumped up from 1 millisecond to over 30 seconds and errors increased. If we browse through the logs you may find some errors from the runtime container, in this case Flask or Gunicorn, such as shown below:

![0*wMySci4wLtVqfVxB](../_resources/e7e770dec5f890cc5b87eff8040c5702.png)
![0*wMySci4wLtVqfVxB](../_resources/24a1b76cafa3a71812e55c029f2aca32.png)
**App Engine Flex Standard Error Log Detail**

Notice that the instance name is given as well. This allows you to identify the instance, in case you need to SSH to it, which you can do with the [gcloud app instances ssh](https://cloud.google.com/sdk/gcloud/reference/app/instances/ssh) command. Suppose that your app is so unhealthy that it does not emit any log messages. There are also log messages for the NGINX health checks that timed out that can be checked, as shown below.

![0*Iy-uMp3Iq8Yjp6K0](../_resources/2c29c47d4ba197581d2bbaf72adc53d0.png)
![0*Iy-uMp3Iq8Yjp6K0](../_resources/3adf8e3fcf7abee2b850f42aa9e0d7a1.png)
**App Engine Flex NGINX Health Check Logs**

Notice that the user agent is GoogleHC for health check and the 502 HTTP response code due to the health check client timing out (upper red box). These logs also give the instance name (lower red box). You can use the instance name from the logs to view details about the instance. Navigate to the [App Engine | Instances](https://console.cloud.google.com/appengine/instances) screen. Select the instance in question and look at the monitoring charts. The chart for CPU is shown below.

![0*5ZiYz0fR9gGAt15p](../_resources/d22f026a3496eae0b456886f63e7c0f7.png)
![0*5ZiYz0fR9gGAt15p](../_resources/027cc5cac28c1ab1318dcb3c28b817e0.png)
**App Engine Flex Instance CPU Utilization**

The CPU usage is kind of high but maybe not so high that it was the cause of the problem. You can also check the charts for memory and disk from the dropdown.

At this point we should suspect our app because there is nothing obviously wrong with the virtual machine instance. There are a number of tools that you can use for detecting problems in your app, such as [Cloud Trace](https://cloud.google.com/trace/docs), which can tell you where the time in your app is spent, [Stackdriver Profiler](https://cloud.google.com/profiler/docs) that can tell you where in your code the CPU resources are being spent and [Stackdriver Debugger](https://cloud.google.com/debugger/docs) to introspect the state of your app. These tools work on the basis of samples and are appropriate for production use. However, you need to set them up in advance of an incident.

To get to the bottom of a problem where the process running the app is totally unresponsive, you may need to SSH to the virtual machine and use other tools to inspect the state of threads or memory or do packet captures. Hopefully, this will be rare and you will be able to get the information that you need from the Cloud Console in most cases without having to resort to that.

# Health checks

The test app has a custom handler for [readiness checks](https://cloud.google.com/appengine/docs/flexible/custom-runtimes/configuring-your-app-with-app-yaml#readiness_checks). App Engine Flex readiness checks confirm that an instance can accept incoming requests. By contrast, a [liveness check](https://cloud.google.com/appengine/docs/flexible/custom-runtimes/configuring-your-app-with-app-yaml#liveness_checks) verifies that the virtual machine and Docker container are running. Other configurations on Google Cloud Platform have health checks that are similar but differ in some details. Kubernetes has a similar concept of [liveness and readiness checks](https://kubernetes.io/docs/tasks/configure-pod-container/configure-liveness-readiness-startup-probes/). Google Cloud Load Balancer also has its own flavor of [health checks](https://cloud.google.com/load-balancing/docs/health-checks).

# Other runtimes and languages

Runtimes have different characteristics in the way that they manage applications. For example, if we change the sleep statement in the home() handler to exit the process

sys.exit(1)
then Flask will restart the app. You can verify this by running the app locally

python3 -m venv envsource env/bin/activatepip3 install -r requirements.txtpython3 main.py

If you send ten or so requests with curl to the app in another terminal
curl http://localhost:8080

Then you can verify that Flask restarts the app. Not all runtimes handle process exits in the same way. In production, the App Engine Flex app.yaml file specifies the [gunicorn](https://gunicorn.org/) HTTP server, which manages a pool of worker processes. If one process exits it will not make your app unavailable because there are other processes already running to handle incoming requests.

Runtimes for Java and Go differ from Python typically exiting the process without restart. In that case the Docker container will also exit, which will be detected by a liveness check resulting in a restart of the VM instance. We can do a similar experiment by making a modification to the [App Engine Flex Go](https://cloud.google.com/appengine/docs/flexible/go/quickstart) quickstart to exit the process when we get an unlucky number as shown below

func handle(w http.ResponseWriter, r *http.Request) { num := rand.Intn(10) if num == 9 { os.Exit(1) } if r.URL.Path != "/" { http.NotFound(w, r) return } fmt.Fprint(w, "Hello world!")}

Then when deployed to App Engine Flex production you can see from the logs that the VM instance is shutdown and restarted.

# App startup

Fast app startup is critical to rapid recovery in the case of an outage. If you have a problem that brings down your fleet, then getting a fix rolled out fast will help reduce your recovery time. In addition, slow starting apps that handle a large amount of traffic are susceptible to thundering herd problems. That is because incoming traffic can overwhelm instances before they are ready to process traffic. You can add a custom readiness check, as described above, to address this problem. However, it may still take time to ramp up a sufficient number of instances to handle incoming traffic. The duration that takes will affect your incident recovery time.

App Engine Flex takes considerably longer to roll out an app change than App Engine Standard. Flex also typically takes longer to roll out an app change than Google Kubernetes Engine (GKE). In the case of GKE an app change will often only involve loading a new container image, typically single digit seconds.

# Log management

If you have a high traffic app you may use a [log exclusion filter](https://cloud.google.com/logging/docs/exclusions) to avoid excessive logs, such as from successfully passing health checks. This should not prevent you from capturing the logs that you need for debugging with a minor adjustment to the filter:

resource.type="gae_app"logName="projects/[your project]/logs/[appengine.googleapis.com](http://appengine.googleapis.com/)%2Fnginx.health_check"httpRequest.status>200

The last line limits the log exclusion filter to unsuccessful requests.

# Error handling

From the experiments above, it is clear that a process exit is handled better than a problem where the app is running but unresponsive. To avoid this is it important for the app to not catch general runtime errors that are not actionable within the context of your app code. Examples of these are RuntimeException in java, which is extended by OutOfMemoryError and other system level errors. The app should only catch application specific exceptions that are expected and that it can reasonably address or do not matter to the health of the app.