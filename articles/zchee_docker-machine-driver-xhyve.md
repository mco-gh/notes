zchee/docker-machine-driver-xhyve

# [(L)](https://github.com/zchee/docker-machine-driver-xhyve#docker-machine-driver-xhyve)docker-machine-driver-xhyve

| **Travis CI** | **Releases** |
| --- | --- |
| [[Travis CI](../_resources/17d9e3f7faa149dd82a94f794679ad37.bin)](https://travis-ci.org/zchee/docker-machine-driver-xhyve) | [![Releases](../_resources/a1ddf345e5b288e08e7331136829562c.bin)](https://github.com/zchee/docker-machine-driver-xhyve/releases) |

[[GA](../_resources/c2196de8ba412c60c22ab491af7b1409.gif)](https://github.com/zchee/docker-machine-driver-xhyve)

libmachine driver plugin for [xhyve](https://github.com/mist64/xhyve) native OS X Hypervisor

Master branch inherited from [nathanleclaire/docker-machine-xhyve](https://github.com/nathanleclaire/docker-machine-xhyve). Thanks [@nathanleclaire](https://github.com/nathanleclaire) :)

If you have issues or pull-requests, Desired to be posted to this repository.

## [(L)](https://github.com/zchee/docker-machine-driver-xhyve#screencast)Screencast

[![asciinema](../_resources/02c3f47e2d605cbefa51b6f221501f2c.png)](https://asciinema.org/a/29930)

## [(L)](https://github.com/zchee/docker-machine-driver-xhyve#requirements)Requirements

### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#docker-machine-minikube-or-minishift)docker-machine, minikube or minishift

- https://github.com/docker/machine
- https://github.com/kubernetes/minikube
- https://github.com/minishift/minishift

docker-machine-driver-xhyve using libmachine plugin model.

**Please do not post the issue of this repository to docker/machine, kubernetes/minikube and minishift/minishift**

It will interfere with the development of docker-machine, minikube or minishift.

If you were doubt problem either, please post to this repository [issues](https://github.com/zchee/docker-machine-driver-xhyve/issues).

- docker-machine
    - See https://github.com/docker/machine/releases
- minikube
    - See https://github.com/kubernetes/minikube/releases
- minishift
    - See https://github.com/minishift/minishift/releases

## [(L)](https://github.com/zchee/docker-machine-driver-xhyve#install)Install

Use [Homebrew/brew](https://github.com/Homebrew/brew):

$ brew install docker-machine-driver-xhyve# docker-machine-driver-xhyve need root owner and uid$ sudo chown root:wheel $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve

$ sudo chmod u+s $(brew --prefix)/opt/docker-machine-driver-xhyve/bin/docker-machine-driver-xhyve

Use ` go ` with ` make `:

If you want to support qcow2 disk image format, need install [mirage/ocaml-qcow](https://github.com/mirage/ocaml-qcow). See [docker/hyperkit#building](https://github.com/docker/hyperkit#building).

# Need Go 1.5 vendoring support$ export GO15VENDOREXPERIMENT=1

$ go get -u -d github.com/zchee/docker-machine-driver-xhyve

$ cd  $GOPATH/src/github.com/zchee/docker-machine-driver-xhyve# Install qcow-format for qcow2 disk image format$ brew install opam libev

$ opam init

$ eval  `opam config env`$ opam install uri qcow-format io-page.1.6.1 conf-libev# Install docker-machine-driver-xhyve binary into /usr/local/bin$ make install# docker-machine-driver-xhyve need root owner and uid$ sudo chown root:wheel /usr/local/bin/docker-machine-driver-xhyve

$ sudo chmod u+s /usr/local/bin/docker-machine-driver-xhyve
We use [Glide](https://github.com/Masterminds/glide) for dependency management.
$ go get github.com/Masterminds/glide
This will install the glide binary into ` $GOPATH/bin `.
Updating Dependencies

If your work requires a change to the dependencies, you need to update the Glide configuration.

- Edit glide.yaml to change the dependencies as needed.
- Delete ` glide.lock ` and re-create the vendor directory by running ` make vendor `. Glide will recognize that there is no lock file and recalculatethe required dependencies.
- Check-in the updated ` glide.yaml ` and ` glide.lock ` files.
- Test that everything still compiles with the new lock file in place by running make clean && make.

Note: In some cases the Glide cache located under ~/.glide/cache can get corrupted. If you seeing Glide errors during ` make vendor `, you can clear the Glide cache via ` glide cc `.

## [(L)](https://github.com/zchee/docker-machine-driver-xhyve#usage)Usage

### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#available-flags)Available flags

Flag name
Environment variable
Type
Default
[object Object]
[object Object]
string
[object Object]
[object Object]
[object Object]
int
[object Object]
[object Object]
[object Object]
int
[object Object]
[object Object]
[object Object]
int
[object Object]
[object Object]
[object Object]
int
[object Object]
[object Object]
[object Object]
string

See [AUTOMATED_SCRIPT.md](https://github.com/boot2docker/boot2docker/blob/master/doc/AUTOMATED_SCRIPT.md#extracting-boot-parameters)

[object Object]
[object Object]
string
[object Object]
[object Object]
[object Object]
string
[object Object]
[object Object]
[object Object]
bool
[object Object]
[object Object]
[object Object]
bool
[object Object]
[object Object]
[object Object]
string
Path to a host folder to be shared inside the guest
[object Object]
[object Object]
string
root path at which the NFS shares will be mounted

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-boot2docker-url)` --xhyve-boot2docker-url `

The URL(Path) of the boot2docker image.
By default, use cached iso file path.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-cpu-count)` --xhyve-cpu-count `

Number of CPUs to use the create the VM.
If set ` -1 `, use logical CPUs usable by the current process.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-memory-size)` --xhyve-memory-size `

Size of memory for the guest.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-disk-size)` --xhyve-disk-size `

Size of disk for the guest (MB).

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-uuid)` --xhyve-uuid `

The UUID for the machine.

By default, generate and use ramdom UUID. See [xhyve/uuid.go](https://github.com/zchee/docker-machine-driver-xhyve/blob/master/xhyve/uuid.go)

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-boot-cmd)` --xhyve-boot-cmd `

Booting xhyve kexec commands.
By default, use

` loglevel=3 user=docker console=ttyS0 console=tty0 noembed nomodeset norestore waitusb=10 base host=boot2docker `

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-boot-kernel)` --xhyve-boot-kernel `

Booting kernel file path.

By default, will automatically parses the file path using ` (vmlinu[xz]|bzImage)[\d]* `.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-boot-initrd)` --xhyve-boot-initrd `

Booting initrd file path.
By default, will automatically parses the ` initrd ` contains file path.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-qcow2)` --xhyve-qcow2 `

Use ` qcow2 ` disk format.

If you using minikube, ` CONFIG_VIRTIO_BLK=y ` support is included in minikube-iso as of version v0.0.6.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-rawdisk)` --xhyve-rawdisk `

Use a simple 'raw disk' format and virtio-blk driver for storage. This may be significantly faster for I/O intensive applications, at the potential cost of data durability.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-virtio-9p)` --xhyve-virtio-9p `

