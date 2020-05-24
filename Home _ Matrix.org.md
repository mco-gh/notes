Home | Matrix.org

# What is this for?

.



#### Matrix for Messaging Apps:

Matrix provides a common language for interoperable communication. Existing messaging apps and solutions gain enormously by linking into Matrix – letting their users reach out with core messaging and VoIP functionality to every other user in the global Matrix ecosystem. Matrix provides the best platform for your app to showcase its differentiating features to the widest possible audience – tempting the rest of the world to install, as your users themselves become your ambassadors. Users should use your app because they want to. Not because they are trapped. Give your users the gift of freedom; they will reward you for it. Building a bridge has never been easier: see how we built the MatrixSlack bridge in under 100 lines of code: https://github.com/matrix-org/matrix-appservice-bridge/blob/master/HOWTO.md

Thinking about adding messaging to your app? *Don’t reinvent the wheel*. Matrix gives you simple HTTP APIs and SDKs (iOS, Android, Web) to add Matrix-enabled chatrooms and direct chats directly into existing apps, complete with end-to-end encryption, emoji, file transfer, etc… whilst exposing the app to a vast ecosystem of potential users, and letting you build directly on all the bridges, bots, services and clients out there in Matrix.



#### Matrix for IoT:

If fragmentation in Messaging and VoIP services is bad, fragmentation in the Internet of Things is even worse. Vendors ranging from Garmin and Fitbit through to Amazon and Apple have launched IoT services, each locked to that particular vendor’s platform. As a user, your data is trapped in each different silo, and you are limited to using the subset of IoT services which connect to those silos.

Matrix provides a way forward, much as it does for human communication scenarios. By building bridges to as many IoT silos as possible, data can be securely published on the Matrix network – liberating it be under the user’s control. IoT developers can then build solutions directly on Matrix rather than integrating separately with vendors, or even publish or consume Matrix data directly from devices.

Matrix.org has shown proof of concepts for several IoT use cases: visualizing OBD2 data across different car vendors (FOSDEM 2015); streaming video from different drone vendors (WebRTC World 2015), etc. We welcome the community to see how Matrix can work for them!

.



#### Matrix for VoIP and WebRTC:

Why is there still no standard, ubiquitous, interoperable way to place a phone call on the internet? Previous open standards have failed to get widespread consumer uptake, leaving proprietary walled gardens like Skype, Viber and WhatsApp to dominate. The situation only gets worse with the advent of WebRTC, giving every website in the world the ability to exchange high quality voice and video calls – but no way to actually route the calls. To “call someone on WebRTC” means to send them an email with a URL you expect them to follow – *email* has become the standard signalling layer for VoIP on the internet.

We believe there is still room for a standard protocol for interoperable VoIP on the internet – one that is simple and familiar to today’s web developers, and well matched to WebRTC. Matrix is that missing signalling layer for WebRTC. If you are building VoIP into your app, or want to expose your existing VoIP app to a wider audience, building on Matrix’s SDKs and bridges should be a no-brainer.



#### Matrix for Bots:

By writing a bot for Matrix you are unleashing it on the widest possible ecosystem imaginable. Matrix’s simple HTTP APIs, SDKs, or existing bot frameworks (go-neb or py-neb) mean you can implement against a single open standard interface… and instantly expose the bot to every messaging platform (IRC, Slack, Gitter, XMPP etc.) connected to Matrix, letting you concentrate on the important bit: the bot itself.

Because Matrix is constantly evolving, with new bridges, networks and apps being added all the time by the wider Matrix developer community, the sky really is the limit in terms of your bot’s audience. And with new bot frameworks popping up all the time you can easily stand on the shoulders of giants without being locked into any single proprietary communication service.

.