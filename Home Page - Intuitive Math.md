Home Page - Intuitive Math

![](../_resources/190788091e0ff3f405ebe79e48590368.png)

This is a math primer that is a little different. It is written using technologies such as React and WebGL with animated explanations of fields like Linear Algebra and Geometry designed to help you develop a visual intuition for what is going on. More fields will be added as time goes on.

![](../_resources/cd827a9adf1fdf21ff33019032767c78.png)

![](../_resources/539ecc09413ac6202f57b5d466bada65.png)
x=x=
y=y=
z=z=

The visualizations are partially interactive. They are done on sine-wave interpolations by default, but if a value is shown below the visualisation, in some cases, you can manually adjust it by dragging it from side to side, or just double-clicking and editing it. Animation will stop for that value as soon as you edit it, and you can undo the stopped animation by clicking the close button:.

Note that due to the limit on the number of concurrently running WebGL contexts implemented by most browsers, I have tried to use some smarts to disable contexts when they are not fully in view. So far, I have tested that this worked on Chrome and Firefox Quantum.

## Why did you write this?

I mainly wrote this to help me consolidate my own notes on the subjects since I personally have a hard time instantly developing an intuition for math. And without the intuition, I have a hard time applying math to problems because I will not know what the tools are actually for.

## Corrections, Errata

Given that I am not an expert in this area, its possible that I probably got something wrong. If you notice something that seems odd, you can reach me at s AT polysquare DOT org. Or, the code is open source, so you can just submit a [pull request](https://github.com/smspillaz/intuitive-math).