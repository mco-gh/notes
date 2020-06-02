> Airflow is a platform created by the community to programmatically author, schedule, and monitor workflows. In this blog we will underestand the basics of airflow

# An Introduction to Apache Airflow
What is Airflow?
----------------

> Airflow is a platform created by the community to programmatically author, schedule, and monitor workflows.

Machine learning is the hot topic of the industry. It won't be so cool if not for the data processing involved

Airflow is an ETL(Extract, Transform, Load) workflow orchestration tool, used in data transformation pipelines.

Uses of Airflow
---------------

Imagine you have an ML model that does twitter sentiment analysis. Now you want to run that model for your favorite people on twitter for their tweets every day. Such a workflow would look something like this.

![](https://i.imgur.com/qgSw3xW.png)

As you can see, the data flows from one end of the pipeline to the other end. There can be branches, but no cycles.

What problems does Airflow solve?
---------------------------------

Crons are an age-old way of scheduling tasks.

1.  With cron creating and maintaining a relationship between tasks is a nightmare, whereas, in Airflow, it is as simple as writing Python code.
2.  Cron needs external support to log, track, and manage tasks. Airflow UI to track and monitor the workflow execution
3.  Cron jobs are not reproducible unless externally configured. The Airflow keeps an audit trail of all tasks executed.
4.  Scalable

How to define a workflow in Airflow?
------------------------------------

Workflows are defined using Python files.

### DAG

Airflow provides `DAG` Python class to create a Directed Acyclic Graph, a representation of the workflow.

`from Airflow.models import DAG from airflow.utils.dates import days_ago args = { 'start_date': days_ago(0), } dag = DAG( dag_id='example_bash_operator', default_args=args, schedule_interval='* * * * *', )`

`start_date` enables you to run a task on a particular date.

`Schedule_interval` is the interval in which each workflow is supposed to run. `'* * * * *'` means the tasks need to run every minute. Don't scratch your brain over this syntax. You can play around with these using [https://crontab.guru/](https://crontab.guru/).

### Operator

`Operators` define the nodes of the DAG. Each operator is an independent task.

In the following example, we use two Operators

`from airflow.operators.bash_operator import BashOperator from airflow.operators.python_operator import PythonOperator`

1.  `PythonOperator` which calls a python function

`def print_function(): print ("Hey I am a task") run_this_last = PythonOperator( task_id='run_this_last', dag=dag, python_callable=print_function )`

2.  `BashOperator` which runs a bash command

`run_this = BashOperator( task_id='run_after_loop', bash_command='echo 1', dag=dag, )`

3.  The tasks are linked together using `>>` python operator.

`run_this >> run_this_last`

A sample DAG with branches would look something like this.

![](https://i.imgur.com/VyqpE8n.png)

Airflow Architecture
--------------------

![](https://i.imgur.com/UT38Lok.png)

Airflow has 4 major components.

### Webserver

The webserver is the component that is responsible for handling all the UI and REST APIs.

### Scheduler

Scheduler goes through the DAGs every `n` seconds and schedules the task to be executed.

The scheduler also has an internal component called **Executor**. The executor is responsible for spinning up workers and executing the task to completion.

### Worker

Workers run the task that is being handed over by the executor.

Types of Executor
-----------------

### SequentialExecutor

SequentialExecutor runs only one task at a time. The workers run the same machine as the scheduler is.

#### Pros

1.  Simple and easy to setup
2.  Good for testing DAGs during development

#### Cons

1.  Not scalable
2.  It cannot run multiple tasks at the same time.
3.  Not suitable for production

### LocalExecutor

LocalExecutor is the same as the Sequential Executor, except it can run multiple tasks at a time.

#### Pros

1.  Can run multiple tasks
2.  Good for running DAGs during development

#### Cons

1.  Not scalable
2.  Single point of failure
3.  Not suitable for production

### CeleryExecutor

Celery is used for running distributed asynchronous python tasks.

Hence, CeleryExecutor has been a part of Airflow for a long time, even before Kubernetes.

CeleryExecutors has a fixed number of workers running to pick-up the tasks as they get scheduled.

#### Pros

1.  It provides scalability.
2.  Celery manages the workers. In case of a failure, Celery spins up a new one.

#### Cons

1.  Celery needs RabbitMQ/Redis to for queuing the task, which is reinventing the wheel of what Airflow already supports.
2.  The above dependency also makes the setup complex.

### KubernetesExecutor

KubernetesExecutor runs each task in an individual Kubernetes pod. Unlike CeleryCelery, [it spins up worker pods on demand](https://bhavaniravi.com/blog/deploying-airflow-on-kubernetes/), hence enabling maximum usage of resources.

#### Pros

1.  It Combines the pros of scalability and simplicity of CeleryExecutor and LocalExecutor.
2.  Fine-grained control over resources allocated to tasks. One can define the amount of CPU/memory required at a task level.

#### Cons

1.  Kubernetes is new to Airflow, and the documentation is not straightforward.

* * *

Now that we have understood Airflow's basics let's learn how to write our workflow in the next post.

* * *

* * *

* * *

*   [← Are your Secrets Safe In Python?](chrome-extension://cjedbglnccaioiolemnfhjncicchinao/blog/secrets-as-python-file)

_I recently moved my blogs from medium. Find more of my writing [here.](https://medium.com/@bhavaniravi)_