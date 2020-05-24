Madlibz API

# Madlibz API

- [API Url and Queries](https://madlibz.herokuapp.com/api#api)

- [Example Calls](https://madlibz.herokuapp.com/api#examples)

- [Help](https://madlibz.herokuapp.com/api#help)

## Get a Random Madlib Template

The base url to get a random madlib template, is as follows:

	                                http://madlibz.herokuapp.com/api/random

The url query options are as follows:

| Query | Type | Description |
| --- | --- | --- |
| minlength | Number | The min number of user inputs in template |
| maxlength | Number | The max number of user inputs in template |

## Example API Calls

Here is an example call:

	                                http://madlibz.herokuapp.com/api/random?minlength=5&maxlength=25

Example output:

{
"blanks":
[
"foreign country",
"adverb",
"adjective",
"animal",
"verb ending in 'ing'",
"verb",
"verb ending in 'ing'",
"adverb",
"adjective",
"a place",
"type of liquid",
"part of the body",
"verb"
],
"value":
[
"If you are traveling in ",

" and find yourself having to cross a piranha-filled river, here's how to do it ",

": \n* Piranhas are more ",
" during the day, so cross the river at night.\n* Avoid areas with netted ",
" traps--piranhas may be ",
" there looking to ",
" them!\n* When ",
" the river, swim ",
". You don't want to wake them up and make them ",

"!\n* Whatever you do, if you have an open wound, try to find another way to get back to the ",

". Piranhas are attracted to fresh ",
" and will most likely take a bite out of your ",
" if you ",
" in the water!",
​ 0
],
"title": "How To Cross a Piranha-Infested River"
}

A demo of the output being used can be seen [here](https://madlibz.herokuapp.com/).

## Help

**Find an error?** Report it here: https://github.com/HermanFassett/madlibz/issues

**Want to add a Madlibs to the API?**

Edit this JSON file here: https://github.com/HermanFassett/madlibz/blob/master/data/templates.json

The format of the file is as follows:

{
"templates": [...]
}

To add your own Madlibs to the file, you need to put it in the "templates" array in the following format:

{
"title": "Your Madlibs Title",
"blanks": ["name", "verb ending in 'ing'"],
"value": ["Hello ", " what are you ", " ?", 0]
}

Where **title** is the name of your Madlibs, **blanks** contains **in order** the input types the user will need to do, and **value** contains the actual text of the Madlibs, split as an array wherever a blank is, and ending with a 0 (non string). Don't forget to include the spaces in these values. The 0 is there mostly for the one word example of Hello _____ noun. It shouldn't matter where in the json file you put your Madlibs, but please do put it at the end, and make sure, in proper json style, that the previous sample has a comma after it!!!