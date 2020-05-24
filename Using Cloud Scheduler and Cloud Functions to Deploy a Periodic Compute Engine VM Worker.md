Using Cloud Scheduler and Cloud Functions to Deploy a Periodic Compute Engine VM Worker.

# Using Cloud Scheduler and Cloud Functions to Deploy a Periodic Compute Engine VM Worker.

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='57' height='57' viewBox='0 0 57 57' data-evernote-id='191' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' clip-rule='evenodd' d='M28.5 1.2A27.45 27.45 0 0 0 4.06 15.82L3 15.27A28.65 28.65 0 0 1 28.5 0C39.64 0 49.29 6.2 54 15.27l-1.06.55A27.45 27.45 0 0 0 28.5 1.2zM4.06 41.18A27.45 27.45 0 0 0 28.5 55.8a27.45 27.45 0 0 0 24.44-14.62l1.06.55A28.65 28.65 0 0 1 28.5 57 28.65 28.65 0 0 1 3 41.73l1.06-.55z' data-evernote-id='192' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) ![1*Q9m-tpUok8AOP7vOa6HgaA.jpeg](../_resources/f9a5656892e6d9c836c801169df835a1.jpg)](https://medium.com/@martinomburajr?source=post_page-----2b897ef68dc5----------------------)

[Martin Ombura Jr.](https://medium.com/@martinomburajr?source=post_page-----2b897ef68dc5----------------------)

[Jun 6](https://medium.com/google-cloud/using-cloud-scheduler-and-cloud-functions-to-deploy-a-periodic-compute-engine-vm-worker-2b897ef68dc5?source=post_page-----2b897ef68dc5----------------------) · 5 min read

In this article we use cloud scheduler to periodically startup and tear down a compute engine (GCE) worker. Cloud Scheduler will periodically poll a cloud function that will instantiate a worker compute engine VM, that will do some work until the scheduler tells the cloud function to shut it down. For our example we shall have the cloud scheduler run every 10 minutes, polling that cloud function to perform its task.

# Architecture

**Cloud Scheduler: **Google Cloud Scheduler is a cron based solution for engineers looking for a way to set up some form of cron functionality with any GCP service.**  **We shall manually create a cron that hits a cloud functions HTTP endpoint that triggers the entire build process.

**Cloud Functions:** Majority of logic for creating the GCE instance will be held within Cloud Function. We shall use the Golang GCP API to perform these calls; but do not worry if you are unfamiliar with Go, I shall heavily comment [my code](https://github.com/martinomburajr/medium/blob/master/gcp/architecture/scheduler-functions-compute-startupscript/cloudfunctions/cloudfunctions.go). Which I supply at the end of the article.

**Compute Engine Instance:** Cloud Functions will create a GCE instance that will perform some work. In our simple example, we shall attach startup and shutdown scripts to the VM, so that whenever the VM is started or stopped, it will write to a `**work.txt**` file in the root folder. This will let us know the VM actually started and did some work. In your case it could be running some analytics, or whatever batch job you want done. Our instance will be preemptible to save costs.

Let’s begin.

# 1. Create a Service Account

We need a service account (SA) that cloud functions uses to act on behalf of us *(the user)* to manage the creation, starting and stopping of the VM. Without it, Cloud Functions wont be authorized to do so. In my example I call the SA`**compute-admin-sa**`, I give it a description to better identify its role *(Figure 1)*.

![1*dJ_HVsS18tq3KTf41gD_iw.png](../_resources/7df86ff60927ef5471cbb4c62f139e3e.png)
**Figure 1:** Creating the Service Account

## 1.2 Apply Service Account Permission.

In this step we define permissions our service account will have. I give it Compute Admin role which grants it full control over Compute Engine. In your case you can be more granular with the scope. After this step, we create the cloud function.

![1*uGNyWiZfDVj3rzrPV3dcig.png](../_resources/f3a7ec62ba91b6ecd0e659cf2bd209b0.png)
**Figure 2:** Applying Roles to Service Account

# 2. Creating the Cloud Function

Navigate to the Cloud Functions Page. Click Create function.
![1*ziXbTeOr0oUesuJ1GU2o8g.png](../_resources/54647162afc35a59288fd8bec8680991.png)
**Figure 3:** Creating Cloud Function (Name, Description and Trigger)

Create a function and let’s give it a descriptive name. `**worker-instance-cloud-function**`. Let’s ensure the Trigger is HTTP as we will call this HTTP URL using Cloud Scheduler.

Next copy the URL provided. This will be how Cloud Scheduler calls this function.

Next we select the Runtime. I amusing Go for my functions logic, so Go 1.11 is appropriate.

![1*9tUxr2SA0PKQC6h5ddg6GA.png](../_resources/1795eacf29439d38f59405a633a77a2c.png)
**Figure 4:** Creating Cloud Function (Regions and Environment Variables)

Next we select the function to execute. In my case its called `**DeployInstance**`**  ***(See Code at Bottom of Page)*

Let’s select a region, typically we should select a region that’s close to our Cloud Scheduler and Compute Engine Instance, in our case us-central1 works.

Let’s then select the Service Account. We use the one we created earlier.

In the Environment Variables section, my code uses 4 core variables. `**PROJECT_ID**`, `**REGION**`, `**ZONE**`, `**INSTANCE_NAME**`**  **fill those in with the variables you want. Make sure they are correct.

Finally **click Create**

Once deployed, you should have a similar looking UI as shown in *Figure 5 below*

![1*xB0YKHz1qO9ndHm_nYzcUQ.png](../_resources/67ffd3dae73c5cd250c6218d2929e9a4.png)
**Figure 5:** Cloud Scheduler after you created the schedule

# Creating the Cloud Scheduler

It’s time to create our scheduler *(Figure 6)*.
![1*LplfhHM_eL6a6uwzNCzlrw.png](../_resources/d61fe83e7f1140ef8406cbacf30f9e5a.png)
**Figure 6:** Creating the Cloud Schedule

Let’s provide a unique descriptive name as well as a cogent description. In my case I name it `**worker-instance-batchwork-scheduler**`** .**

Next let’s set the scheduler to every 10 minutes. Cloud Scheduler uses the familiar Linux Cron syntax. In our case it is `***/10 * * * ***`

Next set the timezone to one similar to your Cloud Function region for uniformity.

Next set the Target as HTTP and paste in the Cloud Function URL we got from creating our Cloud Function. Then select `**GET**` as the HTTP method, as we just want to call the function, passing in no data.

# Running the Schedule

We can run the schedule to see if it works, On the Cloud Scheduler Page, click run now *(Figure 7)*, if it hasn’t run already *(Or you can wait 10 minutes)*