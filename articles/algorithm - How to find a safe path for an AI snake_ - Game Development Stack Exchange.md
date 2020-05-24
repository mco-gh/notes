algorithm - How to find a safe path for an AI snake? - Game Development Stack Exchange

7

I have been working on a game in which a player can compete with a snake ai to get the most apples. The current path finding technique i use (A* Pathfinding) works fine. But I am struggling with coming with an effective way to make sure that the AI snake does not go for an objective that leads to it trapping itself. Consider that the snake can teleport and that there may be max 4 apples on the map at any given time. The decision tree I am trying to create looks somewhat like this:

- If path to goal is safe : go for apple!
- Else check next apple until a safe path is found or all apples are checked.
- If no path to any apple is safe including the paths produced if teleportation is possible, Then find the farthest path to the tail and remain chasing the tail until a safe path to an objective becomes available. If no path to tail is found : stall until death!

The problem is that it is really hard to find a fast and efficient way to determine if a path is safe!

My question is: what is a good way to determine if a path into an enclosed area is safe given that you cannot take the same path back out of that area?

 [algorithm](https://gamedev.stackexchange.com/questions/tagged/algorithm)  [ai](https://gamedev.stackexchange.com/questions/tagged/ai)  [path-finding](https://gamedev.stackexchange.com/questions/tagged/path-finding)  [snake](https://gamedev.stackexchange.com/questions/tagged/snake)

[share](https://gamedev.stackexchange.com/q/133460)|[improve this question](https://gamedev.stackexchange.com/posts/133460/edit)

 [edited Jun 5 '17 at 5:51](https://gamedev.stackexchange.com/posts/133460/revisions)

 [![e18abe8be1d927bd49f36ef2f10cdbc9](../_resources/0393ddbeb45d409d2dfc900458ab8f3e.jpg)](https://gamedev.stackexchange.com/users/26250/congusbongus)

 [congusbongus](https://gamedev.stackexchange.com/users/26250/congusbongus)
 14k4848 silver badges8181 bronze badges

asked Nov 23 '16 at 22:29

 [![picture](../_resources/9f89ecbb2c102241ab303ba9dad5a5d5.jpg)](https://gamedev.stackexchange.com/users/89828/eudy-contreras)

 [Eudy Contreras](https://gamedev.stackexchange.com/users/89828/eudy-contreras)

 9811 silver badge66 bronze badges

 [add a comment]()

##  2 Answers

 [active](https://gamedev.stackexchange.com/questions/133460/how-to-find-a-safe-path-for-an-ai-snake?answertab=active#tab-top)  [oldest](https://gamedev.stackexchange.com/questions/133460/how-to-find-a-safe-path-for-an-ai-snake?answertab=oldest#tab-top)  [votes](https://gamedev.stackexchange.com/questions/133460/how-to-find-a-safe-path-for-an-ai-snake?answertab=votes#tab-top)

4

Take a look at https://github.com/stevennl/Snake, a project demonstrating a few AI algorithms for the game Snake. The project README has a very nice explanation of the algorithm.

The key is for the snake to follow a [***Hamiltonian circuit***](https://en.wikipedia.org/wiki/Hamiltonian_path) (a path that visits every square, and loops back on itself). Many such paths exist for a simple 2D grid, you just have to find one. So something like this:

![VuYe2.png](../_resources/0820b404f32fc74a7f5eb3e716fb4a37.png)

Finding such a path is also known as the [longest path problem](https://en.wikipedia.org/wiki/Longest_path_problem). If you make your AI follow this circuit, it will never trap itself and will be able to grow to the largest size possible - filling the entire grid. If you're lazy you can stop here - your AI doesn't even need to care where the fruit is. Of course, this AI will be horribly slow, and maybe boring to watch.

To make the snake faster at eating fruit, you can make it take shortcuts within the Hamiltonian circuit, as long as taking such shortcuts won't make its head overlap its body after taking the shortcut. Here's an image covering the key points:

>

![PTs5U.png](../_resources/002be4dabf5c1f812d6c5000ec151d2f.png)>   > [https://johnflux.com/2015/05/02/nokia-6110-part-3-algorithms/

This algorithm is much better, but still not the best, since it is still following the original Hamiltonian circuit. It's possible that finding other circuits will allow it to take better shortcuts.

Other things that can complicate the algorithm include:

- Grids with obstacles; these can really complicate the longest path algorithm
- Multiple snakes

[share](https://gamedev.stackexchange.com/a/142067)|[improve this answer](https://gamedev.stackexchange.com/posts/142067/edit)

answered Jun 5 '17 at 5:20

 [![fGGK5.jpg](../_resources/0393ddbeb45d409d2dfc900458ab8f3e.jpg)](https://gamedev.stackexchange.com/users/26250/congusbongus)

 [congusbongus](https://gamedev.stackexchange.com/users/26250/congusbongus)
 14k4848 silver badges8181 bronze badges

-

 Hey thank you so much for putting your time and effort into this answer. I have tried many things. I think I have even looked at that project. I have not solved all my issues regarding making the snake competitive and safe but i have managed to make it last longer. In this video: [youtu.be/vg2k24SuX5k](https://youtu.be/vg2k24SuX5k) you can see my progress. I have stopped working on it due to other school work and project. I will try to resume my work now during the summer break. Once again thank you and I will look into the halmintonian circuit a bit more in detail and also look into the provided git project :) – [Eudy Contreras](https://gamedev.stackexchange.com/users/89828/eudy-contreras)  [Jun 5 '17 at 6:00](https://gamedev.stackexchange.com/questions/133460/how-to-find-a-safe-path-for-an-ai-snake#comment252338_142067)

 [add a comment]()

-1

I assume this is in 2D,

Wouldn't this be doable with iterating? Like, generating a straight line from snake head to goal. Then checking the line for errors, like if there's an obstacle in the way, then create a midpoint that dodges the obstacle.

Like, this:https://www.youtube.com/watch?v=-L-WgKMFuhE

But after you find the path, do two things: 1. With the current state, check if the goal is in an enclosed space with the snake, like the snake is the lid of the jar (terrain) that surrounds the goal. Then confirm there's enough space to jam the snake in there and coil it out. 2. Simulating the "head touches goal in most efficient path", check if you generated a jar, like in (1.)

Either way you'll need to do a lot of pixel crawling, unless you index everything somehow. But with modern day processing power, I doubt you'd need any indexes or optimizations.

I trid to help.

[share](https://gamedev.stackexchange.com/a/138515)|[improve this answer](https://gamedev.stackexchange.com/posts/138515/edit)

answered Mar 12 '17 at 1:36

 [(L)](https://gamedev.stackexchange.com/users/98748/alucard-pawpad)

 [Alucard Pawpad](https://gamedev.stackexchange.com/users/98748/alucard-pawpad)

 1122 bronze badges

 [add a comment]()

##  Your Answer

-
-
-
-
-
-
-
-
-
-
-
-
-
-
-
-

### Sign up or [log in](https://gamedev.stackexchange.com/users/login?ssrc=question_page&returnurl=https%3a%2f%2fgamedev.stackexchange.com%2fquestions%2f133460%2fhow-to-find-a-safe-path-for-an-ai-snake%23new-answer)

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon native iconGoogle js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='1910'%3e%3cpath d='M16.51 8H8.98v3h4.3c-.18 1-.74 1.48-1.6 2.04v2.01h2.6a7.8 7.8 0 0 0 2.38-5.88c0-.57-.05-.66-.15-1.18z' fill='%234285F4' data-evernote-id='2000' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M8.98 17c2.16 0 3.97-.72 5.3-1.94l-2.6-2a4.8 4.8 0 0 1-7.18-2.54H1.83v2.07A8 8 0 0 0 8.98 17z' fill='%2334A853' data-evernote-id='2001' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M4.5 10.52a4.8 4.8 0 0 1 0-3.04V5.41H1.83a8 8 0 0 0 0 7.18l2.67-2.07z' fill='%23FBBC05' data-evernote-id='2002' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M8.98 4.18c1.17 0 2.23.4 3.06 1.2l2.3-2.3A8 8 0 0 0 1.83 5.4L4.5 7.49a4.77 4.77 0 0 1 4.48-3.3z' fill='%23EA4335' data-evernote-id='2003' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Google

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon iconFacebook js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='1911'%3e%3cpath d='M3 1a2 2 0 0 0-2 2v12c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V3a2 2 0 0 0-2-2H3zm6.55 16v-6.2H7.46V8.4h2.09V6.61c0-2.07 1.26-3.2 3.1-3.2.88 0 1.64.07 1.87.1v2.16h-1.29c-1 0-1.19.48-1.19 1.18V8.4h2.39l-.31 2.42h-2.08V17h-2.5z' fill='%234167B2' data-evernote-id='1934' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Facebook

 ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' class='svg-icon native iconLogoGlyphXSm js-evernote-checked' width='18' height='18' viewBox='0 0 18 18' data-evernote-id='1912'%3e%3cpath d='M14 16v-5h2v7H2v-7h2v5h10z' fill='%23BCBBBB' data-evernote-id='2004' class='js-evernote-checked'%3e%3c/path%3e%3cpath d='M12.09.72l-1.21.9 4.5 6.07 1.22-.9L12.09.71zM5 15h8v-2H5v2zm9.15-5.87L8.35 4.3l.96-1.16 5.8 4.83-.96 1.16zm-7.7-1.47l6.85 3.19.63-1.37-6.85-3.2-.63 1.38zm6.53 5L5.4 11.39l.38-1.67 7.42 1.48-.22 1.46z' fill='%23F48024' data-evernote-id='2005' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e) Sign up using Email and Password

### Post as a guest

 Name

 Email
Required, but never shown

** By clicking “Post Your Answer”, you agree to our [terms of service](https://stackoverflow.com/legal/terms-of-service/public), [privacy policy](https://stackoverflow.com/legal/privacy-policy) and [cookie policy](https://stackoverflow.com/legal/cookie-policy)  **

## Not the answer you're looking for? Browse other questions tagged [algorithm](https://gamedev.stackexchange.com/questions/tagged/algorithm)  [ai](https://gamedev.stackexchange.com/questions/tagged/ai)  [path-finding](https://gamedev.stackexchange.com/questions/tagged/path-finding)  [snake](https://gamedev.stackexchange.com/questions/tagged/snake) or [ask your own question](https://gamedev.stackexchange.com/questions/ask).