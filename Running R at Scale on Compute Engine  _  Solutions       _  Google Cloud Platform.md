Running R at Scale on Compute Engine  |  Solutions       |  Google Cloud Platform

star_border
star_border
star_border
star_border
star_border

- [Solutions](https://cloud.google.com/solutions/)

#  Running R at Scale on Compute Engine

- [Contents](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)
- [Objectives](https://cloud.google.com/solutions/running-r-at-scale#objectives)
- [Costs](https://cloud.google.com/solutions/running-r-at-scale#costs)
- [Before you begin](https://cloud.google.com/solutions/running-r-at-scale#before-you-begin)
- [Installing ElastiCluster](https://cloud.google.com/solutions/running-r-at-scale#installing_elasticluster)
- [Configuring ElastiCluster](https://cloud.google.com/solutions/running-r-at-scale#configuring_elasticluster)
    - [Get project credentials](https://cloud.google.com/solutions/running-r-at-scale#get_project_credentials)
    - [Make sure you have SSH keys](https://cloud.google.com/solutions/running-r-at-scale#make_sure_you_have_ssh_keys)
    - [Create the configuration file](https://cloud.google.com/solutions/running-r-at-scale#create_the_configuration_file)
- [Adding R libraries to the deployment](https://cloud.google.com/solutions/running-r-at-scale#adding_r_libraries_to_the_deployment)
- [Creating the cluster](https://cloud.google.com/solutions/running-r-at-scale#creating_the_cluster)
- [Launching R](https://cloud.google.com/solutions/running-r-at-scale#launching_r)
- [Running k-means clustering](https://cloud.google.com/solutions/running-r-at-scale#running_k-means_clustering)
    - [Run the serial version on a single node](https://cloud.google.com/solutions/running-r-at-scale#run_the_serial_version_on_a_single_node)
    - [Run the parallel version on multiple nodes](https://cloud.google.com/solutions/running-r-at-scale#run_the_parallel_version_on_multiple_nodes)
- [Cleaning up](https://cloud.google.com/solutions/running-r-at-scale#clean-up)
- [What's next](https://cloud.google.com/solutions/running-r-at-scale#whats-next)

-

This tutorial shows how to run R scripts for modeling and analytics that span multiple physical nodes in a cluster running on Google Cloud Platform (GCP). The tutorial assumes that you are familiar with GCP, basic shell programming, and R.

Many models require extensive memory or computation that can exceed what is available in a single node.Therefore,[computational clusters](https://cloud.google.com/solutions/using-clusters-for-large-scale-technical-computing)are used to aggregate memory and computation across tens or hundreds of nodes and thousands of computation cores.

A number of packages are available for R that make it easy to program a cluster of nodes for your modeling and analytics:

- [Snow](https://cran.r-project.org/package=snow) provides clustering capabilities using standard sockets or using the high-performance Message Passing Interface (MPI).
- [Rslurm](https://cran.r-project.org/package=rslurm) provides functions to allow you to submit R scripts to a [Slurm](https://slurm.schedmd.com/) cluster workload manager.
- [Rmpi](https://cran.r-project.org/package=Rmpi) provides a low-level interface to the MPI parallel API.

This tutorial uses Rmpi, because it is mature and supports a number of libraries. Using Rmpi, you can use high-performance computing (HPC) clusters and[workload managers](https://cloud.google.com/solutions/using-clusters-for-large-scale-technical-computing#job_schedulers)to submit a job. The job consists of an R script that uses the Rmpi interface to create processes across the nodes in the cluster, and to send and receive messages across those nodes.

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Objectives

- Install a 6-node compute cluster using the cluster-provisioning [ElastiCluster](https://github.com/gc3-uzh-ch/elasticluster) tool and the [Slurm workload manager](https://slurm.schedmd.com/).
- Customize ElastiCluster to install additional software packages.
- Submit a job to the workload manager to run an R script that leverages the computation capabilities across the cluster.

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Costs

This tutorial uses the following billable components of GCP:

- Compute Engine

Use the[Pricing Calculator](https://cloud.google.com/products/calculator/#id=411d8ca1-210f-4f2c-babd-34c6af2b5538)to generate a cost estimate based on your projected usage. New GCP users might be eligible for a[free trial](https://cloud.google.com/free-trial). Using the defaults in this tutorial, a 6-node cluster composed of`n1-standard-4` instances, would cost $1.84/hr. This tutorial should take less than 1 hour of time.

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Before you begin

This tutorial requires macOS or Linux.

star**Note:** For this tutorial, we don't recommend using Cloud Shell.

1.  Select or create a Cloud Platform project. [Go to the Manage resources page](https://console.cloud.google.com/cloud-resource-manager)

2.  Enable billing for your project. [Enable billing](https://support.google.com/cloud/answer/6293499#enable-billing)

3.  Enable the Compute Engine API. [Enable the API](https://console.cloud.google.com/flows/enableapi?apiid=compute)

4. Install the [Google Cloud SDK](https://cloud.google.com/sdk/docs/) on a laptop or desktop computer (your host computer). The host must be running macOS or Linux.

5. Install Python, if it isn't already installed on the host. You can get installers from the [Python download page](https://www.python.org/downloads/).

6. Install [virtualenv](https://pypi.python.org/pypi/virtualenv). This step is optional but highly recommended.

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Installing ElastiCluster

To provision and configure the computational cluster in GCP, you use an open source tool called[ElastiCluster](https://gc3-uzh-ch.github.io/elasticluster/). This tool configures 1 master node with multiple compute nodes. The master node runs a network file system (NFS) file server that's shared across the compute nodes. The master node also runs the Slurm scheduler to manage and schedule jobs on the compute nodes.

ElastiCluster uses[Ansible](https://www.ansible.com/)to automate the configuration of virtual machines.

On your host computer, do the following:
1. If you use `virtualenv`, create a virtual Python environment:

hdr_strong
content_copy
virtualenv elasticluster
. ./elasticluster/bin/activate

2. Install `elasticluster` from source in the GitHub repository:

hdr_strong
content_copy
cd elasticluster
git clone git://github.com/gc3-uzh-ch/elasticluster.git src
cd src
pip install -e .

You are installing ElastiCluster from GitHub because you will make modifications to the Ansible playbooks in later sections.

3. Verify that you have installed the executable `elasticluster` tool:

hdr_strong
content_copy
elasticluster --version

If ElastiCluster is installed, the output will be similar to the following:

hdr_strong
elasticluster version 1.3.dev0

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Configuring ElastiCluster

ElastiCluster uses a configuration file to define clusters and cloud providers. As part of the configuration, you need credentials (a client ID and client secret) for API access. You also need an SSH key to be able to sign in to the cluster.

### Get project credentials

1. In the GCP Console, go to the API Credentials page:

[Go to the API Credentials page](https://console.cloud.google.com/apis/credentials)

2. Select your GCP project.
3. In the **Credentials** tab, click **Create credentials**.
4. Click **OAuth client ID**.
5. If you see a message about setting a product name on the consent screen:
    1. Click **Configure consent screen**.

    2. In the **Product name shown to users** box, enter **elasticluster** and then click **Save**.

6. In the **Create client ID** page, for **Application type**, select **Other**.

7. In the **Name** box, enter `Elasticluster`.
8. Click **Create**.

9. Make a copy your client ID and client secret. You will need these values for the configuration file that you create next.

star**Note:** You can see the client ID and client secret at any time by returning to the **Credentials** page and clicking on the name you specified (`Elasticluster`).

### Make sure you have SSH keys

You need SSH keys so that you can sign in to your cluster. By default, when you first use the `gcloud` command, GCP puts SSH keys in the following folder:

`~/.ssh/google_compute_engine{.pub}`

If you haven't used the `gcloud` tool before, or if the keys aren't in that location, run the following command to download the keys:

hdr_strong
content_copy
gcloud compute config-ssh

### Create the configuration file

You can now create the ElastiCluster configuration file that defines the cluster characteristics that will be provisioned in the GCP project.

star**Note:** A complete sample configuration file is shown in the[Sample configuration file](https://cloud.google.com/solutions/running-r-at-scale#sample_configuration_file)section that follows this procedure.

1. Create a file named `config` in `$(HOME)/.elasticluster`.

2. Add the following lines to configure the provisioning tool to use the GCP provider:

hdr_strong
content_copy
[cloud/google]
provider=google

3. Set the GCP credentials and project ID:
hdr_strong
content_copy
gce_client_id=[YOUR_CLIENT_ID]
gce_client_secret=[YOUR_CLIENT_SECRET]
gce_project_id=[YOUR_PROJECT_ID]

For `[YOUR_CLIENT_ID]` and [`YOUR_CLIENT_SECRET]`, use the values that you got when you created credentials earlier.

For `[YOUR_PROJECT_ID]`, use the ID of the GCP project that you created or selected during setup.

4. Set the default GCP zone. In this example, the [zone](https://cloud.google.com/compute/docs/regions-zones/regions-zones) is set to `us-west1-b`, but you can choose a different zone.

hdr_strong
content_copy
noauth_local_webserver=True
zone=us-west1-b

5. Set the GCP host login values that you use with the `ssh` command to connect to the nodes that you create.

hdr_strong
content_copy
[login/google]
image_user=[YOUR_USERNAME]
image_user_sudo=root
image_sudo=True
user_key_name=elasticluster
user_key_private=~/.ssh/google_compute_engine
user_key_public=~/.ssh/google_compute_engine.pub

For `[YOUR_USERNAME]`, use your GCP username. For example, if you sign in to your GCP account as `johnd@example.com`, your username is `johnd`.

6. Configure Ansible to increase the `ssh` command timeouts and the number of forked processes:

hdr_strong
content_copy
[setup/ansible]
ansible_forks=20
ansible_timeout=200

7. Set up Slurm by defining 2 groups of hosts—the frontend with the role of `slurm_master`, and the remaining ones with the role of `slurm_worker`:

hdr_strong
content_copy
[setup/ansible-slurm]
provider=ansible
frontend_groups=slurm_master,r
compute_groups=slurm_worker,r

These roles are defined in the Ansible playbooks provided by ElastiCluster. This configuration gives all nodes the role `r`, so that the R libraries and runtime will be installed.

8. Define the Slurm cluster:
hdr_strong
content_copy
[cluster/myslurmcluster]
cloud=google
login=google
setup=ansible-slurm
security_group=default

    - The cluster name is `myslurmcluster`. You can use a different name, but if you do, make a note of it because you use this name in later commands.
    - The cluster configuration uses the cloud definition specified in the `cloud/google` section of the file.
    - The host `ssh` keys are specified in the `login/google` section.
    - The cluster setup is specified in the `setup/ansible-slurm` section.

9. Set the image, machine type, node count, and boot disk size for the cluster:
hdr_strong
content_copy
image_id=debian-8-jessie-v20170829
flavor=n1-standard-4
frontend_nodes=1
compute_nodes=5
ssh_to=frontend
boot_disk_size=50

    - In this example, the base image specified by `image_id` is a Debian-based image. Use the most current version of the image, which might not be the version shown in the example.
    - The value of `flavor` specifies a machine of type `n1-standard-4`, as described in the list of [standard machine types](https://cloud.google.com/compute/docs/machine-types#standard_machine_types).
    - The cluster is configured to have 1 frontend node and 5 compute nodes.
    - The `boot_disk_size` applies to each compute node and provisions a 50 GiB local boot disk.

10. Configure the head node to have a 1 TB root volume using a solid-state drive (SSD) [persistent disk](https://cloud.google.com/compute/docs/disks/#pdspecs):

hdr_strong
content_copy
[cluster/myslurmcluster/frontend]
boot_disk_type=pd-ssd
boot_disk_size=1000

Because the NFS server shares the home directories across all the nodes, it's a good idea to use SSD for added performance. However, the `boot_disk_size` value in this section applies only to the frontend node.

11. Save the file.

#### Sample configuration file

The following listing shows a complete configuration file, with placeholders for values that you must supply.

hdr_strong
content_copy
[cloud/google]
provider=google

# Set the credentials and GCP project ID.

# NOTE! Substitute your own client ID, client secret, and project ID

# for the placeholders.

gce_client_id=[YOUR_CLIENT_ID]
gce_client_secret=[YOUR_CLIENT_SECRET]
gce_project_id=[YOUR_PROJECT_ID]

# Set the GCP zone. You can use any zone.

noauth_local_webserver=True
zone=us-west1-b

# Set credentials for using SSH to log in to the cluster.

# NOTE! Substitute your own GCP user name.

# NOTE! Make sure that the gcloud user keys are in the specified

# location on your host computer.

[login/google]
image_user=[YOUR_USERNAME]
image_user_sudo=root
image_sudo=True
user_key_name=elasticluster
user_key_private=~/.ssh/google_compute_engine
user_key_public=~/.ssh/google_compute_engine.pub

# Configure Ansible SSH timeouts and the number of forked processes.

[setup/ansible]
ansible_forks=20
ansible_timeout=200

# Configure Slurm with 2 groups of hosts: 1 frontend (slurm_master) and

# the rest with the role "slurm_worker".

[setup/ansible-slurm]
provider=ansible
frontend_groups=slurm_master,r
compute_groups=slurm_worker,r

# Define the cluster.

[cluster/myslurmcluster]
cloud=google
login=google
setup=ansible-slurm
security_group=default

# Specify the image, machine type, node count, and boot disk size for

# the cluster nodes.

image_id=debian-8-jessie-v20170829
flavor=n1-standard-4
frontend_nodes=1
compute_nodes=5
ssh_to=frontend
boot_disk_size=50

# Configure the head node to have a 1 TB root volume using a

# solid-state drive (SSD).

[cluster/myslurmcluster/frontend]
boot_disk_type=pd-ssd
boot_disk_size=1000

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Adding R libraries to the deployment

The next step is to configure the `elasticluster` R playbook to install additional libraries at the time of deployment.

1. Open the `elasticluster/share/playbooks/roles/r/defaults/main.yml` file.

2. Find the `r_libraries` section and add the following line to specify the `doSNOW` package:

hdr_strong
content_copy
r_libraries:

- devtools # allow installing packages directly from GitHub
- doSNOW

3. Save the file.
You are now ready to create the cluster.

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Creating the cluster

1. From the command line on your host computer, create the cluster:
hdr_strong
content_copy
elasticluster start myslurmcluster

If you used a different name for your cluster than `myslurmcluster`, use that name instead.

The `start` command provisions the nodes using Compute Engine. It configures the nodes by using the Ansible playbooks included in the ElastiCluster source. Setup can take some time, depending on configuration. When it completes, the following output appears:

hdr_strong
Your cluster is ready!

Cluster name: myslurmcluster
Cluster template: myslurmcluster
Default ssh to node: frontend001

- compute nodes: 5
- frontend nodes: 1

To sign in to the frontend node, run the following command:
elasticluster ssh myslurmcluster
To upload or download files to the cluster, use the command:
elasticluster sftp myslurmcluster

2. Use `ssh` to connect to the head node:

hdr_strong
content_copy
elasticluster ssh myslurmcluster

If you haven't used the `gcloud` command-line tool before, your credentials will likely not have been downloaded to your host, and the`ssh` command fails. For more information, see[Make sure you have SSH keys](https://cloud.google.com/solutions/running-r-at-scale#make_sure_you_have_ssh_keys)earlier in this tutorial.

You can also directly log into the Compute Engine nodes using the `gcloud` tool:

hdr_strong
content_copy
gcloud compute ssh myslurmcluster-frontend001

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Launching R

1. On the frontend node of the cluster, verify that Slurm is properly configured and available:

hdr_strong
content_copy
sinfo

The command returns the number of cores available, such as the following:

hdr_strong
PARTITION AVAIL TIMELIMIT NODES STATE NODELIST
main* up infinite 5 idle compute[001-005]

2. Request a subset of the available cores:
hdr_strong
content_copy
salloc --tasks 20 --ntasks-per-node=4 --nodes 5

This command requests 20 cores: 5 nodes with 4 cores each.

In this tutorial, no other users are submitting jobs into the cluster, so the command returns immediately.

The command returns with the shell prompt when the allocation is granted.
3. At the shell prompt, verify that all the software is configured and working:
hdr_strong
content_copy
R

If R is installed and configured correctly, output similar to the following appears:

hdr_strong
R version 3.3.3 (2017-03-06) -- "Another Canoe"
Copyright (C) 2017 The R Foundation for Statistical Computing
Platform: x86_64-pc-linux-gnu (64-bit)

4. Test the cluster and libraries to ensure that R and MPI are working correctly. At the R shell prompt, enter the following lines:

hdr_strong
content_copy
library('Rmpi')
mpi.spawn.Rslaves(nslaves=20)
mpi.remote.exec(mpi.comm.rank())>

The first 2 lines load and initialize `mpi` with 20 worker processes running within the current allocation of cores. The third line executes a command on each of the remote worker processes that returns its unique MPI process ID.

The command returns each processor's rank, from 1 to 20:

hdr_strong
X1 X2 X3 X4 X5 X6 X7 X8 X9 X10 X11 X12 X13 X14 X15 X16 X17 X18 X19 X20
1 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Running k-means clustering

In the previous section, you verified that the cluster and applications are working correctly. In this section, you run a k-means clustering algorithm on test data across the nodes of the Slurm cluster. To demonstrate the advantage of the parallelism that R offers, you run the same computation in 2 ways: a serial version, and a parallel version.

### Run the serial version on a single node

The sample code you use in this section comes from[k-means Parallel R Examples](https://github.com/glennklockwood/paraR/tree/master/kmeans)and[Parallelizing R with BatchJobs](http://www.teraproc.com/teraproc-blog/parallel-r-a-tutorial/).

1. Create a file named `generateData.R` and copy the following R script into it:

hdr_strong
content_copy
nrow <- 50000
sd <- 0.5
real.centers <- list( x=c(-1.3, -0.7, 0.0, +0.7, +1.2),
y=c(-1.0, +1.0, 0.1, -1.3, +1.2) )
data <- matrix(nrow=0, ncol=2)
colnames(data) <- c("x", "y")
for (i in seq(1, 5)) {
x0 <- rnorm(nrow, mean=real.centers$x[[i]], sd=sd)
y0 <- rnorm(nrow, mean=real.centers$y[[i]], sd=sd)
data <- rbind( data, cbind(x0,y0) )
}
write.csv(data, file='dataset.csv', row.names=FALSE)

The script generates 250,000 noisy points in 2 dimensions, using a normal distribution centered around 5 points: (-1.3,-1), (-0.7,1.0), (0.0,0.1), (0.7,-1.3) and (1.2,1.2).

It writes the results into a file named `dataset.csv`.
2. Run the script using the `Rscript` command:

hdr_strong
content_copy
Rscript generateData.R

3. Create a file named `serialKMeans.R` and copy the following script into it:

hdr_strong
content_copy
data <- read.csv('dataset.csv')
ptm<-proc.time()
result <- kmeans(data, centers=5, nstart=1000)
print (result[2])
print(proc.time() - ptm)

This script reconstructs the cluster midpoints by using a k-means algorithm. The k-means algorithm is susceptible to local minimums. Typically you run this algorithm multiple times, and the cluster midpoints that minimize the total error are returned. In this script, the `nstart` variable sets the`kmeans` method to run 1000 repetitions.

4. Run the script you just created:
hdr_strong
content_copy
Rscript serialKMeans.R

Running this script produces output similar to the following:

hdr_strong
$centers
x y
1 -0.74901987 1.05422621
2 0.04395349 0.05488741
3 0.72607851 -1.33580565
4 -1.31769895 -1.00554838
5 1.21740207 1.22001612

user system elapsed
203.108 0.036 203.174

These results indicate that the algorithm successfully reconstructed the cluster centers from the noisy data in roughly 3.5 minutes (203 seconds). (Your results might differ slightly from these.)

### Run the parallel version on multiple nodes

The parallel version of the R application is similar to the serial version, but it runs the k-means algorithm on each of the cores across the cluster. The serial and parallel versions run the same total number of repetitions. The serial version of the algorithm ran the algorithm 1000 times on 1 core. The parallel version runs the algorithm 50 times on each of 20 cores.

1. Create a file named `parallelKMeans.R` and copy the following script into it:

hdr_strong
content_copy
library(foreach)
library(doSNOW)
library(Rmpi)

args = commandArgs(trailingOnly=TRUE)
data <- read.csv(args[1])
cl <- makeCluster( args[2], type="MPI" )
sprintf("start with %s workers", args[2])
numworkers = as.integer(args[2])
nst = 1000/numworkers
ptm<-proc.time()
clusterExport(cl, c('data') )
registerDoSNOW(cl)
results <- foreach( i = 1:numworkers ) %dopar% {
kmeans( x=data, centers=5, nstart=nst )
}
temp.vector <- sapply( results,
function(result) {
result$tot.withinss
} )
result <- results[[which.min(temp.vector)]]
print(proc.time() - ptm)
print(result[2])
stopCluster(cl)
mpi.exit()

Each worker returns the best cluster midpoints and the master then returns the minimum of the returned values.

2. Run the script, specifying the `dataset.csv` file that was generated earlier as the input file, and specifying the number of cores as 20:

hdr_strong
content_copy
Rscript parallelKMeans.R dataset.csv 20

The following output appears:

hdr_strong
Loading required package: iterators
Loading required package: snow
20 slaves are spawned successfully. 0 failed.
[1] "start with 20 workers"
user system elapsed
12.396 11.688 27.092

$centers
x y
1 0.72607851 -1.33580565
2 0.04395349 0.05488741
3 -0.74901987 1.05422621
4 -1.31769895 -1.00554838
5 1.21740207 1.22001612

The output shows the midpoints of the clusters that were reconstructed using the k-means algorithm and should be similar to the midpoints calculated in the serial, single-node version. The elapsed time shows the total wall-clock time for the parallel calculation. With 20-way parallelism, it took only 27 seconds as compared with 203 seconds for the serial, single-node version.

You can run the parallel version with different degrees of parallelism, up to the total number of cores you have available in the cluster. As you increase the number of cores, run times on the cluster show increasing performance, as shown in the following table.

| Number of cores | Seconds |
| --- | --- |
| 1   | 203 |
| 5   | 68  |
| 10  | 41  |
| 20  | 27  |

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)Cleaning up

To avoid incurring charges to your GCP account for the resources used in this tutorial, log out of the cluster head node and execute the following command to delete the cluster resources:

hdr_strong
content_copy
elasticluster stop myslurmcluster
This command frees the nodes and deletes the data on the nodes.

## [arrow_upward](https://cloud.google.com/solutions/running-r-at-scale#top_of_page)What's next

- Review the [recommendations for cluster computing](https://cloud.google.com/solutions/using-clusters-for-large-scale-technical-computing) on GCP.
- Learn more about [using ElastiCluster](http://elasticluster.readthedocs.io/en/latest/install.html).
- Learn more [RHIPE](https://github.com/saptarshiguha/RHIPE/), which provides an R interface to Hadoop, and about other [packages that support parallelism in R](https://cran.r-project.org/web/views/HighPerformanceComputing.html).
- Try out other Google Cloud Platform features for yourself. Have a look at our[tutorials](https://cloud.google.com/docs/tutorials).

Was this page helpful? Let us know how we did:
star_border
star_border
star_border
star_border
star_border

Except as otherwise noted, the content of this page is licensed under the [Creative Commons Attribution 3.0 License](http://creativecommons.org/licenses/by/3.0/), and code samples are licensed under the [Apache 2.0 License](http://www.apache.org/licenses/LICENSE-2.0). For details, see our [Site Policies](https://developers.google.com/terms/site-policies). Java is a registered trademark of Oracle and/or its affiliates.

Last updated November 30, 2017.