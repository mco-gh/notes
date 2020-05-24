Pretty Diff - The difference tool

# Pretty Diff, a language aware file comparison tool, beautifier, minifier and parser.

## Announcement —

Updated to [NPM](https://www.npmjs.com/package/prettydiff).

- [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 80 80' height='16' width='16' x='7' y='7' data-evernote-id='709' class='js-evernote-checked'%3e %3cg transform='translate(-78.37-208.06)' fill='%23111'%3e %3cpath d='m104.28 271.1c-3.571 0-6.373-.466-8.41-1.396-2.037-.93-3.495-2.199-4.375-3.809-.88-1.609-1.308-3.457-1.282-5.544.025-2.086.313-4.311.868-6.675l9.579-40.05 11.69-1.81-10.484 43.44c-.202.905-.314 1.735-.339 2.489-.026.754.113 1.421.415 1.999.302.579.817 1.044 1.546 1.395.729.353 1.747.579 3.055.679l-2.263 9.278'/%3e%3cpath d='m146.52 246.14c0 3.671-.604 7.03-1.811 10.07-1.207 3.043-2.879 5.669-5.01 7.881-2.138 2.213-4.702 3.935-7.693 5.167-2.992 1.231-6.248 1.848-9.767 1.848-1.71 0-3.42-.151-5.129-.453l-3.394 13.651h-11.162l12.52-52.19c2.01-.603 4.311-1.143 6.901-1.622 2.589-.477 5.393-.716 8.41-.716 2.815 0 5.242.428 7.278 1.282 2.037.855 3.708 2.024 5.02 3.507 1.307 1.484 2.274 3.219 2.904 5.205.627 1.987.942 4.11.942 6.373m-27.378 15.461c.854.202 1.91.302 3.167.302 1.961 0 3.746-.364 5.355-1.094 1.609-.728 2.979-1.747 4.111-3.055 1.131-1.307 2.01-2.877 2.64-4.714.628-1.835.943-3.858.943-6.071 0-2.161-.479-3.998-1.433-5.506-.956-1.508-2.615-2.263-4.978-2.263-1.61 0-3.118.151-4.525.453l-5.28 21.948'/%3e %3c/g%3e %3c/svg%3e)Donate](https://liberapay.com/prettydiff/donate)

- [NPM](https://www.npmjs.com/package/prettydiff/)

- [GitHub](https://github.com/prettydiff/prettydiff/)

- [Documentation](https://prettydiff.com/documentation.xhtml)

- [Sparser](https://sparser.io/)

 **Function**    Compare      Beautify      Minify      Parse Table

Latest Commit:**14 May 2019**  Version: **101.0.3**

## Compare Code

 Compare source file

 Source code label [(sourcelabel)](https://prettydiff.com/documentation.xhtml#sourcelabel)

Compare source code
1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

 Compare new file

 New code label [(difflabel)](https://prettydiff.com/documentation.xhtml#difflabel)

Compare new code
1

הההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההההה

XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

###

## Web Tool Options

- Ace Code Editor

   Enable Ace Code Editor      Disable Ace Code Editor (Faster and more accessible)

- Local Storage (localStorage)

   Save nothing      Save input and application state in local browser

- Pretty Diff Comment

## Pretty Diff Options

- Brace Lines [(brace_line)](https://prettydiff.com/documentation.xhtml#brace_line)

 false  true

If true an empty line will be inserted after opening curly braces and before closing curly braces.

- Brace Padding [(brace_padding)](https://prettydiff.com/documentation.xhtml#brace_padding)

 false  true

Inserts a space after the start of a container and before the end of the container if the contents of that container are not indented; such as: conditions, function arguments, and escaped sequences of template strings.

- Brace Style [(brace_style)](https://prettydiff.com/documentation.xhtml#brace_style)

Emulates JSBeautify's brace_style option using existing Pretty Diff options. **none** — Ignores this option

- Style of Indent [(braces)](https://prettydiff.com/documentation.xhtml#braces)

 false  true

Determines if opening curly braces will exist on the same line as their condition or be forced onto a new line. (Allman style indentation).

- Color [(color)](https://prettydiff.com/documentation.xhtml#color)

The color scheme of the reports. **white** — A white and pale grey color scheme

- Force an Empty Line Above Comments [(comment_line)](https://prettydiff.com/documentation.xhtml#comment_line)

 false  true
If a blank new line should be forced above comments.

- Indent Comments [(comments)](https://prettydiff.com/documentation.xhtml#comments)

 false  true

This will determine whether comments should always start at position 0 of each line or if comments should be indented according to the code.

- Generate A Complete HTML File [(complete_document)](https://prettydiff.com/documentation.xhtml#complete_document)

 false  true

Allows a preference for generating a complete HTML document instead of only generating content.

- Compressed CSS [(compressed_css)](https://prettydiff.com/documentation.xhtml#compressed_css)

 false  true

If CSS should be beautified in a style where the properties and values are minifed for faster reading of selectors.

- IE Comments (HTML Only) [(conditional)](https://prettydiff.com/documentation.xhtml#conditional)

 false  true

If true then conditional comments used by Internet Explorer are preserved at minification of markup.

- Ignore Content [(content)](https://prettydiff.com/documentation.xhtml#content)

 false  true

This will normalize all string content to 'text' so as to eliminate some differences from the output.

- Fix Sloppy Code [(correct)](https://prettydiff.com/documentation.xhtml#correct)

 false  true
Automatically correct some sloppiness in code.

- Line Termination [(crlf)](https://prettydiff.com/documentation.xhtml#crlf)

 false  true

If line termination should be Windows (CRLF) format. Unix (LF) format is the default.

- Insert Empty Lines [(css_insert_lines)](https://prettydiff.com/documentation.xhtml#css_insert_lines)

 false  true
Inserts new line characters between every CSS code block.

- Code Comments [(diff_comments)](https://prettydiff.com/documentation.xhtml#diff_comments)

 false  true

If true then comments will be preserved so that both code and comments are compared by the diff engine.

- Context Size [(diff_context)](https://prettydiff.com/documentation.xhtml#diff_context)

This shortens the diff output by allowing a specified number of equivalent lines between each line of difference. This option is only used with diff_format:html.

- Diff Format [(diff_format)](https://prettydiff.com/documentation.xhtml#diff_format)

The format of the output. The command line output format is text, similar to Unix 'diff'. **text** — Formatted similar to the Unix 'diff' command line utility.

- Label for Diff Sample [(diff_label)](https://prettydiff.com/documentation.xhtml#diff_label)

This allows for a descriptive label for the diff file code of the diff HTML output.

- Compare Rendered HTML [(diff_rendered_html)](https://prettydiff.com/documentation.xhtml#diff_rendered_html)

 false  true

Compares complete HTML documents and injects custom CSS so that the differences display not in the code, but in the rendered page in a browser. This option is currently confined only to markup languages, read_method file, and mode diff. Option diff_format is ignored.

- Remove White Space [(diff_space_ignore)](https://prettydiff.com/documentation.xhtml#diff_space_ignore)

 false  true
If white space only differences should be ignored by the diff tool.

- Diff View Type [(diff_view)](https://prettydiff.com/documentation.xhtml#diff_view)

This determines whether the diff HTML output should display as a side-by-side comparison or if the differences should display in a single table column. **sidebyside** — Two column comparison of changes.

- Else On New Line [(else_line)](https://prettydiff.com/documentation.xhtml#else_line)

 false  true
If else_line is true then the keyword 'else' is forced onto a new line.

- Trailing Comma [(end_comma)](https://prettydiff.com/documentation.xhtml#end_comma)

If there should be a trailing comma in arrays and objects. Value "multiline" only applies to modes beautify and diff. **never** — Remove trailing commas

- Force Indentation of All Attributes [(force_attribute)](https://prettydiff.com/documentation.xhtml#force_attribute)

 false  true
If all markup attributes should be indented each onto their own line.

- Force Indentation of All Content [(force_indent)](https://prettydiff.com/documentation.xhtml#force_indent)

 false  true

Will force indentation upon all content and tags without regard for the creation of new text nodes.

- Formatting Arrays [(format_array)](https://prettydiff.com/documentation.xhtml#format_array)

Determines if all array indexes should be indented, never indented, or left to the default. **default** — Default formatting

- Formatting Objects [(format_object)](https://prettydiff.com/documentation.xhtml#format_object)

Determines if all object keys should be indented, never indented, or left to the default. **default** — Default formatting

- Space After Function Name [(function_name)](https://prettydiff.com/documentation.xhtml#function_name)

 false  true
If a space should follow a JavaScript function name.

- Indentation Characters [(indent_char)](https://prettydiff.com/documentation.xhtml#indent_char)

The string characters to comprise a single indentation. Any string combination is accepted.

- Indentation Padding [(indent_level)](https://prettydiff.com/documentation.xhtml#indent_level)

How much indentation padding should be applied to beautification? This option is internally used for code that requires switching between libraries.

- Indent Size [(indent_size)](https://prettydiff.com/documentation.xhtml#indent_size)

The number of 'indent_char' values to comprise a single indentation.

- JavaScript Scope Identification [(jsscope)](https://prettydiff.com/documentation.xhtml#jsscope)

An educational tool to generate HTML output of JavaScript code to identify scope regions and declared references by color. This option is ignored unless the code language is JavaScript or TypeScript. **none** — prevents use of this option

- Language [(language)](https://prettydiff.com/documentation.xhtml#language)

The lowercase single word common name of the source code's programming language. The value 'auto' imposes language and lexer auto-detection, which ignores deliberately specified lexer values. The value 'text' is converted to 'auto' if options 'mode' is not 'diff'. Value 'text' allows literal comparisons.

- Language Auto-Detection Default [(language_default)](https://prettydiff.com/documentation.xhtml#language_default)

The fallback option if option 'lang' is set to 'auto' and a language cannot be detected.

- Formatted Name of the Code's Language [(language_name)](https://prettydiff.com/documentation.xhtml#language_name)

The formatted proper name of the code sample's language for use in reports read by people.

- Parsing Lexer [(lexer)](https://prettydiff.com/documentation.xhtml#lexer)

This option determines which sets of rules to use in the language parser. If option 'language' has a value of 'auto', which is the default value, this option is ignored. The value 'text' is converted to 'auto' if options 'mode' is not 'diff'. Value 'text' allows literal comparisons. **auto** — The value 'auto' imposes language and lexer auto-detection, which ignores deliberately specified language values.

- Method Chains [(method_chain)](https://prettydiff.com/documentation.xhtml#method_chain)

When to break consecutively chained methods and properties onto separate lines. A negative value disables this option. A value of 0 ensures method chains are never broken.

- Keep Comments [(minify_keep_comments)](https://prettydiff.com/documentation.xhtml#minify_keep_comments)

 false  true
Prevents minification from stripping out comments.

- Minification Wrapping [(minify_wrap)](https://prettydiff.com/documentation.xhtml#minify_wrap)

 false  true

Whether minified script should wrap after a specified character width. This option requires a value from option 'wrap'.

- Never Flatten Destructured Lists [(never_flatten)](https://prettydiff.com/documentation.xhtml#never_flatten)

 false  true
If destructured lists in script should never be flattend.

- New Line at End of Code [(new_line)](https://prettydiff.com/documentation.xhtml#new_line)

 false  true
Insert an empty line at the end of output.

- Case Indentation [(no_case_indent)](https://prettydiff.com/documentation.xhtml#no_case_indent)

 false  true

If a case statement should receive the same indentation as the containing switch block.

- Leading 0s [(no_lead_zero)](https://prettydiff.com/documentation.xhtml#no_lead_zero)

 false  true

Whether leading 0s in CSS values immediately preceeding a decimal should be removed or prevented.

- Object/Attribute Sort [(object_sort)](https://prettydiff.com/documentation.xhtml#object_sort)

 false  true
Sorts markup attributes and properties by key name in script and style.

- Parse Format [(parse_format)](https://prettydiff.com/documentation.xhtml#parse_format)

Determines the output format for 'parse' mode. **parallel** — returns an object containing series of parallel arrays

- Retain White Space Tokens in Parse Output [(parse_space)](https://prettydiff.com/documentation.xhtml#parse_space)

 false  true
Whether whitespace tokens should be included in markup parse output.

- Preserve Consecutive New Lines [(preserve)](https://prettydiff.com/documentation.xhtml#preserve)

The maximum number of consecutive empty lines to retain.

- Eliminate Word Wrap Upon Comments [(preserve_comment)](https://prettydiff.com/documentation.xhtml#preserve_comment)

 false  true
Prevent comment reformatting due to option wrap.

- Preserve Markup Text White Space [(preserve_text)](https://prettydiff.com/documentation.xhtml#preserve_text)

 false  true

If text in the provided markup code should be preserved exactly as provided. This option eliminates beautification and wrapping of text content.

- Normalize Quotes [(quote)](https://prettydiff.com/documentation.xhtml#quote)

 false  true

If true and mode is 'diff' then all single quote characters will be replaced by double quote characters in both the source and diff file input so as to eliminate some differences from the diff report HTML output.

- Indent Size [(quote_convert)](https://prettydiff.com/documentation.xhtml#quote_convert)

If the quotes of script strings or markup attributes should be converted to single quotes or double quotes. **none** — Ignores this option

- Indent Size [(selector_list)](https://prettydiff.com/documentation.xhtml#selector_list)

 false  true
If comma separated CSS selectors should present on a single line of code.

- Indent Size [(semicolon)](https://prettydiff.com/documentation.xhtml#semicolon)

 false  true

If true and mode is 'diff' and lang is 'javascript' all semicolon characters that immediately precede any white space containing a new line character will be removed so as to eliminate some differences from the code comparison.

- Label for Source Sample [(source_label)](https://prettydiff.com/documentation.xhtml#source_label)

This allows for a descriptive label of the source file code for the diff HTML output.

- Function Space [(space)](https://prettydiff.com/documentation.xhtml#space)

 false  true
Inserts a space following the function keyword for anonymous functions.

- Close Markup Self-Closing Tags with a Space [(space_close)](https://prettydiff.com/documentation.xhtml#space_close)

 false  true
Markup self-closing tags end will end with ' />' instead of '/>'.

- Script Styleguide [(styleguide)](https://prettydiff.com/documentation.xhtml#styleguide)

Provides a collection of option presets to easily conform to popular JavaScript style guides. **none** — Ignores this option

- Merge Adjacent Start and End tags [(tag_merge)](https://prettydiff.com/documentation.xhtml#tag_merge)

 false  true

Allows immediately adjacement start and end markup tags of the same name to be combined into a single self-closing tag.

- Sort Markup Child Items [(tag_sort)](https://prettydiff.com/documentation.xhtml#tag_sort)

 false  true
Sort child items of each respective markup parent element.

- Keep Ternary Statements On One Line [(ternary_line)](https://prettydiff.com/documentation.xhtml#ternary_line)

 false  true
If ternary operators in JavaScript ? and : should remain on the same line.

- Retain Comment At Code Start [(top_comments)](https://prettydiff.com/documentation.xhtml#top_comments)

 false  true

If mode is 'minify' this determines whether comments above the first line of code should be kept.

- Markup Tag Preservation [(unformatted)](https://prettydiff.com/documentation.xhtml#unformatted)

 false  true

If markup tags should have their insides preserved. This option is only available to markup and does not support child tokens that require a different lexer.

- Variable Declaration Lists [(variable_list)](https://prettydiff.com/documentation.xhtml#variable_list)

If consecutive JavaScript variables should be merged into a comma separated list or if variables in a list should be separated. **none** — Ignores this option.

- Vertical Alignment [(vertical)](https://prettydiff.com/documentation.xhtml#vertical)

 false  true

If lists of assignments and properties should be vertically aligned. This option is not used with the markup lexer.

- Wrap [(wrap)](https://prettydiff.com/documentation.xhtml#wrap)

Character width limit before applying word wrap. A 0 value disables this option. A negative value concatenates script strings.