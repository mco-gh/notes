Talk, then code | Dave Cheney

# Talk, then code

The open source projects that I contribute to follow a philosophy which I describe as *talk, then code*. I think this is generally a good way to develop software and I want to spend a little time talking about the benefits of this methodology.

### Avoiding hurt feelings

The most important reason for discussing the change you want to make is it avoids hurt feelings. Often I see a contributor work hard in isolation on a pull request only to find their work is rejected. This can be for a bunch of reasons; the PR is too large, the PR doesn’t follow the local style, the PR fixes an issue which wasn’t important to the project or was recently fixed indirectly, and many more.

The underlying cause of all these issues is a lack of communication. The goal of the *talk, then code* philosophy is not to impede or frustrate, but to ensure that a feature lands correctly the first time, without incurring significant maintenance debt, and neither the author of the change, or the reviewer, has to carry the emotional burden of dealing with hurt feelings when a change appears out of the blue with an implicit “well, I’ve done the work, all you have to do is merge it, right?”

### What does discussion look like?

Every new feature or bug fix should be discussed with the maintainer(s) of the project before work commences. It’s fine to experiment privately, but do not send a change without discussing it first.

The definition of *talk* for simple changes can be as little as a design sketch in a GitHub issue. If your PR fixes a bug, you should link to the bug it fixes. If there isn’t one, you should raise a bug and wait for the maintainers to acknowledge it before sending a PR. This might seem a little backward–who wouldn’t want a bug fixed–but consider the bug could be a misunderstanding in how the software works or it could be a symptom of a larger problem that needs further investigation.

For more complicated changes, especially feature requests, I recommend that a design document be circulated and agreed upon before sending code. This doesn’t have to be a full blown document, a sketch in an issue may be sufficient, but the key is to reach agreement using words, before locking it in stone with code.

In all cases you shouldn’t proceed to send code until there is a positive agreement from the maintainer that the approach is one they are happy with. A pull request is for life, not just for Christmas.

### Code review, not design by committee

A code review is not the place for arguments about design. This is for two reasons. First, most code review tools are not suitable for long comment threads, GitHub’s PR interface is very bad at this, Gerrit is better, but few have a team of admins to maintain a Gerrit instance. More importantly, disagreements at the code review stage suggests there wasn’t agreement on how the change should be implemented.

* * *

Talk about what you want to code, then code what you talked about. Please don’t do it the other way around.

### Related posts:

1. [How to include C code in your Go package](https://dave.cheney.net/2013/09/07/how-to-include-c-code-in-your-go-package)

2. [Let’s talk about logging](https://dave.cheney.net/2015/11/05/lets-talk-about-logging)

3. [The value of TDD](https://dave.cheney.net/2016/04/11/the-value-of-tdd)

4. [Suggestions for contributing to an Open Source project](https://dave.cheney.net/2016/03/12/suggestions-for-contributing-to-an-open-source-project)

This entry was posted in [Programming](https://dave.cheney.net/category/programming-2), [Small ideas](https://dave.cheney.net/category/small-ideas) and tagged [contributing](https://dave.cheney.net/tag/contributing), [open source](https://dave.cheney.net/tag/open-source) on [February 18, 2019](https://dave.cheney.net/2019/02/18/talk-then-code).