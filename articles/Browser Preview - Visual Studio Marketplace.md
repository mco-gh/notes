Browser Preview - Visual Studio Marketplace

#

 ![icon_128.png](../_resources/4feb1965e4625ae3b7c41b7218af8637.png)
Browser Preview for VS Code

#### A real browser preview inside your editor that you can debug.

Browser Preview for VS Code enables you to open a real browser preview inside your editor that you can debug. Browser Preview is powered by [Chrome Headless](https://developers.google.com/web/updates/2017/04/headless-chrome), and works by starting a headless Chrome instance in a new process. This enables a secure way to render web content inside VS Code, and enables interesting features such as in-editor debugging and more!

![demo.gif](../_resources/18b2785764500a3def207c564e8356b4.gif)

## Getting started

1. Grab extension from [marketplace](https://marketplace.visualstudio.com/items?itemName=auchenberg.vscode-browser-preview)

2. Click the new "Browser Preview" button in the Side Bar to the left or run the command [object Object]

Make sure you have Google Chrome installed on your computer.

## Features

- Browser preview inside VS Code (Powered by [Chrome Headless](https://developers.google.com/web/updates/2017/04/headless-chrome)).
- Ability to have multiple previews open at the same time.
- Debuggable. Launch urls and attach [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome) to the browser view instance, and debug within VS Code.
- Attach Chrome DevTools via [object Object]
- Option to set the default startUrl via [object Object]
- Option to set the path to the chrome exectuable via [object Object]
- Option to set the type of rendering via [object Object] with the support for [object Object] (default one) and [object Object] formats

## How to change the default start url / start page?

Go to your settings, search for "browser preview" and set [object Object] to your desired url.

![settings.png](../_resources/13dc823ad91ba2cd9b5823263ec90ea6.png)

## Launch and Debugging

You can enable in-editor debugging of Browser Preview by installing [Debugger for Chrome](https://marketplace.visualstudio.com/items?itemName=msjsdiag.debugger-for-chrome), and configure VS Code's debugger to either attach or launch to the browser previews by using the following configuration:

[object Object]

The debug configuration also supports these additional properties: [object Object], [object Object], [object Object], [object Object] and [object Object]. See https://github.com/Microsoft/vscode-chrome-debug#other-optional-launch-config-fields for details on how to use.

### Watch It

[Watch an animated gif](https://github.com/auchenberg/vscode-browser-preview/blob/master/docs/DEBUGGING.md) showing how to open the preview and debug a browser app.

## Additional configuration

Browser Preview has the following settings:
[object Object]