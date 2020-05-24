Ionic Framework



- [Home](http://ionicframework.com/docs/)

- [Intro]()

    - [Installation](http://ionicframework.com/docs/intro/installation)

    - [Tutorial](http://ionicframework.com/docs/intro/tutorial)

    - [Deploying](http://ionicframework.com/docs/intro/deploying)

    - [Migration](http://ionicframework.com/docs/intro/migration)

    - [Concepts](http://ionicframework.com/docs/intro/concepts)

- [Components]()

- [API](http://ionicframework.com/docs/api)

- [Native](http://ionicframework.com/docs/native/)

- [Storage](http://ionicframework.com/docs/storage/)

- [Theming]()

- [Ionicons](http://ionicframework.com/docs/ionicons/)

- [CLI]()

- [Troubleshooting](http://ionicframework.com/docs/troubleshooting/)

- [Resources](http://ionicframework.com/docs/developer-resources)

# Installing Ionic

[Improve this doc](https://github.com/ionic-team/ionic-site/edit/master/content/docs/intro/installation/index.md)

Ionic apps are created and developed primarily through the Ionic command line utility (the “CLI”), and use Cordova to build and deploy as a native app. This means we need to install a few utilities to get developing.

### Ionic CLI and Cordova

To create Ionic projects, you’ll need to install the latest version of the CLI and Cordova. Before you do that, you’ll need a recent version of Node.js. [Download the installer](https://nodejs.org/) for Node.js 6 or greater and then proceed to install the Ionic CLI and Cordova for native app development:

	$ npm install -g ionic cordova

>

> You may need to add “sudo” in front of these commands to install the utilities globally

Once that’s done, create your first Ionic app:

	$ ionic start cutePuppyPics

Add –type ionic1 if you’d like to use Ionic 1. To run your app, `cd` into the directory that was created and then run the `ionic serve` command to test your app right in the browser!

	$ cd cutePuppyPics
	$ ionic serve

### [Platform Guides](http://ionicframework.com/docs/intro/installation/#platform-guides)

For those building native apps for iOS and Android (most of you!), each platform has certain features and installation requirements before you can get the most out of your Ionic and Cordova development.

For iOS developers, take a look at the [Cordova iOS Platform Guide](https://cordova.apache.org/docs/en/latest/guide/platforms/ios/) and follow the instructions to install or upgrade Xcode, and possibly register for a developer account to start building apps for iOS.

For Android developers, take a look at the [Cordova Android Platform Guide](https://cordova.apache.org/docs/en/latest/guide/platforms/android/) and follow the instructions to install the SDK and/or Android Studio to start building apps for Android.