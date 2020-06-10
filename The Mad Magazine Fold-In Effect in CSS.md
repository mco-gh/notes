https://thomaspark.co/2020/06/the-mad-magazine-fold-in-effect-in-css/

> After 65 years at Mad Magazine, comic artist Al Jaffee announced his retirement. Jaffee was best known for his Mad Fold-Ins, where folding the page would reveal a hidden message in the artwork. Plenty of examples can be found on the web. The problem is, they all show the before and after statically,

# The Mad Magazine Fold-In Effect in CSS
[![](https://thomaspark.co/wp/wp-content/uploads/2020/06/mad-fold-in-300x300.gif)](https://thomaspark.co/2020/06/the-mad-magazine-fold-in-effect-in-css/)

After 65 years at Mad Magazine, comic artist Al Jaffee [announced his retirement](https://www.washingtonpost.com/arts-entertainment/2020/06/06/al-jaffee-mad-magazine-retires/). Jaffee was best known for his Mad Fold-Ins, where folding the page would reveal a hidden message in the artwork. Plenty of examples can be found on the web. The problem is, they all show the before and after statically, side by side, which diminishes the magic (see [here](https://en.wikipedia.org/wiki/Mad_Fold-in) and [here](https://13thdimension.com/13-mad-fold-ins-an-al-jaffee-celebration/)). There’s a whole generation who may have only seen the fold-ins in this format.

Of course I had to create the paper folding effect for the web. There’s many different ways to achieve this, but this approach is nice because:

*   It’s CSS only, relying on no JavaScript.
*   Uses a single image instead of requiring the image to be sliced up in Photoshop.
*   Can be configured with just HTML by setting CSS variables in a style attribute.

Here’s a demo of it in action, using artwork by Johnny Sampson [in an issue that celebrated Jaffee’s 98th birthday](https://www.madmagazine.com/blog/2019/03/13/a-special-98th-birthday-fold-in-for-al-jaffee). Hover or tap to fold.

![](https://thomaspark.co/wp/wp-content/uploads/2020/06/jaffee.png)

And another by Jaffee himself.

![](https://thomaspark.co/wp/wp-content/uploads/2020/06/MAD-Magazine-520-Fold-in.jpg)

### The Code

The HTML for the effect is fairly straightforward. You might be wondering about the standalone image element — it’s hidden but used to set the size and aspect ratio of the component. The image path is specified there and once again as a CSS variable to set the background image of the other elements.

    
    <span class="jaffee" style="--bg: url('path/to/image.png');">
      <span class="a"></span>
      <span class="bc">
        <span class="b"></span>
        <span class="c"></span>
      </span>
      <img src="path/to/image.png">
    </span>
    

And here is the CSS used to set the positioning, 3D transforms, and transitions.

    
    .jaffee {
      position: relative;
      display: inline-flex;
      justify-content: center;
      transform: rotateX(10deg); 
      transform-style: preserve-3d;
      cursor: grab;
    }
    
    .jaffee img {
      width: auto;
      height: auto;
      max-width: 100%;
      max-height: 56vh;
      opacity: 0;
    }
    
    .jaffee .a,
    .jaffee .b,
    .jaffee .c {
      top: 0;
      display: inline-block;
      height: 100%;
      background-image: var(--bg);
      background-size: cover;
      background-repeat: no-repeat;
    }
    
    .jaffee .a {
      position: absolute;
      left: 0;
      width: 50%;
      background-position: 0 0;
    }
    
    .jaffee .bc {
      position: absolute;
      display: inline-flex;
      width: 50%;
      height: 100%;
      left: 50%;
      transform-origin: left;
      transition: transform 3s;
      transform-style: preserve-3d;
    }
    
    .jaffee .b,
    .jaffee .c {
      position: relative;
      width: 50%;
    }
    
    .jaffee .b {
      background-position: 66.666667% 0;
    }
    
    .jaffee .c {
      background-position: 100% 0;
      transform-origin: left;
      transition: transform 2s;
      backface-visibility: hidden;
    }
    
    .jaffee:hover .bc,
    .jaffee:active .bc {
      transform: rotateY(-180deg) translateZ(-1px);
      transition: transform 2s;
    }
    
    .jaffee:hover .c,
    .jaffee:active .c {
      transform: rotateY(180deg) translateZ(1px);
      transition: transform 3s;
    }