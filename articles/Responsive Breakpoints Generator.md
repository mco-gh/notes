Responsive Breakpoints Generator

   **[![](../_resources/8e53ae6b00a3960687eb742ad6be415f.png)](https://responsivebreakpoints.com/)**  **[Responsive Image Breakpoints Generator](https://responsivebreakpoints.com/)  *v2.0***  [(L)](https://responsivebreakpoints.com/#)

 **Easily generate the optimal responsive image dimensions**

One image for all screen resolutions and different devices is not enough. An image per pixel is too much - so how can someone automatically choose the optimal responsive image sizes?  [Learn more...](https://responsivebreakpoints.com/#intro-details)

     Upload file

Or select one of the predefined images

- *![woman_glasses.jpg](../_resources/956e41f0747543e659126853999365c3.jpg)*

- *![castle.jpg](../_resources/b165cebc7747bf6d594b20b0b0955f3a.jpg)*

- *![robot.png](../_resources/d62fd5b31f20f7b79d3ac7ba83e7d995.png)*

- *![dog.jpg](../_resources/0f7c42482c0da1a585abf7e6e778cc82.jpg)*

## Breakpoints generation settings

### Resolution

 From

 To

- 50

- 200

- 480

- 1080

- 2180

- 3840

### Size step

 Size (KB)

- 5KB

- 25KB

- 45KB

- 65KB

- 85KB

### Maximum images

 Quantity

- 3

- 10

- 18

- 25

- 33

- 40

### Retina resolution

   Include double resolution (DPR 2.0) images

### Art-direction - Image aspect-ratio and view-port ratio

- Desktops-    Original  40%

- Small laptops-    16:9  60%

- Tablets-    4:3  70%

- Smartphones-    1:1  100%

### Automate responsive breakpoints generation

You can use [Cloudinary's API](https://cloudinary.com/documentation/upload_images) to upload your images to the cloud and automatically generate breakpoints programmatically:

- [Ruby on Rails](https://responsivebreakpoints.com/#tab1)

- [Node.js](https://responsivebreakpoints.com/#tab2)

- [PHP](https://responsivebreakpoints.com/#tab3)

- [Python](https://responsivebreakpoints.com/#tab4)

 ``Cloudinary`::`Uploader`.upload(`"sample.jpg", `[[NEWLINE]]```responsive_breakpoints`: { `create_derived`: `true`, `bytes_step`: `20000`, `min_width`: `200`, `max_width`: `1000`, `transformation`: { `crop`: `:fill`, `aspect_ratio`: `"16:9"`, `gravity`: `:auto` } } )`

This [open source tool](https://github.com/cloudinary/responsive_breakpoints_generator) enables you to interactively generate responsive image breakpoints. However, for applications that involve user generated content of images dynamically uploaded to your site, you may want to streamline the breakpoints generation process. [Learn more...](https://cloudinary.com/blog/introducing_intelligent_responsive_image_breakpoints_solutions)

 **Powered by**  [![](../_resources/c3800df499bada79acb6115b11538fbe.png)](https://cloudinary.com/)

Cloudinary is the image back-end for web and mobile developers. An end-to-end solution for all your image-related needs. For more information visit [cloudinary.com](https://cloudinary.com/)

-

|     |     |
| --- | --- |
|     | [(L)](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fwww.facebook.com%2FResponsiveBreakpoints%2F&display=popup&ref=plugin&src=like&kid_directed_site=0&app_id=322099131162878) |

- [**Tweet](https://twitter.com/intent/tweet?hashtags=responsive&original_referer=https%3A%2F%2Fresponsivebreakpoints.com%2F&ref_src=twsrc%5Etfw&text=Responsive%20Image%20Breakpoints%20Generator%20by%20Cloudinary&tw_p=tweetbutton&url=https%3A%2F%2Fresponsivebreakpoints.com&via=cloudinary)

-

-

 [Privacy policy](https://cloudinary.com/privacy) and [Terms of service](https://responsivebreakpoints.com/tos)