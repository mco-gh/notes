atlassian/localstack

[![Build Status](../_resources/64f1b7ce47060cdfca7ac94338e92294.png)](https://travis-ci.org/atlassian/localstack)[[Coverage Status](../_resources/b13f666a6f084fb861d4b54b5d0bb158.bin)](https://coveralls.io/github/atlassian/localstack?branch=master)[[PyPI Version](../_resources/de7feec2a1dc9e70a022af4249e67150.bin)](https://badge.fury.io/py/localstack)[[PyPI License](../_resources/8d6f7fb65930b54b7d7d64aea8faef8c.bin)](https://img.shields.io/pypi/l/localstack.svg)[[Code Climate](../_resources/280dc8dd0cf4a8cef4dd79f5dfb49637.bin)](https://codeclimate.com/github/atlassian/localstack)

# [(L)](https://github.com/atlassian/localstack#localstack---a-fully-functional-local-aws-cloud-stack)LocalStack - A fully functional local AWS cloud stack

[![LocalStack](../_resources/08698cef1872698abaaa17d679f1f02f.png)](https://camo.githubusercontent.com/ce6df7bd0b7ea8f57c26aad2d309ac6c0c32d505/68747470733a2f2f692e696d67736166652e6f72672f666533383130386364362e706e67)

**Please note: The main version of this repository is https://bitbucket.org/atlassian/localstack, please raise PRs against that repo.**

*LocalStack* provides an easy-to-use test/mocking framework for developing Cloud applications.

Currently, the focus is primarily on supporting the AWS cloud stack.
*LocalStack* spins up the following core Cloud APIs on your local machine:

- **API Gateway** at [http://localhost:4567](http://localhost:4567/)
- **Kinesis** at [http://localhost:4568](http://localhost:4568/)
- **DynamoDB** at [http://localhost:4569](http://localhost:4569/)
- **DynamoDB Streams** at [http://localhost:4570](http://localhost:4570/)
- **Elasticsearch** at [http://localhost:4571](http://localhost:4571/)
- **S3** at [http://localhost:4572](http://localhost:4572/)
- **Firehose** at [http://localhost:4573](http://localhost:4573/)
- **Lambda** at [http://localhost:4574](http://localhost:4574/)
- **SNS** at [http://localhost:4575](http://localhost:4575/)
- **SQS** at [http://localhost:4576](http://localhost:4576/)
- **Redshift** at [http://localhost:4577](http://localhost:4577/)

Additionally, *LocalStack* provides a powerful set of tools to interact with the cloud services, including a fully featured KCL Kinesis client with Python binding, simple setup/teardown integration for nosetests, as well as an Environment abstraction that allows to easily switch between local and remote Cloud execution.

## [(L)](https://github.com/atlassian/localstack#why-localstack)Why *LocalStack*?

*LocalStack* builds on existing best-of-breed mocking/testing tools, most notably[kinesalite](https://github.com/mhart/kinesalite)/[dynalite](https://github.com/mhart/dynalite)and [moto](https://github.com/spulec/moto). While these tools are *awesome* (!), they lack functionality for certain use cases. *LocalStack* combines the tools, makes them interoperable, and adds important missing functionality on top of them:

- **Error injection:**  *LocalStack* allows to inject errors frequently occurring in real Cloud environments, for instance ` ProvisionedThroughputExceededException ` which is thrown by Kinesis or DynamoDB if the amount of read/write throughput is exceeded.
- **Actual HTTP REST services**: All services in *LocalStack* allow actual HTTP connections on a TCP port. In contrast, moto uses boto client proxies that are injected into all methods annotated with ` @mock_sqs `. These client proxies do not perform an actual REST call, but rather call a local mock service method that lives in the same process as the test code.
- **Language agnostic**: Although *LocalStack* is written in Python, it works well with arbitrary programming languages and environments, due to the fact that we are using the actual REST APIs via HTTP.
- **Isolated processes**: All services in *LocalStack* run in separate processes. The overhead of additional processes is negligible, and the entire stack can easily be executed on any developer machine and CI server. In moto, components are often hard-wired in RAM (e.g., when forwarding a message on an SNS topic to an SQS queue, the queue endpoint is looked up in a local hash map). In contrast, *LocalStack* services live in isolation (separate processes available via HTTP), which fosters true decoupling and more closely resembles the real cloud environment.
- **Pluggable services**: All services in *LocalStack* are easily pluggable (and replaceable), due to the fact that we are using isolated processes for each service. This allows us to keep the framework up-to-date and select best-of-breed mocks for each individual service (e.g., kinesalite is much more advanced than its moto counterpart).

## [(L)](https://github.com/atlassian/localstack#requirements)Requirements

- ` make `
- ` python 2 `
- ` pip ` (python package manager)
- ` npm ` (node.js package manager)
- ` java `/` javac ` (Java runtime environment and compiler)

## [(L)](https://github.com/atlassian/localstack#installing)Installing

The easiest way to install *LocalStack* is via ` pip `:

	normalpip install localstack
	normal

## [(L)](https://github.com/atlassian/localstack#running-in-docker)Running in Docker

You can also spin up *LocalStack* without any installation requirements, using Docker:

	normaldocker run -it -p 4567-4576:4567-4576 atlassianlabs/localstack
	normal

... or simply use the ` make ` target which runs the same command:

	normalmake docker-run
	normal

## [(L)](https://github.com/atlassian/localstack#developing)Developing

If you pull the repo in order to extend/modify LocalStack, run this command to install all dependencies:

	normalmake install
	normal

This will install the required pip dependencies in a local Python virtualenv directory` .venv ` (your global python packages will remain untouched), as well as some node modules in ` ./localstack/node_modules/ `. Depending in your system, some pip/npm modules may require additional native libs installed.

## [(L)](https://github.com/atlassian/localstack#testing)Testing

The project comes with a set of unit and integration tests which can be kicked off via a make target:

	normalmake test
	normal

## [(L)](https://github.com/atlassian/localstack#running-the-infrastructure)Running the infrastructure

The Makefile contains a target to conveniently run the local infrastructure.

	normalmake infra
	normal

Then you can point your ` aws ` CLI to use the local infrastructure, for example:

	normalaws --endpoint-url=http://localhost:4568 kinesis list-streams
	{
	    "StreamNames": []
	}
	normal

If you are accessing the cloud APIs from within yout Python code, you can also use ` boto3 ` and use the ` endpoint_url ` parameter to connect to the respective service on ` localhost `. See ` localstack.utils.aws.aws_stack ` for convenience methods to connect to the local services.

## [(L)](https://github.com/atlassian/localstack#integration-with-nosetests)Integration with nosetests

If you want to use *LocalStack* in your integration tests (e.g., nosetests), simply fire up the infrastructure in your test setup method and then clean up everything in your teardown method:

	normalfrom localstack.mock import infra

	def setup():
	    infra.start_infra(async=True)

	def teardown():
	    infra.stop_infra()

	def my_app_test():
	    # here goes your test logic
	normal

See the example test file ` tests/test_integration.py ` for more details.

## [(L)](https://github.com/atlassian/localstack#integration-with-javajunit)Integration with Java/JUnit

In order to use *LocalStack* with Java, the project ships with a simple JUnit runner. Take a look at the example JUnit test in ` ext/java `. When you run the test, all dependencies are automatically downloaded and installed to a temporary directory in your system.

	normal@RunWith(LocalstackTestRunner.class)
	public class MyCloudAppTest {

	  @Test
	  public void testLocalS3API() {
	    AmazonS3 s3 = new AmazonS3Client(...);
	    s3.setEndpoint(LocalstackTestRunner.getEndpointS3());
	    List<Bucket> buckets = s3.listBuckets();
	    ...
	  }

	}
	normal

## [(L)](https://github.com/atlassian/localstack#web-dashboard)Web Dashboard

The projects also comes with a simple Web dashboard that allows to view the deployed AWS components and the relationship between them.

	normalmake install-web
	make web
	normal

## [(L)](https://github.com/atlassian/localstack#change-log)Change Log

- v0.3.2: Add support for Redshift API; code refactoring
- v0.3.1: Add Dockerfile and push image to Docker Hub
- v0.3.0: Add simple integration for JUnit; improve process signal handling
- v0.2.11: Refactored the AWS assume role function
- v0.2.10: Added AWS assume role functionality.
- v0.2.9: Kinesis error response formatting
- v0.2.7: Throw Kinesis errors randomly
- v0.2.6: Decouple SNS/SQS: intercept SNS calls and forward to subscribed SQS queues
- v0.2.5: Return error response from Kinesis if flag is set
- v0.2.4: Allow Lambdas to use **file** (import from file instead of exec'ing)
- v0.2.3: Improve Kinesis/KCL auto-checkpointing (leases in DDB)
- v0.2.0: Speed up installation time by lazy loading libraries
- v0.1.19: Pass shard_id in records sent from KCL process
- v0.1.16: Minor restructuring and refactoring (create separate kinesis_util.py)
- v0.1.14: Fix AWS tokens when creating Elasticsearch client
- v0.1.11: Add startup/initialization notification for KCL process
- v0.1.10: Bump version of amazon_kclpy to 1.4.1
- v0.1.9: Add initial support for SQS/SNS
- v0.1.8: Fix installation of JARs in amazon_kclpy if localstack is installed transitively
- v0.1.7: Bump version of amazon_kclpy to 1.4.0
- v0.1.6: Add travis-ci and coveralls configuration
- v0.1.5: Refactor Elasticsearch utils; fix bug in method to delete all ES indexes
- v0.1.4: Enhance logging; extend java KCL credentials provider (support STS assumed roles)
- v0.1.2: Add configurable KCL log output
- v0.1.0: Initial release

## [(L)](https://github.com/atlassian/localstack#contributing)Contributing

We welcome feedback, bug reports, and pull requests!
For pull requests, please stick to the following guidelines:

- Add tests for any new features and bug fixes. Ideally, each PR should increase the test coverage.
- Follow the existing code style (e.g., indents). A PEP8 code linting target is included in the Makefile.
- Put a reasonable amount of comments into the code.
- Separate unrelated changes into multiple pull requests.

Please note that we need to collect a signed **Contributors License Agreement** from each individual developer who contributes code to this repository. Please refer to the following links:

- https://developer.atlassian.com/opensource/
- https://na2.docusign.net/Member/PowerFormSigning.aspx?PowerFormId=3f94fbdc-2fbe-46ac-b14c-5d152700ae5d

## [(L)](https://github.com/atlassian/localstack#license)License

Copyright (c) 2016 Atlassian and others.

*LocalStack* is released under the Apache License, Version 2.0 (see LICENSE.txt).

We build on a number of third-party software tools, with the following licenses:

| Third-Party software | License |
| --- | --- |
| **Python/pip modules:** |     |
| airspeed | BSD License |
| amazon_kclpy | Amazon Software License |
| boto3 | Apache License 2.0 |
| coverage | Apache License 2.0 |
| docopt | MIT License |
| elasticsearch | Apache License 2.0 |
| flask | BSD License |
| flask_swagger | MIT License |
| jsonpath-rw | Apache License 2.0 |
| moto | Apache License 2.0 |
| nose | GNU LGPL |
| pep8 | Expat license |
| requests | Apache License 2.0 |
| sh  | MIT License |
| subprocess32 | PSF License |
| **Node.js/npm modules:** |     |
| dynalite | MIT License |
| kinesalite | MIT License |
| **Other tools:** |     |
| Elasticsearch | Apache License 2.0 |