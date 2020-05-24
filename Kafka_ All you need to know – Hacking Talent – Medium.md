Kafka: All you need to know – Hacking Talent – Medium

# Kafka: All you need to know

## **Apache Kafka’s** popularity is exploding. Learn about what it is, and why it’s becoming a solution of big data and microservices applications

[![1*M-zBw0ieRdzZIQ08MMYbOA.jpeg](../_resources/11e136035586ec66044fd1c47a650f7e.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='107' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@mariavalerocam?source=post_header_lockup)

[Maria Valcam](https://medium.com/@mariavalerocam)

May 23·7 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='108'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

![](../_resources/e19ca4e922a275f2ebbd78465c9a1271.png)![1*8GbrXbHdH5uPGMb5epWhrg.png](../_resources/0c6fb634056732ec7316fb418eb6063d.png)

### What is Kafka

Kafka is a Publish/Subscribe messaging system. It allows **producers** to write ***records*** into Kafka that can be read by one or more **consumers**. These records that cannot be deleted or modify once they are sent to Kafka (this is known as “distributed commit log”).

Records are published into **topics**. Topics are like channels where all the records are stored. Consumers subscribe to one or more topics to read its records.

Kafka has a retention period, so it will store your records for the time or size you specify and can be set by topic.

Consumers label themselves with a **consumer group **name. In a consumer group, one or more consumers work together to consume a topic. When a new record arrives to the topic, it will be sent just to one consumer instance in the consumer group.

![](../_resources/a789803c3dac7d7955e574f65a52c579.png)![0*2VZAwzNcIBNT2FPm](../_resources/6447d569df58003791f9e50af2397bac.png)

### Architecture

Kafka is distributed as in the sense that it stores, receives and sends records on different nodes (called **brokers**). This makes it easy to scale it horizontally and makes it fault-tolerant. Brokers receive records from producers, assigns offsets to them, and commits them to storage on disk.

To run Kafka, you need Zookeeper. Zookeeper is used for:

- •**Controller election**. The controller is one of the brokers and is responsible for maintaining the leader/follower relationship for all the partitions. When a node shuts down, it is the controller that tells other replicas to become partition leaders to replace the partition leaders on the node that is going away. Zookeeper is used to elect a controller, make sure there is only one and elect a new one it if it crashes.
- •**Cluster membership. **Zookeeper maintains a list of all the brokers that are functioning and are a part of the cluster at any given moment.
- •**Topic configuration** — which topics exist, how many partitions each has, where are the replicas, who is the preferred leader, what configuration overrides are set for each topic
- •**Quotas** . How much data is each client allowed to read and write
- •**Access Control Lists (ACL)** . Who is allowed to read and write to which topic (old high level consumer) — Which consumer groups exist, who are their members and what is the latest offset each group got from each partition.

### Deep Dive

As topics can get quite big, they get split into **partitions** (this improves performance and scalability). So a record will be published in a single partition of a topic. Producers can choose the partition in which a record will be sent to, otherwise, the partition is chosen by Kafka.

A partition is owned by a single broker in the cluster, and that broker is called the leader of the partition. A partition may be assigned to multiple brokers, which will result in the partition being replicated. This provides redundancy of records in the partition, such that another broker can take over leadership if there is a broker failure.

About consumer groups, In order to avoid two consumer instances within the same consumer groups reading the same record twice, each partition is tied to only one consumer process per consumer group.

![](../_resources/348d7ce12b75284e0e3218b022c57b61.png)![0*7Izv0MGS2q6-iyTO](../_resources/8ae2b910a216819b85c3c4ae8506c0ca.png)

Kafka follows the principle of a dumb broker and smart consumer. This means that Kafka does not keep track of what records are read by the consumer. By storing the offset of the last consumed record for each partition, either in Zookeeper or in Kafka itself, a consumer can stop and restart without losing its place.

Each record consists of a key, a value, and a timestamp. This key is assigned by Kafka when producers publish a record. Keys are used when records are to be written to partitions in a more controlled manner. The simplest such scheme is to generate a consistent hash of the key, and then select the partition number for that record by taking the result of the hash modulo, the total number of partitions in the topic. This assures that records with the same key are always written to the same partition.

![](../_resources/495873af1be20a779fef62b6dc741ed8.png)![0*ceejxlUjQO38MTw6](../_resources/f3523175860dac2e69f02f3a67e533d0.png)

Note: While records are opaque byte arrays to Kafka itself, it is recommended that additional structure, or schema, be imposed on the record content so that it can be easily understood. Typically, this schema can be JSON or Avro. It is also normal to add some versioning for when it changes.

### Note on Kafka Streams

Kafka’s Streams API allows an application to act as a stream processor, consuming an input stream from one or more topics and producing an output stream to one or more output topics, effectively transforming the input streams to output streams.

It is normally used for enrichment and transformation. For example, we could have a `users` topic and an `enriched-users` topic. So a `UserEnricher` service could read users events, add information about its company and college and publish the same events but with more information into our enriched-users topic.

### Run it locally

You can easily run it using docker:
$ docker network create kafka

$ docker run --network kafka -p 2181:2181 -p 9092:9092 --env ADVERTISED_HOST=`docker-machine ip \`docker-machine active\`` --env ADVERTISED_PORT=9092 spotify/kafka

To test that it is working, let’s create a topic and run a consumer and a producer. Kafka exposes an API for these actions. To make it easy, Kafka brings some script that we can use to easily do this. To use these scripts, we can run an image of Kafka in a container and tell this container to execute one of these scripts.

So to create a topic, we can run a container with `bitnami/kafka:latest` image in interactive mode (`-it`) using the same network that our Kafka and Zookeeper containers are using (` — network kafka`). Let’s check what is the IP of our container:

$ docker network inspect kafka

# Check IPv4Address, for me it shows 172.19.0.2

And now run `kafka-topics.sh` script:

docker run -it --network kafka bitnami/kafka:latest kafka-topics.sh --create --zookeeper 172.19.0.2:2181 --replication-factor 1 --partitions 1 --topic amazingtopic

Now let’s check our topic was created properly:

docker run -it --network kafka bitnami/kafka:latest kafka-topics.sh --zookeeper 172.19.0.2:2181 --describe --topic amazingtopic

And now let’s do the cool stuff: create a Consumer and a Producer. Start creating a consumer by typing:

docker run -it --network kafka bitnami/kafka:latest kafka-console-consumer.sh --bootstrap-server 172.19.0.2:9092 --topic amazingtopic --from-beginning

Now open a new terminal and create a producer:

docker run -it --network kafka bitnami/kafka:latest kafka-console-producer.sh --broker-list 172.19.0.2:9092 --topic amazingtopic

When you run this producer, it lets you type words and it publishes a record to Kafka once you click enter. Try to create some records and see how they arrive to the consumer :D

Note: if you kill the consumer, then produce some more records into our `amazingtopic` and finally run a new consumer, you will see that all the records appear again so there is no lost of information while the consumer was down.

### Troubleshooting

I recommend you to use KafkaManager. This is an application that fetches metrics from Kafka and shows them in a nice interface.

Its interface is really simple, if you access to `localhost:9000` using your browser, its first page will load and you will see a list of all Kafka cluster that it is connected to.

If you click in one of the clusters, a new page with the summary of it will appear and also, you will see several options on the top menu:

![](../_resources/0d066d444f85e2100bea1fd407588a85.png)![0*i2PyfD4CZova5dSE](../_resources/0ee9ffed0f89738bded4373384d1e1ec.png)

- •**Brokers**. In the brokers main page, you can see some basic info for the brokers (like bytes in and bytes out). If you click on one of the brokers ids, you will see information about records and topics handle by this specific broker.
- •**Topic**. Then go to List, you will be redirected to a topics page. Here you can see the number of partitions and replicas for every topic. You can also click on the topic name to find much more information about it.

![](../_resources/7691872714d0489546b41394a1d7ba28.png)![0*bnoEWJe5e04jsltS](../_resources/d34f41bf7143badde75d8a7c0787b384.png)

- •**Consumers**. You will get a list of consumers. Click on one of the consumers name to see the list of topics it is reading from and click on a topic name to see information like % of partitions assigned to a consumer instance, total lag and consumer offset.

### Thanks for reading!

That is all for this overview of Kafka :)

If you want to see code examples of consumers or producers for Kafka, please let me know in a comment below or send a message to my twitter account [@Marvalcam1](https://twitter.com/Marvalcam1)