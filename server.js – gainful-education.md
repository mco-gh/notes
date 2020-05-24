server.js – gainful-education

# server.js – gainful-education

Show
Live

22
const express = require('express'),
app = express(),
puppeteer = require('puppeteer');
​
app.get("/", async (request, response) => {
try {
const browser = await puppeteer.launch({
args: ['--no-sandbox']
});
const page = await browser.newPage();
await page.goto('https://developers.google.com/');
await page.screenshot({path: 'puppeteer.png'});
await browser.close();
response.sendFile('/app/puppeteer.png');
} catch (error) {
response.status(503).end(error.message);
}
});
​
var listener = app.listen(process.env.PORT, function () {
console.log('Your app is listening on port ' + listener.address().port);
});