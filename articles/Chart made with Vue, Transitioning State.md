Chart made with Vue, Transitioning State

 [(L)](http://codepen.io/)

#   [Chart made with Vue, Transitioning State](http://codepen.io/sdras/pen/OWZRZL)

A Pen By [Sarah DrasnerPro](http://codepen.io/sdras)

### Open this Pen in:

 [Editor View /pen/](http://codepen.io/sdras/pen/OWZRZL/)  [Details View /details/](http://codepen.io/sdras/details/OWZRZL/)  [Full Page /full/](http://codepen.io/sdras/full/OWZRZL/)  [PROPresentation Mode /pres/](http://codepen.io/sdras/pres/OWZRZL)  [Open on CrossBrowserTesting →](https://app.crossbrowsertesting.com/livetests/run?url=http%3A%2F%2Fcodepen.io%2Fsdras%2Ffull%2FOWZRZL)

* * *

### Direct Code Links:

 [.html](http://codepen.io/sdras/pen/OWZRZL.html)  [.css](http://codepen.io/sdras/pen/OWZRZL.css)  [.scss](http://codepen.io/sdras/pen/OWZRZL.scss)  [.js](http://codepen.io/sdras/pen/OWZRZL.js)  [.babel](http://codepen.io/sdras/pen/OWZRZL.babel)

* * *

### Editor Layout

 [Use Left Layout](http://codepen.io/sdras/pen/OWZRZL/left/)  [Use Top Layout](http://codepen.io/sdras/pen/OWZRZL/top/)  [Use Right Layout](http://codepen.io/sdras/pen/OWZRZL/right/)

 ![User Gravatar](../_resources/ea1636b2c647ebcf16a2e3b34597034f.png)

- [New Pen](http://codepen.io/pen/)

- [New Post](http://codepen.io/write/)

- [New Project](http://codepen.io/project/)

- [Recent Activity](http://codepen.io/marcacohen/activity/)

- [Embed Theme Builder](http://codepen.io/marcacohen/embed/builder/public/)

- [Settings](http://codepen.io/marcacohen/settings/editor/)

- [Check Out CodePen PRO](http://codepen.io/pro)

- [Help](http://blog.codepen.io/documentation/)

- [Log Out](http://codepen.io/logout)

- [Your Profile](http://codepen.io/marcacohen/)

 [Pens](http://codepen.io/marcacohen/pens/public/)  [Projects](http://codepen.io/marcacohen/projects/)  [Posts](http://codepen.io/marcacohen/posts/published/)  [Collections](http://codepen.io/marcacohen/collections/)

## Pen Settings

 [HTML](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#settings-html)  [CSS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#settings-css)  [JavaScript](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#settings-js)  [Behavior](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#settings-behavior)

#### Code Indentation

 Spaces   Tabs         Width of Indent

#### Save Automatically?

 Autosave
If active, Pens will autosave every 30 seconds after being saved once.

#### Auto-Updating Preview

 Enabled

If enabled, the preview panel updates automatically as you code. If disabled, use the "Run" button to update.

## HTML

## HTML

- [Tidy HTML](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

-

- [Analyze HTML](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Maximize HTML Editor](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Minimize HTML Editor](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

34

1
▾
<div  id="app">
2
▾
 <select  v-model="selected">
3
▾
   <option  v-for="option in options"  v-bind:value="option.value">
4
    {{ option.text }}
5
   </option>
6
 </select>
7

8
▾
 <svg  viewBox="0 0 400 400">
9
▾
   <!--xaxis -->
10
▾
   <g  targetVal="targetVal"  class="xaxis">
11
     <line  x1="0"  y1="1"  x2="350"  y2="1"/>
12
▾
     <g  v-for="(select, index) in targetVal">
13
       <line  y1="0"  y2="7"  v-bind="{ 'x1':index*10, 'x2':index*10 }"/>
14
▾

       <text  v-if="index % 5 === 0"  v-bind="{ 'x':index*10, 'y':20 }">{{ index }}</text>

## CSS

## CSS(SCSS)

- [Tidy CSS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [View Compiled CSS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Analyze CSS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Maximize CSS Editor](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Minimize CSS Editor](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

61

1
▾
body {
2
 font-family: 'Mada', sans-serif;
3
 background: #222;
4
}
5
​
6
▾
#app {
7
 text-align: center;
8
 max-width: 400px;
9
 margin: 30px  auto;
10
 display: table;
11
}
12
​

## JS

## JS(Babel)

- [Tidy JS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [View Compiled JS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Analyze JS](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Maximize JS Editor](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

- [Minimize JS Editor](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

51

1
▾
new  Vue({
2
 el: '#app',
3
▾
 data() {
4
▾
   return {
5
▾

     selected: [25, 37, 15, 13, 25, 30, 11, 17, 35, 10, 25, 15, 5, 27, 15, 13, 25, 36, 15, 14, 35, 10, 14, 15, 35, 17, 12, 13, 25, 30, 14, 17, 35, 10, 25, 15],

6
▾

     targetVal: [25, 37, 15, 13, 25, 30, 11, 17, 35, 10, 25, 15, 5, 27, 15, 13, 25, 36, 15, 14, 35, 10, 14, 15, 35, 17, 12, 13, 25, 30, 14, 17, 35, 10, 25, 15],

7
▾
     options: [
8
▾

    { text: 'First Dataset', value: [25, 37, 15, 13, 25, 30, 11, 17, 35, 10, 25, 15, 5, 27, 15, 13, 25, 36, 15, 14, 35, 10, 14, 15, 35, 17, 12, 13, 25, 30, 14, 17, 35, 10, 25, 15] },

9
▾

    { text: 'Second Dataset', value: [13, 25, 30, 11, 17, 35, 10, 25, 15, 5, 27, 15, 13, 25, 36, 15, 14, 35, 10, 14, 15, 35, 17, 12, 13, 25, 30, 14, 17, 35, 10, 25, 15, 25, 37, 15] },

10
▾

    { text: 'Third Dataset', value: [35, 10, 25, 15, 5, 27, 15, 13, 25, 36, 15, 14, 35, 10, 14, 15, 35, 17, 12, 13, 25, 30, 14, 17, 35, 10, 25, 15, 25, 37, 15, 13, 25, 30, 11, 17] }

11
    ]
12
  }
13
},
14
▾
 computed: {

999px

     0          5          10          15          20          25          30          35      0          5          10          15          20          25          30          35

- [   Share on Twitter](https://twitter.com/intent/tweet?text=Chart%20made%20with%20Vue,%20Transitioning%20State&url=http://codepen.io/sdras/pen/OWZRZL&via=CodePen)

- [   Share on Facebook](https://www.facebook.com/sharer/sharer.php?u=http://codepen.io/sdras/pen/OWZRZL)

- [   Share on Google+](https://plus.google.com/share?url=http://codepen.io/sdras/pen/OWZRZL)

#####  Send SMS with Full Page URL to your phone [(L)](http://blog.codepen.io/documentation/features/sms/)

   **10** left this month

 [   Save as GitHub Gist]()  [   Export .zip](http://codepen.io/sdras/share/zip/OWZRZL/)  [   Embed Pen](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#0)

[(L)](http://codepen.io/sdras/pen/OWZRZL/?editors=1000#)Window size:  x
Viewport size:  x
![close_icon.png](../_resources/84fc025b2e6ece6f37cfbf5a8c7b496d.png)[< 1 min to Spreed]()