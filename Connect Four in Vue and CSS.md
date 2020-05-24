Connect Four in Vue and CSS

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='672'%3e%3cuse xlink:href='/svg_sprite%3fv=8885a907%23x' data-evernote-id='673' class='js-evernote-checked'%3e%3c/use%3e%3c/svg%3e)

-
-
-
-
-
-
-

34

1
▾
<div  id="game">
2
​
3

 <div  id="winner-burst"  :class="[currentTurnColor, gameOver && 'burst']"></div>

4
​
5
▾
 <div  class="flex">
6
   <p  v-html="message"  role="status"></p>
7
▾
   <button  :disabled="!areThereMoves"  @click="startNewGame">New game</button>
8
 </div>
9
​
10
▾
 <div  id="button-board">
11
▾
   <div  v-for="i in 8"  :data-column="i - 1"  @click.stop="dropPiece">
12
▾

     <button  :data-column="i - 1"  @click.stop="dropPiece"  @keydown="handleMoveCursor"  @mouseover="handleHover"  :aria-label="`Drop ${currentTurnColor} piece in column ${i}`"  :tabindex="gameOver || isADraw ? '-1' : '0'">

13
       <span></span>
14
     </button>
15
▾
     <div  class="slot"  :hidden="gameOver || isADraw"  aria-hidden="true">
16
▾
       <div  :class="currentTurnColor">
17
         {{ getPieceIcon(currentTurnColor) }}
18
       </div>
19
     </div>
20
   </div>
21
 </div>

## CSS(SCSS)

## CSS(SCSS)

-
-
-
-
-
-
-

318

1
$yellow: #ffd100;
2
$orange: #ff6a13;
3
$lightBlue: #7ba7bc;
4
$lightGray: #a7a8aa;
5
$darkGray: #53565a;
6
$white: #fff;
7
$red: #e4002b;
8
​
9
$breakpoint: 40rem;
10
$unit: 3vmin;
11
​
12
*,
13
*:before,
14
▾
*:after {
15
 box-sizing: inherit;
16
 font-family: inherit;
17
 color: inherit;
18
 position: inherit;
19
}
20
​
21
▾
*:focus {
22
 outline: 0.15rem  dotted  $orange;
23
 outline-offset: 0.15rem;
24
}

## JS(Babel)

## JS(Babel)

-
-
-
-
-
-
-

194

1
//Tried auto-generating this grid to keep the syntax shorter,
2
//but ran into issues with object duplication (when one updates, all update),
3
//so I just stuck with this ¯\_(ツ)_/¯
4
▾
const  emptyGrid  = [
5
 [{}, {}, {}, {}, {}, {}, {}, {}],
6
 [{}, {}, {}, {}, {}, {}, {}, {}],
7
 [{}, {}, {}, {}, {}, {}, {}, {}],
8
 [{}, {}, {}, {}, {}, {}, {}, {}],
9
 [{}, {}, {}, {}, {}, {}, {}, {}],
10
 [{}, {}, {}, {}, {}, {}, {}, {}]
11
];
12
​
13
▾
const  game  =  new  Vue({
14
 el: "#game",
15
​
16
▾
 data: () => ({
17
   grid: emptyGrid,
18

   redTurn: true, //if false, it's yellow's turn. Better to use a boolean than strings.

19
   gameOver: false
20
 }),
21
​
22
 //Prevent users from navigating away from a game accidentally