Free API to generate avatars with initials - User Initial avatars

# UI Avatars

## Generate avatars with initials from names.

UI Avatars has a simple-to-use API with no limiting or login. No usage tracking and no information is stored. The final images are cached, but nothing else.

**NEW:**  [better language/script support](https://ui-avatars.com/#language-script-support).

![Example avatars](../_resources/31c292b57c009cb93ac81ed8876f554e.png)

## Usage

All requests returns a image stream to be used direcly in a `<img/>` tag.

### Generate a avatar with default settings, for user "John Doe".

`GET https://ui-avatars.com/api/?name=John+Doe`

### Generate a blue avatar

`GET https://ui-avatars.com/api/?background=0D8ABC&color=fff`

## Settings

### Image Size (`size`)

Avatar image size in pixels. Between: 16 and 256. Default: 64
`GET https://ui-avatars.com/api/?size=128`

### Font Size (`font-size`)

Font size in percentage of `size`. Between 0.1 and 1. Default: 0.5
`GET https://ui-avatars.com/api/?font-size=0.33`

### Initial Characters (`length`)

Length of the generated initials. Default: 2
`GET https://ui-avatars.com/api/?length=1`

### Name (`name`)

The name used to generate initials. You can specify the initals yourself as well. Default: John Doe

`GET https://ui-avatars.com/api/?name=Elon+Musk`

### Rounded Image (`rounded`)

Boolean specifying if the returned image should be a circle. Default: false
`GET https://ui-avatars.com/api/?rounded=true`

### Background Color (`background`)

Hex color for the image background, without the hash (#). Default: ddd
`GET https://ui-avatars.com/api/?background=a0a0a0`

### Font Color (`color`)

Hex color for the font, without the hash (#). Default: 222
`GET https://ui-avatars.com/api/?color=ff0000`
All settings above can be mixed together as you desire.

## With gravatar or similar

A good use-case would be using it as a fallback for Gravatar. Example:

`https://www.gravatar.com/avatar/EMAIL_MD5?d=https%3A%2F%2Fui-avatars.com%2Fapi%2F/Lasse+Rafn/128`

Because of limitations in Gravatar, we must pass in the parameters as sub-directories, instead of query-parameters. You should also consider urlencoding the name, in case it contains special characters. It's a limitation by Gravatar, not UI Avatars.

The order is as follows:

- name
- size
- background
- color
- length
- font-size
- rounded

## Retina

I recommend using 1.5x or 2x sizes for your avatars, but keeping the img tag the original size, to ensure crisp avatars on high DPI screens.

## Language/Script support

I have added support for some unicode scripts/languages that are not supported by the typical fonts. Current support:

- Arabic
- Armenian
- Bengali
- Georgian
- Hebrew
- Chinese
- Japanese
- Mongolian
- Thai
- Tibetan

## Wordpress plugin

You can also use the [Wordpress plugin](https://wordpress.org/plugins/wp-initials-avatar/), which is also free.

* * *

Made by [Lasse Rafn](https://twitter.com/lasserafn)
[Code on Github](https://github.com/LasseRafn/ui-avatars)

[Hosted on Linode](https://www.linode.com/?r=b05be75c869a29b689317ac1f61442d3ba3eaee6)