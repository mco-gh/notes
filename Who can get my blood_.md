Who can get my blood?

## HTML(Pug)

## HTML(Pug)

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='679'%3e%3cuse xlink:href='/svg_sprite%3fv=9637ff09%23x' data-evernote-id='680' class='js-evernote-checked'%3e%3c/use%3e%3c/svg%3e)

-
-
-
-
-
-
-

46

1
-
2
 var BLOOD_TYPES = ["O−", "O+", "A−", "A+", "B−", "B+", "AB−", "AB+"];
3

4
mixin  bloodSelector(value)
5
 div=  value
6
​
7
mixin  bloodTypeMixin(value, side)
8
 .human(class=side)
9
   .scribble
10
     span.blood_type=  value
11
     .head
12
     .body
13
   .via
14
   .blood_via
15
​
16
#about
17
 .mySocial
18
   a.social(
19
    href="https://www.linkedin.com/in/rominamartinliberon/",
20
     target="_new"
21
   )
22
     i.fab.fa-linkedin
23
   a.social(href="https://rominamartin.github.io/", target="_new")

## CSS(SCSS)

## CSS(SCSS)

-
-
-
-
-
-
-

xxxxxxxxxx
312

1
$wires_color: #ccc;
2
$human_color: #666;
3
$blood_color: #b51e23;
4
$transition_time: 1s;
5
$global_background: #f7f7f7;
6
​
7
▾
body {
8
 overflow-y: hidden;
9
 background: $global_background;
10
 font-family: "Montserrat", sans-serif;
11
}
12
▾
#about {
13
 position: absolute;
14
 top: 10px;
15
 left: 10px;
16
 z-index: 2;
17
▾
 a {
18
   display: inline-block;
19
   height: 2.5em;
20
   margin: 0  5px;
21
}
22
▾
 a  i {
23
   font-size: 1.5em;
24
▾
  &.fa-linkedin {

## JS

## JS

-
-
-
-
-
-
-

67

1
const  humans_parent  =  document.getElementById("humans");
2
▾
const  BLOOD_TYPES  = {
3
 "O−": ["O−", "O+", "A−", "A+", "B−", "B+", "AB−", "AB+"],
4
 "O+": ["O+", "A+", "B+", "AB+"],
5
 "A−": ["A−", "A+", "AB−", "AB+"],
6
 "A+": ["A+", "AB+"],
7
 "B−": ["B−", "B+", "AB−", "AB+"],
8
 "B+": ["B+", "AB+"],
9
 "AB−": ["AB−", "AB+"],
10
 "AB+": ["AB+"]
11
};
12
const  reset_button  =  document.getElementById("reset");
13
const  selector  =  document.getElementById("blood_selector");
14
const  blood_vias  =  document.querySelectorAll("#humans .human .blood_via");
15

const  blood_bag  =  document.querySelector("#blood_content > div.main_bag > div");

16
const  center_via  =  document.querySelector(".center_via > .blood_via");
17
const  blood_types  =  document.querySelectorAll(".blood_type");
18
let  lastCalled;
19
addListeners();
20
​
21
▾
function  callIfChildren(e) {
22
 if (lastCalled) change();