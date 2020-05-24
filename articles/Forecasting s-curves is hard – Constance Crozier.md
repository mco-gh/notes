Forecasting s-curves is hard – Constance Crozier

# Forecasting s-curves is hard

S-curves (or sigmoid functions) are commonly used to model the evolution of social or biological systems over time [1]. These functions start with exponential growth, then increase linearly, and finally level off (therefore end up looking like a wonky s). Many things that we think of as exponential functions will actually follow an s-curve (otherwise the system would reach infinity). One famous example is the adoption of a new technology. The graph below shows the percentage of US adults who own a smartphone over time, with a best-fit s-curve imposed on the top. In this case the exponential growth occurs because of the way publicity and supply are rolled out. However, there are only a limited number of potential consumers (some of whom will never get a smartphone) and so the growth gradually slows to zero.

![smart_phones.png](../_resources/a5f95fd233bc9f18d71a96b7ad9ea3b8.png)
US smartphone ownership [2]

Another example, and the reason that these curves have been back in the news, is the propagation of disease. In this case the exponential growth occurs when the virus is new, such that most people encountering it will not have developed immunity. The level-off occurs because the virus is no longer encountering people without immunity (either due to ‘herd immunity’ or isolation of those infected). The graph below shows the number of deaths in China from the SARS outbreak in 2003, again with a best-fit s-curve.

![sars-1.png](../_resources/fe841a5d1e736be0d9cd1c4204a68de1.png)
Deaths due to SARS in China [3]

S-curves have only three parameters, and so it is perhaps impressive that they fit a variety of systems so well. Broadly, the three parameters describe the initial growth rate, the level-off rate, and the value at which it levels-off. Therefore, if you can estimate these three numbers, then you have the trend curve. Many of us will have learnt in school that if there are three parameters to be found, you need three data points to define the function. This would suggest that you could perfectly predict the level-off point based on only three observations (spoiler: you can’t).

In reality, while we can say that the overall trend of the data is likely to fit to some s-curve, the individual points will not all lie along it. This can be seen in both of the previous examples. This discrepancy is often described as ‘modelling error’, which comprises both errors in the measurement of the data, and the fact that the s-curve model is fundamentally wrong. To quote George Box “all models are wrong, but some are useful”.

Intuitively, it makes sense that it should not be possible to forecast the curve from the early data; to assume this, means believing that we can’t affect the outcome. However, in my experience “intuition” and “mathematics” can often be hard to reconcile. Therefore, I decided to investigate how much the “best fit s-curve” changes as more data becomes available. Below is a s-curve that I chose at random. The points shown are “noisy observations” – which is the maths-y way of saying ‘points from the curve with a random amount of error applied’.

![witgh_data.png](../_resources/c3fe74a962a0263d479c08eb51eaca48.png)

In this case, the s-curve model is a perfect fit – I have literally generated the data from an s-curve. This means that if there was zero error then we would only need three points to find the curve. All this to say, that this example is idealistic – in reality there is unlikely to be a curve that fits the data so well. Below is an animation showing the best fit s-curve (found using a least squares optimisation) as more data becomes available.

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='vp-spin-trace js-evernote-checked' viewBox='0 0 50 50' focusable='false' data-evernote-id='3'%3e%3ccircle cx='50%25' cy='50%25' r='20' data-evernote-id='61' class='js-evernote-checked'%3e%3c/circle%3e%3c/svg%3e)![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='vp-spin-circle js-evernote-checked' viewBox='0 0 50 50' focusable='false' data-evernote-id='4'%3e%3ccircle cx='50%25' cy='50%25' r='20' data-evernote-id='62' class='js-evernote-checked'%3e%3c/circle%3e%3c/svg%3e)

# [Staff Picks](https://vimeo.com/staffpicks)

