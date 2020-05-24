EditorConfig

## What's an EditorConfig file look like?

### Example file

Below is an example `.editorconfig` file setting end-of-line and indentation styles for Python and JavaScript files.

	*# EditorConfig is awesome: https://EditorConfig.org
	*
	*# top-most EditorConfig file
	*root = true

	*# Unix-style newlines with a newline ending every file
	*[*]
	end_of_line = lf
	insert_final_newline = true

	*# Matches multiple files with brace expansion notation
	# Set default charset
	*[*.{js,py}]
	charset = utf-8

	*# 4 space indentation
	*[*.py]
	indent_style = space
	indent_size = 4

	*# Tab indentation (no size specified)
	*[Makefile]
	indent_style = tab

	*# Indentation override for all JS under lib directory
	*[lib/**.js]
	indent_style = space
	indent_size = 2

	*# Matches the exact files either package.json or .travis.yml
	*[{package.json,.travis.yml}]
	indent_style = space
	indent_size = 2

Check the Wiki for some real-world examples of [projects using EditorConfig files](https://github.com/editorconfig/editorconfig/wiki/Projects-Using-EditorConfig).

### Where are these files stored?

When opening a file, EditorConfig plugins look for a file named `.editorconfig` in the directory of the opened file and in every parent directory. A search for `.editorconfig` files will stop if the root filepath is reached or an EditorConfig file with `root=true` is found.

EditorConfig files are read top to bottom and the most recent rules found take precedence. Properties from matching EditorConfig sections are applied in the order they were read, so properties in closer files take precedence.

**For Windows Users:** To create an `.editorconfig` file within Windows Explorer, you need to create a file named `.editorconfig.`, which Windows Explorer will automatically rename to `.editorconfig`.

### File Format Details

EditorConfig files use an INI format that is compatible with the format used by [Python ConfigParser Library](https://docs.python.org/2/library/configparser.html), but `[` and `]` are allowed in the section names. The section names are filepath [globs](https://en.wikipedia.org/wiki/Glob_(programming)) (case sensitive), similar to the format accepted by [gitignore](https://git-scm.com/docs/gitignore#_pattern_format). Only forward slashes (`/`, not backslashes) are used as path separators and octothorpes (`#`) or semicolons (`;`) are used for comments. Comments should go on their own lines. EditorConfig files should be UTF-8 encoded, with either `CRLF` or `LF` line separators. EditorConfig files are read top to bottom and the most recent rules found take precedence.

Filepath glob patterns and currently-supported EditorConfig properties are explained below.

#### Wildcard Patterns

Special characters recognized in section names for wildcard matching:

[object Object]
Matches any string of characters, except path separators ([object Object])
[object Object]
Matches any string of characters
[object Object]
Matches any single character
[object Object]
Matches any single character in *name*
[object Object]
Matches any single character not in *name*
[object Object]

Matches any of the strings given (separated by commas) (**Available since EditorConfig Core 0.11.0**)

[object Object]

Matches any integer numbers between *num1* and *num2*, where num1 and num2 can be either positive or negative

Special characters can be escaped with a backslash so they won't be interpreted as wildcard patterns.

#### Supported Properties

Note that not all properties are supported by every plugin. The wiki has a [complete list of properties](https://github.com/editorconfig/editorconfig/wiki/EditorConfig-Properties).

- `indent_style`: set to "open-quotetabclose-quote" or "open-quotespaceclose-quote" to use hard tabs or soft tabs respectively.

- `indent_size`: a whole number defining the number of columns used for each indentation level and the width of soft tabs (when supported). When set to "open-quotetabclose-quote", the value of **`tab_width`** (if specified) will be used.

- `tab_width`: a whole number defining the number of columns used to represent a tab character. This defaults to the value of **`indent_size`** and doesn't usually need to be specified.

- `end_of_line`: set to "open-quotelfclose-quote", "open-quotecrclose-quote", or "open-quotecrlfclose-quote" to control how line breaks are represented.

- `charset`: set to "open-quotelatin1close-quote", "open-quoteutf-8close-quote", "open-quoteutf-8-bomclose-quote", "open-quoteutf-16beclose-quote" or "open-quoteutf-16leclose-quote" to control the character set.

- `trim_trailing_whitespace`: set to "open-quotetrueclose-quote" to remove any whitespace characters preceding newline characters and "open-quotefalseclose-quote" to ensure it doesn't.

- `insert_final_newline`: set to "open-quotetrueclose-quote" to ensure file ends with a newline when saving and "open-quotefalseclose-quote" to ensure it doesn't.

- `root`: special property that should be specified at the top of the file outside of any sections. Set to "open-quotetrueclose-quote" to stop `.editorconfig` files search on current file.

For any property, a value of "unset" is to remove the effect of that property, even if it has been set before. For example, add `indent_size = unset` to undefine **`indent_size`** property (and use editor default).

Currently all properties and values are case-insensitive. They are lowercased when parsed. Generally, if a property is not specified, the editor settings will be used, i.e. EditorConfig takes no effect on that part. For any property, a value of "unset" is to remove the effect of that property, even if it has been set before. For example, add "indent_size = unset" to undefine **`indent_size`** property (and use editor default).

It is acceptable and often preferred to leave certain EditorConfig properties unspecified. For example, **`tab_width`** need not be specified unless it differs from the value of **`indent_size`**. Also, when **`indent_style`** is set to "tab", it may be desirable to leave **`indent_size`** unspecified so readers may view the file using their preferred indentation width. Additionally, if a property is not standardized in your project (**`end_of_line`** for example), it may be best to leave it blank.