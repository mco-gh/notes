TeamOverVue/OverVue

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='68'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='969' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/TeamOverVue/OverVue#------overvue-beta)  [![apple-icon-72x72.png](../_resources/72663375b5bbc8c058851f0a12603bd7.png)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/overvue-icons/apple-icon-72x72.png)

OverVue (Beta)
**Prototyping Tool for Vue Developers**

OverVue is a prototyping tool that allows developers to *dynamically* create and visualize a Vue application, implementing a real-time intuitive *tree display* of component hierarchy and a live-generated *code preview*. The resulting boilerplate can be *exported* as a template for further development.

这个程序能帮你生成Vue 组件, 设置 routes , 也可以帮你显像Component Parent-Child组件树。你只要做一些小配置然后可以下载code boilerplate. 这样你就可以很方便简洁地生成Vue前台APP了！

[![screenshot.png](../_resources/f00de103cca6fd2abdd2fad480121a0e.png)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/gifs/screenshot.png)

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='69'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='980' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/TeamOverVue/OverVue#features)Features

- Upload a frontend mockup image
- Visualize draggable and resizable components
- Create parent-child hierarchy of components
- Add html elements to components
- Create routes to be used by Vue Router
- Live-generated previewable code snippets for each component
- Live-generated tree view to aid in visualizing parent-child hierarchy
- Save projects and open previous projects
- Export full boilerplate code for a working frontend

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='70'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='992' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/TeamOverVue/OverVue#how-to-use)How to use

- Opening the application will create by default a root App component and a root route called "HomeView"
- Upload a mockup from your filesystem if you'd like. Remove the mockup and choose a new one if needed.[![upload-image-drawers.gif](../_resources/a9a13f987b67cfbef16bfe11419b535d.gif)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/gifs/upload-image-drawers.gif)
- To add a new component, type its name in the component name box and select any HTML elements that should be rendered by that component.
- HTML elements can also be added after creation by selecting the component in the display, then selecting HTML elements.
- Select a parent component for the new component if needed.
- After adding, you can move and resize the component in the display.[![component_creation.gif](../_resources/228e80ffaad5003354fc5839209f2e87.gif)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/gifs/component_creation.gif)
- You can also add children to components by right-clicking the component to add children to, and you can see the tree re-render as you create new components or change the hierarchy.[![HTML-elements-tree-rerender.gif](../_resources/70a048a7eea2bd21ffb49c21d5b4443d.gif)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/gifs/HTML-elements-tree-rerender.gif)
- The dashboard shows info about each component (code snippets and HTML elements). Click a component in the display to see its properties.

[![snippets-active-component.gif](../_resources/3381aa6ebdd4eb728d5b3af5552fa0f1.gif)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/gifs/snippets-active-component.gif)

- You can add new routes and view all components and routes in the sidebar.[![sidebar-components-routes.gif](../_resources/6686c338346497f41e34cd0cff8cf496.gif)](https://raw.githubusercontent.com/jeisele2/OverVue/master/src/assets/gifs/sidebar-components-routes.gif)
- When finished creating, you can export to a file location of your choice. Below is the exported file structure:

	public/
	  index.html
	src/
	  assets/
	  components/
	    UserCreatedComponent1.vue
	    UserCreatedComponent2.vue
	    ...
	  views/
	    HomeView.vue
	    UserCreatedRouteComponent1.vue
	    UserCreatedRouteComponent2.vue
	    ...
	  App.vue
	  main.js
	  router.js
	babel.config.js
	package.json

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='71'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1016' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/TeamOverVue/OverVue#running-a-local-version)Running a local version

This app was developed using the Quasar framework, so first you will need to install the Quasar cli

	npm i -g @quasar/cli

Install dependencies

	npm i

To run electron app in dev mode

	quasar dev -m electron

To build a new .dmg

	quasar build -m electron

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='72'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1022' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/TeamOverVue/OverVue#contributing)Contributing

We'd love for you to test this application out and submit any issues you encounter. Also feel free to fork to your own repo and submit PRs. Here are some features we're thinking about adding:

- Vuex state prototyping and boilerplate export
- Ability to add additional mockup images for more routes
- Ability to nest HTML elements
- Option to export files in TypeScript

#### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='73'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='1030' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/TeamOverVue/OverVue#authors)Authors

	Contributors:
	Joseph Eisele @jeisele2
	Dean Chung @deanfchung
	Dean Ohashi @dnohashi
	Drew Nguyen @drewngyen

Inspired by [PreVue](https://github.com/open-source-labs/PreVue)