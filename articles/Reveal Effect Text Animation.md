Reveal Effect Text Animation

## HTML(Pug)

## HTML(Pug)

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='820'%3e%3cpath d='M100 78.905L78.735 100 49.608 71.094 21.263 99.217 0 78.123 28.344 50 0 21.877 21.263.78l28.345 28.125L78.735 0 100 21.094 70.862 50z' data-evernote-id='270' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

-

- [View Compiled HTML](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Analyze HTML](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Maximize HTML Editor](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Minimize HTML Editor](https://codepen.io/okawa-h/pen/qGJMMo#0)

-
-

40

1
main
2
 ul.inner
3
   li
4
     p(data-js="reveal") SANDWICHES&nbsp;&amp;&nbsp;PANCAKE
5
     p(data-js="reveal") GARDEN
6

     p(data-js="reveal") MORNING&nbsp;&amp;&nbsp;TOMORROW&nbsp;&amp;&nbsp;FRIEND

7

     p(data-js="reveal") ORANGE&nbsp;&amp;&nbsp;BIRD&nbsp;&amp;&nbsp;SHEEP&nbsp;&amp;&nbsp;CUP&nbsp;&amp;&nbsp;BUS

8
     p(data-js="reveal") APPLE&nbsp;&amp;&nbsp;FRUIT&nbsp;&amp;&nbsp;CAR
9

     p(data-js="reveal") CAKE&nbsp;&amp;&nbsp;PICTURE&nbsp;&amp;&nbsp;CAT&nbsp;&amp;&nbsp;STAMP

10

     p(data-js="reveal") PLANE&nbsp;&amp;&nbsp;BOOK&nbsp;&amp;&nbsp;RACKET&nbsp;&amp;&nbsp;GLASS&nbsp;&amp;&nbsp;BED

11
   li
12

     p(data-js="reveal") APPLE<br>BANANA&nbsp;&amp;&nbsp;PINE APPLE&nbsp;&amp;&nbsp;SHEEP

13
     p(data-js="reveal") BANANA&nbsp;&amp;&nbsp;PINE APPLE
14
   li
15
     p(data-js="reveal") PUMPKIN&nbsp;&amp;&nbsp;TARO&nbsp;&amp;&nbsp;CARROT
16
   li
17
     p(data-js="reveal") HORSERADISH&nbsp;&amp;&nbsp;LETTUCE
18
     p(data-js="reveal") PUMPKIN&nbsp;&amp;&nbsp;TARO&nbsp;&amp;&nbsp;CARROT

## CSS(Stylus)

## CSS(Stylus)

-

- [View Compiled CSS](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Analyze CSS](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Maximize CSS Editor](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Minimize CSS Editor](https://codepen.io/okawa-h/pen/qGJMMo#0)

-
-

​x

1
​
2
body {
3
 -webkit-font-smoothing: antialiased;
4
 -moz-osx-font-smoothing: grayscale;
5
 background-color: #000;
6
}
7
​
8
main {
9
 padding: 10vw  0;
10
}
11
​
12
ul {
13
 width: 100%;
14
 max-width: 70%;
15
 margin: 0  auto;
16
}
17
​
18
li {
19
 margin: 10vw  0;
20
 text-align: left;
21
}
22
​
23
p {
24
 display: block;

## JS(Babel)

## JS(Babel)

- [Tidy JS](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [View Compiled JS](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Analyze JS](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Maximize JS Editor](https://codepen.io/okawa-h/pen/qGJMMo#0)
- [Minimize JS Editor](https://codepen.io/okawa-h/pen/qGJMMo#0)

-
-

49

1
​
2
const  COLOR_LIST  = ['#7f00ff','#ff00ff','#0000ff','#007fff','#00ffff'];
3
let  $targetList;
4
​
5
▾
const  init  = () => {
6
​
7
 $targetList  =  document.querySelectorAll('[data-js="reveal"]');
8
​
9
 setup();
10
​
11
 window.addEventListener('scroll',onScroll,false);
12
 window.dispatchEvent(new  Event('scroll'));
13
​
14
}
15
​
16

const  getArrayRandomValue  = (array) =>  array[Math.floor(Math.random() *  array.length)];

17
​
18
▾
const  setup  = () => {
19
​
20
▾
 for (const  $target  of  $targetList) {
21
​