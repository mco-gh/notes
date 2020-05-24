kabirvirji/singlespotify

# [(L)](https://github.com/kabirvirji/singlespotify#singlespotify-)singlespotify 🎵

> Create Spotify playlists based on one artist through the command line

[[68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f64652d372e372e312d627269676874677265656e2e737667](../_resources/42c2b4d0ea187f55e8452b2c24804eeb.bin)](https://camo.githubusercontent.com/78fa7385f165085af2991d9b708f4e52b6b125a4/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f6e6f64652d372e372e312d627269676874677265656e2e737667)

[![singlespotify.gif](../_resources/b7a74cc3743897a2c301d609227f7a32.gif)](https://github.com/kabirvirji/singlespotify/blob/master/singlespotify.gif)

## [(L)](https://github.com/kabirvirji/singlespotify#install)Install

` $ npm install -g singlespotify `

**Note:** Node version 7.7.1+ required. ` $ node -v ` to check which version you have installed. The latest version can be downloaded [here](https://nodejs.org/en/)

## [(L)](https://github.com/kabirvirji/singlespotify#usage)Usage

` $ singlespotify "artist_name" `
The program will then prompt you for your Spotify username and bearer token.

You can get the bearer token here: https://developer.spotify.com/web-api/console/post-playlists/

Click **GET OAUTH TOKEN** and make sure to check *playlist-modify-public*
` $ singlespotify --help `

	normalUsage
	      $ singlespotify --artist [-a] "artist_name"
	      ? Enter your Spotify username <username>
	      ? Enter your Spotify bearer token <bearer>

	    Options
	      --name [-n] "playlist name"

	    Example
	      $ singlespotify "Kanye West" -n "My awesome playlist!"
	      ? Enter your Spotify username kabirvirji
	      ? Enter your Spotify bearer token ************************************************************

	    For more information visit https://github.com/kabirvirji/singlespotify
	normal

![](playlist.png)

## [(L)](https://github.com/kabirvirji/singlespotify#changelog)Changelog

- **03/15/17** Added [Inquirer](https://github.com/SBoudrias/Inquirer.js) and [conf](https://github.com/sindresorhus/conf) for authentication
- **03/16/17** Removed ` -a ` flag and added option to choose playlist name with ` -n ` flag

Shoutout to [kshvmdn](https://github.com/kshvmdn) for all the help!