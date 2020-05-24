Page transitions with Vue.js – Alexis Gaillard – Medium

# Vue transitions with Vue.js

[![1*DWypZvQxeH3dzdwSTl5m3g.jpeg](../_resources/c7489aa2c87b41fe764bfd8de050bcad.jpg) ![](data:image/svg+xml,%3csvg viewBox='0 0 70 70' xmlns='http://www.w3.org/2000/svg' data-evernote-id='149' class='js-evernote-checked'%3e%3cpath d='M5.53538374%2c19.9430227 C11.180401%2c8.78497536 22.6271155%2c1.6 35.3571429%2c1.6 C48.0871702%2c1.6 59.5338847%2c8.78497536 65.178902%2c19.9430227 L66.2496695%2c19.401306 C60.4023065%2c7.84329843 48.5440457%2c0.4 35.3571429%2c0.4 C22.17024%2c0.4 10.3119792%2c7.84329843 4.46461626%2c19.401306 L5.53538374%2c19.9430227 Z'%3e%3c/path%3e%3cpath d='M65.178902%2c49.9077131 C59.5338847%2c61.0657604 48.0871702%2c68.2507358 35.3571429%2c68.2507358 C22.6271155%2c68.2507358 11.180401%2c61.0657604 5.53538374%2c49.9077131 L4.46461626%2c50.4494298 C10.3119792%2c62.0074373 22.17024%2c69.4507358 35.3571429%2c69.4507358 C48.5440457%2c69.4507358 60.4023065%2c62.0074373 66.2496695%2c50.4494298 L65.178902%2c49.9077131 Z'%3e%3c/path%3e%3c/svg%3e)](https://medium.com/@alexis.gaillard?source=post_header_lockup)

[Alexis Gaillard](https://medium.com/@alexis.gaillard)

Apr 21·4 min read![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='svgIcon-use js-evernote-checked' width='15' height='15' data-evernote-id='150'%3e%3cpath d='M7.438 2.324c.034-.099.09-.099.123 0l1.2 3.53a.29.29 0 0 0 .26.19h3.884c.11 0 .127.049.038.111L9.8 8.327a.271.271 0 0 0-.099.291l1.2 3.53c.034.1-.011.131-.098.069l-3.142-2.18a.303.303 0 0 0-.32 0l-3.145 2.182c-.087.06-.132.03-.099-.068l1.2-3.53a.271.271 0 0 0-.098-.292L2.056 6.146c-.087-.06-.071-.112.038-.112h3.884a.29.29 0 0 0 .26-.19l1.2-3.52z'%3e%3c/path%3e%3c/svg%3e)

![](../_resources/de9f8e65dd76979e03d35f810f5b4abc.png)![1*0AnfnxoVhXBrvnuN0LRvPg.jpeg](../_resources/a94afa55123c559ff9fa96ee8f8e2f92.jpg)

*I’ve been recently working on Vue.js SPA with interesting animations scenarios and ended up with some examples which seemed worth sharing.

In this example I will use the G*[*SAP animation’s library *](https://greensock.com/gsap)*wich is the fullest option out there but the same logic could rely on a lighter library — or even simple CSS’s based animations. I’ve been working with the great V*[*ue CLI 3 *](https://cli.vuejs.org/)*development tooling, with base presets including R*[*outer *](https://router.vuejs.org/)*and V*[*uex.*](https://vuex.vuejs.org/)

* * *

*...*

### Concept

We need to understand when the component’s hooks triggers in combination with the router navigation guards as this will become the reference points to keep our animations synchronized with the routing.

![](../_resources/eef5b17245995f1ac93c689af6886407.png)![1*tGaYB5bRJpQ8A6A0uPdNFg.png](../_resources/35cb8d893d191b6eda34923cebd35fb4.png)

[Component lifecycle](https://vuejs.org/v2/guide/instance.html#Lifecycle-Diagram) + [in component router guards](https://router.vuejs.org/guide/advanced/navigation-guards.html#in-component-guards)

![](../_resources/32b5dc639fc4e627f047711a232db867.png)![1*WL8VmAGtdJlhwG8j7FNi2A.png](../_resources/92c10091f605af197d4025ce3e0bd9f7.png)

Console outputs

Also keep in mind that we can use [named view](https://router.vuejs.org/guide/essentials/named-views.html#nested-named-views), and keep some components rendered while navigating to defined vues, leading to more creative transition scenarios such as follow:

![](../_resources/d9e7b0cb8042dff117e2802c30fb1b38.png)

 [![21147252_166225210609381_3138951344765796352_a.jpg](../_resources/114b03baf3ed8c545a80d508a508e3c5.jpg)](https://www.instagram.com/a.l.e.x.i.s.g.a.i.l.l.a.r.d/?utm_source=ig_embed)

 [a.l.e.x.i.s.g.a.i.l.l.a.r.d](https://www.instagram.com/a.l.e.x.i.s.g.a.i.l.l.a.r.d/?utm_source=ig_embed)

  102 followers

 [View Profile](https://www.instagram.com/a.l.e.x.i.s.g.a.i.l.l.a.r.d/?utm_source=ig_embed)

 [![56483280_587901291723125_7132261144298800898_n.jpg](../_resources/ddaaba5b7c641ea777b870024164d324.jpg)](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)

![56483280_587901291723125_7132261144298800898_n.jpg](../_resources/ddaaba5b7c641ea777b870024164d324.jpg)

Click video for sound

[(L)](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed&utm_campaign=embed_video_watch_again)[Watch Again on Instagram](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed&utm_campaign=embed_video_watch_again)

[(L)](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed&utm_campaign=embed_video_watch_again)

 [ ![21147252_166225210609381_3138951344765796352_a.jpg](../_resources/114b03baf3ed8c545a80d508a508e3c5.jpg)        a.l.e.x.i.s.g.a.i.l.l.a.r.d         12 posts · 102 followers               ![50850097_807094832960143_61868228841296104_n.jpg](../_resources/52ff393effed36e921e23aacbdf94df4.jpg)  ![41584487_251740408741564_455377193208381440_n.jpg](../_resources/d281e5b9788387861c56468ae85aa55d.jpg)](https://www.instagram.com/a.l.e.x.i.s.g.a.i.l.l.a.r.d/?utm_source=ig_embed)

 [View More on Instagram](https://www.instagram.com/a.l.e.x.i.s.g.a.i.l.l.a.r.d/?utm_source=ig_embed)

 [  Like](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)  [ Comment](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)  [ Share]()  [ Save](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)

 [29 likes](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)

 [Add a comment...](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)  [Instagram](https://www.instagram.com/p/BwZ1K7Jodf2/?utm_source=ig_embed)

Animations scenario for [@akira.studio](https://www.instagram.com/akira.studio/). Design by [@damienharmand](https://www.instagram.com/damienharmand/)

### Getting started

You need to make the required GSAP plugins available globally like so:

![](../_resources/1becab6087d2afcbb795953fc3d9c5da.png)![1*EZthBZ1mFUzBRFINrMmanw.png](../_resources/93b55286e2d336dcc8c67b976e22a4c6.png)

### Animating on enter

On enter we describe our animation scenario in the “mounted” hook of the component, we need our template rendered in order to targets our nodes with the “$refs” object:

![](../_resources/c6d70c58fd63dc10fa8bac88ce2df2f5.png)![1*XrDUhEwlQKvQrjrstkO9Pw.png](../_resources/9d72404bef25f783f2b30378c5787bc6.png)

Note that “mounted” does not guarantee that all child components have also been mounted. If you want to wait until the entire view has been rendered, you can use [vm.$nextTick](https://vuejs.org/v2/api/#vm-nextTick) inside of “mounted”.

### Animating on leaving

Here we need to trigger the navigation to the next vue when the exit animation ends. The “beforeRouteLeave” [in-component guard](https://router.vuejs.org/guide/advanced/navigation-guards.html#in-component-guards) can be used for that:

![](../_resources/5fcb5ead8b88048cb1a132e2c6ed87c1.png)![1*bqwvVWO39Jbfx763JDlohg.png](../_resources/84c8b0d44286dbfe126efa227e4dd0d3.png)

### Manage origins and destinations

The opening animation scenario of a vue might be different depending of the exit animation scenario of the previous vue for ex.

To manage origins and destinations a solution could be to save the previous vue name in our store, then use conditional statements like so:

![](../_resources/bf2d32558d01be610fda1d57633236c9.png)![1*OrrmAaB_q3QTAMEaQEltbg.png](../_resources/21bec22a03a6453dc67af12fccc337f8.png)

We could use the beforeRouteEnter router guard to push the name of the previous route in the store depending of your needs.

When leaving, you might need to know the destination in order to chain meaningfully the leaving animation scenario with the entering scenario of the next vue. We can rely on the beforeRouteLeave in-component guard for that:

![](../_resources/5b7604996bccfe7fea379a7088d6c24d.png)![1*cNh4Hmrf9Hn97OmgxyIruA.png](../_resources/22faec895a051edb1ddf8c341368d6c8.png)

This kind of logic should be tightly coupled with your data fetching, images caching and components preloading, to give transitions a perfect rendering.

### Keep your files tidy

Animations’ timelines syntax are verbose and your component’s files will quickly look bloated. Break down your animations in mixins:

![](../_resources/067ab03b8f27d7361bb45fbca9ff4746.png)![1*ozCSAOl1059Zj6VWM0s_Rw.png](../_resources/88c7f7b197d32edc9adb27804a54ef74.png)

An animation mixin file.

![](../_resources/625cc68db0a79f6614e0f5ff200b18da.png)![1*wW4-elvrHIKzroW08DBKgw.png](../_resources/1963ea81f69fb2bc4402e4efed032ae5.png)

Import the animations mixins in you component.

### Conclusion

After some tries I found the same creative freedom than during my old Flash/ActionScript days while developing a fully accessible/indexable HTML5 app, wich is great. Working this type of transitions can be a great added value in many contexts, however the level of complexity and the amongst of code can increase quickly, that’s why this type of architecture is better suited to projects who doesn’t own too many pages types.

* * *

*...*

### Notes

— We make extensive use of the “$.refs” object wich is considered as an edge case by the official Vue documentation. Of course it’s not optimal to select nodes of markups right after they have been mounted in the DOM and I hope to find a cleaner solution in the future.

— Navigation guards in deeply nested components can be buggy, keep your animation’s description at the top level of your app.

— Avoid the “keep-alive” option on your GSAP animated components for obvious reasons.

— Transitions system on single elements/components is already really comprehensive with [Vue.js](https://fr.vuejs.org/v2/guide/transitions.html#hooks-JavaScript); make sure that what you’re writing is not redundant with what is already available.

— Either your animations underline functional logics -and shouldn’t exceed 400ms- or participate to a more immersive storytelling, they should always be meaningful.

Thank you for your attention!