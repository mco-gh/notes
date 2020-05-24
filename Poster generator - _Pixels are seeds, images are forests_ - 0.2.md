Poster generator - "Pixels are seeds, images are forests" - 0.2

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='869'%3e%3cpath d='M100 78.905L78.735 100 49.608 71.094 21.263 99.217 0 78.123 28.344 50 0 21.877 21.263.78l28.345 28.125L78.735 0 100 21.094 70.862 50z' data-evernote-id='267' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

- [Tidy HTML](https://codepen.io/sbuellet/pen/JqqKMp#0)

-

- [Analyze HTML](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Maximize HTML Editor](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Minimize HTML Editor](https://codepen.io/sbuellet/pen/JqqKMp#0)

-
-

28

1
<canvas  id="canvas"></canvas>
2
<canvas  id="canvas2svg"></canvas>
3
​
4
▾
<div  class="container">
5
​
6

  <input  type="text"  id="imgUrl"  name="imgUrl"  required  size="30"  value="https://images.unsplash.com/photo-1559386484-97dfc0e15539?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60">

7
▾
  <label  for="imgUrl">Image URL</label>
8
  <hr>
9
​
10

  <input  id="imgSrcSize"  name="imgSrcSize"  type="range"  value="1"  min="0.001"  max="10"  step=".0001">

11
▾
  <label  for="imgSrcSize">Image source Size</label>
12
  <hr>
13
​
14

  <input  id="gridSize"  name="gridSize"  type="range"  value="20"  min="10"  max="100"  step=".1">

15
▾
  <label  for="gridSize">Grid size</label>
16
  <hr>
17
​
18

  <input  id="posterize_levels"  name="posterize_levels"  type="range"  value="10"  min="1"  max="20"  step=".1">

19
▾
  <label  for="posterize_levels">Posterize levels</label>

## CSS(SCSS)

## CSS(SCSS)

- [Tidy CSS](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [View Compiled CSS](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Analyze CSS](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Maximize CSS Editor](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Minimize CSS Editor](https://codepen.io/sbuellet/pen/JqqKMp#0)

-
-

xxxxxxxxxx
68

1
▾
* {
2
  margin: 0;
3
  padding: 0;
4
  box-sizing: border-box;
5
}
6
​
7
▾
body {
8
  align-items: center;
9
  color: #222;
10
  background-color:#fff;
11
  display: flex;
12
  flex-direction: column;
13
  font-size: 0.8em;
14
  font-family: "Open Sans", "Arial", sans-serif;
15
  min-height: 100vh;
16
  justify-content: center;
17
  margin: 0;
18
}
19
​
20
▾
hr {
21
  margin: 5px  0;
22
  border: solid  1px  #eee;
23
}
24
​

## JS(Babel)

## JS(Babel)

- [Tidy JS](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [View Compiled JS](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Analyze JS](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Maximize JS Editor](https://codepen.io/sbuellet/pen/JqqKMp#0)
- [Minimize JS Editor](https://codepen.io/sbuellet/pen/JqqKMp#0)

-

-

496

1
var  inputs  =  document.querySelectorAll(".container input, select");
2
let  img;
3
let  gridSize  =  20;
4
let  marginGrid  =  1;
5
//let w = window.innerWidth;
6
//let h = window.innerHeight;
7
let  w  =  400;
8
let  h  =  600;
9
let  showTxt  =  new  Boolean("true");
10
let  showCells  =  new  Boolean("false");
11
let  colorMode  =  "r";
12
let  shapeMode  =  "leaf";
13
​
14
let  imgUrl  =
15

  "https://images.unsplash.com/photo-1559386484-97dfc0e15539?ixlib=rb-1.2.1&auto=format&fit=crop&w=500&q=60";

16

//let imgUrl = "https://images.unsplash.com/photo-1545742145-a673fae1edfc?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=634&q=80";

17
​
18
let  imgSrcSize  =  1;
19
let  addRed  =  0;
20
let  addGreen  =  0;
21
let  addBlue  =  0;
22
let  contrast  =  1;