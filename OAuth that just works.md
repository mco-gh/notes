OAuth that just works.

![oauth.io](../_resources/67006a2215ff84c0a9e4008fa70d7b67.png)

![oauth.io](../_resources/9bc03f7b818dd37d007c54cacc621467.png)

![oauth.io](../_resources/642d558f9cb8395909ca05f472696f66.png)

![oauth.io](../_resources/e55f06c8ea5ad335afa2aff0d0e9a1f1.png)

![oauth.io](../_resources/2c460c8bed15ebe6b493515be46b24ad.png)

![oauth.io](../_resources/95760b54a8807d58467c4be6966cadab.png)

YOUR APP

# Forget OAuth complexity.

[Go to my Dashboard](https://oauth.io/dashboard)

## Features

![](../_resources/791b22ee8cea795295d741328d599a51.png)
[OAuth Integration](https://oauth.io/home/api_integration)
![](../_resources/cac75bff7aa08a754a6c4f0a534906f8.png)
[User Management](https://oauth.io/home/user_management)
![](../_resources/889bea426f0e4c8abeb2fee21b16d444.png)
[OAuth Providing](https://oauth.io/home/oauth_server)

### OAuth Integration

#### Access your user's resources in 5 lines

**
 Integrate OAuth in **90 seconds**
**
 **100+ API** providers available
**

 SDKs available for **JavaScript**, **NodeJS**,**PHP**, **iOS**, **Android**, **Phonegap**

**
 Easy integration management in your **OAuth.io dashboard**
OAuth.popup('facebook').then((facebook) => {
return facebook.me()
}).then((me) => {
console.log('Your name is ' + me.name)
}).catch((error) => {
console.error(error)
})
![](../_resources/d23bc042fce63b65f91855e251f756d4.png)
![](../_resources/a125d011be26651e60ec4d277d4c71d8.png)
![](../_resources/eb622549c93d0c8a6167ec7ff25d2ec3.png)
![](../_resources/6f03e15211282d788a168f55883f4be9.png)
![](../_resources/bfa40a29570ecfd1c6c16dd852b7a3a6.png)
![](../_resources/816e5a71e66ee490015cc66b4c892f34.png)

[^ Back to top ^](https://oauth.io/home)

### User Management

![](../_resources/793af66a7181a90a518ed4b9c39d1b7e.png)
![](../_resources/752a229df8c3d8c396ea7e30e2d650e9.png)
![](../_resources/5e147bd48c3a48cb0496789daf68414c.png)
![](../_resources/5e147bd48c3a48cb0496789daf68414c.png)
![](../_resources/5e147bd48c3a48cb0496789daf68414c.png)

#### Simplified User Management

**
 Simplified **social signin / signup** with our SDK
**
 Use any of our **100+ providers** for your user management
**
 Your user base safely curated by **StormPath**
User.signin(email, password).done((user) => {
console.log(user.data.firstname);
}).fail((err) => {
// email/password incorrect.
});

[^ Back to top ^](https://oauth.io/home)

### OAuth Server

#### Become the provider

**
 Easily add an **OAuth 2.0 layer** on your existing API
**
 **Become a platform** and let developers build apps over your service
**
 Either choose **OAuth.io as your developer portal** or create your own
**
 Your service **automatically available in OAuth.io**
app.get('/me', **OAuthProvider.OAuth2.check()**, (req, res, next) => {
let user = req.session.user,
response
delete user.password
if (**req.OAuth2.scope['user_info']**) {
response = user
}
else {
response = {
error: 'Access not permitted by user'
}
}
res.send(response)
});
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/aa28f928df4ed0e858984410fddf87a2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)
![](../_resources/9d5ba4ce83ca511212a91a15a4c21db2.png)

[^ Back to top ^](https://oauth.io/home)

### Subscription & Pricing

####

No credit card required to signup

### OAuth Integration & User Management plans

$ 19
/mth
**20,000** API calls / mth
Support type: Emails
$ 99
/mth
**400,000** API calls / mth
Support type: Priority emails
$ 299
/mth
**8,000,000** API calls / mth
Support type: Priority emails

### OAuth Server - Become an OAuth Provider

##### Try it for free, [contact us](https://oauth.io/mailto:support@oauth.io) for more.

[Manage my plans](https://oauth.io/dashboard/my-plans)[Go to my dashboard](https://oauth.io/dashboard)