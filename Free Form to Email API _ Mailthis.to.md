Free Form to Email API | Mailthis.to

 ![](../_resources/5ed4b39f43cfdbc913822b022f293def.png)

## Quickstart

Post any HTML form to .

You will receive a request from us to verify your email. Once you verify your email, you will begin to receive messages from your MailThis.to form submissions. You are protected from spam with Recaptcha.

* * *

 ![](../_resources/7e426f89688c63a6d9a8a7bf6fbebe13.png)

## Full API Guide

### 1. Create an Email Alias (recommended)

Register a username to use in place of your email address when building forms, to reduce spam.

 **Enter your Email Address:**
 **Enter your Desired Alias:**

 ![](../_resources/613606a1e0383598f74410471b2b5937.png)

### 2. Build your form

Create an HTML form which posts data to the Mailthis.to API.

1
2
3
4
5
6
7
8
9
10
11
12
13

<form  action="https://mailthis.to/you@mail.com"
 method="POST"  encType="multipart/form-data">
 <input  type="text"  name="name"  placeholder="Your name">
 <input  type="email"  name="_replyto"  placeholder="Your email">
 <textarea  name="message"  placeholder="Enter your message here"></textarea>
 <input  type="file"  name="file"  placeholder="Attachments (optional)">
 <input  type="hidden"  name="_subject"  value="Contact form submitted">
 <input  type="hidden"  name="_after"  value="https://myhomepage.net/">
 <input  type="hidden"  name="_honeypot"  value="">
 <input  type="hidden"  name="_confirmation"  value="">
 <input  type="submit"  value="Send">
</form>

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 ![](../_resources/10123164eb3d08409260c94d0061c835.png)

### 3. Use advanced fields (optional)

 **_subject**
This allows you to specify a custom subject for your email message.
 **_replyto**
This allows you to specify a custom reply-to field for your email message.
 **_after**

This allows you to specify a redirect URL to send users to after they send a message.

 **_honeypot**

This is a special field which acts as a form of SPAM protection. This hidden field will not be shown to regular visitors, but most SPAM bots will automatically enter a value into this field. If Mailthis.to detects a value, the data is considered SPAM and won't be processed (no email will get sent).

 **File uploads**

Simply add a file upload, switch your form to **encType="multipart/form-data"** and you will receive the file as an attachment.

 **_confirmation**

Set a custom confirmation message shown to the user after successfully submitting the form.

### 4. Example using AJAX (advanced)

You can also use AJAX to send email, without an HTML form. However, in order to prevent spam, your users will need to complete recaptcha after your request is completed.

To do this, redirect your users to after your request has completed.

[See an Example](https://gist.github.com/kidGodzilla/bdd453129a1e30ac9d86b9fd7b412ca8)