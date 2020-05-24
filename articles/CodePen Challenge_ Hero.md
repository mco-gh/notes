CodePen Challenge: Hero

## HTML

## HTML

**0** unsaved changes ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-x js-evernote-checked' data-evernote-id='589'%3e%3cuse xlink:href='/svg_sprite%3fv=9637ff09%23x' data-evernote-id='590' class='js-evernote-checked'%3e%3c/use%3e%3c/svg%3e)

-
-
-
-
-
-
-

10

1
▾
<section  class="hero">
2
▾
 <div  class="hero__image-wrapper">
3

   <img  id="hero__image"  src="https://picsum.photos/1280/720"  alt="Picsum placeholder image"  />

4
 </div>
5
▾
 <div  class="hero__text">
6
▾
   <h1>Can't see text over an image?</h1>
7
▾

   <p>Fear not! Darkening the image behind the text will make the text much easier to see!</p>

8
▾
   <button  id="hero__img-refresh">Refresh Image</button>
9
 </div>
10
</section>

## CSS

## CSS

-
-
-
-
-
-
-

​x

1
▾
body {
2
 margin: 0px;
3
}
4
​
5
▾
.hero {
6
 display: flex;
7
 position: relative;
8
 align-items: center;
9
 justify-content: center;
10
 width: 100vw;
11
 max-width: 1280px;
12
 height: 100vh;
13
 max-height: 720px;
14
 margin: 0  auto;
15
 color: #fff;
16
 text-align: center;
17
}
18
​
19
▾
.hero:after {
20
 z-index: 0;
21
 position: absolute;
22
 width: 100%;
23
 height: 100%;
24
 background-color: rgba(0, 0, 0, 0.4);
25
 content: "";
26
}
27
​
28
▾
.hero__image-wrapper {
29
 display: flex;
30
 position: absolute;
31
 width: 100%;
32
 height: 100%;
33
}

## JS

## JS

-
-
-
-
-
-
-

8

1
var  imgRefreshBtn  =  document.getElementById("hero__img-refresh");
2
​
3
// Update the picsum image source on btn click
4
▾
imgRefreshBtn.onclick  =  function () {
5
 document.getElementById("hero__image").src  =
6
   "https://picsum.photos/1280/720?rand="  +  new  Date().getTime();
7
};
8
​