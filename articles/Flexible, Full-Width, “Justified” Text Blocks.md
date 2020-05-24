Flexible, Full-Width, “Justified” Text Blocks

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='775'%3e%3cpath d='M100 78.905L78.735 100 49.608 71.094 21.263 99.217 0 78.123 28.344 50 0 21.877 21.263.78l28.345 28.125L78.735 0 100 21.094 70.862 50z' data-evernote-id='264' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

- [Tidy HTML](https://codepen.io/reubenlillie/pen/xemGmd#0)

-

- [Analyze HTML](https://codepen.io/reubenlillie/pen/xemGmd#0)
- [Maximize HTML Editor](https://codepen.io/reubenlillie/pen/xemGmd#0)
- [Minimize HTML Editor](https://codepen.io/reubenlillie/pen/xemGmd#0)

-
-

25

1
<!DOCTYPE html>
2
▾
<html  lang="en">
3
​
4
▾
<head>
5
 <meta  charset="utf-8">
6
 <meta  name="viewport"  content="width=device-width, initial-scale=1.0">
7
▾
 <title>Flexible Full-Width “Justified” Text Blocks</title>
8
</head>
9
​
10
▾
<body>
11
▾
 <blockquote  class="text-block">
12
▾
   <span  class="text-line">You can’t stay</span>
13
▾
   <span  class="text-line">in your corner</span>
14
▾
   <span  class="text-line">of the Forest</span>
15
▾
   <span  class="text-line">waiting for others</span>
16
▾
   <span  class="text-line">to come to you</span><span  class="append">.</span>
17
▾
   <span  class="text-line">You have to</span>
18
▾

   <span  class="text-line">go to them sometimes</span><span  class="append">.</span>

19
▾
   <cite>
20
▾
       <span  class="text-line"> —Winnie the Pooh</span>
21
   </cite>

## CSS

## CSS

- [Tidy CSS](https://codepen.io/reubenlillie/pen/xemGmd#0)

-

- [Analyze CSS](https://codepen.io/reubenlillie/pen/xemGmd#0)
- [Maximize CSS Editor](https://codepen.io/reubenlillie/pen/xemGmd#0)
- [Minimize CSS Editor](https://codepen.io/reubenlillie/pen/xemGmd#0)

-
-

xxxxxxxxxx
32

1
▾
body {
2
 display: flex;
3
 font-family: Montserrat, sans-serif;
4
 margin: 0;
5
 min-height: 100vh;
6
}
7
​
8
▾
cite {
9
 font-stretch: condensed;
10
 font-style: normal;
11
 font-weight: bold;
12
}
13
​
14
▾
.text-block {
15
 display: grid;
16
 grid-template-columns: max-content  1fr;
17
 margin: auto;
18
 text-transform: uppercase;
19
 width: max-content;
20
}
21
​
22
.text-line,
23
▾
.text-block  cite {
24
 display: flex;

## JS

## JS

- [Tidy JS](https://codepen.io/reubenlillie/pen/xemGmd#0)

-

- [Analyze JS](https://codepen.io/reubenlillie/pen/xemGmd#0)
- [Maximize JS Editor](https://codepen.io/reubenlillie/pen/xemGmd#0)
- [Minimize JS Editor](https://codepen.io/reubenlillie/pen/xemGmd#0)

-
-

45

1
// Compiles a node list of indiviual lines inside text blocks
2
var  lines  =  document.querySelectorAll(".text-line");
3
​
4
// Compiles a node list of elements appended to the ends of lines
5
var  appendages  =  document.querySelectorAll(".append");
6
​
7
// Wraps each character of a string inside a `<span>` element
8
▾
var  wrapCharacters  =  function(lines) {
9
▾
 return  lines.forEach(function(line) {
10
   var  characters  =  line.innerHTML.split("");
11
   var  wrappedCharacters  =  characters
12
▾
    .map(function(character) {
13
▾
       if (character  ===  " ") {
14
         return  '<span class="text-line">&nbsp;</span>';
15
      }
16
       return  '<span class="text-line">'  +  character  +  "</span>";
17
    })
18
    .join("");
19
   return (line.innerHTML  =  wrappedCharacters);