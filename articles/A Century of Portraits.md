A Century of Portraits

# A Century of Portraits:

A Visual Historical Record of American High School Yearbooks

 ![decade_averages_labelled.png](../_resources/29cf7f4adc03aec52ac124e7e8e63b03.png)
Average images of high school students for each decade of the 20th century.

## Abstract

Many details about our world are not captured in written records because they are too mundane or too abstract to describe in words. Fortunately, since the invention of the camera, an ever-increasing number of photographs capture much of this otherwise lost information. This plethora of artifacts documenting our “visual culture” is a treasure trove of knowledge as yet untapped by historians. We present a dataset of 37,921 frontal-facing American high school yearbook photos that allow us to use computation to glimpse into the historical visual record too voluminous to be evaluated manually. The collected portraits provide a constant visual frame of reference with varying content. We can therefore use them to consider issues such as a decade’s defining style elements, or trends in fashion and social norms over time. We demonstrate that our historical image dataset may be used together with weakly-supervised data-driven techniques to perform scalable historical analysis of large image corpora with minimal human effort, much in the same way that large text corpora together with natural lan- guage processing revolutionized historians’ workflow. Furthermore, we demonstrate the use of our dataset in dating grayscale portraits using deep learning methods.

## People

- [Shiry Ginosar](http://www.eecs.berkeley.edu/~shiry/)
- [Kate Rakelly](http://people.eecs.berkeley.edu/~rakelly/)
- [Sarah Sachs](http://www.sarahmsachs.com/) (Brown University)
- [Brian Yin](http://www.linkedin.com/pub/brian-yin/86/143/b83)
- [Alexei A. Efros](http://www.eecs.berkeley.edu/~efros/)

## Paper

- [![Ginosar15_yearbooks.png](../_resources/39e635c256deab5aef1b1f7d4421567f.png)](http://people.eecs.berkeley.edu/~shiry/publications/IEEE_yearbooks.pdf)

#### A Century of Portraits: A Visual Historical Record of American High School Yearbooks

 **Shiry Ginosar**, Kate Rakelly, Sarah Sachs, Brian Yin, Alexei A. Efros *A Century of Portraits: A Visual Historical Record of American High School Yearbooks*, **To Appear in** Extreme Imaging Workshop, International Conference on Computer Vision, ICCV 2015. **and** IEEE Transactions on Computational Imaging, September 2017. [PDF](http://people.eecs.berkeley.edu/~shiry/publications/IEEE_yearbooks.pdf), [BibTeX](http://people.eecs.berkeley.edu/~shiry/projects/yearbooks/yearbooks.html#yearbooks)

## Sample Results

### The Top Trends of Each Decade

 ![disc_decades_detail.png](../_resources/eede276480e7d65e54b9bbdae7820009.png)

Discriminative clusters of high school girls’ styles from the 1960's and 1970's. The left-most entry in each row displays the cluster average. Note that the clusters correspond to the quintessential hair and accessory styles of each decade: The bob, “winged” flip, bubble cut and signature glasses of the 60's. The long hair, Afros and bouffants of the 70's. These fashions emerge from the data in a weakly-supervised, data-driven process.

### The Evolution of Smiles in Photographs

Video courtesy of [Slate.com](http://www.slate.com/)

 ![all_avg_lip_curve_5yr_std.png](../_resources/eab73f6f97f206fa367b516025a0b573.png)

Smiles increasing over time, but women always smile more than men: Male and female Average lip curvature by year with one STD error bars.

## Dataset

- [![](../_resources/4a52ec4966402b8039ea7af5121146aa.png)](https://www.dropbox.com/s/ubjjoo0b2wz4vgz/faces_aligned_small_mirrored_co_aligned_cropped_cleaned.tar.gz?dl=0)

#### The Yearbook Dataset

The [Yearbook Dataset](https://www.dropbox.com/s/ubjjoo0b2wz4vgz/faces_aligned_small_mirrored_co_aligned_cropped_cleaned.tar.gz?dl=0) of frontal-facing American high-school seniors from 1905 to 2013 is hosted on space donated by [Dropbox](https://www.dropbox.com/). All faces are aligned using an affine transformation in a process described in the paper.

The training and test lists for female faces used in the paper are also provided.

If you would like to obtain other formats of the data (raw images, non-frontal facing portraits etc) or, alternatively, if you would like to **contribute** more yearbook data send us an email to: <shiry at eecs dot berkeley dot edu>.

## Trained Dating Models

 [Caffe](http://caffe.berkeleyvision.org/) trained dating models on [Model Zoo](https://github.com/BVLC/caffe/wiki/Model-Zoo#yearbook-photo-dating).

## Popular Press

### Radio and Television

 [![](../_resources/147eb363eb7af3aa935a929055a391b4.png)](http://www.today.com/health/smile-or-not-smile-evolution-faces-photos-over-100-years-t59016)

 [![](../_resources/8fa5e8cda27008efea75305e96ee3aca.png)](https://www.youtube.com/watch?v=upZBLqwDpS0)

 [![](../_resources/7ac3116ee75a0861bdbc31bade6a9070.png)](http://www.cbc.ca/radio/spark/304-yearbook-photo-analysis-social-media-imposters-and-more-1.3366518/what-your-yearbook-photo-says-about-social-evolution-1.3368450)

### Printed News and Blogs

 [![](../_resources/ccacac8009b6e25d37a15bc20a1f3480.png)](https://www.washingtonpost.com/news/wonk/wp/2015/12/01/researchers-have-discovered-a-surprising-reason-we-smile-in-photos/)

 [![](../_resources/c5fde49258b1000bcc688675bf221980.png)](http://www.technologyreview.com/view/543871/data-mining-reveals-how-smiling-evolved-during-a-century-of-yearbook-photos/)

 [![2000px-Wired_logo.svg.png](../_resources/aeee8ce1ec5ec57f4760bebc9d7001b7.png)](http://www.wired.co.uk/news/archive/2015-11/24/evolution-of-smiles-data-mining)

 [![](../_resources/90850a7791b704597c648e8dfec97c94.png)](http://www.slate.com/blogs/the_vault/2015/12/07/history_of_the_american_yearbook_photo.html)

 [![](../_resources/81a2507c8e696fff7c110a4350e6c406.png)](http://www.techtimes.com/articles/110383/20151126/software-reveals-how-smiling-evolved-during-100-years-of-yearbook-photos.htm)

 [![](../_resources/3d41e0e19470baaa11b28978f7f15125.png)](http://petapixel.com/2015/11/27/this-is-how-smiles-in-yearbook-photos-have-changed-over-the-past-100-years/)

 [![](../_resources/d2665a9e3b766a569f97641ef2aba1cd.png)](http://www.engadget.com/2015/11/27/yearbook-photos-evolution/)

 [![medical_daily.gif](../_resources/11bd9924b2be18f00109f43f541560d1.gif)](http://www.medicaldaily.com/say-cheese-yearkbook-photos-show-how-our-smiles-have-changed-last-100-years-364212)

 [![](../_resources/1cadce717dbdc99854be19eff953a679.png)](http://www.netzpiloten.de/algorithmus-fotografie-berkely-studie/)

 [![stern.svg.png](../_resources/9bccc4e36b2eed503d431ea7439f6060.png)](http://www.stern.de/panorama/wissen/mensch/portraetfotos-von-1900-bis-heute---evolution-des-laechelns-6578382.html)

 [![](../_resources/97a0327db711640bb9e0ce3ff58e2562.png)](http://www.smh.com.au/technology/sci-tech/the-evolution-of-the-smile-captured-in-100-years-of-yearbook-photos-20151127-gl9jhv.html)

 [![](../_resources/1d7211e71913cdbcc3f1671c3b1f17c4.png)](http://www.smithsonianmag.com/smart-news/yearbook-photos-show-how-smiles-have-widened-over-decades-180957437/?no-ist)

 [![](../_resources/fcbea64f028dbbfe8b7e9a93306bf18d.png)](http://www.refinery29.com/2015/11/98385/smiling-evolution-photography-yearbook-photos)

 [![](../_resources/b022ee06f3c0eafd976114b759895797.png)](http://www.livescience.com/53020-how-yearbook-photos-changed.html)

## Funding

This material is based upon work supported by the NSF Graduate Research Fellowship DGE 1106400, ONR MURI N000141010934 and an NVidia hardware grant.

## See Also

Developed concurrently and independent from our work, Prof. [Nathan Jacobs](http://cs.uky.edu/~jacobs/)' group at the University of Kentucky also proposed using yearbook data for [dating images](http://cs.uky.edu/~jacobs/papers/salem2016f2y.pdf).

 [Patrick Feaster](http://www.phonozoic.net/) from Indiana University Bloomington published a fascinating blog post in 2014 [using face averaging in yearbook photographs to track the rise of the photo smile](https://griffonagedotcom.wordpress.com/2014/12/18/say-cheese-using-face-averaging-to-track-the-rise-of-the-photo-smile/). He also provides several hypotheses on why smiles came to be the norm in portraiture.

 [Jason Salavon](https://en.wikipedia.org/wiki/Jason_Salavon), an American contemporary artist and an Associate Professor at The University of Chicago, created a piece in 1998 from average images of personally-significant yearbook photographs. In his work titled [The Class of 1988 & The Class of 1967](http://www.salavon.com/work/Class/), he presents averages of all the male and female students of his graduating class of 1988 and contrasts them with averages of the students in his mother's graduating class of 1967 from the same hometown of Fort Worth, Texas.