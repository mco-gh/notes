Securing communications between Google services with Application Layer Transport Security

## [Securing communications between Google services with Application Layer Transport Security](https://security.googleblog.com/2017/12/securing-communications-between-google.html)

December 13, 2017

 Posted by Cesar Ghali and Julien Boeuf, Engineers on the Security & Privacy Team

At Google, protection of customer data is a top priority. One way we do this is by protecting data in transit by default. We protect data when it is sent to Google using secure communication protocols such as TLS (Transport Layer Security). Within our infrastructure, we protect service-to-service communications at the application layer using a system called Application Layer Transport Security (ALTS). ALTS authenticates the communication between Google services and helps protect data in transit. Today, we’re releasing a whitepaper, “[Application Layer Transport Security](https://cloud.google.com/security/encryption-in-transit/application-layer-transport-security),” that goes into detail about what ALTS is, how it protects data, and how it’s implemented at Google.

**ALTS is a highly reliable, trusted system that provides authentication and security for our internal Remote Procedure Call (RPC) communications.** ALTS requires minimal involvement from the services themselves. When services communicate with each other at Google, such as the Gmail frontend communicating with a storage backend system, they do not need to explicitly configure anything to ensure data transmission is protected - it is protected by default. All RPCs issued or received by a production workload that stay within a physical boundary controlled by or on behalf of Google are protected with ALTS by default. This delivers numerous benefits while allowing the system work at scale:

1. **More precise security:** Each workload has its own identity. This allows workloads running on the same machine to authenticate using their own identity as opposed to the machine’s identity.

2. **Improved scalability:** ALTS accommodates Google’s massive scale by using an efficient resumption mechanism embedded in the ALTS handshake protocol, allowing services that were already communicating to easily resume communications. ALTS can also accommodate the authentication and encryption needs of a large number of RPCs; for example, services running on Google production systems collectively issue on the order of O(1010) RPCs per second.

3. **Reduced overhead:** The overhead of potentially expensive cryptographic operations can be reduced by supporting long-lived RPC channels.

**
**
**Multiple features that ensure security and scalability**

Inside physical boundaries controlled by or on behalf of Google, all scheduled production workloads are initialized with a certificate that asserts their identity. These credentials are securely delivered to the workloads. When a workload is involved in an ALTS handshake, it verifies the remote peer identity and certificate. To further increase security, all Google certificates have a relatively short lifespan.

ALTS has a flexible trust model that works for different types of entities on the network. Entities can be physical machines, containerized workloads, and even human users to whom certificates can be provisioned.

ALTS provides a handshake protocol, which is a Diffie-Hellman (DH) based authenticated key exchange protocol that Google developed and implemented. At the end of a handshake, ALTS provides applications with an authenticated remote peer identity, which can be used to enforce fine-grained authorization policies at the application layer.

**
**
**
**

**ALTS ensures the integrity of Google traffic is protected, and encrypted as needed.**

After a handshake is complete and the client and server negotiate the necessary shared secrets, ALTS secures RPC traffic by forcing integrity, and optional encryption, using the negotiated shared secrets. We support multiple protocols for integrity guarantees, e.g., AES-GMAC and AES-VMAC with 128-bit keys. **Whenever traffic leaves a physical boundary controlled by or on behalf of Google, e.g., in transit over WAN between datacenters, all protocols are upgraded automatically to provide encryption as well as integrity guarantees.** In this case, we use the AES-GCM and AES-VCM protocols with 128-bit keys.

More details on how Google data encryption is performed are available in another whitepaper we are releasing today, “[Encryption in Transit in Google Cloud](https://cloud.google.com/security/encryption-in-transit).”

In summary, ALTS is widely used in Google’s infrastructure to provide service-to-service authentication and integrity, with optional encryption for all Google RPC traffic. For more information about ALTS, please read our whitepaper, “[Application Layer Transport Security](https://cloud.google.com/security/encryption-in-transit/application-layer-transport-security).”

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

#### No comments :

[Post a Comment](https://www.blogger.com/comment.g?blogID=1176949257541686127&postID=4480987565772339436&isPopup=true)

#### Links to this post

[Create a Link](https://www.blogger.com/blog-this.g)