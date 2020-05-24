Landmark Computer Science Proof Cascades Through Physics and Math | Quanta Magazine

###### [computational complexity](https://www.quantamagazine.org/tag/computational-complexity/)

# Landmark Computer Science Proof Cascades Through Physics and Math

Computer scientists established a new boundary on computationally verifiable knowledge. In doing so, they solved major open problems in quantum mechanics and pure mathematics.

[![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='220' data-evernote-id='214' class='js-evernote-checked'%3e%3cpath fill='currentColor' d='M9.4 4.2h31.2c8.6 0 9.4 7 9.4 15.6s-.7 15.6-9.4 15.6h-2.2l-.9 9.4-18.8-9.4H9.4c-8.6 0-9.4-7-9.4-15.6S.7 4.2 9.4 4.2z' data-reactid='221' data-evernote-id='513' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) 4](https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/#comments)

###### Read Later

A new proof in computer science also has implications for researchers in quantum mechanics and pure math.

[DVDP](https://davidope.com/) for Quanta Magazine

[ ![QuantaTeam_Kevin.jpg](../_resources/3deced7795fb8fd6939784497d4a4e44.jpg)    ### Kevin Hartnett  *Senior Writer*](https://www.quantamagazine.org/authors/kevin-hartnett/)

* * *

*March 4, 2020*

* * *

[View PDF/Print Mode![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='icon-l theme__accent ml05 js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='273' data-evernote-id='216'%3e%3cpath fill='currentColor' d='M39.9%2c27.5h4.9v22.4H0.1V5.1h22.4V10H5v35h35V27.5z M49.8%2c0.1h-2.4h-1H33.8V5h7.6L20.7%2c25.8l3.4%2c3.4L45%2c8.4v7.7h4.9V2.6L49.8%2c0.1z' data-reactid='274' data-evernote-id='556' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/#)

[algorithms](https://www.quantamagazine.org/tag/algorithms/)[computational complexity](https://www.quantamagazine.org/tag/computational-complexity/)[computer science](https://www.quantamagazine.org/tag/computer-science/)[entanglement](https://www.quantamagazine.org/tag/entanglement/)[graph theory](https://www.quantamagazine.org/tag/graph-theory/)[mathematics](https://www.quantamagazine.org/tag/mathematics/)[quantum computing](https://www.quantamagazine.org/tag/quantum-computing/)[quantum information theory](https://www.quantamagazine.org/tag/quantum-information-theory/)

[![Ad_Article_320x600_math.jpg](../_resources/adc44108cd53bd3b3b7181473a5190a0.jpg)](https://www.quantamagazine.org/gift-store)

In 1935, Albert Einstein, working with Boris Podolsky and Nathan Rosen, grappled with a possibility revealed by the new laws of quantum physics: that two particles could be entangled, or correlated, even across vast distances.

The very next year, Alan Turing formulated the first general theory of computing and proved that there exists a problem that computers will never be able to solve.

These two ideas revolutionized their respective disciplines. They also seemed to have nothing to do with each other. But now [a landmark proof](https://arxiv.org/abs/2001.04383) has combined them while solving a raft of open problems in computer science, physics and mathematics.

The new proof establishes that quantum computers that calculate with entangled quantum bits or qubits, rather than classical 1s and 0s, can theoretically be used to verify answers to an incredibly vast set of problems. The correspondence between entanglement and computing came as a jolt to many researchers.

“It was a complete surprise,” said [Miguel Navascués](https://www.iqoqi-vienna.at/en/team/navascues-group/miguel-navascues/), who studies quantum physics at the Institute for Quantum Optics and Quantum Information in Vienna.

The proof’s co-authors set out to determine the limits of an approach to verifying answers to computational problems. That approach involves entanglement. By finding that limit the researchers ended up settling two other questions almost as a byproduct: Tsirelson’s problem in physics, about how to mathematically model entanglement, and a related problem in pure mathematics called the Connes embedding conjecture.

In the end, the results cascaded like dominoes.

“The ideas all came from the same time. It’s neat that they come back together again in this dramatic way,” said [Henry Yuen](http://www.henryyuen.net/) of the University of Toronto and an author of the proof, along with [Zhengfeng Ji](https://www.uts.edu.au/staff/zhengfeng.ji) of the University of Technology Sydney, [Anand Natarajan](http://www.its.caltech.edu/~anataraj/) and [Thomas Vidick](http://users.cms.caltech.edu/~vidick/) of the California Institute of Technology, and [John Wright](https://www.cs.utexas.edu/people/faculty-researchers/john-wright) of the University of Texas, Austin. The five researchers are all computer scientists.

## Undecidable Problems

Turing defined a basic framework for thinking about computation before computers really existed. In nearly the same breath, he showed that there was a certain problem computers were provably incapable of addressing. It has to do with whether a program ever stops.

Typically, computer programs receive inputs and produce outputs. But sometimes they get stuck in infinite loops and spin their wheels forever. When that happens at home, there’s only one thing left to do.

“You have to manually kill the program. Just cut it off,” Yuen said.

Turing proved that there’s no all-purpose algorithm that can determine whether a computer program will halt or run forever. You have to run the program to find out.

### Share this article

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='318' data-evernote-id='217'%3e%3cpath fill='currentColor' d='M13 16.5h5.1v-5c-.2-2.7.3-5.4 1.7-7.7 1.8-2.5 4.9-4 8-3.8 3.1-.1 6.2.2 9.2 1l-1.3 7.7C34.4 8.3 33 8 31.6 8c-2 0-3.8.7-3.8 2.7v5.9H36l-.6 7.5h-7.6V50h-9.6V23.9H13v-7.4z' data-reactid='319' data-evernote-id='598' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](http://www.facebook.com/sharer.php?u=https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='323' data-evernote-id='218'%3e%3cpath fill='currentColor' d='M50 9.9c-1.9.8-3.8 1.3-5.9 1.6 2.1-1.3 3.7-3.2 4.5-5.6-2 1.2-4.2 2-6.5 2.5-3.8-4.1-10.3-4.5-14.5-.8-2.8 2.5-4 6.3-3.1 10-8.2-.5-15.8-4.3-21-10.6-2.7 4.6-1.3 10.5 3.2 13.5C5 20.4 3.4 20 2 19.2c0 4.8 3.4 8.9 8.2 9.9-.9.2-1.8.4-2.7.3-.6 0-1.3-.1-1.9-.2 1.3 4.1 5.2 6.9 9.5 7C10.8 39.5 5.4 41 0 40.4c13.5 8.5 31.5 4.6 40.2-8.7 3-4.6 4.6-10 4.6-15.5v-1.3c2-1.3 3.7-3.1 5.2-5' data-reactid='324' data-evernote-id='601' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://twitter.com/share?url=https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/&text=Landmark%20Computer%20Science%20Proof%20Cascades%20Through%20Physics%20and%20Math&via=QuantaMagazine)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' x='0px' y='0px' viewBox='0 0 50 50' enable-background='new 0 0 50 50' xml:space='preserve' data-reactid='328' data-evernote-id='219'%3e%3cg data-reactid='329' data-evernote-id='604' class='js-evernote-checked'%3e%3c!-- react-text: 330 --%3e %3c!-- /react-text --%3e%3cpath fill='currentColor' d='M20.6%2c38.5c-0.8%2c0-1.6%2c0.3-2.2%2c0.8L16%2c41.9c-1.1%2c1-2.4%2c1.6-3.9%2c1.6c-1.5%2c0-2.8-0.5-3.9-1.6c-0.5-0.5-0.9-1.1-1.2-1.8 c-0.3-0.7-0.4-1.4-0.4-2.1c0-0.7%2c0.1-1.4%2c0.4-2.1c0.3-0.7%2c0.7-1.2%2c1.2-1.8l9.1-9c1-0.9%2c2.2-1.8%2c3.8-2.7s3-0.7%2c4.3%2c0.7 c0.6%2c0.6%2c1.3%2c0.8%2c2.2%2c0.8s1.5-0.3%2c2.1-0.9c0.6-0.6%2c0.9-1.3%2c0.9-2.2s-0.3-1.6-0.9-2.2c-2.2-2.2-4.8-3.1-7.8-2.7 c-3%2c0.4-5.9%2c2-8.8%2c4.8l-9.2%2c9c-1.1%2c1.1-1.9%2c2.4-2.5%2c3.8C0.7%2c35%2c0.4%2c36.5%2c0.4%2c38c0%2c1.6%2c0.3%2c3%2c0.9%2c4.4c0.6%2c1.4%2c1.4%2c2.7%2c2.5%2c3.8 c1.1%2c1.1%2c2.4%2c2%2c3.8%2c2.5c1.4%2c0.6%2c2.9%2c0.8%2c4.4%2c0.8s2.9-0.3%2c4.3-0.8c1.4-0.6%2c2.7-1.4%2c3.8-2.5l2.5-2.5c0.6-0.6%2c0.9-1.3%2c0.9-2.1 s-0.3-1.6-0.9-2.2C22.1%2c38.8%2c21.4%2c38.5%2c20.6%2c38.5z' data-reactid='331' data-evernote-id='605' class='js-evernote-checked'%3e%3c/path%3e%3c!-- react-text: 332 --%3e %3c!-- /react-text --%3e%3cpath fill='currentColor' d='M48.7%2c7.9c-0.6-1.4-1.4-2.7-2.5-3.8c-2.4-2.4-5.1-3.6-8-3.7c-3-0.1-5.5%2c0.9-7.7%2c3.1l-3.1%2c3.1c-0.6%2c0.6-0.9%2c1.3-0.9%2c2.1 s0.3%2c1.6%2c0.9%2c2.2s1.3%2c0.9%2c2.2%2c0.9s1.6-0.3%2c2.2-0.8l3.1-3.1c1.2-1.1%2c2.4-1.5%2c3.7-1.3c1.3%2c0.3%2c2.5%2c0.9%2c3.4%2c1.9 c0.5%2c0.5%2c0.9%2c1.1%2c1.2%2c1.8c0.3%2c0.7%2c0.4%2c1.4%2c0.4%2c2.1c0%2c0.7-0.1%2c1.4-0.4%2c2.1c-0.3%2c0.7-0.7%2c1.2-1.2%2c1.8l-9.7%2c9.6 c-2.2%2c2.2-3.9%2c3.1-5.1%2c2.7s-2-0.8-2.4-1.3c-0.6-0.6-1.3-0.8-2.2-0.8s-1.5%2c0.3-2.1%2c0.9c-0.6%2c0.6-0.9%2c1.3-0.9%2c2.2s0.3%2c1.5%2c0.9%2c2.1 c1%2c1%2c2.1%2c1.8%2c3.2%2c2.3s2.4%2c0.7%2c3.6%2c0.7c1.5%2c0%2c3-0.4%2c4.6-1.1c1.6-0.7%2c3.1-1.9%2c4.6-3.4l9.8-9.6c1.1-1.1%2c1.9-2.4%2c2.5-3.8 c0.6-1.4%2c0.9-2.9%2c0.9-4.4C49.6%2c10.8%2c49.3%2c9.3%2c48.7%2c7.9z' data-reactid='333' data-evernote-id='606' class='js-evernote-checked'%3e%3c/path%3e%3c!-- react-text: 334 --%3e %3c!-- /react-text --%3e%3c/g%3e%3c/svg%3e)](https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/#0)

###### Copied!

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' x='0px' y='0px' viewBox='0 0 50 50' enable-background='new 0 0 50 50' xml:space='preserve' data-reactid='343' data-evernote-id='220'%3e%3cpath fill='currentColor' d='M25%2c29.5l-5.2-4.3L1.8%2c43.8h46L30.1%2c25.2L25%2c29.5z M32.6%2c23.2l17.2%2c17.9c0-0.2%2c0.1-0.3%2c0.1-0.5c0-0.2%2c0-0.4%2c0-0.6V9.1 L32.6%2c23.2z M0%2c9.1v31c0%2c0.2%2c0%2c0.4%2c0%2c0.6s0.1%2c0.3%2c0.1%2c0.5l17.3-17.8L0%2c9.1z M48.4%2c6.2H1.6L25%2c25L48.4%2c6.2z' data-reactid='344' data-evernote-id='614' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/mailto:?subject=Landmark%20Computer%20Science%20Proof%20Cascades%20Through%20Physics%20and%20Math&body=Computer%20scientists%20established%20a%20new%20boundary%20on%20computationally%20verifiable%20knowledge.%20In%20doing%20so,%20they%20solved%20major%20open%20problems%20in%20quantum%20mechanics%20and%20pure%20mathematics.%0A%0Ahttps://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/)

[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='350' data-evernote-id='221'%3e%3cpath fill='currentColor' d='M2.6%2c1.7C1.3%2c1.6%2c0.1%2c2.7%2c0%2c4.1c0%2c0.1%2c0%2c0.3%2c0%2c0.4v9.9c0%2c8.1%2c8%2c14.4%2c15%2c14.4c8-0.1%2c14.6-6.4%2c15-14.4v-10 c0.1-1.4-0.9-2.6-2.3-2.8c-0.2%2c0-0.4%2c0-0.5%2c0L2.6%2c1.7z M9%2c9.8l6%2c5.7l6-5.7c2.8-1.1%2c3.9%2c2%2c2.8%2c2.8L16%2c20.1c-0.6%2c0.3-1.3%2c0.3-1.9%2c0 l-7.9-7.5C5.2%2c11.5%2c6.5%2c8.4%2c9%2c9.8L9%2c9.8z' data-reactid='351' data-evernote-id='619' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://getpocket.com/save?url=https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/&title=Landmark%20Computer%20Science%20Proof%20Cascades%20Through%20Physics%20and%20Math)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='4 0 33 33' enable-background='new 0 0 30 30' data-reactid='355' data-evernote-id='222'%3e%3cpath fill='currentColor' d='M39.58%2c19.65A4.72%2c4.72%2c0%2c0%2c0%2c31.91%2c16a22.4%2c22.4%2c0%2c0%2c0-10.42-3.09l2-6.38%2c5.6%2c1.31a3.91%2c3.91%2c0%2c1%2c0%2c.43-2.08L23.05%2c4.27A1.08%2c1.08%2c0%2c0%2c0%2c21.79%2c5L19.26%2c12.9A22.6%2c22.6%2c0%2c0%2c0%2c8%2c16a4.68%2c4.68%2c0%2c1%2c0-5.56%2c7.51%2c8.32%2c8.32%2c0%2c0%2c0-.08%2c1.12c0%2c3.21%2c1.89%2c6.2%2c5.31%2c8.41a22.69%2c22.69%2c0%2c0%2c0%2c12.23%2c3.3A22.67%2c22.67%2c0%2c0%2c0%2c32.15%2c33c3.43-2.21%2c5.31-5.2%2c5.31-8.41a8.77%2c8.77%2c0%2c0%2c0-.06-1%2c4.65%2c4.65%2c0%2c0%2c0%2c2.18-3.93M33.05%2c5.8a1.78%2c1.78%2c0%2c1%2c1-1.8%2c1.78%2c1.79%2c1.79%2c0%2c0%2c1%2c1.8-1.78M11.52%2c22.53a2.71%2c2.71%2c0%2c0%2c1%2c2.69-2.66%2c2.65%2c2.65%2c0%2c1%2c1-2.69%2c2.66m14.93%2c7.73c-1.37%2c1.35-3.47%2c2-6.43%2c2h0c-3%2c0-5.06-.65-6.43-2a1.05%2c1.05%2c0%2c0%2c1%2c0-1.5%2c1.09%2c1.09%2c0%2c0%2c1%2c1.52%2c0c.94.93%2c2.54%2c1.38%2c4.91%2c1.38h0c2.37%2c0%2c4-.45%2c4.91-1.38a1.08%2c1.08%2c0%2c0%2c1%2c1.52%2c0%2c1.07%2c1.07%2c0%2c0%2c1%2c0%2c1.5m-.63-5.1a2.65%2c2.65%2c0%2c1%2c1%2c2.66-2.63%2c2.65%2c2.65%2c0%2c0%2c1-2.66%2c2.63' transform='translate(-0.42 -3.68)' data-reactid='356' data-evernote-id='622' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://www.reddit.com/submit?url=https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='360' data-evernote-id='223'%3e%3cpath fill='currentColor' d='M12.9%2c18L3.2-0.1h4.4l5.7%2c11.5l0.3%2c0.6c0.1%2c0.2%2c0.2%2c0.4%2c0.3%2c0.7c0%2c0.1%2c0%2c0.2%2c0%2c0.2v0.2l0.4%2c0.9l0.5%2c0.7 l0.8-1.6l0.9-1.8l5.8-11.5h4.1l-9.8%2c18.3v11.7h-3.7V18z' data-reactid='361' data-evernote-id='625' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://news.ycombinator.com/submitlink?u=https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/&t=Landmark%20Computer%20Science%20Proof%20Cascades%20Through%20Physics%20and%20Math)[ ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='absolute fit-x mxa c-1a1a1a js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='365' data-evernote-id='224'%3e%3cpath fill='currentColor' d='M30%2c0 0%2c0 0%2c30 10%2c30 10%2c20 20%2c20 20%2c10 30%2c10 z' data-reactid='366' data-evernote-id='628' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://share.flipboard.com/bookmarklet/popout?v=Landmark%20Computer%20Science%20Proof%20Cascades%20Through%20Physics%20and%20Math&url=https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/)

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='ml05 icon icon-offset closed js-evernote-checked' viewBox='0 0 30 30' enable-background='new 0 0 30 30' data-reactid='368' data-evernote-id='225'%3e%3cpath fill='currentColor' d='M15%2c20.7c-0.1%2c0-0.3%2c0-0.4-0.1L0.3%2c10.7l0.9-1.2L15%2c19l13.8-9.5l0.9%2c1.2l-14.3%2c9.8C15.3%2c20.6%2c15.1%2c20.7%2c15%2c20.7 z' data-reactid='369' data-evernote-id='630' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)

* * *

### Newsletter

*Get Quanta Magazine delivered to your inbox*

[(L)](https://www.quantamagazine.org/landmark-computer-science-proof-cascades-through-physics-and-math-20200304/#newsletter)

[Most recent newsletter![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='ml05 icon js-evernote-checked' viewBox='0 0 50 50' enable-background='new 0 0 50 50' data-reactid='382' data-evernote-id='226'%3e%3cpath fill='currentColor' d='M50 25l-17.4-8.7v6.5H0v4.4h32.6v6.5' data-reactid='383' data-evernote-id='638' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](http://us1.campaign-archive2.com/home/?u=0d6ddf7dc1a0b7297c8e06618&id=f0cb61321c)

![ConnesStitch_1840.jpg](../_resources/c9cafb0598e14262828223039f314721.jpg)

The computer scientists Henry Yuen, Thomas Vidick, Zhengfeng Ji, Anand Natarajan and John Wright co-authored a proof about verifying answers to computational problems and ended up solving major problems in math and quantum physics.

(Yuen) Andrea Lao; (Vidick) Courtesy of Caltech; (Ji) Anna Zhu; (Natarajan) David Sella; (Wright) Soya Park

“You’ve waited a million years and a program hasn’t halted. Do you just need to wait 2 million years? There’s no way of telling,” said [William Slofstra](http://elliptic.space/), a mathematician at the University of Waterloo.

In technical terms, Turing proved that this halting problem is undecidable — even the most powerful computer imaginable couldn’t solve it.

After Turing, computer scientists began to classify other problems by their difficulty. Harder problems require more computational resources to solve — more running time, more memory. This is the study of computational complexity.

Ultimately, every problem presents two big questions: “How hard is it to solve?” and “How hard is it to verify that an answer is correct?”

## Interrogate to Verify

When problems are relatively simple, you can check the answer yourself. But when they get more complicated, even checking an answer can be an overwhelming task. However, in 1985 computer scientists realized it’s possible to develop confidence that an answer is correct even when you can’t confirm it yourself.

The method follows the logic of a police interrogation.

If a suspect tells an elaborate story, maybe you can’t go out into the world to confirm every detail. But by asking the right questions, you can catch your suspect in a lie or develop confidence that the story checks out.

In computer science terms, the two parties in an interrogation are a powerful computer that proposes a solution to a problem — known as the prover — and a less powerful computer that wants to ask the prover questions to determine whether the answer is correct. This second computer is called the verifier.

To take a simple example, imagine you’re colorblind and someone else — the prover — claims two marbles are different colors. You can’t check this claim by yourself, but through clever interrogation you can still determine whether it’s true.

Put the two marbles behind your back and mix them up. Then ask the prover to tell you which is which. If they really are different colors, the prover should answer the question correctly every time. If the marbles are actually the same color — meaning they look identical — the prover will guess wrong half the time.

“If I see you succeed a lot more than half the time, I’m pretty sure they’re not” the same color, Vidick said.

By asking a prover questions, you can verify solutions to a wider class of problems than you can on your own.

*open-quote*

You’ve waited a million years and a program hasn’t halted. Do you just need to wait 2 million years? There’s no way of telling.

*close-quote*
William Slofstra, University of Waterloo

In 1988, computer scientists considered what happens when two provers propose solutions to the same problem. After all, if you have two suspects to interrogate, it’s even easier to solve a crime, or verify a solution, since you can play them against each other.

“It gives more leverage to the verifier. You interrogate, ask related questions, cross-check the answers,” Vidick said. If the suspects are telling the truth, their responses should align most of the time. If they’re lying, the answers will conflict more often.

Similarly, researchers showed that by interrogating two provers separately about their answers, you can quickly verify solutions to an even larger class of problems than you can when you only have one prover to interrogate.

Computational complexity may seem entirely theoretical, but it’s also closely connected to the real world. The resources that computers need to solve and verify problems — time and memory — are fundamentally physical. For this reason, new discoveries in physics can change computational complexity.

“If you choose a different set of physics, like quantum rather than classical, you get a different complexity theory out of it,” Natarajan said.

The new proof is the end result of 21st-century computer scientists confronting one of the strangest ideas of 20th-century physics: entanglement.

## The Connes Embedding Conjecture

When two particles are entangled, they don’t actually affect each other — they have no causal relationship. Einstein and his co-authors elaborated on this idea in their 1935 paper. Afterward, physicists and mathematicians tried to come up with a mathematical way of describing what entanglement really meant.

Yet the effort came out a little muddled. Scientists came up with two different mathematical models for entanglement — and it wasn’t clear that they were equivalent to each other.

In a roundabout way, this potential dissonance ended up producing an important problem in pure mathematics called the Connes embedding conjecture. Eventually, it also served as a fissure that the five computer scientists took advantage of in their new proof.

The first way of modeling entanglement was to think of the particles as spatially isolated from each other. One is on Earth, say, and the other is on Mars; the distance between them is what prevents causality. This is called the tensor product model.

But in some situations, it’s not entirely obvious when two things are causally separate from each other. So mathematicians came up with a second, more general way of describing causal independence.

When the order in which you perform two operations doesn’t affect the outcome, the operations “commute”: 3 x 2 is the same as 2 x 3. In this second model, particles are entangled when their properties are correlated but the order in which you perform your measurements doesn’t matter: Measure particle A to predict the momentum of particle B or vice versa. Either way, you get the same answer. This is called the commuting operator model of entanglement.

*open-quote*
The verification capability of this type of model is really mind-boggling.
*close-quote*
Henry Yuen, University of Toronto

Both descriptions of entanglement use arrays of numbers organized into rows and columns called matrices. The tensor product model uses matrices with a finite number of rows and columns. The commuting operator model uses a more general object that functions like a matrix with an infinite number of rows and columns.

Over time, mathematicians began to study these matrices as objects of interest in their own right, completely apart from any connection to the physical world. As part of this work, a mathematician named [Alain Connes](https://www.ihes.fr/en/professeur/alain-connes-2/) conjectured in 1976 that it should be possible to approximate many infinite-dimensional matrices with finite-dimensional ones. This is one implication of the Connes embedding conjecture.

The following decade a physicist named Boris Tsirelson posed a version of the problem that grounded it in physics once more. Tsirelson conjectured that the tensor product and commuting operator models of entanglement were roughly equivalent. This makes sense, since they’re theoretically two different ways of describing the same physical phenomenon. Subsequent work showed that because of the connection between matrices and the physical models that use them, the Connes embedding conjecture and Tsirelson’s problem imply each other: Solve one, and you solve the other.

Yet the solution to both problems ended up coming from a third place altogether.

## Game Show Physics

In the 1960s, a physicist named John Bell came up with a test for determining whether entanglement was a real physical phenomenon, rather than just a theoretical notion. The test involved a kind of game whose outcome reveals whether something more than ordinary, non-quantum physics is at work.

Computer scientists would later realize that this test about entanglement could also be used as a tool for verifying answers to very complicated problems.

But first, to see how the games work, let’s imagine two players, Alice and Bob, and a 3-by-3 grid. A referee assigns Alice a row and tells her to enter a 0 or a 1 in each box so that the digits sum to an odd number. Bob gets a column and has to fill it out so that it sums to an even number. They win if they put the same number in the one place her row and his column overlap. They’re not allowed to communicate.

Under normal circumstances, the best they can do is win 89% of the time. But under quantum circumstances, they can do better.

Imagine Alice and Bob split a pair of entangled particles. They perform measurements on their respective particles and use the results to dictate whether to write 1 or 0 in each box. Because the particles are entangled, the results of their measurements are going to be correlated, which means their answers will correlate as well — meaning they can win the game 100% of the time.

![QuantumGames_560.jpg](../_resources/7db3425834e5b386bcf372a557bd94af.jpg)

Lucy Reading-Ikkanda/Quanta Magazine

So if you see two players winning the game at unexpectedly high rates, you can conclude that they are using something other than classical physics to their advantage. Such Bell-type experiments are now called “nonlocal” games, in reference to the separation between the players. Physicists actually perform them in laboratories.

“People have run experiments over the years that really show this spooky thing is real,” said Yuen.

As when analyzing any game, you might want to know how often players can win a nonlocal game, provided they play the best they can. For example, with solitaire, you can calculate how often someone playing perfectly is likely to win.

But in 2016, William Slofstra proved that [there’s no general algorithm](https://www.quantamagazine.org/the-universes-ultimate-complexity-revealed-by-simple-quantum-games-20190305/) for calculating the exact maximum winning probability for all nonlocal games. So researchers wondered: Could you at least [approximate the maximum-winning percentage](https://www.quantamagazine.org/in-quantum-games-theres-no-way-to-play-the-odds-20190401/)?

Computer scientists have homed in on an answer using the two models describing entanglement. An algorithm that uses the tensor product model establishes a floor, or minimum value, on the approximate maximum-winning probability for all nonlocal games. Another algorithm, which uses the commuting operator model, establishes a ceiling.

These algorithms produce more precise answers the longer they run. If Tsirelson’s prediction is true, and the two models really are equivalent, the floor and the ceiling should keep pinching closer together, narrowing in on a single value for the approximate maximum-winning percentage.

But if Tsirelson’s prediction is false, and the two models are not equivalent, “the ceiling and the floor will forever stay separated,” Yuen said. There will be no way to calculate even an approximate winning percentage for nonlocal games.

In their new work, the five researchers used this question — about whether the ceiling and floor converge and Tsirelson’s problem is true or false — to solve a separate question about when it’s possible to verify the answer to a computational problem.

## Entangled Assistance

In the early 2000s, computer scientists began to wonder: How does it change the range of problems you can verify if you interrogate two provers that share entangled particles?

Most assumed that entanglement worked against verification. After all, two suspects would have an easier time telling a consistent lie if they had some means of coordinating their answers.

But over the last few years, computer scientists have realized that the opposite is true: By interrogating provers that share entangled particles, you can verify a much larger class of problems than you can without entanglement.

“Entanglement is a way to generate correlations that you think might help them lie or cheat,” Vidick said. “But in fact you can use that to your advantage.”

To understand how, you first need to grasp the almost otherworldly scale of the problems whose solutions you could verify through this interactive procedure.

Imagine a graph — a collection of dots (vertices) connected by lines (edges). You might want to know whether it’s possible to color the vertices using three colors, so that no vertices connected by an edge have the same color. If you can, the graph is “three-colorable.”

If you hand a pair of entangled provers a very large graph, and they report back that it can be three-colored, you’ll wonder: Is there a way to verify their answer?

For very big graphs, it would be impossible to check the work directly. So instead, you could ask each prover to tell you the color of one of two connected vertices. If they each report a different color, and they keep doing so every time you ask, you’ll gain confidence that the three-coloring really works.

But even this interrogation strategy fails as graphs get really big — with more edges and vertices than there are atoms in the universe. Even the task of stating a specific question (“Tell me the color of *XYZ* vertex”) is more than you, the verifier, can manage: The amount of data required to name a specific vertex is more than you can hold in your working memory.

But entanglement makes it possible for the provers to come up with the questions themselves.

“The verifier doesn’t have to compute the questions. The verifier forces the provers to compute the questions for them,” Wright said.

The verifier wants the provers to report the colors of connected vertices. If the vertices aren’t connected, then the answers to the questions won’t say anything about whether the graph is three-colored. In other words, the verifier wants the provers to ask correlated questions: One prover asks about vertex *ABC* and the other asks about vertex *XYZ*. The hope is that the two vertices are connected to each other, even though neither prover knows which vertex the other is thinking about. (Just as Alice and Bob hope to fill in the same number in the same square even though neither knows which row or column the other has been asked about.)

*open-quote*

The ideas all came from the same time. It’s neat that they come back together again in this dramatic way.

*close-quote*
Henry Yuen, University of Toronto

If two provers were coming up with these questions completely on their own, there’d be no way to force them to select connected, or correlated, vertices in a way that would allow the verifier to validate their answers. But such correlation is exactly what entanglement enables.

“We’re going to use entanglement to offload almost everything onto the provers. We make them select questions by themselves,” Vidick said.

At the end of this procedure, the provers each report a color. The verifier checks whether they’re the same or not. If the graph really is three-colorable, the provers should never report the same color.

“If there is a three-coloring, the provers will be able to convince you there is one,” Yuen said.

As it turns out, this verification procedure is another example of a nonlocal game. The provers “win” if they convince you their solution is correct.

In 2012, Vidick and [Tsuyoshi Ito](https://cs.uwaterloo.ca/~tito/) proved that it’s possible to play a wide variety of nonlocal games with entangled provers to verify answers to at least the same number of problems you can verify by interrogating two classical computers. That is, using entangled provers doesn’t work against verification. And last year, Natarajan and Wright proved that interacting with entangled provers actually expands the class of problems that can be verified.

But computer scientists didn’t know the full range of problems that can be verified in this way. Until now.

## A Cascade of Consequences

In their new paper, the five computer scientists prove that interrogating entangled provers makes it possible to verify answers to unsolvable problems, including the halting problem.

“The verification capability of this type of model is really mind-boggling,” Yuen said.

But the halting problem can’t be solved. And that fact is the spark that sets the final proof in motion.

Imagine you hand a program to a pair of entangled provers. You ask them to tell you whether it will halt. You’re prepared to verify their answer through a kind of nonlocal game: The provers generate questions and “win” based on the coordination between their answers.

If the program does in fact halt, the provers should be able to win this game 100% of the time — similar to how if a graph is actually three-colorable, entangled provers should never report the same color for two connected vertices. If it doesn’t halt, the provers should only win by chance — 50% of the time.

That means if someone asks you to determine the approximate maximum-winning probability for a specific instance of this nonlocal game, you will first need to solve the halting problem. And solving the halting problem is impossible. Which means that calculating the approximate maximum-winning probability for nonlocal games is undecidable, just like the halting problem.

This in turn means that the answer to Tsirelson’s problem is no — the two models of entanglement are not equivalent. Because if they were, you could pinch the floor and the ceiling together to calculate an approximate maximum-winning probability.

“There cannot be such an algorithm, so the two [models] must be different,” said [David Pérez-García](https://www.ucm.es/mathqi/david-perez-garcia) of the Complutense University of Madrid.

The new paper proves that the class of problems that can be verified through interactions with entangled quantum provers, a class called MIP*, is exactly equal to the class of problems that are no harder than the halting problem, a class called RE. The title of the paper states it succinctly: “MIP* = RE.”

In the course of proving that the two complexity classes are equal, the computer scientists proved that Tsirelson’s problem is false, which, due to previous work, meant that the Connes embedding conjecture is also false.

For researchers in these fields, it was stunning that answers to such big problems would fall out from a seemingly unrelated proof in computer science.

“If I see a paper that says MIP* = RE, I don’t think it has anything to do with my work,” said Navascués, who co-authored previous work tying Tsirelson’s problem and the Connes embedding conjecture together. “For me it was a complete surprise.”

Quantum physicists and mathematicians are just beginning to digest the proof. Prior to the new work, mathematicians had wondered whether they could get away with approximating infinite-dimensional matrices by using large finite-dimensional ones instead. Now, because the Connes embedding conjecture is false, they know they can’t.

“Their result implies that’s impossible,” said Slofstra.

The computer scientists themselves did not aim to answer the Connes embedding conjecture, and as a result, they’re not in the best position to explain the implications of one of the problems they ended up solving.

“Personally, I’m not a mathematician. I don’t understand the original formulation of the Connes embedding conjecture well,” said Natarajan.

### Related:

* * *

1. 1.

##### [The Universe’s Ultimate Complexity Revealed by Simple Quantum Games](https://www.quantamagazine.org/the-universes-ultimate-complexity-revealed-by-simple-quantum-games-20190305/)

2. 2.

##### [Computer Scientists Expand the Frontier of Verifiable Knowledge](https://www.quantamagazine.org/computer-scientists-expand-the-frontier-of-verifiable-knowledge-20190523/)

3. 3.

##### [In Quantum Games, There’s No Way to Play the Odds](https://www.quantamagazine.org/in-quantum-games-theres-no-way-to-play-the-odds-20190401/)

He and his co-authors anticipate that mathematicians will translate this new result into the language of their own field. In a blog post [announcing the proof](https://mycqstate.wordpress.com/2020/01/14/a-masters-project/), Vidick wrote, “I don’t doubt that eventually complexity theory will not be needed to obtain the purely mathematical consequences.”

Yet as other researchers run with the proof, the line of inquiry that prompted it is coming to a halt. For more than three decades, computer scientists have been trying to figure out just how far interactive verification will take them. They are now confronted with the answer, in the form of a long paper with a simple title and echoes of Turing.

“There’s this long sequence of works just wondering how powerful” a verification procedure with two entangled quantum provers can be, Natarajan said. “Now we know how powerful it is. That story is at an end.”