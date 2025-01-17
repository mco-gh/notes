An introduction to GraphQL

# An introduction to GraphQL

## GraphQL is a query language for your API, and a set of server-side runtimes (implemented in various backend languages) for executing queries

 Published Jan 30, 2018, Last Updated Jun 29, 2019

- [What is GraphQL](https://flaviocopes.com/graphql/#What-is-GraphQL)
- [GraphQL Principles](https://flaviocopes.com/graphql/#GraphQL-Principles)
- [GraphQL vs REST](https://flaviocopes.com/graphql/#GraphQL-vs-REST)
    - [Rest is a concept](https://flaviocopes.com/graphql/#Rest-is-a-concept)
    - [A single endpoint](https://flaviocopes.com/graphql/#A-single-endpoint)
    - [Tailored to your needs](https://flaviocopes.com/graphql/#Tailored-to-your-needs)
    - [GraphQL makes it easy to monitor for fields usage](https://flaviocopes.com/graphql/#GraphQL-makes-it-easy-to-monitor-for-fields-usage)
    - [Access nested data resources](https://flaviocopes.com/graphql/#Access-nested-data-resources)
    - [Types](https://flaviocopes.com/graphql/#Types)
    - [Which one is better?](https://flaviocopes.com/graphql/#Which-one-is-better)
- [GraphQL Queries](https://flaviocopes.com/graphql/#GraphQL-Queries)
    - [Fields and arguments](https://flaviocopes.com/graphql/#Fields-and-arguments)
    - [Aliases](https://flaviocopes.com/graphql/#Aliases)
    - [Fragments](https://flaviocopes.com/graphql/#Fragments)
- [GraphQL Variables](https://flaviocopes.com/graphql/#GraphQL-Variables)
    - [Making variables required](https://flaviocopes.com/graphql/#Making-variables-required)
    - [Specifying a default value for a variable](https://flaviocopes.com/graphql/#Specifying-a-default-value-for-a-variable)
- [GraphQL Directives](https://flaviocopes.com/graphql/#GraphQL-Directives)
    - [@include(if: Boolean)](https://flaviocopes.com/graphql/#includeif-Boolean)
    - [@skip(if: Boolean)](https://flaviocopes.com/graphql/#skipif-Boolean)

## What is GraphQL

GraphQL is the new frontier in APIs (*Application Programming Interfaces*) design, and in how we build and consume them.

It’s a query language, and a set of server-side runtimes (implemented in various backend languages) for executing queries. It’s not tied to a specific technology, but you can implement it in any language.

It is a methodology that **directly competes with REST** (*REpresentational State Transfer*) APIs, much like REST competed with **SOAP** at first.

And as we’ll see, it’s very different from REST. It creates a whole new dimension for API design.

GraphQL was **developed at Facebook**, like many of the technologies that are shaking the JavaScript world lately, like [React](https://flaviocopes.com/react/) and React Native, and it was publicly **launched in 2015** - although Facebook used it internally for a few years before.

Many big companies are adopting GraphQL beside Facebook, including GitHub, Pinterest, Twitter, Sky, The New York Times, Shopify, Yelp and thousands many other.

I’ve first been in touch with GraphQL when GitHub decided to implement the v4 of their API using that technology, and I joined their beta program. That’s when I discovered it’s a game changer in many aspects.

## GraphQL Principles

**GraphQL exposes a single endpoint**.

You **send a query to that endpoint** by using a special Query Language syntax. That query is **just a string**.

The server responds to a query by providing a JSON object.

Let’s see a first example of such a query. This query gets the name of a person with `id=1`:

	GET /graphql?query={ person(id: "1") { name } }

or:

	{
	  person(id: "1") {
	    name
	  }
	}

We’ll get this JSON response back:

	{
	  "name": "Tony"
	}

Let’s add a bit more complexity: we get the name of the person, and the city where the person lives, by extracting it from the `address` object. We don’t care about other details of the address, and the server does not return them back to us because we didn’t ask for them:

	GET /graphql?query={ person(id: "1") { name, address { city } } }

or

	{
	  person(id: "1") {
	    name
	    address {
	      city
	    }
	  }
	}

This is what we get back:

	{
	  "name": "Tony",
	  "address": {
	    "city": "York"
	  }
	}

As you can see the data we get is basically the same structure of the request we sent, filled with values that were fetched.

## GraphQL vs REST

Since REST is such a popular approach to building APIs, and much more widespread than GraphQL, it’s fair to assume you are familiar with it, so let’s see the differences between GraphQL and REST.

### Rest is a concept

REST is a de-facto architecture standard but it actually has no specification and tons of unofficial definitions. GraphQL has a [specification](https://graphql.github.io/graphql-spec/) draft, and it’s a [Query Language](http://graphql.org/learn/queries/) instead of an architecture, with a well defined set of tools built around it (and a flourishing ecosystem).

While REST is built on top of an existing architecture, which in the most common scenarios is HTTP, GraphQL on the other hand is building its own set of conventions. Which can be an advantage point or not, since REST benefits *for free* by caching on the HTTP layer.

### A single endpoint

GraphQL has only one endpoint, where you send all your queries. With a REST approach, you create multiple endpoints and use HTTP **verbs** to distinguish read actions (`GET`) and write actions (`POST`, `PUT`, `DELETE`). GraphQL does not use HTTP verbs to determine the request type.

### Tailored to your needs

With REST, you generally cannot choose what the server returns back to you, unless the server implements partial responses using [sparse fieldsets](http://jsonapi.org/format/#fetching-sparse-fieldsets), and clients use that feature. The API maintainer cannot enforce such filtering.

The API will usually return you much more information than what you need, unless you control the API server as well, and you tailor your responses for each different request.

With GraphQL you explicitly request just the information you need, you don’t “opt out” from the full response default, but it’s mandatory to pick the fields you want.

This helps saving resources on the server, since you most probably need less processing, and also network savings, since the payload to transfer is smaller.

### GraphQL makes it easy to monitor for fields usage

With REST, unless forcing sparse fieldsets, there is no way to determine if a field is used by clients, so when it comes to refactoring or deprecating, it’s impossible to determine actual usage.

GraphQL makes it possible to track which fields are used by clients.

### Access nested data resources

GraphQL allows to generate a lot less network calls.

Let’s do an example: you need to access the names of the friends of a person. If your REST API exposes a `/person` endpoint, which returns a person object with a list of friends, you generally first get the person information by doing `GET /person/1`, which contains a list of ID of its friends.

Unless the list of friends of a person already contains the friend name, with 100 friends you’d need to do 101 HTTP requests to the `/person` endpoint, which is a huge time cost, and also a resource intensive operation.

With GraphQL, you need only one request, which asks for the names of the friends of a person.

### Types

A REST API is based on JSON which cannot provide type control. **GraphQL has a Type System**.

### Which one is better?

Organizations around the world are questioning their API technology choices and they are trying to find out if migrating from REST to GraphQL is best for their needs.

GraphQL is a perfect fit when you need to expose complex data representations, and when clients might need only a subset of the data, or they regularly perform nested queries to get the data they need.

As with programming languages, there is no single winner, it all depends on your needs.

## GraphQL Queries

In this section you’ll learn how is a GraphQL query composed.
The concepts I’ll introduce are

- fields and arguments
- aliases
- fragments

### Fields and arguments

Take this simple GraphQL query:

	{
	  person(id: "1") {
	    name
	  }
	}

In this query you see 2 **fields**, `person` and `name`, and 1 **argument**.

The field `person` returns an *Object* which has another field in it, a *String*.

The argument allows us to specify which person we want to reference. We pass an `id`, but we could as well pass a `name` argument, if the API we talk to has the option to find a person by name.

Arguments are not limited to any particular field. We could have a `friends` field in `person` that lists the friends of that person, and it could have a `limit` argument, to specify how many we want the API to return:

	{
	  person(id: "1") {
	    name
	    friends(limit: 100)
	  }
	}

### Aliases

You can ask the API to return a field with a different name. For example here you request the `name` field, but you want it returned as `fullname`:

	{
	  owner: person(id: "1") {
	    fullname: name
	  }
	}

will return

	{
	  "data": {
	    "owner": {
	      "fullname": "Tony"
	    }
	  }
	}

This feature, beside creating more ad-hoc naming for your client code, in case you need, is the only thing that can make the query work if you need to **reference the same endpoint 2 times in the same query**:

	{
	  owner: person(id: "1") {
	    fullname: name
	  }
	  first_employee: person(id: "2") {
	    fullname: name
	  }
	}

### Fragments

In the above query we replicated the person structure. Fragments allow us to specify the structure just once (a very useful thing when you have many similar fields):

	{
	  owner: person(id: "1") {
	    ...personFields
	  }
	  first_employee: person(id: "2") {
	    ...personFields
	  }
	}

	fragment personFields on person {
	  fullname: name
	}

## GraphQL Variables

More complex GraphQL queries need to use **variables**, a way to dynamically specify a value that is used inside a query.

In this case we added the person id as a string inside the query:

	{
	  owner: person(id: "1") {
	    fullname: name
	  }
	}

The id will most probably change dynamically in our program, so we need a way to pass it, and **not with string interpolation**.

With variables, the same query can be written as this:

	query GetOwner($id: String) {
	  owner: person(id: $id) {
	    fullname: name
	  }
	}

	{
	  "id": "1"
	}

In this snippet we have assigned the `GetOwner` name to our query. Think of it as named functions, while previously you had an anonymous function. Named queries are useful when you have lots of queries in your application.

The query definition with the variables looks like a function definition, and it works in an equivalent way.

### Making variables required

Appending a `!` to the type:

	query GetOwner($id: String!)

instead of `$id: String` will make the $id variable required.

### Specifying a default value for a variable

You can specify a default value using this syntax:

	query GetOwner($id: String = "1")

## GraphQL Directives

Directives let you include or exclude a field if a variable is true or false.

	query GetPerson($id: String) {
	  person(id: $id) {
	    fullname: name,
	    address: @include(if: $getAddress) {
	      city
	      street
	      country
	    }
	  }
	}

	{
	  "id": "1",
	  "getAddress": false
	}

In this case if `getAddress` variable we pass is true, we also get the address field, otherwise not.

We have 2 directives available: `include`, which we have just seen (includes if true), and `skip`, which is the opposite (skips if true)

### @include(if: Boolean)

	query GetPerson($id: String) {
	  person(id: $id) {
	    fullname: name,
	    address: @include(if: $getAddress) {
	      city
	      street
	      country
	    }
	  }
	}

	{
	  "id": "1",
	  "getAddress": false
	}

### @skip(if: Boolean)

	query GetPerson($id: String) {
	  person(id: $id) {
	    fullname: name,
	    address: @skip(if: $excludeAddress) {
	      city
	      street
	      country
	    }
	  }
	}

	{
	  "id": "1",
	  "excludeAddress": false
	}

* * *

[Found a typo or problem? Edit this page](https://github.com/flaviocopes/website-content/blob/content/post/graphql/index.md)