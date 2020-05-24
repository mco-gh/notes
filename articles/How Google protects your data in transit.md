How Google protects your data in transit

## [How Google protects your data in transit](https://cloudplatform.googleblog.com/2017/12/how-Google-protects-your-data-in-transit.html)

Wednesday, December 13, 2017
 By Maya Kaczorowski, Security and Privacy Product Manager

Protecting your data is of the utmost importance for Google Cloud, and one of the ways we protect customer data is through encryption. We [encrypt your data at rest, by default](https://cloud.google.com/security/encryption-at-rest/), as well as while it’s in transit over the internet from the user to Google Cloud, and then internally when it’s moving within Google, for example between data centers.

We aim to create trust through transparency, and today, we’re releasing a whitepaper, “[Encryption in Transit in Google Cloud](https://cloud.google.com/security/encryption-in-transit/),” that describes our approach to protecting data in transit.

Google Cloud employs several security measures to help ensure the authenticity, integrity and privacy of data in transit. Authentication means we know and verify the data source. Integrity means we make sure data you send arrives at its destination unaltered. Encryption means we make your data confidential while in transit to keep it private.

###

Your data is encrypted in transit by default

**By default, when a user connects to Google Cloud, the connection between the user and Google is encrypted**. That means that when you connect to Google Cloud, the data you send is encrypted using HTTPS, so that an adversary cannot snoop on your traffic. (You can find out more about HTTPS at Google in our [HTTPS transparency report](https://transparencyreport.google.com/https/overview).) Google implements TLS and other encryption in transit protocols by using BoringSSL, an open-source cryptographic library derived from OpenSSL.

**By default, Google Cloud encrypts and authenticates all data in transit at one or more network layers when data moves outside physical boundaries not controlled by or on behalf of Google.** For comparison, data in transit inside a physical boundary is authenticated but not necessarily encrypted because rigorous security controls are already in place. To ensure we are protecting data against any potential threats, our inherent assumption is that the wide area network is only semi-trusted — that is, that network links between physical boundaries can be compromised by an active adversary who can snoop, inject or alter traffic on the wire. Encrypting data in transit helps protect against this type of activity.

At the network layer, Google Cloud’s virtual network infrastructure automatically encrypts VM to VM traffic if it crosses a physical boundary not controlled by or on behalf of Google. On top of this, at the application layer, [Application Layer Transport Security](https://security.googleblog.com/2017/12/securing-communications-between-google.html) automatically provides authentication, integrity and encryption of remote procedure calls from service to service, when those calls leave a physical boundary controlled by or on behalf of Google. Each service that runs in Google’s infrastructure has a service account identity with associated cryptographic credentials that are used to authenticate these communications.

###

[Google Cloud Encryption in Transit](https://www.youtube.com/watch?v=Dzju5aALHRQ)

You have additional options to encrypt your data in transit

In addition to default protections, Google Cloud customers have many options to further encrypt data in transit, including IPsec tunnels, free and automated TLS certificates and Istio.

With [Google Cloud VPN](https://cloud.google.com/vpn/docs/concepts/overview), you can send requests from your on-premise machine to a service hosted on Google Cloud through a secure, IPsec VPN tunnel at the network layer. You can also set up multiple, load-balanced tunnels through multiple VPN gateways.

For applications built on Google Cloud, Google provisions free and automated certificates to implement TLS in [Firebase Hosting](https://firebase.google.com/docs/hosting/custom-domain) and [Google App Engine custom domains](https://cloudplatform.googleblog.com/2017/09/introducing-managed-SSL-for-Google-App-Engine.html).

[Istio](https://istio.io/) is an open-source service mesh developed by Google, IBM, Lyft and others, to simplify service discovery and connectivity. Istio authentication aims to automatically encrypt data in transit between services, and manage the associated keys and certificates.

### Google helps the internet encrypt data in transit

In addition to how we specifically protect Google Cloud users, we have several open-source projects and other efforts to improve the internet’s security at large and support the use of encryption in transit. These include [Certificate Transparency (CT)](https://www.certificate-transparency.org/), which is designed to audit and monitor certificates issued by publicly trusted CAs. Certificate Transparency helps detect certificates that may not have been issued according to industry standards, or may not have been requested by the domain owner.

### Your data is yours

While we’re on the topic of data protection and privacy, it's useful to reinforce how we think about customer data. **In Google Cloud, you choose what data your business stores and what applications your business creates and runs on the service. We process your data only according to our agreement with your business**. You can read more about how we keep your business data private on our [Privacy website](https://privacy.google.com/businesses/).

To learn more about how we encrypt your data at rest and our overall security design, read our whitepapers “[Encryption at Rest in Google Cloud Platform](https://cloud.google.com/security/encryption-at-rest/default-encryption/)” and “[Google Infrastructure Security Design Overview](https://cloud.google.com/security/security-design/).”

Safe computing!

![Share on Google+](../_resources/c620b1a7b369ad2749d0baf881d4ccbb.png)![Share on Twitter](../_resources/4e2633eb72f2026ba8464540a445a45f.png)![Share on Facebook](../_resources/a4a815e062b3a04ad2cb425115438650.png)

Labels:[Security & Identity](https://cloudplatform.googleblog.com/search/label/Security%20%26%20Identity)