- [  # After The Fall    ## from Matthew Freidell](https://vimeo.com/channels/staffpicks/405104495?from=outro-embed)
- [  # Second To None by Vincent Gallagher    ## from Second to None](https://vimeo.com/channels/staffpicks/407694202?from=outro-embed)
- [  # Apart / Spolu sami    ## from Diana Cam Van Nguyen](https://vimeo.com/channels/staffpicks/403252865?from=outro-embed)

 [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 140 40' preserveAspectRatio='xMidYMid' role='img' focusable='false' aria-labelledby='logo-icon-title' data-evernote-id='23' class='js-evernote-checked'%3e%3ctitle id='logo-icon-title' data-evernote-id='183' class='js-evernote-checked'%3eVimeo%3c/title%3e%3cg data-evernote-id='184' class='js-evernote-checked'%3e%3cpath class='fill logo-v js-evernote-checked' d='M31.277 18.832c-.14 3.052-2.27 7.229-6.39 12.531-4.259 5.536-7.863 8.306-10.811 8.306-1.825 0-3.371-1.687-4.633-5.059l-2.529-9.275c-.938-3.372-1.943-5.06-3.019-5.06-.234 0-1.054.494-2.458 1.477l-1.474-1.901c1.546-1.358 3.071-2.717 4.572-4.078 2.062-1.783 3.609-2.72 4.642-2.814 2.438-.234 3.938 1.433 4.502 5.001.608 3.851 1.03 6.246 1.266 7.182.704 3.195 1.476 4.791 2.321 4.791.657 0 1.641-1.037 2.954-3.108 1.312-2.072 2.015-3.649 2.109-4.732.188-1.789-.516-2.686-2.109-2.686-.75 0-1.522.173-2.318.514 1.54-5.044 4.481-7.495 8.823-7.355 3.22.095 4.737 2.184 4.552 6.266z' data-evernote-id='185'%3e%3c/path%3e%3cpath class='fill logo-i js-evernote-checked' d='M50.613 28.713c-1.313 2.484-3.119 4.733-5.417 6.748-3.143 2.718-6.285 4.076-9.425 4.076-1.456 0-2.57-.469-3.343-1.406-.773-.938-1.137-2.153-1.09-3.653.045-1.548.526-3.938 1.441-7.173.914-3.232 1.373-4.967 1.373-5.201 0-1.218-.423-1.828-1.266-1.828-.282 0-1.079.494-2.393 1.477l-1.618-1.901c1.501-1.358 3.001-2.717 4.502-4.078 2.017-1.783 3.518-2.72 4.504-2.814 1.546-.14 2.684.314 3.411 1.367.726 1.052.996 2.417.81 4.098-.61 2.852-1.268 6.472-1.972 10.864-.046 2.01.681 3.014 2.182 3.014.656 0 1.827-.693 3.518-2.083 1.406-1.156 2.555-2.243 3.447-3.262l1.336 1.755zm-6.12-25.016c-.047 1.168-.633 2.288-1.76 3.361-1.266 1.212-2.767 1.82-4.501 1.82-2.672 0-3.963-1.166-3.869-3.499.045-1.213.76-2.381 2.144-3.501 1.384-1.119 2.919-1.68 4.609-1.68.984 0 1.805.387 2.462 1.155.656.772.961 1.553.915 2.344z' data-evernote-id='186'%3e%3c/path%3e%3cpath class='fill logo-m js-evernote-checked' d='M94.543 28.713c-1.314 2.484-3.117 4.733-5.416 6.748-3.145 2.718-6.285 4.076-9.426 4.076-3.051 0-4.527-1.687-4.432-5.06.045-1.501.338-3.306.877-5.415.539-2.108.832-3.748.879-4.921.049-1.779-.492-2.673-1.623-2.673-1.223 0-2.682 1.456-4.375 4.362-1.788 3.05-2.754 6.003-2.894 8.861-.095 2.02.103 3.568.592 4.645-3.272.096-5.565-.444-6.873-1.617-1.171-1.032-1.708-2.742-1.614-5.135.045-1.501.276-3.001.69-4.502.414-1.5.644-2.837.69-4.011.095-1.734-.54-2.604-1.9-2.604-1.177 0-2.444 1.339-3.806 4.011-1.361 2.673-2.113 5.465-2.253 8.371-.094 2.627.074 4.456.503 5.486-3.219.096-5.505-.582-6.857-2.035-1.122-1.214-1.634-3.06-1.539-5.54.044-1.214.258-2.911.645-5.084.386-2.175.603-3.87.647-5.087.093-.841-.119-1.263-.633-1.263-.281 0-1.079.475-2.393 1.424l-1.687-1.901c.234-.184 1.71-1.545 4.432-4.078 1.969-1.828 3.306-2.766 4.009-2.812 1.219-.095 2.204.409 2.954 1.511s1.126 2.38 1.126 3.834c0 .469-.047.915-.14 1.336.703-1.077 1.523-2.017 2.463-2.814 2.156-1.874 4.572-2.931 7.245-3.166 2.298-.187 3.938.352 4.925 1.617.795 1.033 1.17 2.511 1.125 4.433.329-.28.681-.586 1.056-.915 1.078-1.267 2.133-2.273 3.164-3.023 1.736-1.267 3.541-1.97 5.418-2.112 2.25-.187 3.867.35 4.852 1.611.844 1.028 1.219 2.5 1.127 4.415-.047 1.309-.363 3.213-.949 5.712-.588 2.501-.879 3.936-.879 4.31-.049.982.047 1.659.279 2.034.236.373.797.559 1.689.559.656 0 1.826-.693 3.518-2.083 1.406-1.156 2.555-2.243 3.447-3.262l1.337 1.757z' data-evernote-id='187'%3e%3c/path%3e%3cpath class='fill logo-e js-evernote-checked' d='M120.922 28.642c-1.361 2.249-4.033 4.495-8.02 6.743-4.971 2.856-10.012 4.284-15.125 4.284-3.797 0-6.52-1.267-8.16-3.797-1.172-1.735-1.734-3.797-1.688-6.189.045-3.797 1.736-7.407 5.064-10.832 3.658-3.75 7.973-5.627 12.945-5.627 4.596 0 7.033 1.873 7.314 5.615.188 2.384-1.125 4.842-3.938 7.368-3.004 2.76-6.781 4.515-11.328 5.263.842 1.169 2.109 1.752 3.799 1.752 3.375 0 7.059-.855 11.045-2.574 2.859-1.207 5.111-2.461 6.754-3.76l1.338 1.754zm-15.969-7.345c.045-1.259-.469-1.89-1.547-1.89-1.406 0-2.83.969-4.283 2.906-1.451 1.936-2.201 3.789-2.248 5.562-.025 0-.025.305 0 .911 2.295-.839 4.287-2.122 5.971-3.849 1.357-1.491 2.06-2.707 2.107-3.64z' data-evernote-id='188'%3e%3c/path%3e%3cpath class='fill logo-o js-evernote-checked' d='M140.018 23.926c-.189 4.31-1.781 8.031-4.783 11.169-3.002 3.137-6.73 4.706-11.186 4.706-3.705 0-6.52-1.195-8.441-3.585-1.404-1.777-2.182-4.001-2.32-6.668-.236-4.029 1.217-7.729 4.361-11.101 3.377-3.746 7.619-5.618 12.732-5.618 3.281 0 5.766 1.102 7.457 3.301 1.594 2.015 2.32 4.614 2.18 7.796zm-7.95-.264c.047-1.269-.129-2.434-.527-3.49-.4-1.057-.975-1.587-1.725-1.587-2.391 0-4.361 1.293-5.906 3.877-1.316 2.115-2.02 4.371-2.111 6.766-.049 1.176.164 2.21.633 3.104.514 1.032 1.242 1.549 2.182 1.549 2.109 0 3.914-1.244 5.416-3.735 1.267-2.068 1.945-4.23 2.038-6.484z' data-evernote-id='189'%3e%3c/path%3e%3c/g%3e%3c/svg%3e)](https://vimeo.com/408599958)

It may not be surprising that in the exponential growth phase the estimate is very bad, but even in the linear phase (when 40+ points are available) the correct curve has not been found. In fact, it is only once the data starts to level-off that the correct s-curve is found. This is especially unhelpful when you consider that it can be quite hard to tell which part of the curve you on; hindsight is 20-20.

This is not to say that it is impossible to model or predict s-curves. Only that, contextual information about the system you are modelling is likely required. For biological systems, are there physical parameters which govern the initial growth rate? For technological changes, can the final level-off be reasonably estimated? This information is application specific. In other words, data enthusiasts (such as myself) should leave the modelling up to the professionals.

**Edit: 20/04/20**

I’ve had several requests to share the code used to generate the animation. The optimisation I used is part of another project which I can’t share, but I have uploaded a script which should reproduce the animation [here](https://github.com/constancecrozier/blog_code/blob/master/scurve_animation.py).

R**eferences**

[1] Nieto et. al, “Performance analysis of technology using the S curve model: the case for digital signal procession technologies” 1998.

[2] Comscore Whitepaper: ‘The 2016 U.S. Mobile App Report”, September 13, 2016
[3] World Health Organisation https://www.who.int/csr/sars/country/en/

### **Share this:

- [Twitter](https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/?share=twitter&nb=1)
- [Facebook](https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/?share=facebook&nb=1)

-

[Like](https://widgets.wp.com/likes/index.html?ver=20190321#)

- [![952793cd8139441af257b0704766524b](../_resources/fb19f8dad68168c0929b5ec0cd225422.jpg)](https://en.gravatar.com/grjenkin)
- [![79398c0cdf7b336d4345ea075e159261](../_resources/0ac46676256f95b2351753a7680ba3a7.png)](https://en.gravatar.com/maxefremov)
- [![a73eb8e22f867c31c92d969838e6e0bc](../_resources/505c9cf24e11bc4251ee00061d0b84fc.png)](https://en.gravatar.com/trivialscientist)
- [![3bb65f771a0b31b87bc62d5120060579](../_resources/0106515e1c152179a1e9434993b0dcfe.jpg)](https://en.gravatar.com/jimrosenz)
- [![1c731cf1e4497d86714c39d8210309ae](../_resources/3c12e57272b7454838463cc6b5851915.png)](https://en.gravatar.com/carun13)
- [![10b5c39ff4ffe244e009100bbc4df11e](../_resources/a3ca5701c9f45cf278e546dd0ade5651.png)](https://en.gravatar.com/duncangh24)

[6 bloggers](https://widgets.wp.com/likes/index.html?ver=20190321#) like this.

[exponential growth](https://constancecrozier.com/tag/exponential-growth/)[extrapolation](https://constancecrozier.com/tag/extrapolation/)[forecasting](https://constancecrozier.com/tag/forecasting/)[s-curves](https://constancecrozier.com/tag/s-curves/)

Posted on [April 16, 2020](https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/) by [constance](https://constancecrozier.com/author/constancellc/) in [Uncategorized](https://constancecrozier.com/category/uncategorized/)[18](https://constancecrozier.com/2020/04/16/forecasting-s-curves-is-hard/#comments)