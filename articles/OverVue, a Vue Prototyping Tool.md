OverVue, a Vue Prototyping Tool.

# OverVue, a Vue Prototyping Tool.

[![0*qkQXMFum9cSW5AZD](../_resources/2fd584b6aa9a67ff5d481d9f793a0b5c.jpg)](https://medium.com/@deanchung_22636?source=post_page---------------------------)

[Dean Chung](https://medium.com/@deanchung_22636?source=post_page---------------------------)

[Jul 26](https://medium.com/@deanchung_22636/overvue-a-vue-prototyping-tool-f2b8a2f0c229?source=post_page---------------------------) · 4 min read

![1*3Kvo1fMGpdtrC637LzKqdw.png](../_resources/c6fe46faa634978b1b93204a4f8a0fea.png)
![1*3Kvo1fMGpdtrC637LzKqdw.png](../_resources/28800006ee1bd3e217e5d4af402eec3b.png)

As of July 2019, Vue sits atop all JavaScript frameworks in GitHub stars and #3 overall, surpassing React by over ten thousand stars and leaving Angular in the dust.

As the youngest of the big three front-end JavaScript frameworks it has exploded in popularity and has quickly become beloved in the developer community. This is despite the fact that Angular and React are backed by Google and Facebook.

As the youngest framework of the three, the developer ecosystem for Vue lags behind those of its competitors. OverVue is here to deliver and to help developers to quickly begin building their web applications.

At its core, OverVue is a desktop application built with Vue and Electron that allows the user to create Vue components, establish parent-child hierarchy, and to set up routes with Vue Router, all from a beautiful user interface. Once satisfied, the user can generate the file and export the boilerplate code to a project. Here are some more of its hot features!

# Upload an Image

This first part is optional, but very useful if you have a well thought out design that you are ready to turn into code. Open the sidebar on the left and click ‘upload image’ to choose your mockup image from your file system. Clicking the arrow next to ‘Dashboard’ will toggle between showing and minimizing your dashboard.

![1*M4Gqbr3U63KNWzr1VS-g8Q.gif](../_resources/109d1cd8c8ad69292804ba6e3a41f57a.jpg)
![1*qaE_mHtnz77xa_4RQZtTXQ.gif](../_resources/4c7ca8436479c75907b564a26d2f1080.gif)
Image Upload

# **Create a Component**

Creating a component in OverVue is very simple. Give your component a name, select any HTML elements to place in the Vue template, and select a parent from the dropdown menu in the sidebar if applicable. Once you create your component, you can drag and resize your component to fit your image mockup. If you forget to specify parent-child hierarchy in the dropdown menu, you can simply right-click your component to adjust the hierarchy.

# Component OverVue

Toggle between active components with a left click. Adjust your desired HTML elements from the component menu on the left and keep track of them in the dashboard. Visualize your parent child hierarchy with Team OverVue’s beautifully re-rendering tree.

![1*ZobDODRkl_QeNM0M_4z0lg.gif](../_resources/8a38eb7701a566356db7554647f263f0.jpg)
![1*cKBIp-6ivSH_tJwh1bREPQ.gif](../_resources/b169e699edbeb927dbca246d4090c711.gif)
Tree and HTML re-render

# Code Snippets

Click the code snippet tab in the dashboard panel to see your code. Feel free to copy the code onto your clipboard and paste it directly into your project.

![1*qaE_mHtnz77xa_4RQZtTXQ.gif](../_resources/793059478d20bc7fbd32a8bdb4ec5cb9.jpg)
![1*M4Gqbr3U63KNWzr1VS-g8Q.gif](../_resources/58995b25dfd1e0529b918df29945e3c5.gif)
Code

# Router Support

Enter a route name in the ‘routes’ dropdown and hit ‘enter’ to add routes to your application. Toggling between routes will only show on the canvas the components that exist in the active path. This is essentially what Vue Router does in practice in your application. Any changes to your route structure will seamlessly update the visualization tree.

![1*cKBIp-6ivSH_tJwh1bREPQ.gif](../_resources/c0708a23380fc48f667310a86380eee0.jpg)
![1*ZobDODRkl_QeNM0M_4z0lg.gif](../_resources/37a954529f39a20a9db44f8b2daa86e1.gif)
Routes

# Save/Export

Once you are done you can save your project and open it later, or you can export your new boilerplate code to your workspace. A package.json is created and you can npm/yarn install your dependencies.

# Moving Forward

There are several features we have not yet completed. Since this tool is open source, help is welcome. Some features we did not yet implement are:

1. Vuex state management
2. TypeScript integration
3. Ability to nest HTML elements

4. Ability to drag only a specific parent along with its children with Vue Draggable Resizable.

5. A CLI version and npm package
6. Ability to upload multiple images for each route
Any suggestions are welcome!

The OverVue team is proud to launch our product in Beta. We welcome the first users and testers of our application. We are happy to help developers speed up their initial application architecture setup and to speed up development with this beautiful abstraction.

Check out our website [here](http://www.overvue.io/?source=post_page---------------------------).

Check out the GitHub [here](http://www.github.com/TeamOverVue/OverVue?source=post_page---------------------------).

We intended for this to be easy to use and pleasant to experience for anyone familiar with Vue or a similar framework. Huge thank you for all the hard work of my fellow software engineers Dean Ohashi, Drew Nguyen, and Joseph Eisele.