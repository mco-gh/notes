Practical Vue Components

 [JavaScript](https://laracasts.com/skills/javascript)

#  Practical Vue Components

As you continue building new projects, you'll find yourself reaching for the same crop of components over and over again. Most websites require modals, dropdowns, tooltips, and more. While you can certainly use a UI framework, let's instead learn how to construct these components (and more) from scratch.

 Intermediate
Difficulty

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='13' height='16' viewBox='0 0 13 16' class='tw-mr-2 js-evernote-checked' data-evernote-id='241'%3e%3cpath fill='%23FFF' fill-rule='nonzero' d='M4.129 6.866v5.888a.614.614 0 0 1-.395.58 3.442 3.442 0 0 1-1.167.188c-1.236 0-2.564-.529-2.564-1.69V4.3c-.028-.517.145-1.431.976-1.926.386-.23 2.412-1.588 3.43-2.274A.571.571 0 0 1 5.01.075c.19.108.309.316.309.541v.892c0 .34-.265.616-.591.616a.592.592 0 0 1-.554-.402c-.92.616-2.273 1.52-2.61 1.72-.302.18-.368.512-.38.692 0 .202.041.361.117.448.21.238.909.09 1.671-.388.733-.458 4.346-2.966 4.382-2.992a.568.568 0 0 1 .606-.03.62.62 0 0 1 .313.544v.07a.625.625 0 0 1-.263.512s-2.508 1.746-2.73 1.895c-.85.57-1.152 1.27-1.152 2.673zM13 3.893v7.997a.623.623 0 0 1-.276.521s-3.445 2.79-4.144 3.232c-.367.234-.835.357-1.352.357-1.228 0-2.499-.693-2.499-1.852V6.505l.002-.009c.012-.45.113-1.094.917-1.713C6.13 4.413 9 2.371 9.123 2.285a.572.572 0 0 1 .608-.036.62.62 0 0 1 .315.545v.892c0 .34-.264.616-.59.616a.59.59 0 0 1-.544-.375 191.5 191.5 0 0 0-2.563 1.847c-.38.294-.431.487-.438.735.001.184.05.325.146.417.301.288 1.113.167 1.912-.333.592-.37 3.143-2.424 4.076-3.185a.574.574 0 0 1 .623-.067.616.616 0 0 1 .332.552zm-1.182 2.745l-2.953 2.39v1.232l2.953-2.39V6.638z' data-evernote-id='242' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)1 episode

![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' width='13' height='13' viewBox='0 0 13 13' class='tw-mr-2 js-evernote-checked' data-evernote-id='244'%3e%3cpath fill='%23FFF' fill-rule='evenodd' d='M6.5 0C2.925 0 0 2.925 0 6.5S2.925 13 6.5 13 13 10.075 13 6.5 10.075 0 6.5 0zm2.967 9L6 6.913V3h1v3.391l3 1.761L9.467 9z' data-evernote-id='245' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)  9:21 mins

[Start Series](https://laracasts.com/series/practical-vue-components/episodes/1)

![](data:image/svg+xml,%3csvg viewBox='0 0 33.83098862 33.83098862' width='290' height='290' xmlns='http://www.w3.org/2000/svg' class='circle-chart js-evernote-checked' data-evernote-id='250'%3e%3ccircle stroke='rgba(0%2c 0%2c 0%2c .2)' stroke-width='1' fill='none' cx='16.91549431' cy='16.91549431' r='15.91549431' class='circle-chart__background js-evernote-checked' data-evernote-id='251'%3e%3c/circle%3e %3ccircle stroke='white' stroke-width='1' stroke-dasharray='3%2c100' stroke-linecap='round' fill='none' cx='16.91549431' cy='16.91549431' r='15.91549431' class='circle-chart__circle js-evernote-checked' data-evernote-id='252'%3e%3c/circle%3e%3c/svg%3e)  ![](../_resources/519990a5fcabaafa376fd922e95482b8.png)

##### [Let's get started!](https://laracasts.com/series/practical-vue-components/episodes/1)