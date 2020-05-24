Web Scraping with Go

# Web Scraping with Go

## Overview

## Introduction

Web scraping ([Wikipedia entry](https://en.wikipedia.org/wiki/Web_scraping)) is a handy tool to have in your arsenal. It can be useful in a variety of situations, like when a website does not provide an API, or you need to parse and extract web content programmatically. This tutorial walks through using the standard library to perform a variety of tasks like making requests, changing headers, setting cookies, using regular expressions, and parsing URLs. It also covers the basics of the **goquery** package (a jQuery like tool) to scrape information from an HTML web page on the internet.

If you need to reverse engineering a web application based on the network traffic, it may also be helpful to learn how to do [packet capture, injection, and analysis with Gopacket](https://www.devdungeon.com/content/packet-capture-injection-and-analysis-gopacket).

If you are downloading and storing content from a site you scrape, you may be interested in [working with files in Go](https://www.devdungeon.com/content/working-files-go).

## Ethics and guidelines of scraping

Before doing any web scraping, it is important to understand what you are doing technically. If you use this information irresponsibly, you could potentially cause a denial-of-service, incur bandwidth costs to yourself or the website provider, overload log files, or otherwise stress computing resources. If you are unsure of the repercussions of your actions, do not perform any scraping without consulting a knowledgable person. You are responsible for the actions you take including any cost or repercussion that comes along with it.

When doing any scraping or crawling, you should be considerate of the server owners and use good rate limiting, prevent overloading a single site, and use reasonable settings and limits.

It is important to understand that some sites have terms of service that do not allow scraping. While you might not face legal problems, they could ban your account if you have one, block your IP address, or otherwise revoke your access to the website or service. Before scraping any site, find out if there are any rules or guidelines explicitly stated in the terms of service.

Also keep in mind that some websites do provide APIs. Check to see if an API is avaiable before scraping. If a website or service provides an API, you should use that. APIs are intended to be used programmatically and are also much more efficient.

## Prerequisites

- [Go](https://golang.org/) - The Go programming language (tested with 1.6)

- [goquery](https://github.com/PuerkitoBio/goquery) (for some examples) - Go version of jQuery for DOM parsing

The only dependency, other than Go itself, is the goquery package. Goquery is not needed for every example, as the majority of examples rely only on the standard library. To install the **goquery** dependency, use **go get**:

`go get github.com/PuerkitoBio/goquery`

If you have issues with your $GOPATH when using **go get**, be sure to read up about [Workspaces](https://golang.org/doc/code.html#Workspaces) and [the GOPATH environment variable](https://golang.org/doc/code.html#GOPATH) and make sure you have a **GOPATH** set.

## Make an HTTP GET request

The first step to web scraping is being able to make an HTTP request. Let's look a very basic HTTP GET request and how to check the response code and view the content. Note the default timeout of an HTTP request using the default **transport** is forever.

`// make_http_request.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"io"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"os"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Make HTTP GET request[[NEWLINE]]    response, err := http.Get("https://www.devdungeon.com/")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Copy data from the response to standard output[[NEWLINE]]    n, err := io.Copy(os.Stdout, response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]log.Println("Number of bytes copied to STDOUT:", n)[[NEWLINE]]}`

## Make an HTTP GET request with timeout

When using **http.Get()** to make a request, it uses the default HTTP client with default settings. If you want to override the settings you need to create your own client and use that to make the request. This example demonstrates how to create an **http.Client** and use it to make a request.

`// make_http_request_with_timeout.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"io"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"os"[[NEWLINE]]"time"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Create HTTP client with timeout[[NEWLINE]]    client :=&http.Client{[[NEWLINE]]Timeout:30* time.Second,[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Make request[[NEWLINE]]    response, err := client.Get("https://www.devdungeon.com/")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Copy data from the response to standard output[[NEWLINE]]    n, err := io.Copy(os.Stdout, response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]log.Println("Number of bytes copied to STDOUT:", n)[[NEWLINE]]}`

## Set HTTP headers (Change user agent)

In the first example we saw how to use the default HTTP client to make a request. Then we saw how to create out own client so we could customize the settings, like the timeout. Similarly, the HTTP clients use a default **Request** type which we can also customize. This example will walk through creating a request and modifying the headers before sending.

I highly recommed being a good net citizen and providing a descriptive user agent with a string that is easily parsable with a regular expression and contains a link to a website or GitHub repo so a network admin can learn about what the bot is and rate limit or block your bot if it causes problems.

`# Example of a decent bot user agent[[NEWLINE]]MyScraperBot v1.0 https://www.github.com/username/MyNanoBot - This bot does x, y, z`

Another reason to change your user agent might be to impersonate a different user agent. The default Go user agent may get blocked and you might have to impersonate a Firefox browser. It can also be useful for testing applications to see how they behave when various mobile and desktop user agents are presented.

This example will demonstrate how to change the HTTP headers before sending your request. To set your user agent, you will need to add/override the User-Agent header. Note you can change any header this way, including your cookies, if you wanted to manually manage them. We'll talk more about the cookies later. This only requires the standard library.

`// http_request_change_headers.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"io"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"os"[[NEWLINE]]"time"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Create HTTP client with timeout[[NEWLINE]]    client :=&http.Client{[[NEWLINE]]Timeout:30* time.Second,[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Create and modify HTTP request before sending[[NEWLINE]]    request, err := http.NewRequest("GET","https://www.devdungeon.com",nil)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    request.Header.Set("User-Agent","Not Firefox")[[NEWLINE]][[NEWLINE]]// Make request[[NEWLINE]]    response, err := client.Do(request)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Copy data from the response to standard output[[NEWLINE]]    _, err = io.Copy(os.Stdout, response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]}`

## Download a URL

You may want to simply download the contents of a page and store it for offline review at a later date, or download a binary file after determining what URL contains the file you want. This example demonstrates how to make an HTTP request and stream the contents to a file. This only requires the standard library.

`// download_url.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"io"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"os"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Make request[[NEWLINE]]    response, err := http.Get("https://www.devdungeon.com/archive")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Create output file[[NEWLINE]]    outFile, err := os.Create("output.html")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer outFile.Close()[[NEWLINE]][[NEWLINE]]// Copy data from HTTP response to file[[NEWLINE]]    _, err = io.Copy(outFile, response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]}`

## Use substring matching to find page title

Probably the simplest way to search for something in an HTML document is to do a regular substring match. You will need to first convert the response in to a string and then use the **strings** package in the standard library to do substring searches. This is not my preferred way of searching for things, but it can be viable depending on what you are looking for. It is definitely worth knowing and understanding this technique in case you want to use it. Thanks [xiegeo](https://www.reddit.com/r/golang/comments/86xrek/web_scraping_with_go/dw9i8yb/) for reminding me to include this section.

Next we will look at using regular expressions, which are even more powerful than simple substring matches. After that, we'll look at using the **goquery** package to parse the HTML DOM and look for data in a structured way using jQuery like syntax.

`// substring_matching.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"fmt"[[NEWLINE]]"io/ioutil"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"os"[[NEWLINE]]"strings"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Make HTTP GET request[[NEWLINE]]    response, err := http.Get("https://www.devdungeon.com/")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Get the response body as a string[[NEWLINE]]    dataInBytes, err := ioutil.ReadAll(response.Body)[[NEWLINE]]    pageContent :=string(dataInBytes)[[NEWLINE]][[NEWLINE]]// Find a substr[[NEWLINE]]    titleStartIndex := strings.Index(pageContent,"<title>")[[NEWLINE]]if titleStartIndex ==-1{[[NEWLINE]]        fmt.Println("No title element found")[[NEWLINE]]        os.Exit(0)[[NEWLINE]]}[[NEWLINE]]// The start index of the title is the index of the first[[NEWLINE]]// character, the < symbol. We don't want to include[[NEWLINE]]// <title> as part of the final value, so let's offset[[NEWLINE]]// the index by the number of characers in <title>[[NEWLINE]]    titleStartIndex +=7[[NEWLINE]][[NEWLINE]]// Find the index of the closing tag[[NEWLINE]]    titleEndIndex := strings.Index(pageContent,"</title>")[[NEWLINE]]if titleEndIndex ==-1{[[NEWLINE]]        fmt.Println("No closing tag for title found.")[[NEWLINE]]        os.Exit(0)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// (Optional)[[NEWLINE]]// Copy the substring in to a separate variable so the[[NEWLINE]]// variables with the full document data can be garbage collected[[NEWLINE]]    pageTitle :=[]byte(pageContent[titleStartIndex:titleEndIndex])[[NEWLINE]][[NEWLINE]]// Print out the result[[NEWLINE]]    fmt.Printf("Page title: %s\n", pageTitle)[[NEWLINE]]}`

## Use regular expressions to find HTML comments

Regular expressions are a powerful way of searching for text patterns. I am providing one example of using regular expressions for reference, but I do not recommend using this method unless you have no other choice. In the next examples, I will look at using goquery, an easier way of finding data in a structured HTML document.

`// find_html_comments_with_regex.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"fmt"[[NEWLINE]]"io/ioutil"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"regexp"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Make HTTP request[[NEWLINE]]    response, err := http.Get("https://www.devdungeon.com")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Read response data in to memory[[NEWLINE]]    body, err := ioutil.ReadAll(response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal("Error reading HTTP body. ", err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Create a regular expression to find comments[[NEWLINE]]    re := regexp.MustCompile("<!--(.|\n)*?-->")[[NEWLINE]]    comments := re.FindAllString(string(body),-1)[[NEWLINE]]if comments ==nil{[[NEWLINE]]        fmt.Println("No matches.")[[NEWLINE]]}else{[[NEWLINE]]for _, comment := range comments {[[NEWLINE]]            fmt.Println(comment)[[NEWLINE]]}[[NEWLINE]]}[[NEWLINE]]}`

## Use goquery to find all links on a page

This example will make use of the goquery package to parse the HTML DOM and let us search for specific elements in a convenient, jQuery-like way. We perform the HTTP request like normal, and then create a goquery document using the response. With the goquery document object, we can call **Find()** and process each element found. In this case, we will search for **a** elements, or links.

I am only scratching the surface of what [goquery](https://github.com/PuerkitoBio/goquery) can do. Here is an example of what it can do:

`// Example of a more complex goquery to find an element in the DOM[[NEWLINE]]// https://github.com/PuerkitoBio/goquery[[NEWLINE]]document.Find(".sidebar-reviews article .content-block")`

This is a full working example of how to use goquery to find all the links on a page and print them out.

`// find_links_in_page.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"fmt"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]][[NEWLINE]]"github.com/PuerkitoBio/goquery"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]// This will get called for each HTML element found[[NEWLINE]]func processElement(index int, element *goquery.Selection){[[NEWLINE]]// See if the href attribute exists on the element[[NEWLINE]]    href, exists := element.Attr("href")[[NEWLINE]]if exists {[[NEWLINE]]        fmt.Println(href)[[NEWLINE]]}[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Make HTTP request[[NEWLINE]]    response, err := http.Get("https://www.devdungeon.com")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Create a goquery document from the HTTP response[[NEWLINE]]    document, err := goquery.NewDocumentFromReader(response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal("Error loading HTTP response body. ", err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Find all links and process them with the function[[NEWLINE]]// defined earlier[[NEWLINE]]    document.Find("a").Each(processElement)[[NEWLINE]]}`

## Parse URLs

In the previous example we looked at finding all the links on a page. A common task after that is to examine the URL and determine if it is a relative URL that leads somewhere on the same site, or a URL that leads off-site somewhere. You can use the string functions to search and parsae the URL manually, but there is a better way!

The Go standard library provides a convenient **URL** type that can handle all of the URL string parsing for us. Let it handle the heavy lifting with string parsing, and just get the hostname, port, query, requestURI, using the predefined functions. Read more about the **url** package and the **url.URL** type at https://golang.org/pkg/net/url/.

`// parse_urls.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"fmt"[[NEWLINE]]"log"[[NEWLINE]]"net/url"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Parse a complex URL[[NEWLINE]]    complexUrl :="https://www.example.com/path/to/?query=123&this=that#fragment"[[NEWLINE]]    parsedUrl, err := url.Parse(complexUrl)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Print out URL pieces[[NEWLINE]]    fmt.Println("Scheme: "+ parsedUrl.Scheme)[[NEWLINE]]    fmt.Println("Host: "+ parsedUrl.Host)[[NEWLINE]]    fmt.Println("Path: "+ parsedUrl.Path)[[NEWLINE]]    fmt.Println("Query string: "+ parsedUrl.RawQuery)[[NEWLINE]]    fmt.Println("Fragment: "+ parsedUrl.Fragment)[[NEWLINE]][[NEWLINE]]// Get the query key/values as a map[[NEWLINE]]    fmt.Println("\nQuery values:")[[NEWLINE]]    queryMap := parsedUrl.Query()[[NEWLINE]]    fmt.Println(queryMap)[[NEWLINE]][[NEWLINE]]// Craft a new URL from scratch[[NEWLINE]]var customURL url.URL[[NEWLINE]]    customURL.Scheme="https"[[NEWLINE]]    customURL.Host="google.com"[[NEWLINE]]    newQueryValues := customURL.Query()[[NEWLINE]]    newQueryValues.Set("key1","value1")[[NEWLINE]]    newQueryValues.Set("key2","value2")[[NEWLINE]]    customURL.Fragment="bookmarkLink"[[NEWLINE]]    customURL.RawQuery= newQueryValues.Encode()[[NEWLINE]][[NEWLINE]]fmt.Println("\nCustom URL:")[[NEWLINE]]    fmt.Println(customURL.String())[[NEWLINE]]}`

## Use goquery to find all images on a page

We can also leverage the **goquery** package to search for other elements. This is another simple example similar to finding the links on a page. This example will show how to search for images on a page and list the URLs. This example is written slightly different, to demonstrate how to create an anonymous function to handle the processing instead of a named function.

`// find_images_in_page.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"fmt"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]][[NEWLINE]]"github.com/PuerkitoBio/goquery"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]// Make HTTP request[[NEWLINE]]    response, err := http.Get("https://www.devdungeon.com")[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]// Create a goquery document from the HTTP response[[NEWLINE]]    document, err := goquery.NewDocumentFromReader(response.Body)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal("Error loading HTTP response body. ", err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Find and print image URLs[[NEWLINE]]    document.Find("img").Each(func(index int, element *goquery.Selection){[[NEWLINE]]        imgSrc, exists := element.Attr("src")[[NEWLINE]]if exists {[[NEWLINE]]            fmt.Println(imgSrc)[[NEWLINE]]}[[NEWLINE]]})[[NEWLINE]]}`

## Make HTTP POST request with data

Making a POST request is similar to a GET request. In fact, it is as simple as changing the word "GET" to "POST" in the request. However, a POST request is often accompanied with a payload. This could be a binary file or a URL encoded form. This example will demonstrate how to make a POST request with URL encoded form data and how to post a file like when uploading a file..

`// http_post_with_payload.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]]"net/url"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]][[NEWLINE]]response, err := http.PostForm([[NEWLINE]]"http://example.com/form",[[NEWLINE]]        url.Values{[[NEWLINE]]"username":{"MyUsername"},[[NEWLINE]]"password":{"123"},[[NEWLINE]]},[[NEWLINE]])[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]]    defer response.Body.Close()[[NEWLINE]][[NEWLINE]]log.Println(response.Header)// Print the response headers[[NEWLINE]][[NEWLINE]]// To upload a file, use Post instead of PostForm, provide[[NEWLINE]]// a content type like application/json or application/octet-stream,[[NEWLINE]]// and then provide the an io.Reader with the data[[NEWLINE]][[NEWLINE]]// http.Post("http://example.com/upload", "image/jpeg", &buff)[[NEWLINE]]}`

## Make HTTP request with cookie

Since cookies are simply HTTP headers, you can manually set and manage cookies yourself by checking and setting the header values as needed.

Go offers a better way of managing cookies with a **Cookie** type that is used by the **Request** and **Response** type. You can see the source code for the **Cookie** at https://golang.org/src/net/http/cookie.go

These are some of the cookie functions available on the **Request** and **Response** types:

`// Cookie functions for Request [[NEWLINE]]// https://golang.org/pkg/net/http/#Request[[NEWLINE]]Request.AddCookie()// Add cookie to request[[NEWLINE]]Request.Cookie()// Get specific cookie[[NEWLINE]]Request.Cookies()// Get all cookies[[NEWLINE]][[NEWLINE]]// Cookie functions for Response[[NEWLINE]]// https://golang.org/pkg/net/http/#Response[[NEWLINE]]Response.Cookies()// Get all cookies`

Alternatively, you could use a library that is not part of the standard library like the [sessions package provided by Gorilla](https://github.com/gorilla/sessions), but that will not be covered here.

There is also a **cookiejar** type. It is essentially a collection of cookies separated by URL. You can read more about at https://golang.org/pkg/net/http/cookiejar/. It is useful if you need to manage cookies for multiple sites.

`// http_request_with_cookie.go[[NEWLINE]]package main[[NEWLINE]][[NEWLINE]]import([[NEWLINE]]"fmt"[[NEWLINE]]"log"[[NEWLINE]]"net/http"[[NEWLINE]])[[NEWLINE]][[NEWLINE]]func main(){[[NEWLINE]]    request, err := http.NewRequest("GET","https://www.devdungeon.com",nil)[[NEWLINE]]if err !=nil{[[NEWLINE]]        log.Fatal(err)[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Create a new cookie with the only required fields[[NEWLINE]]    myCookie :=&http.Cookie{[[NEWLINE]]Name:"cookieKey1",[[NEWLINE]]Value:"value1",[[NEWLINE]]}[[NEWLINE]][[NEWLINE]]// Add the cookie to your request[[NEWLINE]]    request.AddCookie(myCookie)[[NEWLINE]][[NEWLINE]]// Ask the request to tell us about itself,[[NEWLINE]]// just to confirm the cookie attached properly[[NEWLINE]]    fmt.Println(request.Cookies())[[NEWLINE]]    fmt.Println(request.Header)[[NEWLINE]][[NEWLINE]]// Do something with the request[[NEWLINE]]// client := &http.Client{}[[NEWLINE]]// client.Do(request)[[NEWLINE]]}`

## Log in to a website

Logging in to a site is relatively simple conceptually. You make an HTTP POST to a specific URL containing your username and password, and it returns a cookie, which is simply an HTTP header, that contains a unique key that matches your session on the server. Most websites work the same in this regard, although custom authentication mechanisms, CAPTCHAs, two-factor authentication, and other security measures complicate this process.

Logging in to a site is going to have to be tailored specifically to your target website. You will have to reverse engineer the authentication process from the site. Many websites use a simple form-based login system. Inside a browser like Chrome or Firefox, you can right click on one of the form fields and choose "inspect". This will allow you to see how the form is constructed, what the target action url is, and how the form fields are named in order to recreate the request programmatically.

You can inspect the form in the source of the HTML, or you can monitor the network traffic itself. The brwoser extensions will let you see the POST requests going on behind the scene on a website, but you could use other tools as well like jsfiddler, burp suite, Zed Attack Proxy (ZAP), or any other man-in-the-middle proxying tool.

Typically, you will need to get the URL in the **action** attribute of the **form**, and the **name** attribute of the of the username and password **input** fields. Once you have that information, you can make the POST request to the URL, and then store the session cookie the server provides in its response. You will need to pass the session cookie with any subsequent requests you make to the server.

Because every website has it's own mechanism for authentication, I am only covering this at the conceptual level and not providing a code example.

## Web crawling

Crawling is simply an extension of scraping. We already looked at how to [find all links on a page](https://www.devdungeon.com/content/web-scraping-go#find_all_links_on_page), and how to [parse URLs](https://www.devdungeon.com/content/web-scraping-go#parse_urls), which are the important steps. You want to find all the links on a page, parse the url, decide if you want to follow it, and then make a request to the new url, repeating the process.

After parsing a URL, you can determine whether it belongs to the same site you are already on, or leads to another website. You can also look for a file extension at the end of the URL for clues about what it leads to.

You can crawl in a breadth-first or a depth-first manner. One depth-first approach would be to crawl only URLs from the same website before crawling the next website in the list. A breadth-first approach would be to prioritize links that lead to websites you have never seen before.

For a code example of a web crawler, check out the DevDungeon Web Genome project in the next section.

## DevDungeon Project: Web Genome

Web Genome is a breadth first web crawler that stores HTTP headers in a MongoDB database with a web interface all written in Go. Read more on the [Web Genome project page](https://www.devdungeon.com/content/web-genome) and browse the source code at https://github.com/DevDungeon/WebGenome.

Visit the Web Genome website at [http://www.webgeno.me](http://www.webgeno.me/).

## Conclusion

With this reference code, you should be able to perform basic web scraping tasks to suit your needs. There are also more features in the goquery library that I have not covered. Refer to the official repository at https://github.com/PuerkitoBio/goquery for the latest information.