StdLib — Function as a Service Software Library

Welcome to StdLib!

Forgot Password?

 [New User?](https://stdlib.com/#)

 [(L)](https://stdlib.com/)  [Documentation](https://docs.stdlib.com/main)
 Community

 [**  GitHub](https://github.com/stdlib/lib)

 [**  Twitter](https://twitter.com/stdlibhq)

 [**  Slack]()

 [**  Sign Up](https://stdlib.com/#)  [**  Log In](https://stdlib.com/#)

 Infinitely scalable, self-healing web services in an instant.

StdLib is the easiest way to create, distribute and discover web services. Ship products and build your API business faster than ever before using cutting edge "server-less" technology.

 [** stdlib/lib   **  1,878](https://github.com/stdlib/lib)  [Sign Up Free]()

#  Create functions and turn them into scalable API Services

You've never shipped code this quickly. Use our command line tools to turn your code into infinitely scalable web services in seconds. Want to see how fast you're going to be able to move?  Go ahead, give StdLib a spin — we've built this web-based demo so you can build a live service without installing anything.

StdLib Service Creator
****f
****main
**function.json**
**index.js**
**env.json**
**package.json**
**README.md**
package.json
f/main/index.js

** This file exports the function that will be executed as part of your microservice. You can have multiple functions (and thus endpoints) in your service.

4

1
module.exports  = (params, callback) => {
2
 let  name  =  params.kwargs.name  ||  'World';
3
 return  callback(null, `Hello ${name}`);
4
};

**Not Logged In( [Log In](https://stdlib.com/#) )
Environment
**

#  Share, discover and integrate with other developers and companies

Think of us like GitHub for the service layer. Share your services with others for free, or use StdLib as a tool to build an API business from the ground up. Set rate limits for both unauthenticated guests and authenticated users, then choose price points based on request volume or compute usage. Whether you're providing open services for others or building the next Twilio, we're here to make it easy — just look at what StdLib developers are doing right now.

 [NEW · 6 hours ago tanyi/demo10.0.3  Service  tanyi · Apr 10th 2017, 9:16 AM](https://stdlib.com/tanyi/demo1)[NEW · 2 days ago jckcthbrt/kaomoji1.0.2  Service  jckcthbrt · Apr 8th 2017, 6:32 AM](https://stdlib.com/jckcthbrt/kaomoji)[NEW · 2 days ago swarajd/atcvrserv0.0.0  Service  swarajd · Apr 8th 2017, 4:59 AM](https://stdlib.com/swarajd/atcvrserv)[NEW · 4 days ago amillet89/prospector0.0.0  Prospects a domain using Clearbit  amillet89 · Apr 6th 2017, 8:40 PM](https://stdlib.com/amillet89/prospector)

#  Code templates, automated documentation, built-in SDKs

Whether you're building a new Vue.js app or working on an Alexa Skill, StdLib has code templates that allow you to go from zero to one — no familiarity required. We also automatically generate documentation pages for your services, and our pre-built SDKs for the command line, Node.js, Python and Ruby means other developers can access your services seamlessly without any additional work on your behalf. Go ahead and take a look at our Markdown service to see how easy it is to develop with the StdLib SDKs.

[stdlib/markdown](https://stdlib.com/stdlib/markdown) · playground
**  Run Service
Node.js
Python
Ruby
Shell
HTTPS

**  Installation  [** GitHub: stdlib/lib-node](https://github.com/stdlib/lib-node)

1

1
$ npm install lib --save

**  Usage

10

1
const  lib  =  require('lib');
2
​
3
lib.stdlib.markdown(
4
{
5
   'md': '# Hello!\n\nTransform **me** into `markdown`!'
6
},
7
(err, result) => {
8
   */* handle */*
9
}
10
);

#  Organizational features you've been missing everywhere else

Used "server-less" architecture before? Find out what you've been missing. New to the space? Start with the best.

- 🗄   Service Registration usable publicly and privately

- 📦   Package Management for managing versions across your team

- 🛠   Development Framework that fits cleanly into your workflow

- 🏷   Version Control to run software releases smoothly

- ⚙   Execution Gateway to access your services globally

- 🚀   Distributed Hosting built with "server-less" technology

- 🔑   Immutable Releases ensuring functional lock-in

- 📝   Mutable Staging Environments for testing and development

 [Sign Up Free]()

# Community

 [Contact](https://stdlib.com/mailto:contact@stdlib.com)  [Careers](https://stdlib.com/mailto:careers@stdlib.com)  [Twitter](https://twitter.com/stdlibhq)  [GitHub](https://github.com/stdlib/lib)

# About

 [Docs](https://docs.stdlib.com/main)  [Search](https://stdlib.com/search)  [Pricing](https://stdlib.com/pricing)

StdLib · A Standard Library for Microservices
San Francisco · Toronto · New York City
© 2017 Polybit Inc.
 ![](../_resources/f8ec25609a6e1031f1989b72b59024ca.png)

[(L)](https://stdlib.com/#)Window size:  x
Viewport size:  x