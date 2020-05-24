Shields.io: Quality metadata badges for open source projects

## *☙ *Your Badge* ❧*

### Static

* * *

Using dash "-" separator
`https://img.shields.io/badge/<LABEL>-<MESSAGE>-<COLOR>.svg`
Dashes [object Object]
→
[object Object] Dash
Underscores [object Object]
→
[object Object] Underscore
[object Object] or Space [object Object]
→
[object Object] Space
Using query string parameters

`https://img.shields.io/static/v1.svg?label=<LABEL>&message=<MESSAGE>&color=<COLOR>`

### Colors

![-brightgreen-brightgreen.png](../_resources/76390e23431cd21641d8fc3fdf111ff7.png)![-critical-critical.png](../_resources/fcc476197821a10e1192df76c44cc0b0.png)![-yellowgreen-yellowgreen.png](../_resources/0ab8864bb64385c7f506c6a95eb4e766.png)![-green-green.png](../_resources/8d65ea720aff4f24a84391555ae09087.png)![-blue-blue.png](../_resources/78d82a2c6c9ad93132c671a7a60a9d7e.png)![-9cf-9cf.png](../_resources/dc2970dda0b979c8232b9835f73a96e6.png)![-orange-orange.png](../_resources/3df5cbeb8881bf4cd0bccee9821f6d36.png)![-lightgrey-lightgrey.png](../_resources/d15d06599eeda95d34980647782f527e.png)

![-success-success.png](../_resources/32e19d0b37354be0274340d3c7a5d7a3.png)![-important-important.png](../_resources/63663619308a7ab62a3aa4ffdc341516.png)![-ff69b4-ff69b4.png](../_resources/a8c577f213f7dcd65851a6355d9db0dc.png)![-informational-informational.png](../_resources/9d004d020591cb42b88985a32ace7355.png)![-inactive-inactive.png](../_resources/cfbf35773d18277ea49edbc3fd5fcd0e.png)

![-blueviolet-blueviolet.png](../_resources/1e8d4bdf012efaf3538ab724e516bc6a.png)![-red-red.png](../_resources/c33b94846f185b0102189dfc6579732b.png)![-yellow-yellow.png](../_resources/54d08c8dd16d7967f9e976d445dae2ee.png)

### Endpoint

`https://img.shields.io/endpoint.svg?url=<URL>&style<STYLE>`
Create badges from [your own JSON endpoint](https://shields.io/endpoint).

### Dynamic

`https://img.shields.io/badge/dynamic/json.svg?url=<URL>&label=<LABEL>&query=<[$.DATA.SUBDATA](https://jsonpath.com/)>&color=<COLOR>&prefix=<PREFIX>&suffix=<SUFFIX>`

`https://img.shields.io/badge/dynamic/xml.svg?url=<URL>&label=<LABEL>&query=<[//data/subdata](http://xpather.com/)>&color=<COLOR>&prefix=<PREFIX>&suffix=<SUFFIX>`

`https://img.shields.io/badge/dynamic/yaml.svg?url=<URL>&label=<LABEL>&query=<[$.DATA.SUBDATA](https://jsonpath.com/)>&color=<COLOR>&prefix=<PREFIX>&suffix=<SUFFIX>`

* * *

## *☙ *Styles* ❧*

The following styles are available. Flat is the default. Examples are shown with an optional logo:

[object Object]
![style-plastic-green.png](../_resources/46bb48be91275210668e40777e120ba8.png)
[object Object]
![style-flat-green.png](../_resources/942b71e02d67eb3f4229b08dd861cbdc.png)
[object Object]
![style-flat--square-green.png](../_resources/086c0f3177360a8497c2423cf0a31e7f.png)
[object Object]
![style-for--the--badge-green.png](../_resources/1401add2b92d7625277ce324adc8654d.png)
[object Object]
![style-popout-green.png](../_resources/f53c1d7141c8b5a39638342a3b98dd96.png)
[object Object]
![style-popout--square-green.png](../_resources/9fcbd6f9bc031c39f905702d0e0a3df5.png)
[object Object]
![style-social-green.png](../_resources/520d3b04fc569efc480df04ac32f1880.png)

Here are a few other parameters you can use: (connecting several with "&" is possible)

[object Object]

Override the default left-hand-side text ([URL-Encoding](https://developer.mozilla.org/en-US/docs/Glossary/percent-encoding) needed for spaces or special characters!)

[object Object]

Insert one of the named logos from (bitcoin, dependabot, discord, gitlab, npm, paypal, serverfault, stackexchange, superuser, telegram, travis) or [simple-icons](https://simpleicons.org/). Simple-icons are referenced using names as they appear on the simple-icons site. If the name includes spaces, replace them with dashes (e.g: [object Object])

[object Object]
Insert custom logo image (≥ 14px high)
[object Object]

Set the color of the logo (hex, rgb, rgba, hsl, hsla and css named colors supported)

[object Object]
Set the horizontal space to give to the logo
[object Object]

Specify what clicking on the left/right of a badge should do (esp. for social badge style)

[object Object]

Set background of the left part (hex, rgb, rgba, hsl, hsla and css named colors supported). The legacy name "colorA" is also supported.

[object Object]

Set background of the right part (hex, rgb, rgba, hsl, hsla and css named colors supported). The legacy name "colorB" is also supported.

[object Object]

Set the HTTP cache lifetime (rules are applied to infer a default value on a per-badge basis, any values specified below the default will be ignored). The legacy name "maxAge" is also supported.

We support `.svg`, `.json`, `.png` and a few others, but use them responsibly.