Microsoft, Google Beat Humans at Image Recognition | EE Times

![industrial-control-designline-secondary.gif](../_resources/7201d1143246b674069cc605d8a5ad7d.gif)

News & Analysis

# Microsoft, Google Beat Humans at Image Recognition

Deep learning algorithms compete at ImageNet challenge

[**R. Colin Johnson**](https://www.eetimes.com/profile.asp?piddl_userid=42105)

2/18/2015 08:15 AM EST
[14 comments](https://www.eetimes.com/document.asp?doc_id=1325712#msgs)

![GooglePlus_Button.jpg](../_resources/f4873a85d1f9b6e75f6b947703c507ca.gif)
![spacer.gif](../_resources/f4873a85d1f9b6e75f6b947703c507ca.gif)
![eetimes_rating_dot_10x7.gif](../_resources/f4873a85d1f9b6e75f6b947703c507ca.gif)

1 saves

- [Login to Rate](#)

|     |
| --- |
|     |

[**Tweet](https://twitter.com/intent/tweet?original_referer=https%3A%2F%2Fwww.eetimes.com%2Fdocument.asp%3Fdoc_id%3D1325712&ref_src=twsrc%5Etfw&text=Microsoft%2C%20Google%20Beat%20Humans%20at%20Image%20Recognition%20%7C%20EE%20Times&tw_p=tweetbutton&url=https%3A%2F%2Fwww.eetimes.com%2Fdocument.asp%3Fdoc_id%3D1325712&via=eetimes)

[inShare.](#)51

[(L)](https://plus.google.com/share?app=110&url=https%3A%2F%2Fwww.eetimes.com%2Fdocument.asp%3Fdoc_id%3D1325712)

PORTLAND, Ore. -- First computers beat the best of us at [chess](https://www.eetimes.com/document.asp?doc_id=1210114), then [poker](https://www.eetimes.com/document.asp?doc_id=1168863), and finally [Jeopardy](https://www.eetimes.com/document.asp?doc_id=1258562). The next hurdle is image recognition — surely a computer can't do that as well as a human. Check that one off the list, too. Now Microsoft has programmed the first computer to beat the humans at image recognition.

The competition is fierce, with the [ImageNet Large Scale Visual Recognition Challenge](http://image-net.org/) doing the judging for the 2015 championship on December 17. Between now and then expect to see a stream of papers claiming they have one-upped humans too. For instance, only 5 days after Microsoft announced it had beat the human benchmark of 5.1% errors with a 4.94% error grabbing neural network, Google announced it had one-upped Microsoft by 0.04%.

[![The top row is a representative of the categories that Microsoft's algorithm found in the database and the image columns below are examples that fit.(Source: Microsoft)](../_resources/32c9269677f85642bcaaa13bbfc0d7f1.jpg)](https://www.eetimes.com/document.asp?doc_id=1325712&image_number=1)

The top row is a representative of the categories that Microsoft's algorithm found in the database and the image columns below are examples that fit.

(Source: Microsoft)

ImageNet, with hundreds of object categories and millions of example images, has been running the competition since 2010 with about 50 institutions competing, but this is the first year than a computer will take the crown from the best human score. All the contestants are using what today is called deep learning algorithms, which are all derived from various versions of artificial neural networks which mimic the way the human brain works to varying degrees. Most of the contestants freely provide papers describing their algorithm in great detail -- in the spirit of open source without providing the exact code -- explaining why their algorithm worked so well. Here [Microsoft](http://arxiv.org/pdf/1502.01852.pdf) revealed it was using deep convolutional neural networks (CNNs) with 30 weight layers. [Google](http://arxiv.org/pdf/1502.03167.pdf) revealed its batch normalization technique that keeps from saturating neurons during initialization.

"In previous work, the neural units were hand-designed and fixed during training. In contrast, we make the units smarter by allowing them to take a more flexible form," Jian Sun, principal researcher for the Visual Computing Group, Microsoft Research Asia told EE Times. "More importantly, the particular form of each unit is learned by end-to-end training. We observed that introducing smarter units can considerably improve the model."

When questioned further as to why their current neural network was able to take the crown as the first to beat the human experts, Sun responded by citing details of its Deep Learning algorithm, which usually initializes by training on 1.2 million training images, then verifies on 50,000 validation images, and finally applies what it learned to 100,000 test images in the main image database. Microsoft, however, took a slightly different tactic.

"A robust initialization method, as a part of training algorithm, was needed since training very deep neural networks is difficult. Previous work either resorts to pre-training or adding auxiliary training tasks. In our work, we derive a theoretically sound initialization method which allows us to freely exploit more powerful -- deeper and wider -- neural networks," Sun told EE Times.

Nvidia is a sponsor of the annual ImageNet Challenge, and supplies access to arrays of its graphic processing units (GPUs) to all contestants. Microsoft did use Nvidia GPUs, but bought and configured their own supercomputer using them to simulate parametric rectified linear neural units to become the "1st to beat a human" at image classification.

The teams results are already being applied to Microsoft's Bing image search and OneDrive. Sun's team consisted of Kaiming He, at Microsoft Research Asia’s Visual Computing Group, and two academic interns, Xiangyu Zhang of Xi’an Jiaotong University and Shaoqing Ren of the University of Science and Technology of China.

— R. Colin Johnson, Advanced Technology Editor, [EE Times](https://www.eetimes.com/)  [(L)](https://plus.google.com/+RColinJohnson/posts)

**Related articles:**

- [Electronic Brain by 2023](https://www.eetimes.com/document.asp?doc_id=1324121)
- [Neurogrid's Electronic Brain Controls Robotics](https://www.eetimes.com/document.asp?doc_id=1322206)
- [IBM's Watson computer beats humans at Jeopardy](https://www.eetimes.com/document.asp?doc_id=1258562)
- [The Next Generation of Chess Playing Machines is Introduced by IBM By Tets Maniwa](https://www.eetimes.com/document.asp?doc_id=1210114)
- [AI beats human poker champions](https://www.eetimes.com/document.asp?doc_id=1168863)