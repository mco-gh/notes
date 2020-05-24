Small Quote Generator

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='677'%3e%3cuse xlink:href='/svg_sprite%3fv=9637ff09%23x' data-evernote-id='678' class='js-evernote-checked'%3e%3c/use%3e%3c/svg%3e)

-
-
-
-
-
-
-

14

1
▾
 <header  class="header">
2
▾
   <!-- Left Column -->
3
▾
   <div  class="left-column">
4
▾
     <div  class="button-container">
5
▾
       <span  id="generate-quote"  class="generate-button">New Quote</span>
6
     </div>
7
   </div>
8
▾
   <!-- Right Column -->
9
▾
   <div  class="right-column">
10
▾
     <q  id="quote"  class="quote-container">
11
      Logic will get you from A to B. Imagination will take you everywhere.</q>
12
▾
     <span  class="hero">- Albert Einstein </span>
13
   </div>
14
 </header>

## CSS(SCSS)

## CSS(SCSS)

-
-
-
-
-
-
-

60

1
▾
body {
2
 margin: 0;
3
}
4
▾
.header {
5

 background-image: url("https://raw.githubusercontent.com/erickkg/CodePenChallenges/master/Hero/albertBackground.jpg");

6
 background-size: cover;
7
 background-repeat: no-repeat;
8
 height: 100vh;
9
 width: 100vw;
10
 display: flex;
11
 justify-content: space-between;
12
 background-color: rgb(27, 27, 27);
13
 margin: 0;
14
 color: rgb(255, 255, 255);
15
 text-align: center;
16
}
17
​
18
▾
.left-column {
19
 display: flex;
20
 flex-direction: column;
21
 justify-content: flex-end;

## JS

## JS

-
-
-
-
-
-
-

25

1
const  generateButton  =  document.getElementById("generate-quote");
2
​
3
// Event listener
4
▾
generateButton.addEventListener("click", function () {
5
 newQuote();
6
});
7
​
8
//quotes
9
▾
let  quotes  = [
10

 "Learn from yesterday, live for today, hope for tomorrow. The important thing is not to stop questioning.",

11
 "Anyone who has never made a mistake has never tried anything new.",
12

 "The world is a dangerous place to live; not because of the people who are evil, but because of the people who don't do anything about it.",

13

 "We cannot solve our problems with the same thinking we used when we created them.",

14
 "If you can't explain it simply, you don't understand it well enough",
15
 "The only source of knowledge is experience.",
16

 "Education is what remains after one has forgotten what one has learned in school.",

17

 "Only one who devotes himself to a cause with his whole strength and soul can be a true master. For this reason mastery demands all of a person.",

18
 "Logic will get you from A to B. Imagination will take you everywhere."
19
];