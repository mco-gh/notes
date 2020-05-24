Deep Learning is Eating Software

[(L)](https://petewarden.com/2017/11/13/deep-learning-is-eating-software/)

# Deep Learning is Eating Software

*[November 13, 2017](https://petewarden.com/2017/11/13/deep-learning-is-eating-software/)*  *   By   [Pete Warden](https://petewarden.com/author/petewarden/)*  *in [Uncategorized](https://petewarden.com/category/uncategorized/)**[9 Comments](https://petewarden.com/2017/11/13/deep-learning-is-eating-software/#comments)*

![pacman](../_resources/94052bff0e807cdce0a6e473a18ed943.png)

*[Photo by John Watson](https://www.flickr.com/photos/john/2252140144/in/photolist-4r1NNu-2UYGXU-pjNtMR-gFYA6-djo9Kn-zDRnn-6apFK7-8WggdV-5W7ymz-5rapuC-aMa3i-4DpYfH-bGNzAk-79RQvS-6Pftz7-53Lys-49DS1j-Duf4n-3CXPer-aMa3g-9cy9Qr-5W7xQz-bvqZ3n-9XEYgq-e18yX3-6tpEQc-fswp5H-4r1YDz-7hpcwZ-3YdJs-6y9fsH-nnEmmt-JnnmX9-qWNUC-8PDYvL-5SV7uK-6tEgpz-b5CvGv-9bVBHR-2GnPF-9DuqJJ-5dGts6-7yC3f7-yHewN-9uE4zw-9yMnr-syfp3-e1RHUZ-7Q3tV-idqiU)*

When I had a drink with Andrej Karpathy a couple of weeks ago, we got to talking about where we thought machine learning was going over the next few years. Andrej threw out the phrase “Software 2.0”, and I was instantly jealous because it captured the process I see happening every day across hundreds of projects. I held my tongue until he got [his blog post out there](https://medium.com/@karpathy/software-2-0-a64152b37c35), but now I want to expand my thoughts on this too.

The pattern is that there’s an existing software project doing data processing using explicit programming logic, and the team charged with maintaining it find they can replace it with a deep-learning-based solution. I can only point to examples within Alphabet that we’ve made public, like [upgrading search ranking](https://www.wired.com/2016/02/ai-is-changing-the-technology-behind-google-searches/), [data center energy usage](https://deepmind.com/blog/deepmind-ai-reduces-google-data-centre-cooling-bill-40/), [language translation](https://en.wikipedia.org/wiki/Google_Neural_Machine_Translation), and [solving Go](https://deepmind.com/blog/alphago-zero-learning-scratch/), but these aren’t rare exceptions internally. What I see is that almost any data processing system with non-trivial logic can be improved significantly by applying modern machine learning.

This might sound less than dramatic when put in those terms, but it’s a radical change in how we build software. Instead of writing and maintaining intricate, layered tangles of logic, the developer has to become [a teacher](https://petewarden.com/2014/06/06/how-i-teach-computers-to-think/), a curator of training data and an analyst of results. This is very, very different than the programming I was taught in school, but what gets me most excited is that it should be far more accessible than traditional coding, once the tooling catches up.

The essence of the process is providing a lot of examples of inputs, and what you expect for the outputs. This doesn’t require the same technical skills as traditional programming, but it does need a deep knowledge of the problem domain. That means motivated users of the software will be able to play much more of a direct role in building it than has ever been possible. In essence, the users are writing their own user stories and feeding them into the machinery to build what they want.

Andrej focuses on areas like audio and speech recognition in his post, but I’m actually arguing that there will be an impact across many more domains. The classic “[Machine Learning: The High-Interest Credit Card of Technical Debt](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/43146.pdf)” identifies a very common pattern where machine learning systems become embedded in deep stacks of software. What I’m seeing is that the problem is increasingly solved by replacing the whole stack with a deep learning model! Taking the analogy to breaking point, this is like consolidating all your debts into a single loan with lower payments. A single model is far easier to improve than a set of deeply interconnected modules, and the maintenance becomes far easier. For many large systems there’s no one person who can claim to understand what they’re actually doing anyway, so there’s no real loss in debuggability or control.

I know this will all sound like more deep learning hype, and if I wasn’t in the position of seeing the process happening every day I’d find it hard to swallow too, but this is real. Bill Gates is supposed to have said “*Most people overestimate what they can do in one year and underestimate what they can do in ten years*“, and this is how I feel about the replacement of traditional software with deep learning. There will be a long ramp-up as knowledge diffuses through the developer community, but in ten years I predict most software jobs won’t involve programming. As Andrej memorably puts it, “[deep learning] is better than you”!

### Share this:

- [Twitter](https://petewarden.com/2017/11/13/deep-learning-is-eating-software/?share=twitter&nb=1)
- [Facebook351](https://petewarden.com/2017/11/13/deep-learning-is-eating-software/?share=facebook&nb=1)
- [Google](https://petewarden.com/2017/11/13/deep-learning-is-eating-software/?share=google-plus-1&nb=1)

-
[Like](https://widgets.wp.com/likes/#)

- [![hanxue](../_resources/1f6e89fa18824892273911515f7dcdbb.jpg)](https://en.gravatar.com/leehanxue)
- [![mhneifer](../_resources/0a2a145390dc5fe1ea09e21dc9c82800.png)](https://en.gravatar.com/howlingneifer)
- [![Didi Oviatt - Author](../_resources/8b91dde8ab3296ec1184c6b304defbee.jpg)](https://en.gravatar.com/didioviatt)

[3 bloggers](https://widgets.wp.com/likes/#) like this.

### *Related*

[How to optimize Raspberry Pi code using its GPU](https://petewarden.com/2014/08/07/how-to-optimize-raspberry-pi-code-using-its-gpu/)With 48 comments

[How I got sued by Facebook](https://petewarden.com/2010/04/05/how-i-got-sued-by-facebook/)With 43 comments

[How to break into machine learning](https://petewarden.com/2016/04/18/how-to-break-into-machine-learning/)With 8 comments

.