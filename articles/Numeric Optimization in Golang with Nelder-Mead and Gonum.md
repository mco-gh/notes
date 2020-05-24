Numeric Optimization in Golang with Nelder-Mead and Gonum

`8.402      2.491`
![Picture4.png](../_resources/b3514822add3c1e19c997ca0c28c1638.png)

The least squares result is in red. Pretty close too! Finally, let me add the true line in blue with the slope and intercept values I used to *generate* the test dataset, **2.38** and **8.29**.

![Picture5.png](../_resources/8ebe910dd79f5710e5c98e27bfe06afb.png)

Note that in my example there’s only one place where Nelder-Mead is mentioned. That’s because the optimize package is abstracted enough that I can easily swap out the actual algorithm. Overall, I think the optimize package is very well organized and easy to work with, and I look forward to trying out more of the gonum collection!

VividCortex offers free trials; click below to navigate to the sign-up page: **https://app.vividcortex.com/sign-up**