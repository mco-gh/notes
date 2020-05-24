AWS IAM Policies in a Nutshell

![AWS IAM Policies in a Nutshell](../_resources/2cfe7888f5bf99a587d898b38404a6fb.png)

# [Introduction](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#introduction)

In this post we're going to go through an explanation and tutorial of IAM policies. The long, deep, dark of AWS documentation can sometimes (understatement) overcomplicate concepts. In fact, it's so generally overly wordy and jumbled, and of course this is all my opinion, that it results in a ton of copy-paste mania.

I've tried my best to keep it brief and simple in order to reduce the pain that we'll all inevitably deal with while diving deep into docs. However, since it's such a wide topic, its still a bit longer than I wanted. I do have a nice tl;dr at the end though that will hopefully hit the pure basics and be useful as a reference.

Let's look at what we'll be covering:

## Table of Contents:

1. [Overview](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#overview)

2. [The Who aka "Principal"](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-principal)

3. [The What aka "Action"](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-action)

4. [The Which aka "Resource"](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-resource)

5. [The When aka "Condition"](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-condition)

6. ["Not" Versions in Policies](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#not-versions)

7. [Policies In A Nutshell and Code Block](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#policies-in-a-nutshell)

8. [Using Policies](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#policy-usage)

9. [Final Thoughts](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#final-thoughts)

# [Overview](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#overview)

In the beginning... there is the natural, general flow of working with IAM policies (of which I am guilty of):

1. develop app feature
2. deploy to AWS
3. realize you need IAM
4. get overwhelmed by docs
5. fall asleep trying to read the docs
6. begin copy and pasting example policies to fit your app
7. bashing your head and fingers against the keyboard until it works
Not a good pattern right?
So let's just break it all down into one simple statement.
What is an AWS IAM Policy?

**A set of rules that, under the correct `conditions`, define what `actions` the policy `principal` or holder can take to specified AWS `resources`.**

That still sounds a bit stiff. How about:
**Who can do what to which resources. When do we care?**
There we go. Let's break down the simple statement even more:

#### The "Who":

"Who" is trying to do stuff? This can be a User, Groups of users and "roles.".

The first two are self-explanatory. The last one is just allows us to let other things, like EC2 servers, become the "Who."

(We can also allow for [federated users](https://aws.amazon.com/iam/details/manage-federation/) to be the "who" but we won't dive into that.)

#### The "What":

"What" actions can the "Who" take? Run EC2 instances? Put objects to S3? Put logs to cloud watch?

#### The "Which":

"What" actions can the "Who" take on "Which" resources?

So the "Who" can put and get objects to S3? But to which S3 buckets? All of them? Only ones in us-east-1?

#### The "When":

When do we care? If the IP matches a certain range of IPs? If the date-time is before a particular day? If the AWS user's username includes the string "cheese"?

Let's translate our simple statement over to one that follows AWS's policy language now.

#### A Simple Policy Example:

	{
	  "Version": "2012-10-17",
	  "Id": "some-unique-id",
	  "Statement": {
	    "Sid": "1",
	    "Effect": "Allow",
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
	    "Action": [
	      "s3:PutObject",
	      "s3:Get*"
	    ],
	    "Resource": "arn:aws:s3:::kfc-bucket/*",
	    "Condition": {
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

`"Version"` - There's only two verisons - `2012-10-17` and `2008-10-17`. Always use the newest.

`"Id"` (optional) - Suggested to be a uuid. Required by some services, but not by many. We won't use this property in our examples.[*](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#id-footnote)

`"Statement"` - Remember: who can do what to which resources... and when. This is the meat of Policies. This can be one of those statements or an array of many.

*Everything else is inside of a statement.*

`"Sid"` (optional) - an ID for each of the individual statements. Optional and isn't even exposed in the IAM API, so we won't do cover this.[*](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#id-footnote)

`"Effect"` - Either `Allow` or `Deny`. If we used `Deny` in the above example, it would just flip the policy. We would deny the user `colonel` from getting and putting objects to the `kfc-bucket`. That would be sad.

`"Principal"` - The "Who." In this example we specify the ARN, Amazon Resource Name (unique AWS id of a resource), of the IAM user `colonel`.

`"Action"` - The "What." The two actions in our example are `s3:PutObject` and `s3:Get*`. They perform any action that begins with the characters `Get` (i.e. GetObject, GetBucket, etc) and put things to/from S3.

`"Resource"` - The "Which." Which resource they can do "what" to, is anything in the bucket `kfc-bucket`.

`"Condition"` - The conditions that must present for this policy to be relevant, is when the current date is greater than Feb 28, 2017 ([when US East 1 went down](https://aws.amazon.com/message/41926/)).

###### * - ID and SID are required by some services. If so, it will be specified in the docs specific to that service, i.e. SQS and SNS.

Even though there are a number of properties, 99% of the time will be spent on **"Principal"**, **"Action"**, **"Resource"** and **"Condition"**. Because of this, that will be our main focus.

Let's walk through these primary sections.

# [The "Who" aka `Principal`](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-principal)

For IAM Users and Roles, we just grab its ARN (found in the IAM console or returned in the CLI) and follow the format of:

`"Principal": {"AWS": "<ARN OF YOUR IAM USER OR ROLE BUT NOT GROUPS>"}`

So groups don't work. Kind of frustrating. I'm sure there's a good reason for it, but we'll talk about how to use policies on groups later on.

For AWS services:

	"Principal": {
	  "Service": "ec2.amazonaws.com"
	}

This allows an AWS service as the `Principal`. In this case our "who" is the EC2 service. Anytime we want another AWS resource to do something for us independently, we need to give it permissions i.e. a EC2 server putting objects to S3.

*Note: `ec2.amazonaws.com` is just AWS's "friendly" name to specify EC2 as a service.*

We can also use an array to specify multiple `Principal`s. For example:

	"Principal": {
	  "AWS": [
	    "<Arn of user 1>",
	    "<Arn of user 2>"
	  ]
	}

NOW. HUGE Gotcha. **If we're making and attaching policies to IAM users, groups and roles, the `principal` (or Who) isn't needed.** That's because when you attach a policy to an IAM user for example, the policy assumes that the user who we've attached the policy to is the `principal`.

But... why is there a `Principal` field then? Even though the majority of our policies are attached to IAM users, groups and roles, they're also used in places without these assumptions. The most common ones are: S3 buckets, Glacier, SNS, SQS and AWS Role Trust Policies.

In fact, if you've done anything with S3, you've seen the infamous "Bucket Policy." Those are just policies! And they're the type where we need to specify the principal. The main difference on those is that the only `resource` or "which" that they care about is the bucket the policy is on.

Before we move on, I mentioned that groups can't be specified as principals. Well, as we just mentioned, the `principal` is implied on IAM users and groups. Therefore, if we wanted a group to be the `principal`, just attach a policy to the group and the `principal` will be assumed to be the group. I bring this up just in case you try and specify a group ARN an on an S3 bucket policy, it won't work.

#### The "Who" Users vs The "Who" Resources

What's the difference between attaching a policy to an IAM user vs a resource like an S3 bucket?

The easiest way to explain the difference here is to use this analogy:

**If the policy is attached to the user, group or role it's like a permission slip. If it's attached to the resource, it's like a VIP list.**

If it's with the user, just imagine the user `colonel` walking around with a permission slip. He shows up to a resource, we'll call `kfc-bucket`, and requests objects. To determine permissions we look at the slip, and he gets the objects or doesn't. Since the slip is with the user, we don't need to know who it applies to, obviously it's for the user.

If it's with the resource, then imagine `colonel` walking around with nothing. Instead, the permission slip is on the `kfc-bucket`. When `colonel` shows up to the `kfc-bucket`, we check the permission slip on the bucket and that's where we determine if he gets the objects or not. Since the slip is with the resource, we need to know who is allowed in or not, therefore we need to specify the `principal`s.

#### AWS Roles and `Principal`s

Even though IAM users and groups imply a "who" on their permission policy, IAM roles do so only after we've specified the who via a "Trust Policy." Therefore, when creating a role we have to pass it these two separate policy documents:

1) The **"Trust Policy"** is a policy that does nothing more than state "who" can assume this role. Yes, they look exactly like normal policies.

2) The **Permissions Policy** is just what we've shown so far. "What" actions can the owner of this role take to "which" resources?

IF we're creating IAM roles in the console, guess what? We don't really worry about the first policy. Instead, when creating a role we select a service that will serve as the who:

![a-step-21.png](../_resources/4b7f7c18c5dec6e3e74a89c08324eb20.png)

This sets up that first "trust policy" document for us. Then we attach a policy to the role like we would a user or group.

For the CLI (or CloudFormation) however, we have to do both steps. Let's say we want to create a role for **AWS CodePipeline**. To do so we first need to create the role with the following "trust policy":

	{
	  "Version":"2012-10-17",
	  "Statement": {
	    "Effect":"Allow",
	    "Principal": {
	      "Service": "codepipeline.amazonaws.com"
	    },
	    "Action":"sts:AssumeRole"
	  }
	}

**This should look familiar because it's just another policy**. The differences are that it has the `principal` pointing to the CodePipeline service and allows the `action` of assuming a role. This points out the fact that to use a role, a service (i.e. CodePipeline) must have the permission to do so.

The CLI call for this would be:

	aws iam create-role --role-name CodePipelineExampleRole \
	--assume-role-policy-document '{"Version":"2012-10-17","Statement":{"Effect":"Allow","Principal":{"Service":"codepipeline.amazonaws.com"},"Action":"sts:AssumeRole"}}'

And NOW we can go about attaching policies for permissions like normal.

	aws iam put-role-policy --role-name CodePipelineExampleRole \
	--policy-name CodePipelineExamplePolicy \
	--policy-document file://some-policy.json

*note: you can pass json files to the CLI like above*
`some-policy.json` might be something like:

	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {
	      "Effect": "Allow",
	      "Action": [
	        "codebuild:BatchGetBuilds",
	        "codebuild:StartBuild"
	      ],
	      "Resource": "*"
	    },
	    // .. more policy statements
	  ]
	}

So **TL;DR** steps for roles:

1) Attach a trust policy - What service can assume this role? aka take the `action`  `sts:AssumeRole`

2) Attach the permissions policy - "What" actions can the owner of this role take to "which" resources?

### Making The "Who" aka `Principal` In a Nutshell (TL;DR)

**If we're attaching the policy to an IAM User or Group** - no action other than attaching the policy to said user or group is needed. The "Who" or `principal` is assumed to be the User or Group.

**If we're attaching the policy to a Resource** - like an S3 bucket, the "Who" or `principal` needs to be specified. It can be ARNs of users, roles; AWS services like `ec2.amazon.com`; or even other AWS Accounts.

**If we're attaching the policy to a Role** - we specify the "Who" or `principal` by attaching a "trust policy" that says who can assume the role. From there we attach the normal permission policies, WITHOUT a `principal`, and the "Who" is determined by the trust policy.

# [The "What" aka `Action`](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-action)

What can our `principal` do? We've already seen some of the actions in action (ha). From our original example:

	{
	  "Version": "2012-10-17",
	  "Statement": {
	    "Effect": "Allow",
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
	    "Action": [
	      "s3:PutObject",
	      "s3:Get*"
	    ],
	    "Resource": "arn:aws:s3:::kfc-bucket/*",
	    "Condition": {
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

The actions are any action that begins with `Get` and `PutObjects` with respect to S3.

The format of `action` is a string or array of actions that take the format of:
`<service>:<action in service>`
Examples are:

	"Action": [
	  "codecommit:GetBranch",
	  "s3:GetObject",
	  "lambda:InvokeFunction"
	]

Actions like the above specify exact actions the policy refers to.
Some examples using the wildcard character:

	"Action": [
	  "ec2:*",
	  "s3:Get*",
	  "cloudformation:*",
	]

In these, the wildcard represents anything. So for the `s3:Get*` that would apply to any action that begins with the string `Get`.

This is where it can be a bit overwhelming. Where do you find all of these actions? How do you know what you're policy needs?? There's so many!

To answer the first question, use this link:

[List of all actions by services](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actionsconditions.html)

Once on this list, select the service your interested in getting `action`s for. At the top of the page there will be an "Actions for ." This is a list of all `action`s that can be used in IAM Policies.

For the second question, this is dependent upon your application, infrastructure and specific needs. What actions are needed specifically? To be completely honest, this is going to take some diligence, trial and error until you become more familiar with the relationships between actions.

### Making The "What" aka `Actions` in Nutshell (TL;DR)

1. Figure out what actions are needed for your services.

2. Find the exact name of these actions and add them to the `Action` section. [Use this link to ID the actions](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actionsconditions.html)

3. If unsure of what the needs are and have a safe AWS development environment, keep the actions general (via the wildcard * operator) and then cherry pick the ones you need when the service is fully built.

# [The "Which" aka `Resource`](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-resource)

Which `Resource` can our `Principal` take `Action` on? It's our target. The most general target of all is just:

`"Resource": "*"`

This means everything. Apply this to EVERYTHING. And obviously that's not good. Maybe we want to make it for just EC2 services in US East 1:

`"Resource": "arn:aws:ec2:us-east-1::*"`
Maybe we want it for an exact S3 bucket:
`"Resource": "arn:aws:s3:us-east-1:111222333444:kfc-bucket"`

This would map to the bucket `kfc-bucket` that is in `us-east-1` belonging to the AWS Account with an ID of `111222333444`.

Maybe we want any S3 bucket or Ec2 resource in US West 2:

	"Resource": [
	  "arn:aws:ec2:us-west-2::*",
	  "arn:aws:s3:us-west-2::*"
	]

* * *

Quick aside - the anatomy of an ARN, Amazon Resource Name, is as follows
`arn:aws:[service]:[region]:[account]:resourceType/resourcePath  `

* * *

We can also leverage the concept of `Policy Variables` to make these ARNs even more dynamic. Suppose we want to allow get/put to a folder named after the current IAM user in a bucket called `userbucket`:

	{
	  "Version": "2012-10-17",
	  "Statement": [
	    {
	      "Action": [
	        "s3:GetObject",
	        "s3:PutObject"
	      ],
	      "Effect": "Allow",
	      "Resource": "arn:aws:s3:::userbucket/${aws:username}/*"
	    }
	  ]
	}

The `${aws:username}`, and all policy variables, are data that are sent up with requests. There's a variety of them like `aws:CurrentTime` or `aws:SourceIp`. A full list is here:

[Policy Variables List](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-infotouse)

A note on `resource` in context of S3. IAM policies can imply the "who" or the `prinicpal` when we attach a policy to them. One might think that a bucket would imply the `resource` be itself. However, it doesn't. When attaching a policy to an S3 bucket (aka bucket policy), we must still specify the resource, which is always the S3 bucket optionally followed by nested folders/objects within.

#### Making The "Which" aka `Resource` in a Nutshell (TL;DR)

Get the ARN or ARNs that you'd like the policy to apply to and specify them in the `Resource` property. Leverage wildcards and [policy variables](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-infotouse) to target more general sets of resources.

# [The "When" aka `Condition`](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#the-condition)

"When" can our `Prinicpal` take `actions` on a `resource`? When `conditions` permit.

In our original example, we applied a `condition` of time:

	{
	  "Version": "2012-10-17",
	  "Statement": {
	    "Effect": "Allow",
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
	    "Action": [
	      "s3:PutObject",
	      "s3:Get*"
	    ],
	    "Resource": "arn:aws:s3:::kfc-bucket/*",
	    "Condition": {
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

If the date is greater than Feb 28, 2017, then this policy is then relevant. If the date is before our specified time, then this policy isn't applicable. So before Feb 28, our `colonel` can't access his bucket. Assuming no us-east-1 outage, `colonel` will be able to access his bucket on the day of the time specified.

The format of a `condition` is:

	"Condition": {
	  "<Condition Operator>": {
	    "<Condition Key>": "<Condition Value>"
	  }
	}

In plain english:

	"Condition": {
	  "<What's the comparison we're making?>": {
	    "<Value being passed in the request>": "<Value to compare against>"
	  }
	}

Let's step through each of the special keys and values in the condition block.

#### Condition Operators

What comparison are we making? A string comparison? An IP comparison? A username comparison? Each of these have a special operator.

Example of locking down an S3 Bucket to an IP address via conditions:

	{
	  "Version": "2012-10-17",
	  "Statement": {
	    "Effect": "Allow",
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
	    "Action": [
	      "s3:*"
	    ],
	    "Resource": "arn:aws:s3:::kfc-bucket/*",
	    "Condition": {
	      "IpAddress": {
	        "aws:SourceIp": "123.456.789.000/32"
	      },
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

The `condition operators` in this example are `IpAddress` and `DateGreaterThan`. Now `colonel` can only access his bucket both at a certain time and from a certain IP address. This shows that multiple conditions can be used as well.

[A list of condition operators to be used can be found here.](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AccessPolicyLanguage_ConditionType)

#### Condition Keys

These are the AWS ready values about the current request trying to pass the policy. When a request comes through, AWS makes a variety of these "keys" available for use within our policies.

We saw two above `aws:SourceIp` and `aws:CurrentTime` - and as mentioned in the `Resource` section, these are also known as `Policy Variables`. I say "also" because when using `aws:SourceIp` in a `Resource` or a `Condition Value`, the documentation refers to it as a `Policy Variable`. When something like `aws:SourceIp` is used in in a `Condition Key`, it's just called a Condition Key.

There are a set of general condition keys / policy variables that are globally available. This list can be found here:

[Link to AWS Global Condition Keys](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#AvailableKeys)

And then of course we can see the exact same list for `Policy Variables` that we also listed above here:

[Policy Variables List](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_variables.html#policy-vars-infotouse)

As we can see, they're the same.

Are there more? You betcha. There's a set available to each service we can use. For example we could do something like:

	{
	  "Version":"2012-10-17",
	  "Statement":[
	    {
	      "Effect": "Allow",
	      "Action": "ec2:*",
	      "Resource": "*",
	      "Condition": {
	        "StringEquals": {
	          "ec2:Region": "us-east-1"
	        },
	        "ArnEquals": {
	          "ec2:Vpc": "ARN of VPC"
	        }
	      }
	    }
	  ]
	}

This says that we can perform any actions on EC2 resources, but only in the `us-east-1` region and only if they reside in a particular virtual private cloud (VPC). The keys `ec2:Region` and `ec2:Vpc` are specific to to requests dealing with EC2.

How do we find these condition keys for each service?

1. [Go to this list (listed above as well)](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actionsconditions.html)

2. Select the service of interest
3. Scroll down to the **"Condition context keys for "**

If there are condition keys available, they'll be listed at the bottom of the service's page.

#### Condition Values

This is simply the value that we're looking to compare against. So in this example:

	{
	  "Version": "2012-10-17",
	  "Statement": {
	    "Effect": "Allow",
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
	    "Action": [
	      "s3:*"
	    ],
	    "Resource": "arn:aws:s3:::kfc-bucket/*",
	    "Condition": {
	      "IpAddress": {
	        "aws:SourceIp": "123.456.789.000/32"
	      },
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

Our condition values are the specific IP address and the time stamp. We have to decide what those values will be.

The only real note here is that within these values we can also use `Policy Variables`, the wildcard character (*) to denote any string and the question mark (?) to denote any one character.

An example of all of these together:

	{
	  "Condition": {
	    "ArnEquals": {
	      "ec2:Vpc": "arn:aws:ec2:us-east-?::vpc/*"
	    },
	    "StringLike": {
	      "ec2:ResourceTag/name": "*-${aws:username}"
	    }
	  }
	}

This says any VPC in any of the `us-east` based regions AND if it has a tag that matches anything with the current users name at the end.

#### Making The "When" aka `Condition`s in a Nutshell (TL;DR)

Decide if the policy should only apply under certain conditions.
If so...

**1)**  [Use this link about condition operators](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/(http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AccessPolicyLanguage_ConditionType)) to select the conditions what the policy should check for. These are `condition operators`.

**2)** Decide what piece of information about the current request you'd like to check. This is the `condition key`. [Use this link about global condition keys](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys) to pick the global pieces of information on a request you'd like to check against.

If you need to check against pieces of information specific to a service, navigate to [this link that shows all of the different service condition keys and contexts](http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actionsconditions.html). Select the service of interest. Scroll to the bottom. Select the piece of information you'd like to check against.

**3)** Finally input the value, or `condition value`, to compare against the `condition key`.

# [`Not` Versions of Policies](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#not-versions)

`Resource`, `Action` and `Principal` have a reverse:
`NotResource`
`NotAction`
`NotPrincipal`

As you might suspect, they just specify what it does NOT apply to. There's some gotchas surrounding `Not`s though, so unless it's really needed, stick to the positive version. For example, if we've specified that we can NOT take action on resources that are NOT "example resource," what's the expected outcome? That we can access it? Nope it's just specified that we aren't not allowed to act on it. But we still need to be allowed to do it....

... yes it's confusing. So again, just stick with positives if possible. The stated benefit of using `Not`s is that they "can sometimes make policies shorter."

Don't get too hung up on the negative versions, everything can be done with positives, at the cost of potentially being a bit more verbose. When it comes to security though, that's probably a good thing.

# [Policies In A Nutshell and Code Block](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#policies-in-a-nutshell)

An IAM policy:

**A set of rules that, under the correct `conditions`, define what `actions` the policy `principal` or holder can take to specified AWS `resources`.**

Or more simply put:
**Who can do what to which resources. When do we care?**
Example policy:

	{
	  "Version": "2012-10-17",
	  "Statement": {
	    "Effect": "Allow",
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},
	    "Action": [
	      "s3:PutObject",
	      "s3:Get*"
	    ],
	    "Resource": "arn:aws:s3:::kfc-bucket/*",
	    "Condition": {
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

Outline of the example policy:

	{
	  // Version of the policy language to use.  Just use 2012-10-17.
	  "Version": "2012-10-17",
	  "Statement": {
	    // Allow or Deny.  Flips the policy to do "Deny" whatever is
	    // specified if set to deny.
	    "Effect": "Allow",

	    // The "Who."  Who is this policy relevant to?
	    //
	    // If it's on an IAM user or group, we don't need to
	    // specify this because it's implied.  It's like a permission
	    // slip that the user / group carries around.
	    //
	    // If it's on a resource, like an S3 bucket, we do need
	    // to specify it.  In this case, it's like a VIP list that
	    // says who can take the actions on the target resource.
	    //
	    // If it's on an IAM role, we need to specify the
	    // principal in a separate "trust policy" document.
	    "Principal": {"AWS": "arn:aws:iam::111222333444:user/colonel"},

	    // The "What."  What can our Principal do?
	    //
	    // Fill this with a list of actions needed by your principal.
	    //
	    // 1. Find all the actions here:
	    //    http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actionsconditions.html
	    //
	    // 2. Navigate to the service of interest to find a list of actions
	    //    that can be specified for that service.
	    "Action": [
	      "s3:PutObject",
	      // wildcard means any combo of characters.  So GetObject, GetBucket, etc.
	      // would apply to the following action
	      "s3:Get*"
	    ],

	    // The "Which."  Which resources can our Principal take action on?
	    //
	    // 1. If the resource is already created, than just grab the ARN
	    // 2. If you want to apply them to an entire service, make use of wildcards
	    //    and policy variables
	    //
	    // For reference, the anatomy of an Amazon Resource Name is:
	    // arn:aws:[service]:[region]:[account]:resourceType/resourcePath
	    //
	    // Where for if service, region or account are irrelevant, you can just
	    // collapse them like below.
	    "Resource": "arn:aws:s3:::kfc-bucket/*",

	    // The "When."  When does this policy apply?
	    //
	    // 1. Pick what "condition operator", this policy cares about.
	    //    In this example, that's `DateGreaterThan`.  A link to global ones:
	    //
	    //     http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AccessPolicyLanguage_ConditionType
	    //
	    // 2. Decide what piece of the incoming request you'd like to look at.
	    //    This is the "condition key".  In this example, it's `aws:CurrentTime`.
	    //    This represents the current time of the incoming request.
	    //    A list of condition keys:
	    //
	    //    http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements.html#AvailableKeys
	    //
	    //    More are available for each service under this link:
	    //    http://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_actionsconditions.html
	    //    And then follow through to the service of interest.
	    //
	    //  3. Pick the value of to compare against.  In this example it's Feb 28 2017.
	    "Condition": {
	      "DateGreaterThan": {
	        "aws:CurrentTime": "2017-02-28T00:00:00Z"
	      }
	    }
	  }
	}

# [Using Policies](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#policy-usage)

So we understand the anatomy of a policy, but what about using it? While we're not going to dive into that in this article, using policies is a cinch.

The workflow is conceptually straight forward:
**a)** create the policy
**b)** attach it to a user, group, role or resource.

In fact, the majority of tutorials out there have you just select from AWS's large set of pre-made policies! Depending on the nature of your infrastructure or application you may as well be able to get away with using many of the pre-made policies. As needs become more specific though you will have to create your own. The pre-made ones are great references though.

For IAM Users, Groups and Roles, you'll create your policy and then simply attach it to one of the three. The CLI experience obviously requires some different steps, but the concept is still same.

For Resources like S3 Buckets, you'll directly attach policies generally in that service's API or console interface.

# [Final Thoughts](http://start.jcolemorrison.com/aws-iam-policies-in-a-nutshell/#final-thoughts)

The goal of the post is just to get a grasp on the anatomy of an IAM policy. The difficulty with policies isn't really the concept or the anatomy. Instead, it's the overwhelming number of possible actions, principals, resources and conditions that we can insert into them. Additionally the "context" of the policies (i.e. using them on an S3 bucket vs an IAM user) also changes what can be inserted into them.

The path to really understanding these is going to come piecemeal as experience is built with each individual service. The first step is definitely learning this anatomy and the basic concepts. The second step is going to be familiarizing yourself with all of the actions and conditions for services that you're applying policies too. The third step will just be tinkering around to understand the gotchas and edge-cases for each.

My absolute final primary word of advice though is: *begin with the end in mind*. Literally ask yourself and team: Who can do what to which resources. When do we care? List those out in a pseudo code or just plain language. And then seek out, using the resources defined above, to create a policy that fulfills the answer to your question. (Oh, and test it).

* * *

As usual, if you find any technical glitches or hiccups PLEASE leave a comment or hit me up on twitter or with a message!

Be sure to signup for weekly updates!!

* * *

*More from the blog*

- [Build and Deploy a Node API and React Web App on AWS](http://start.jcolemorrison.com/build-deploy-node-react-on-aws/)
- [Docker for a Fresh MySQL or MongoDB Instance in Any Project](http://start.jcolemorrison.com/docker-fresh-mysql-or-mongodb-instances-in-projects/)
- [Guide to Fault Tolerant and Load Balanced AWS Docker Deployment on ECS](http://start.jcolemorrison.com/guide-to-fault-tolerant-and-load-balanced-aws-docker-deployment-on-ecs/)
- [React and Redux Sagas Authentication App Tutorial](http://start.jcolemorrison.com/react-and-redux-sagas-authentication-app-tutorial/)