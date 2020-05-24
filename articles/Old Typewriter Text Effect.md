Old Typewriter Text Effect

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='870'%3e%3cpath d='M100 78.905L78.735 100 49.608 71.094 21.263 99.217 0 78.123 28.344 50 0 21.877 21.263.78l28.345 28.125L78.735 0 100 21.094 70.862 50z' data-evernote-id='269' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

- [Tidy HTML](https://codepen.io/chris22smith/pen/VOamoe#0)

-

- [Analyze HTML](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Maximize HTML Editor](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Minimize HTML Editor](https://codepen.io/chris22smith/pen/VOamoe#0)

-
-

2

1
▾

<p  class="typewriter">You don't know about me without you have read a book by the name of The Adventures of Tom Sawyer; but that ain't no matter. That book was made by Mr. Mark Twain, and he told the truth, mainly. There was things which he stretched, but mainly he told the truth. That is nothing. I never seen anybody but lied one time or another, without it was Aunt Polly, or the widow, or maybe Mary. Aunt Polly - Tom's Aunt Polly, she is - and Mary, and the Widow Douglas is all told about in that book, which is mostly a true book, with some stretchers, as I said before.</p>

2
▾
<p  class="typewriter">- The Adventures of Huckleberry Finn, Mark Twain -</p>

## CSS(SCSS)

## CSS(SCSS)

- [Tidy CSS](https://codepen.io/chris22smith/pen/VOamoe#0)
- [View Compiled CSS](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Analyze CSS](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Maximize CSS Editor](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Minimize CSS Editor](https://codepen.io/chris22smith/pen/VOamoe#0)

-
-

​x

1
▾
body {
2
 background-color:#ffe;
3
 margin:4em;
4
 max-width:40em;
5
}
6
​
7
▾
.typewriter {
8
 font-family:monospace;
9
 line-height:1.5;
10
}
11
​
12
​

## JS

## JS

- [Tidy JS](https://codepen.io/chris22smith/pen/VOamoe#0)

-

- [Analyze JS](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Maximize JS Editor](https://codepen.io/chris22smith/pen/VOamoe#0)
- [Minimize JS Editor](https://codepen.io/chris22smith/pen/VOamoe#0)

-
-

30

1
console.clear();
2
​
3
const  typing  =  document.querySelectorAll('.typewriter');
4
​
5
▾
function  type(element) {
6
​
7
▾
function  randomOpacity() {
8
 return (Math.floor(Math.random() *  50) +  50)/100;
9
}
10
​
11
▾
function  randomEms() {
12
▾
 if (Math.random() >  .8) {
13
 return (Math.floor(Math.random() *  100) -  50)/800;
14
}
15
▾
 else {
16
   return  0;
17
}
18
}
19
​
20
▾
function  wrap(char) {
21

 return  '<span style="opacity:'  +  randomOpacity() +  '; text-shadow:'  +  randomEms() +  'em '  +  randomEms() +  'em currentColor;">'  +  char  +  '</span>';