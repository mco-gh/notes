Screen.rip

 ![](../_resources/1cb06d059c55dc8ba037d145547b43a1.png)

# Screen.rip

## Programmable Screenshot API

 [Take 10,000 shots for $7](https://screen.rip/#get-token)  [Learn how to use](https://screen.rip/#how-to-use)

## How to use

### Use Screen.rip to build...

- ☺︎Auto-updating screenshots for landing pages and support articles

- ☺︎Side-by-side comparisons for A/B tests

- ☺︎Detect visual regressions

- ☺︎Reproduce customers' screen for support requests

- ☺︎Pair with [Page.REST](https://page.rest/) to build site galleries similar to Land-book

- ☺︎[ProductHunt style](https://twitter.com/chrismessina/status/917995061836689408) social sharing

Wanna see how it works? Play with the samples below. **Change the URLs to any site you like'.**

### Simple GET request

Making a GET request is the easiest way to take a screenshot. Provide the URL of the page as a query string.

curl  -X GET \
"https://screen.rip/capture?token=YOUR_TOKEN&url=https://producthunt.com"

### Clip part of the page

You can configure how to capture the screenshot. Pass the configuration options as a POST request.

In the example, we pass a CSS selector to clip the screenshot to capture only the tweet popup.

xxxxxxxxxx

curl  -X  POST \
-H  "Authorization: Bearer YOUR_TOKEN" \
-H  "Content-Type: application/json" \
-d  '{
 "url": "https://twitter.com/BarackObama/status/896523232098078720",
 "clip": ".permalink-tweet-container",
 "format": "jpg",
 "quality": 90
}' \
"https://screen.rip/capture"

### Run custom scripts

The API supports running a script before taking the screenshot.

In the example, we run a script to scroll to a specific section of the page and then highlight a paragraph of the article before taking the screenshot.

xxxxxxxxxx

curl  -X  POST \
-H  "Authorization: Bearer YOUR_TOKEN" \
-H  "Content-Type: application/json" \
-d  '{

 "url": "http://cosmos.nautil.us/short/138/if-you-cant-find-dark-matter-look-first-for-a-dark-force",

 "runjs": "window.scroll(0, 2200); var r = document.createRange(); var p = document.querySelector(\"article p:nth-of-type(4)\"); r.selectNode(p); window.getSelection().addRange(r);"

}' \
"https://screen.rip/capture"

### More options

- ❖Set cookies (capture pages behind logins)

- ❖Set custom HTTP Headers

- ❖Post data

- ❖Resize the viewport

- ❖Wait for an element to appear on the page

- ❖Capture full page screenshots

- ❖Export as PNG or JPG

Download the [Postman collection](https://app.getpostman.com/run-collection/161ef8394e0ba1330d62) for complete API examples.

*Screen.rip runs each request in a separate browser context and doesn't retain any data from a session.*

## Get a token

A token will be valid for 365 days. You can make 10,000 successful requests.

  Your name

  Email

  Credit or debit card
0123456789０１２３４５６７８９

Number4242 4242 4242 4242 4240MM / YY000000

Created by [Lakshan Perera](https://www.laktek.com/). Also, built [Page.REST](https://page.rest/)