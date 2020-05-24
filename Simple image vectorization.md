Simple image vectorization

# Simple image vectorization

Vectorization is when you take some minecraft-style raster image and make a crisp vector picture out of it.

 ![Bitmap_VS_SVG.png](../_resources/124d3d89a9d34c3f6f065b152349ffc4.png)

Yug, modifications by 3247 [[CC BY-SA 2.5](https://creativecommons.org/licenses/by-sa/2.5)]

It's especially useful when you want to turn a satellite photo into a map. Or if you want to scan some blueprint and turn it into a CAD model. Or if you want to reissue an old game and you don't want to redraw all the artwork from scratch.

The algorithm I'm going to show you has nothing to do with all these things. It's a basic vectorization technique which, in its original form, has little to none applications in the industry.

On the plus side, it illustrates the approach rather well. It shows how things like bilinear interpolation, gradient descent, and parametric splines work together to solve a real-world problem. At the very least, it makes learning about all these things a little more compelling.

## An input image

A raster image is essentially a rectangular table of things. If it's a full-color RGB, then it's a table of color pixels. Color pixels are the triplets of 8-bit integer values where each value represents an amount of red, green, and blue color.

Medical images, such as obtained from computed tomography, are usually the tables of 12-bit or 16-bit integers. It's not a color really since the values come from invisible X-ray radiation, but they are called gray values nevertheless.

Satellite images may have a lot of channels. Apart from the colors of the visible specter they may contain ultra-violet and infra-red luminosity. Channels may be represented by integers or floating point values.

Our image will be a simple gray-scale bitmap.
 ![](../_resources/6b19af2be194b03499d1815c6a784c3e.png)

Technically, we can already turn it into vectors rather easily. Let's just agree on some threshold, and mark the contour of all the pixels that have the values exceeding this threshold.

 ![](../_resources/f1aaf067a0b51e4115e8d75b62daf6ec.png)

Well, it's simple, but it's not what we wanted. We want curves, not corners. And for that, we have to make our image less cornery.

## Image interpolation

Let's say our image is not a table of values. Let's say we only know the values in the centers of the pixels, and we have to guess the values between them somehow.

This is called interpolation. The simplest case would be the nearest neighbor interpolation, where for every point on an image, the value is the value from the nearest pixel's center. But this simply turns it back into a table.

A little more advanced is the bilinear interpolation. The value is the linear sum of the four neighboring values. It looks like this.

|     |
| --- |
| // pixel value with out of bounds checksfunction  pixel_in(pixels, i, j) { if(i >= pixels.length) return  pixel_in(pixels, pixels.length-1, j); if(i < 0) return  pixel_in(pixels, 0, j); if(j >= pixels[0].length) return  pixel_in(pixels, i, pixels[0].length-1); if(j < 0) return  pixel_in(pixels, i, 0); return  pixels[i][j];<br>}// linear interpolationfunction  value_in(pixels, x, y) { var  j = Math.floor(x - 0.5); var  tj = x - 0.5 - j; var  i = Math.floor(y - 0.5); var  ti = y - 0.5 - i; return  pixel_in(pixels, i, j) * (1 - ti) * (1 - tj)<br>+ pixel_in(pixels, i, j+1) * (1 - ti) * (tj)<br>+ pixel_in(pixels, i+1, j+1) * (ti) * (tj)<br>+ pixel_in(pixels, i+1, j) * (ti) * (1 - tj);<br>} |

If we darken the pixels where the interpolated value meets the threshold, we'll get some kind of a contour.

 ![](../_resources/c4ae0175ba08f99016e5e34bf09f2a63.png)
Interpolation: nearest neighbor;   bilinear.

There are other methods. Plenty of them. But linear interpolation solves the cornery border problem just fine. Although, the border we see is just the borderline of some threshold. It's not a vector representation yet.

## Turning an interpolated image into a contour

We can borrow an idea from the [simplest possible smooth contouring](https://wordsandbuttons.online/the_simplest_possible_smooth_contouring_algorithm.html) algorithm. We'll build an initial border from the source pixels, and then we'll use our linearly interpolated image to find the best place to put each contour point so the image value will meet the threshold value.

With the distance field, it's easy. You take its gradient, take the difference between the value you have and the threshold value. Since it's the distance field, the value difference is exactly the distance you should move your point for. And the gradient is the exact opposite direction. You just inverse, multiply, add — and you're there.

Unfortunately, we don't have a distance field. We have a continuous image which only resembles one.

But the principle still works. If you move against the gradient, you will get closer to the threshold value. And the more the difference, the further you have to go. It's just you wouldn't always get there in one try.

So let's try several times then. Let's make an [iterative algorithm](https://wordsandbuttons.online/interactive_introduction_to_iterative_algorithms.html) out of it.

|     |
| --- |
| // gradientfunction  gradient(pixels, x, y) { const  eps = 1e-5; return [(value_in(pixels, x + eps, y) - value_in(pixels, x, y)) / eps,<br>(value_in(pixels, x, y + eps) - value_in(pixels, x, y)) / eps];<br>}// how far should you shift the point to meet the isoline // if value_in were a distance functionfunction  gradient_shift(pixels, threshold, x, y) { var  g = gradient(pixels, x, y); var  g_norm = Math.sqrt(g[0]*g[0] + g[1]*g[1]); var  d = threshold - value_in(pixels, x, y); return [g[0] * d / g_norm / g_norm, g[1] * d / g_norm / g_norm];<br>}// brings a point closer to the threshold isolinefunction  fit_point_better(pixels, threshold, point) { const  ok_error = 1/255; if(Math.abs(value_in(pixels, point[0], point[1]) - threshold) < ok_error) return  point; gs = gradient_shift(pixels, threshold, point[0], point[1]) var  new_point = [point[0] + gs[0], point[1] + gs[1]]; return  fit_point_better(pixels, threshold, new_point);<br>} |

We'll move our contour points against the gradient until we're close enough to the threshold

 ![](../_resources/25cf38941caf250f959c03162f98c865.png)

That's good but we can do better. Let's make the contour smooth.

## Cubic splines

All we have to do to make the contour smooth is to turn each line segment into a parametric cubic curve.

It's probably sounds more complicated than it is. A parametric cubic curve is just a pair of polynomials. If you have the points and partial derivatives in this points, you can get the coefficients for them from this pair of [linear systems](https://wordsandbuttons.online/programmers_introduction_to_linear_equations.html):

Px(t1)' = 3axt12 + 2bxt1 + c = dx1/dt
Px(t1) = axt13 + bxt12 + cxt1 + d = x1
Px(t2) = axt23 + bxt22 + cxt2 + d = x2
Px(t2)' = 3axt22 + 2bxt2 + c = dx2/dt

Py(t1)' = 3ayt12 + 2byt1 + c = dy1/dt
Py(t1) = ayt13 + byt12 + cyt1 + d = y1
Py(t2) = ayt23 + byt22 + cyt2 + d = y2
Py(t2)' = 3ayt22 + 2byt2 + c = dy2/dt

The curve itself will then look like this.
 ![](../_resources/6c03ea9ac4ed5aad5ab165960208138f.png)

Even more, since we get to choose the parameter range, we can make it [0..1]. This greatly simplifies our system and makes it really easy to solve.

Here is the function that makes one array of polynomial coefficients from two pairs of point and tangent values.

|     |
| --- |
| // solver specific to [0..1] parametrized splinesfunction  spline_for(p1, p1d, p2, p2d) {// A = [// [1, 0, 0, 0],// [0, 1, 0, 0],// [1, 1, 1, 1],// [0, 1, 2, 3]];// B = [p1, p1d, p2, p2d]  return [ p1, p1d, 3*p2 - p2d - 3*p1 - 2*p1d, p2d + p1d - 2*p2 + 2*p1 ];<br>} |

The polynomial is then computed in every *t* with this function.

|     |
| --- |
| // polynomialfunction  polynomial_in_t(A, t){ var  pt = 0.0; for(var  i = 0; i < A.length; ++i){ pt += A[i] * Math.pow(x, i);<br>} return  pt;<br>} |

So for every line segment with tangents, we can make a parametric polynomial. There is one problem though. We don't have tangents.

We have the gradient, which is orthogonal to the tangent, but there are two possible tangents in every point. The tangent can be oriented left or right from the gradient.

But this is solvable. Let's just pick the direction we like and keep it consistent.

Let the curves that originally come from horizontally oriented segments always have both tangents that way that *dx > 0*. And the ones that come from vertically oriented segments, will have *dy > 0*.

It looks like we have enough parts to assemble an algorithm.

## Creating splines from the pixels

Let's split our vectorization into two parts. First, we'll get points and tangents for every line segment from the pixels. Then we'll turn it all into polynomial splines.

The function that does the first part looks like this.

|     |
| --- |
| function  turn_pixels_into_points_and_tangents(pixels, threshold) { var  points = []; var  tangents = []; // "horizontal" pieces   for(var  i = 0; i <= pixels.length; i += 1) { var  old_point = []; var  old_tangent = []; for(var  j = 0; j <= pixels[0].length; j += 1) { // if right, left, top, and bottom pixels have a sign change,  // there should be a spline there  var  sign_change_on_the_right = (pixel_in(pixels, i-1, j+0) - threshold) * (pixel_in(pixels, i+0, j+0) - threshold) < 0; var  sign_change_on_the_left = (pixel_in(pixels, i-1, j-1) - threshold) * (pixel_in(pixels, i+0, j-1) - threshold) < 0; var  sign_change_on_the_bottom = (pixel_in(pixels, i+0, j-1) - threshold) * (pixel_in(pixels, i+0, j+0) - threshold) < 0; var  sign_change_on_the_top = (pixel_in(pixels, i-1, j-1) - threshold) * (pixel_in(pixels, i-1, j+0) - threshold) < 0; if(sign_change_on_the_right \|\| sign_change_on_the_left) { // fits the point on a threshold isoline  var  point = fit_point_better(pixels, threshold, [j, i]); var  g = gradient(pixels, point[0], point[1]);  // we want our tangent to be X-positive for horizontal pieces  var  tangent = g[1] >= 0 ? [g[1], -g[0]] : [-g[1], g[0]];  // this is an T or X junction, the tangent is ambiguous  if(sign_change_on_the_left + sign_change_on_the_right + sign_change_on_the_top + sign_change_on_the_bottom > 2) tangent = [0., 0.];  // store the point+tangent and the previous point+tangent  // if there is one  if(sign_change_on_the_left && old_point) { points.push([old_point, point]); tangents.push([old_tangent, tangent]);<br>}  // save the point+tangent for later  if(sign_change_on_the_right) { old_point = point; old_tangent = tangent;<br>} } }<br>} // "vertical" pieces  for(var  j = 0; j <= pixels[0].length; j += 1) { var  old_point = []; var  old_tangent = []; for(var  i = 0; i <= pixels.length; i += 1) { var  sign_change_on_the_right = (pixel_in(pixels, i-1, j+0) - threshold) * (pixel_in(pixels, i+0, j+0) - threshold) < 0; var  sign_change_on_the_left = (pixel_in(pixels, i-1, j-1) - threshold) * (pixel_in(pixels, i+0, j-1) - threshold) < 0; var  sign_change_on_the_bottom = (pixel_in(pixels, i+0, j-1) - threshold) * (pixel_in(pixels, i+0, j+0) - threshold) < 0; var  sign_change_on_the_top = (pixel_in(pixels, i-1, j-1) - threshold) * (pixel_in(pixels, i-1, j+0) - threshold) < 0; if(sign_change_on_the_bottom \|\| sign_change_on_the_top) { var  point = fit_point_better(pixels, threshold, [j, i]); var  g = gradient(pixels, point[0], point[1]); var  tangent = g[0] < 0 ? [g[1], -g[0]] : [-g[1], g[0]]; if(sign_change_on_the_left + sign_change_on_the_right + sign_change_on_the_top + sign_change_on_the_bottom > 2) tangent = [0., 0.]; if(sign_change_on_the_top && old_point) { points.push([old_point, point]); tangents.push([old_tangent, tangent]);<br>} if(sign_change_on_the_bottom) { old_point = point; old_tangent = tangent;<br>} } }<br>} return [points, tangents];<br>} |

And the one that does the second part — like this.

|     |
| --- |
| function  turn_points_and_tangents_into_splines(points_and_tangents)<br>{ var  splines = []; var  points = points_and_tangents[0]; var  tangents = points_and_tangents[1]; for(var  i = 0; i < points.length; ++i) { var  Px = spline_for( points[i][0][0], tangents[i][0][0], points[i][1][0], tangents[i][1][0]); var  Py = spline_for( points[i][0][1], tangents[i][0][1], points[i][1][1], tangents[i][1][1]); splines.push([Px, Py]);<br>} return  splines} |

This split is not essential for the algorithm, but it makes it possible to edit the model in both image and spline representation.

## Import, edit, export

Now, when we have the algorithm, let's see how it works in practice. Let's import a gray-scale image from PGM, turn it into splines, edit them, then export them as SVG.

PGM is a 1-channel ASCII image format. You can make a PGM file in GIMP or any other raster image editor.

Grey value threshold:

When the image is imported, we can either edit the source image pixel-by-pixel or move the splines' points and tangents. Click on a canvas to increase a pixel's luminosity. Click holding the Shift key to reduce it. Please note that in this example, image editing overrides vectors.

 ![](../_resources/7a12d9efb0c53f04916e75e09acff327.png)
Click to edit: image;   points;   tangents;

When you're happy with the splines, you can export them in SVG. In this example, only the outline is supported. No filling, no coloring.

You don't have to export the polynomials. SVG supports Bezier curves, and they are basically the same as cubics. Only instead of coefficients, you write down the control points.

The first point is the starting point of the spline. The second is the sum of the first point and one-third of a tangent vector. The third is the subtraction of the finishing point of the spline and the one-third of a second tangent. The fourth is the finishing point of the spline.

The code for the export function, just as all the code mentioned here including the visuals, is available [on Github](https://github.com/akalenuk/wordsandbuttons/blob/master/pages/simple_image_vectorization.html).

## Conclusion

The algorithm shows how bilinear interpolation, polynomial approximation, differential analysis, and iterative algorithms work together to solve a practical problem.

I hope this page will not only satisfy one's curiosity but help someone retain inspiration while studying these things. I know from my experience that basic calculus while being not more complicated than the traffic code, is particularly hard to learn because you don't see the application right away. You learn about series, limits, derivatives, integrals, and for what reason? How do you turn this knowledge into something useful?

Well, this is one of the many examples.

|     |     |     |
| --- | --- | --- |
|  [![](../_resources/f40ceaef9a95b0e6c77e3de01c2c1a67.png)](https://wordsandbuttons.online/index.html) |  ← there's more. | + [Github](https://github.com/akalenuk/wordsandbuttons) & [Twitter](https://twitter.com/wordsandbuttons) & [Hacker News](https://news.ycombinator.com/from?site=wordsandbuttons.online) |