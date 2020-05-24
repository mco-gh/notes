Introduction to Go Modules – Roberto Selbach

Introduction to Go Modules – Roberto Selbach

![](../_resources/1ec0acf049e4d6351489af6bb4ee771a.jpg)https://roberto.selbach.ca/intro-to-go-modules/

The upcoming version 1.11 of the Go programming language will bring experimental support for modules , a new dependency management system for Go. A few days ago, I wrote a quick post about it . Since that post went live, things changed a bit and as we’re now very close to the new release, I thought it would be a good time for another post with a more hands-on approach. So here’s what we’ll do: we’ll create a new package and then we’ll make a few releases to see how that would work. Creating a Module So first things first. Let’s create our package. We’ll call it “testmod”. An important detail here: