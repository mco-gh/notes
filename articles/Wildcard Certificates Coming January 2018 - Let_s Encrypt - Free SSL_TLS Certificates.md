Wildcard Certificates Coming January 2018 - Let's Encrypt - Free SSL/TLS Certificates

# Wildcard Certificates Coming January 2018

Jul 6, 2017 • Josh Aas, ISRG Executive Director

Let’s Encrypt will begin issuing wildcard certificates in January of 2018. Wildcard certificates are a commonly requested feature and we understand that there are some use cases where they make HTTPS deployment easier. Our hope is that offering wildcards will help to accelerate the Web’s progress towards 100% HTTPS.

Let’s Encrypt is currently securing 47 million domains via our fully automated DV certificate issuance and management API. This has contributed heavily to the Web going from 40% to 58% encrypted page loads since Let’s Encrypt’s service became available in December 2015. If you’re excited about wildcard availability and our mission to get to a 100% encrypted Web, we ask that you contribute to our [summer fundraising campaign](https://letsencrypt.org/donate/).

A wildcard certificate can secure any number of subdomains of a base domain (e.g. *.example.com). This allows administrators to use a single certificate and key pair for a domain and all of its subdomains, which can make HTTPS deployment significantly easier.

Wildcard certificates will be offered free of charge via our [upcoming ACME v2 API endpoint](https://letsencrypt.org/2017/06/14/acme-v2-api.html). We will initially only support base domain validation via DNS for wildcard certificates, but may explore additional validation options over time. We encourage people to ask any questions they might have about wildcard certificate support on our [community forums](https://community.letsencrypt.org/).

We decided to announce this exciting development during our summer fundraising campaign because we are a nonprofit that exists thanks to the generous support of the community that uses our services. If you’d like to support a more secure and privacy-respecting Web, [donate today](https://letsencrypt.org/donate/)!

We’d like to thank our [community](https://letsencrypt.org/getinvolved/) and our [sponsors](https://letsencrypt.org/sponsors/) for making everything we’ve done possible. If your company or organization is able to sponsor Let’s Encrypt please email us at [sponsor@letsencrypt.org](https://letsencrypt.org//2017/07/06/wildcard-certificates-coming-jan-2018.htmlmailto:sponsor@letsencrypt.org).