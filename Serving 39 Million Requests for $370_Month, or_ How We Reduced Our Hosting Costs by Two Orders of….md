Serving 39 Million Requests for $370/Month, or: How We Reduced Our Hosting Costs by Two Orders of…

# Serving 39 Million Requests for $370/Month, or: How We Reduced Our Hosting Costs by Two Orders of Magnitude

When I joined Postlight as an engineer last year, my first task was a big one: Rewrite the Readability Parser API. For those unfamiliar with the Readability Parser, it was the API that powered the popular Readability read-it-later app, along with many other services and apps across the web. The Parser API accepted a link to any article on the internet, then returned a structured representation of that article — [extracting content from the chaos of the web](https://trackchanges.postlight.com/extracting-content-from-the-chaos-of-the-web-introducing-the-mercury-web-parser-e920a1db7f86). (What did Readability have to do with Postlight? That’s a different story.)

The reasons for the rewrite were threefold:

1. 1The groundbreaking Readability API had grown old and somewhat brittle over the years. Parsed results were stored in a database, which meant that this database had grown to store a massive slice of the internet. It was next to impossible to perform slightly complex queries, which meant we had very little idea what was happening with the API. It also meant that the API’s response wouldn’t contain updated results if the original article changed.

2. 2The service was originally written and maintained by people who were no longer with the company, and new engineers like me lacked the domain knowledge necessary to update or fix the API in any non-trivial way.

3. 3Last and probably most significantly, the *free* Readability API was costing the company roughly $10,000 per month.

The rewrite had a few goals:

1. 1Produce a functionally equivalent library that would return the same or better results than the original.

2. 2Write something well tested and extensible in a language that Postlight engineers could easily contribute to.

3. 3Reduce the $10,000 monthly cost.

For the language, we settled on JavaScript. Choosing JavaScript meant that our new library could, in theory, run on both the server and in the browser. Every engineer at Postlight has at least some web experience, so choosing JavaScript also meant that nearly every one of them could contribute to Mercury. (Readability was written in Python, and while many Postlight engineers write beautiful Python, it lacked the in-browser benefits.)

Finally, we focused on cost, and the answer here was simple. To drastically reduce our costs, we chose a serverless architecture running on [AWS Lambda](https://aws.amazon.com/lambda/) and [API Gateway](https://aws.amazon.com/api-gateway/), built and deployed using the [Serverless framework](http://serverless.com/).

Last October, we [released the Mercury Web Parser](https://trackchanges.postlight.com/extracting-content-from-the-chaos-of-the-web-introducing-the-mercury-web-parser-e920a1db7f86), and the results were astounding. Our costs dropped immediately, and today, Mercury Web Parser costs around $400 per month to operate — roughly two orders of magnitude less than the cost to operate the Readability API. (Your mileage and needs, of course, will vary. Our previous costs also included database expenses, which we chose to forego in our serverless setup, opting instead for short-term caching.)

Here’s a breakdown of how we did it.

### Step 1: Just Go Serverless

Adopting a serverless architecture will dramatically decrease the cost of most APIs, assuming you can meet the needs of your service in a serverless environment. I’ll say this again: **Simply moving to a serverless environment had the single greatest impact on reducing hosting costs.** After we’d made the switch, the hard work was done. Our extremely expensive operating costs immediately shrunk by two orders of magnitude. But, even after the initial serverless switch, there’s still room to cut down on costs.

If you don’t have any experience with Lambda, its pricing [breaks down](https://aws.amazon.com/lambda/pricing/) like so:

> The Lambda free tier includes 1M free requests per month and 400,000 GB-seconds of compute time per month. The memory size you choose for your Lambda functions determines how long they can run in the free tier. The Lambda free tier does not automatically expire at the end of your 12 month AWS Free Tier term, but is available to both existing and new AWS customers indefinitely.

When you’re looking to optimize costs on Lambda, the most important thing to note from the above (apart from the incredible fact that a function with less than 1 million short-running invocations per month is free indefinitely) is that the memory size allocated to your function determines the cost to run your function. That cost increases or decreases proportionally to the time it takes to execute your function.

(Note: GB-seconds is a calculation of function execution time per GB of memory allocated to your function. So, for example, if you invoke your function one time for 3 seconds, and you’ve allocated 1GB to that function, you’ve executed 3GB-seconds of compute time. If you decreased that allocation to 512MB and the execution time remained 3 seconds, you’d cut your compute time in half, to 1.5GB-seconds.)

This means you can reduce Lambda costs by either speeding up the time it takes to execute your function, lowering your memory allocation, or both. Since we were already feeling good about our execution speed, memory was the obvious first step.

### Step 2: Lower Your Memory Allocation

Memory allocations for Lambda functions range from 128MB to 1536MB. The process for lowering your Lambda costs is simple. Incrementally [decrease the](https://serverless.com/framework/docs/providers/aws/guide/functions#configuration)`[memorySize](https://serverless.com/framework/docs/providers/aws/guide/functions#configuration)`[allocation in your Serverless config](https://serverless.com/framework/docs/providers/aws/guide/functions#configuration) (if you’re not using Serverless, you can do this directly in your Lambda dashboard), deploy, and then keep an eye on your function’s latency (this requires setting up a CloudWatch dashboard for your function, which is a topic for another post). If our function’s latency didn’t show a significant change after a few hours, then a day, then a week, we’d keep our changes and enjoy the decreased costs.

Remember, each time you halve your function’s memory allocation, you’re roughly halving your Lambda costs. For example, according to the official [Lambda Pricing Calculator](https://s3.amazonaws.com/lambda-tools/pricing-calculator.html), 1 million invocations (excluding the free tier), running for an average of 2 seconds (not fast, not particularly slow), at 1GB of memory, would cost $33.54. Make that 512MB, and it’s $16.87. 256MB translates to $8.54.

For the Mercury Web Parser, we’re currently running our function at 256MB and all is well.

### Step 3: Cache Your API Gateway Responses

If it makes sense for your service, caching responses in API Gateway can significantly cut down your Lambda invocations. Mercury users, for example, often request results for the same articles. We pay around $14 a month for a 0.5GB API Gateway cache with a 1 hour TTL. In the last month, 52% (20.3MM out of 39MM) of our API requests were served from the cache, meaning less than half (18.7MM requests) required invoking our Lambda function. That $14 saves us around $240 a month in Lambda costs.

### A Note on Scaling

It may not be immediately obvious, but apart from cost savings, a serverless architecture can also come with a considerable decrease in maintenance, configuration, and complexity. Our API could be serving 1,000 requests or 100,000,000 requests using the same configuration, cache, and deploy methods.

Additionally, as the service scales out to handle more requests, costs don’t necessarily increase all that much. Remember that over half of our API requests can be served from our cache. So far, this percentage has only increased the more the API is used.

### Final Cost Breakdown

Our current costs for running the Mercury Web Parser API, after all of the optimizations above, look like this:

**API Gateway:**

- •Costs for Requests served: **$137** ($3.50 per million API calls received)
- •Cache: **$14**
- •Data Transfer Out: **$42** (This is calculated at a rate of $0.09/GB)

**Lambda**

- •Request costs: **$3**
- •Compute costs: **$174** (averaging 2.37s/invocation with a memory allocation of 256MB)

**Total cost: $370**

### Bullish on Serverless

Our experience with the serverless architecture (in particular using the Serverless framework with AWS) has been incredible. We’ve used Lambda for everything from parsing the web to writing Slack bots; from batch resizing hundreds of thousands of photos in parallel to batch transcoding hundreds of thousands of videos.

The more we use it, the more confident we are with the serverless approach to solving a lot of problems that [previously required a server](https://trackchanges.postlight.com/fat-static-and-happy-building-bloomberg-lens-8a458a10ed2a). To date, the Mercury Web Parser and the tools it powers have been the best validation of our decision to go serverless when possible.

> Sidenote: If you’d like to give Serverless a try but don’t want to > [> spend an hour configuring your environment](https://trackchanges.postlight.com/if-you-wish-to-write-javascript-from-scratch-you-must-first-create-the-universe-3d746049a4c4)> , try our > [> Serverless boilerplate](https://github.com/postlight/serverless-babel-starter)> , pre-packed with modern JavaScript transpiling, a sensible linter, and code formatting with > [> Prettier](https://github.com/prettier/prettier)> .

![](../_resources/e609fb0c189686777f715b2280788481.png)![1*UO5m91j-4IoVfZaNwPMdmQ.jpeg](../_resources/3c884f0f76ba35aada618828513b34fd.jpg)

Mercury Reader, a Chrome extension for a cleaner reading experience

### Mercury Web Parser in the Wild

At Postlight, we’ve used the Mercury Web Parser to power:

- •[Mercury AMP Converter](https://mercury.postlight.com/amp-converter/), a tool that makes any web site Google AMP-ready with one line of code.
- •[Mercury Reader](https://mercury.postlight.com/reader/), a Chrome extension used by over 1 million users that, with the click of a button, removes ads and distractions from articles, leaving only text and images for a beautiful reading view on any site.
- •[Bloomberg Lens](https://trackchanges.postlight.com/fat-static-and-happy-building-bloomberg-lens-8a458a10ed2a), a Chrome Extension and iOS Share Sheet application that presents related news, company data, and person information for any article on the web.

We’re also supporting thousands of developers who use Mercury every day to extract structured content from any article on the web. All of this, as I mentioned at the start, amounts to 39 million requests/month, and costs us just $370.

That’s a little less than 10 bucks for every million requests, and it can scale with no effort. We couldn’t be happier with those numbers.

![](../_resources/1fca0a197c17743493ef7da52454a6fa.png)

 ![Track-Changes-Logo-2-300x35-300x35.png](../_resources/8ef3e7202c53186abb3e557f7484232b.png)

#  Never miss an update

Sign up to the Track Changes newsletter

   Sign up