Enable ` virtio-9p ` folder share.

If you using docker-machine, ` CONFIG_NET_9P=y ` support is included in boot2docker as of version v1.10.2.

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-experimental-nfs-share-pathtohostfolder)` --xhyve-experimental-nfs-share /path/to/host/folder `

Share ` path/to/host/folder ` inside the guest at the path specified by ` --xhyve-experimental-nfs-share-root ` (which itself defaults to ` /xhyve-nfsshares `).

Can be specified multiple times

#### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#--xhyve-experimental-nfs-share-root-path)` --xhyve-experimental-nfs-share-root /path `

By default, NFS Shares will be mounted in the Guest at ` /xhyve-nfsshares `.

You can change this default by specifying ` --xhyve-experimental-nfs-share-root /path `, ` /path ` being a path to the root

## [(L)](https://github.com/zchee/docker-machine-driver-xhyve#known-isuue)Known isuue

### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#does-not-clean-up-the-vmnet-when-remove-a-vm)Does not clean up the vmnet when remove a VM

Currently, ` docker-machine-driver-xhyve ` does not clean up the ` dhcpd_leases `.

like,

# Running xhyve vm. for example, assign 192.168.64.1$ docker-machine create --driver xhyve xhyve-test |# Send ACPI signal(poweroff) signal over the ssh$ docker-machine rm xhyve-test |# Re-create xhyve vm, will assign 192.168.64.2docker-machine create --driver xhyve xhyve-test

It will assigned to 192.168.64.**2**. If create another vm, assigned to 192.168.64.**3**.

But 192.168.64.**1** are not using anyone.
` vmnet.framework ` seems to have decide the IP based on below files

- ` /var/db/dhcpd_leases `
- ` /Library/Preferences/SystemConfiguration/com.apple.vmnet.plist `

So, If you want to reset IP database, please remove it manually. but **very risky**.

Note that ` vmnet.framework ` shared net address range is ` 192.168.64.1 ` ~ ` 192.168.64.255 `. You can make 255 vm.

I will implement the clean-up process after understanding the ` vmnet.framework `.

### [(L)](https://github.com/zchee/docker-machine-driver-xhyve#cant-launch-on-macos-10114-build-15e27e)Can't launch on macOS 10.11.4 build 15E27e

Mac OS X 10.11.4 build ` 15E27e ` has a **Hypervisor.framework bug**.
This is Apple's bug.
But, Apple has been fixed build ` 15E33e `.

If you launch the ` docker-machine-driver-xhyve ` on build 15E27e, will displayed

open : no such file or directory
and, In original ` xhyve `,
hv_vm_create failed
See

- https://asciinema.org/a/34798 (15E27e)
- https://asciinema.org/a/34797 (15E33e)

## [(L)](https://github.com/zchee/docker-machine-driver-xhyve#could-you-report)Could you report?

I'm very anxious whether other users(except me) are able to launch the xhyve.

So, if you were able to launch the xhyve use docker-machine-driver-xhyve, Could you post a report to this issue thread?

https://github.com/zchee/docker-machine-driver-xhyve/issues/18

If macOS launched by the ` Vagrant `, can be build, but will not be able to launch the Hypervisor.

The cause probably because backend vm (Virtualbox, VMWare, parallels...) to hide the CPU infomation.

In the case of VMWare,
$ system_profiler SPHardwareDataType

system_profiler[458:1817] platformPluginDictionary: Can't get X86PlatformPlugin, return value 0system_profiler[458:1817] platformPluginDictionary: Can't get X86PlatformPlugin, return value 0

Hardware:
Hardware Overview:
Model Name: Mac
Model Identifier: VMware7,1
// Where is "Processor Name:" field? Processor Speed: 2.19 GHz
Number of Processors: 1
Total Number of Cores: 1
L2 Cache: 256 KB
L3 Cache: 6 MB
Memory: 2 GB
Boot ROM Version: VMW71.00V.0.B64.1505060256
SMC Version (system): 1.16f8

Serial Number (system): ************ Hardware UUID: ********-****-****-****-************$ git clone https://github.com/mist64/xhyve &&  cd xhyve

$ make
$ ./xhyverun.sh
vmx_init: processor not supported by Hypervisor.framework
Unable to create VM (-85377018)