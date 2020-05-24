cloudfoundry-incubator/bosh-google-cpi-release

###    README.md

# [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#bosh-google-cpi-release)BOSH Google CPI release

This is a [BOSH](http://bosh.io/) release for the BOSH Google CPI.

## [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#releases)Releases

Releases are available on bosh.io: https://bosh.io/releases/github.com/cloudfoundry-incubator/bosh-google-cpi-release?all=1. Please see [CHANGELOG.md](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release/blob/master/CHANGELOG.md) for details of each release.

### [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#stemcell)Stemcell

Stemcells are available on bosh.io: http://bosh.io/stemcells/bosh-google-kvm-ubuntu-trusty-go_agent

## [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#usage)Usage

If you are not familiar with [BOSH](http://bosh.io/) and its terminology please take a look at the [BOSH documentation](http://bosh.io/docs).

### [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#deploy-a-bosh-director-on-google-cloud-platform)Deploy a BOSH Director on Google Cloud Platform

Complete instructions for deploying a BOSH Director are available in the [docs/bosh/README.md](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release/blob/master/docs/bosh/README.md) file.

### [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#deploy-other-software)Deploy other software

After you have followed the instructions for deploying a BOSH director in [docs/bosh/README.md](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release/blob/master/docs/bosh/README.md), you may deploy releases like CloudFoundry by following the links below:

- [Deploying Cloud Foundry on Google Compute Engine](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release/blob/master/docs/cloudfoundry)

## [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#developing)Developing

Contributions to the CPI are welcome. Unit and integration tests for any new features are encouraged. Developers may find it easier to set the GOPATH to the directory of the check-out repository:

	normalcd bosh-google-cpi-release
	export GOPATH=$pwd
	PATH=$PATH:$GOPATH/bin
	normal

### [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#running-integration-tests)Running integration tests

1. Set your project:

	normalexport GOOGLE_PROJECT=your-project-id
	normal

2. Create the infrastructure required to run tests:

	normalmake configint
	normal

3. Run the integration tests:

	normalmake testint
	normal

To destroy the infrastructure required to run the integration tests, execute:

	normal  make cleanint
	normal

## [(L)](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release#contributing)Contributing

For detailes on how to contribute to this project - including filing bug reports and contributing code changes - pleasee see [CONTRIBUTING.md](https://github.com/cloudfoundry-incubator/bosh-google-cpi-release/blob/master/CONTRIBUTING.md).