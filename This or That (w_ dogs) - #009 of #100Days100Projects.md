This or That (w/ dogs) - #009 of #100Days100Projects

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='789'%3e%3cpath d='M96.8 83.7L63.1 50l33.7-33.7c3.6-3.6 3.6-9.4 0-13.1s-9.5-3.6-13.1 0L50 36.9 16.3 3.2C12.7-.4 6.9-.4 3.2 3.2s-3.6 9.5 0 13.1L36.9 50 3.2 83.7c-3.6 3.6-3.6 9.4 0 13.1s9.5 3.6 13.1 0L50 63.1l33.7 33.7c3.6 3.6 9.4 3.6 13.1 0s3.6-9.5 0-13.1z' data-evernote-id='277' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

- [Tidy HTML](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)

-

- [Analyze HTML](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Maximize HTML Editor](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Minimize HTML Editor](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)

-
-

40

1
<div  id="app"></div>
2
​
3
▾
<!-- SOCIAL PANEL HTML -->
4
▾
<div  class="social-panel-container">
5
▾
 <div  class="social-panel">
6
▾
   <p>Created with <i  class="fa fa-heart"></i> by
7
▾
     <a  target="_blank"  href="https://florin-pop.com">Florin Pop</a></p>
8
▾
   <button  class="close-btn"><i  class="fas fa-times"></i></button>
9
▾
   <h4>Get in touch on</h4>
10
▾
   <ul>
11
▾
     <li>
12
▾
       <a  href="https://twitter.com/florinpop1705"  target="_blank">
13
         <i  class="fab fa-twitter"></i>
14
       </a>
15
     </li>
16
▾
     <li>
17
▾
       <a  href="https://linkedin.com/in/florinpop17"  target="_blank">
18
         <i  class="fab fa-linkedin"></i>
19
       </a>
20
     </li>

## CSS

## CSS

- [Tidy CSS](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)

-

- [Analyze CSS](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Maximize CSS Editor](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Minimize CSS Editor](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)

-
-

xxxxxxxxxx
339

1
@import  url('https://fonts.googleapis.com/css?family=Muli&display=swap');
2

@import  url('https://fonts.googleapis.com/css?family=Montserrat:400,700&display=swap');

3
​
4
▾
* {
5
 box-sizing: border-box;
6
}
7
​
8
▾
body {
9
 font-family: 'Monserrat', sans-serif;
10
 min-height: 100vh;
11
 margin-bottom: 50px;
12
 display: flex;
13
 align-items: center;
14
 justify-content: center;
15
}
16
​
17
▾
.main {
18
 display: flex;

## JS(Babel)

## JS(Babel)

- [Tidy JS](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [View Compiled JS](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Analyze JS](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Maximize JS Editor](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)
- [Minimize JS Editor](https://codepen.io/FlorinPop17/pen/rNBRYKZ#0)

-
-

157

1
▾
class  App  extends  React.Component {
2
▾
 state  = {
3
   dogs: [],
4
   database: undefined,
5
   idx1: undefined,
6
   idx2: undefined
7
 };
8
​
9
▾
 componentDidMount  = () => {
10
   const  database  =  firebase.database().ref('/dogs');
11
​
12
   this.setState(
13
▾
     {
14
       database
15
     },
16
▾
     () => {
17
       this.getDogs();
18
     }
19
   );
20
​
21
▾
   setTimeout(() => {
22
     this.getRandomDogs();
23
   }, 2000);