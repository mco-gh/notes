Programming is Hard

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#what-programming-is-not-about) What programming is not about

Programming is not about mashing the keyboard and typing as fast as possible. It is not about religiously memorizing keyboard shortcuts and ultimately rendering the mouse obsolete. It is not about learning every single programming language out there, if that is even possible in the first place. A good programmer is not defined by the brand, price, performance, and operating system of their computer, nor by their preference of code editors and [IDEs](https://en.wikipedia.org/wiki/Integrated_development_environment)—[VS Code](https://code.visualstudio.com/), [Atom](https://atom.io/), [IntelliJ IDEA](https://www.jetbrains.com/idea/), [Vim](https://www.vim.org/), [Notepad++](https://notepad-plus-plus.org/), or otherwise. Contrary to popular belief thanks to many Hollywood films, programming is definitely *not* equivalent to hacking.

Furthermore, it goes beyond memorizing the syntax and built-in functionalities of a programming language. Logic, conditions, `if` statements, and algorithms—particularly those of sorting—do not paint a full picture of what programming truly is. Mathematics, recursion, computer science, and design patterns do not do justice to it either. Although they are a huge part of what programming is, they are only one piece of the puzzle.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#designing-and-planning) Designing and planning

Before writing a single line of code, the design and architecture of a project is thoroughly planned to ensure (or at least increase the likelihood of having) a smooth development cycle. This is where software design comes into play. Toolchains, pipelines, layers of abstractions for public and internal [APIs](https://en.wikipedia.org/wiki/Application_programming_interface), modularization, object relationships, and database structuring are all planned out during this stage of development.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#we-are-living-breathing-debuggers) We are living, breathing debuggers

The art of programming requires us to think outside the box and solve problems with the most pragmatic, effective, and feasible solutions. This is probably why we are most likely the "I.T. guy" or "customer support" of the household. It is practically our job to fix what is broken. It is as if "programming" is a glorified way of saying "problem solving".

In other words, we are living, breathing debuggers on and off our computers, and because of this, it is important that we know how to read and write documentation. Proper documentation—which comes in the form of actual pages of detailed documentation, or as simple as sprinkling worthwhile comments to the code base—serves as one of the most important lifelines of a programmer. Without it, we are lost in the dark, unable to fulfill our very duties as debuggers. Little to no progress can be made because most of our time would be spent on experimenting and investigating how a framework or legacy code base works. Overall, it would result in a terribly awful [developer experience](https://dev.to/samjarman/the-best-practices-for-a-great-developer-experience-dx-b3a).

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#consider-all-possible-scenarios) Consider all possible scenarios

Debugging is already hard enough as it is. To make matters worse, the execution of code is usually not linear. Large projects entail multiple "branches" of possible execution paths due to program logic with the `if` statement. We have to account for *every* single possible scenario and error, especially if it involves user input. The cognitive load required to keep track of *every* possible execution path makes programming all the more difficult.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#user-experience) User Experience

Stepping outside the world of development, we fill in the shoes of an average user. In addition to providing functionality, adding new features, fixing bugs, and documenting our code base, we also focus on how an average user interacts with our app or software. We consider multiple factors that lead to great user experience such as (but not limited to) accessibility, usability, user-friendliness and -discoverability, UI design, color themes, [functional animations](https://uxplanet.org/functional-animation-in-ux-design-what-makes-a-good-transition-d6e7b4344e5e), and performance.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#performance-and-optimization) Performance and Optimization

Speaking of which, performance is a huge facet of programming in itself. We, especially those with a background in computer science, strive to use and write the most time- and space-efficient algorithms. We obsess over the unfathomable time scale of microseconds in order to squeeze the most out of our available memory, CPUs, and GPUs.

In the context of web development, network optimization is an important concept to grasp. We jump through hoops to [minify](https://en.wikipedia.org/wiki/Minification_(programming)) and compress our HTML, CSS, and JavaScript just to minimize the payload of a response from the server. Images and other miscellaneous resources are also compressed and [lazy-loaded](https://developers.google.com/web/fundamentals/performance/lazy-loading-guidance/images-and-video/) to minimize the amount of data the user has to download before a page becomes meaningful and usable.

However, there are times when we become too obsessed with performance. **Premature optimization** becomes a problem when we unnecessarily preoccupy ourselves with optimizing certain parts of a code base instead of focusing on what needs to be done for actual progress and productivity. In that case, we must have the wisdom to judge which parts of the code base *really* need optimization.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#security) Security

Beyond the UI and logic of our software, as programmers, we are responsible for the security of our users. In our day and age where data is greatly coveted and heavily monetized, it is more important than ever to make sure that the personal information of our users are safe. We take extra steps in protecting private data because *our* users trust *our* software. If we do not uphold that responsibility, we are certainly *not* real programmers, not even by a longshot.

We can never be too safe when approaching security. As a general rule of thumb, we *"never trust user input"*. It can even be considered a "best practice" to go to great lengths to sanitize data and user input. Not only do we put our software and infrastracture at great risk if we are not careful with them, we also run the risk of compromising sensitive user data—the very data we promise to protect as programmers.

Security is not exclusive to user data and input, though. Viruses, worms, Trojan horses, adware, key loggers, ransomware, and other forms of computer malware continue to spread and plague millions upon millions of computers and devices around the world. Even after decades of technological improvements in hardware and software, there is no such thing as an invulnerable system. Security is simply a craft that is continually being honed but will never be perfected for there will always be the inquisitive few who investigate and search for every possible way to "hack" a system.

For that reason, regardless of use case and user base, we design our software with security in mind as one of the top priorities if not *the* top priority. We do this to protect our users from the aforementioned threats that may cause inconveniences such as data loss, file corruption, and system crashes to name a few.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#teamwork-makes-the-dream-work) Teamwork makes the dream work

Even if it does not necessarily relate to programming, teamwork plays an extremely integral role in software development. With all the complexity and moving parts of any large project, it is impossible for only one person to develop quality software at the brisk pace of regular iteration or under the strict deadlines and time constraints of a client or any supervising entity.

This is why we have various teams of people who specialize in one of the many facets of programming. One person will never have all the skills and knowledge required to effectively and cohesively glue every facet together. One team may be responsible for UI design and accessibility while another may work on the functionality of the software itself. If all of the competencies of the various specialized teams are combined, the resulting software will have the best functionality, user experience, performance, and security it can possibly have within financial and practical constraints.

For time management and meeting deadlines, workflow organization and automation are of utmost importance. We take the time to properly configure our build tools and pipelines because doing so will save us a lot of time in the future. In general, the return on investment increases as time passes by.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#working-well-with-others) Working well with others

To expound on the idea of teamwork and cooperation, we establish healthy relationships with our peers because in the end, the success of a project greatly depends on the success of the team behind it. We make it an effort to foster a supportive working environment, where experienced seniors thoughfully guide newcomers.

Since we develop software as a team, we have to be mindful of others reading our code. To keep the development cycle sustainable in the long-term, readability and maintainability are considered to be just as important as the logic and functionality of a project. We consistently write good, readable code while providing informative [commit messages](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository) and documentation because these will definitely help us and others understand our code more.

Speaking of others reading our code, a code review is a great opportunity to learn more about best practices in programming. It is also another way of familiarizing ourselves with a code base and its underlying design and architecture. Although *constructive* criticism is unpleasant and difficult to handle on the receiving end, it is important to take it as sound advice in order for us to improve as programmers.

#   [(L)](https://dev.to/somedood/programming-is-hard-2p87#programming-is-hard) Programming is hard

Programming encompasses many aspects beyond functionality such as user experience, performance, security, and teamwork. It is not enough to strictly focus on one aspect alone while omitting the others. For projects of notable size and significance, it is not as simple as typing a few lines of code. It requires a lot of careful planning, designing, consideration, and team cooperation to be successful. In fact, more time is spent thinking than typing when programming, especially during long sessions of debugging.

In the end, programming is really about continuous, nonstop learning. Adaptability and constant learning are the keys to surviving this industry. We cannot expect to stay relevant if we do not do our part to keep learning. In such a volatile industry of exponential technological improvement, we have to keep up with its fast pace lest we end up in the dust.

I want to conclude this article by recognizing the hard work of all the developers around the world. To write this article, I had to reflect on the daily workflow of a team of developers. I had to look into the many aspects of programming and software development that usually go unnoticed. Since then, I have had a greater appreciation for all the software installed in my computer. To that end, I encourage everyone to thank a programmer today, regardless of experience. Where would we be without them?

*Never take their hard work for granted.*