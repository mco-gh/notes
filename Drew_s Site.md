Drew's Site

#  Building a Programming Language Pt. 1 - Lexing

##  18 July 2019

It has long been a dream of mine to create a programming language from scratch. So I've finally decided to go ahead and do it. This post will be part of a series exploring how I wrote my first language step by step.

Keep in mind, this is my first semi-serious toy language. So I am not an expert in this field. Still I thought that this series might be a helpful guide for others trying to get into programming languages.

This series assumes some basic knowledge of programming. All samples are written in TypeScript so knowledge of TypeScript is a bonus.

**Update:** I've created a sandbox where you can run and play with the code from this post and other posts in the series. [It's available here](https://repl.it/@DrewYoungwerth/Smol).

# An Introduction to Smol

I'm calling this language Smol, as in a "small", easy to implement language. Here's what it looks like:

	# Supports numbers, strings and bools
	10;
	"Hello World!";
	true;
	false;

	# Constant declaration (x cannot be reassigned)
	let x = 5;

	# Variable declaration (y CAN be reassigned)
	var y = 10;

	# Proper infix notation
	let a = 5 * (3 + 4);

	# Function definition
	let foo = |x, y| {
	    # Basic if statement
	    if x > y { return x };

	    # Basic while loop
	    while x < y {
	        x += 1;
	        print("X is currently:");
	        print(x);
	    };

	    x # Supports implicit returns (the last expression of a function is returned automatically)
	};

	print(foo(x, y));

# Implementation Step 1 - Lexing

We'll start with the lexer (the part of our program that breaks smol text code into identifiable tokens). We'll be writing all of our programming language in TypeScript.

Lets start by defining what a Token looks like:
token.ts

	export type Token = {
	    // Our type is what we have identified the token to be
	    type: "operator" | "keyword" | "terminator" | "identifier" | "left-paren" |
	        "right-paren" | "pipe" | "left-curly" | "right-curly" | "string" | "number" |
	        "comma" | "boolean";

	    // The actual token
	    value: string;
	}

Now lets build the actual lexer.
lexer.ts

	export function lexer(smol: string) {
	    // First we break down the code into individual characters.
	    const chars = smol.split("");

	    // This will be where we store all the tokens we found.
	    const tokens: Token[] = [];

	    // This loop will consume all the characters and find the tokens inside.
	    while (chars.length > 0) {
	        // We remove the first character in the chars list.
	        const char = chars.shift()!;

	        // We copy (but do not remove) the next character as well.
	        // We need to look ahead one character to fully understand what the next token will be (in some cases).
	        const next = chars[0]

	        // A semicolon is our expression terminator.
	        if (char === ";") {
	            tokens.push({ type: "terminator", value: char });

	            // Any time we continue it means we have identified a token and consumed all the
	            // characters needed for that token.
	            continue;
	        }

	        // We'll define the isLetter function later
	        if (isLetter(char)) {
	            // Knowing the first character is a letter means our token can be a keyword, boolean,
	            // operator or identifier. To figure out which, we'll have to consume more characters
	            // until we find a space. We'll call this operation "extractWord" and write the function
	            // later (We'll define most of these helpers later on).
	            const word = `${char}${extractWord(chars)}`;

	            // Now that we have the word, we'll figure out what the word is.

	            if (isKeyword(word)) {
	                tokens.push({ type: "keyword", value: word });
	                continue;
	            }

	            if (isOperator(word)) {
	                tokens.push({ type: "operator", value: word });
	                continue;
	            }

	            if (isBool(word)) {
	                tokens.push({ type: "boolean", value: word });
	                continue;
	            }

	            // Since it wasn't anything above, it must be an identifier.
	            tokens.push({ type: "identifier", value: word });
	            continue;
	        }

	        // If we've made it this far, our char is not a letter or a semi-colon. So lets continue
	        // figuring out what our next token is.

	        if (isNum(char)) {
	            tokens.push({ type: "number", value: `${char}${extractNum(chars)}` });
	            continue;
	        }

	        // To make finding negative numbers easy, we consider a minus where the next character is a
	        // number to be a negative number.
	        if (char === "-" && isNum(next)) {
	            tokens.push({ type: "number", value: `-${extractNum(chars)}` });
	            continue;
	        }

	        // Our char is a " which means our token is a string.
	        if (char === "\"") {
	            tokens.push({ type: "string", value: extractString(chars) });
	            continue;
	        }

	        // Not all operators start with letters, so we need to look for them here too.
	        if (isOperator(char)) {
	            const fullOp = `${char}${extractOperator(chars)}`;
	            if (!isOperator(fullOp)) {
	                throw new Error(`Unkown operator: ${fullOp}`);
	            }
	            tokens.push({ type: "operator", value: fullOp });
	            continue;
	        }

	        // Whitspace characters can be ignored.
	        if (char === " " || char === "\t" || char === "" || char === "\n") continue;

	        // The rest of our known characters have their own type. So all we need to do is add them
	        // to our list and move on.

	        if (char === "|") {
	            tokens.push({ type: "pipe", value: "|" });
	            continue;
	        }

	        if (char === "{") {
	            tokens.push({ type: "left-curly", value: "{" });
	            continue;
	        }

	        if (char === "}") {
	            tokens.push({ type: "right-curly", value: "}" });
	            continue;
	        }

	        if (char === "(") {
	            tokens.push({ type: "left-paren", value: "(" });
	            continue;
	        }

	        if (char === ")") {
	            tokens.push({ type: "right-paren", value: ")" });
	            continue;
	        }

	        if (char === ",") {
	            tokens.push({ type: "comma", value: "," });
	            continue;
	        }

	        // If we've made it this far then the user put in a character that we don't understand.
	        throw new Error(`Unexpected token: ${char}`);
	    }

	    // Finally we return all the tokens we've found.
	    return tokens;
	}

Here are all the helpers we used earlier. The most important thing to note is that our "extract" functions need to acutally consume and modify the chars array we defined in our lexer function.

	const operators = [
	    "+", "-", "*", "/", "=", "==", "and", "or", "xor", "<", ">", ">=", "<=", "<>",
	    "=>", ".", "?"
	];

	const keywords = ["let", "var", "for", "in", "return", "break", "continue", "if", "else", "elif"];

	const isLetter = (char: string) => (/[a-zA-Z]|_/g).test(char);

	const isNum = (char: string) => (/[0-9]/g).test(char);

	const isOperator = (str: string) => operators.includes(str);

	const isKeyword = (str: string) => keywords.includes(str);

	const isBool = (str: string) => str === "true" || str === "false";

	const extractWord = (chars: string[]) => {
	    let word = "";
	    while (isLetter(chars[0]) || isNum(chars[0])) {
	        word += chars.shift();
	    }
	    return word;
	};

	const extractNum = (chars: string[]) => {
	    let hasHadDot = false;
	    let num = "";
	    while (chars.length > 0) {
	        const next = chars[0];
	        if (next === "." && hasHadDot) break;

	        if (next === ".") {
	            hasHadDot = true;
	            num += chars.shift();
	            continue;
	        }

	        if (isNum(next)) {
	            num += chars.shift();
	            continue;
	        }

	        break;
	    }
	    return num;
	};

	const extractString = (chars: string[]) => {
	    let string = "";
	    while (chars.length > 0) {
	        const char = chars.shift();
	        if (char === "\"") break;
	        string += char;
	    }
	    return string;
	};

	const extractOperator = (chars: string[]) => {
	    let op = "";
	    while (isOperator(chars[0])) {
	        op += chars.shift();
	    }
	    return op;
	};

In the next post of the series we'll implement a parser for our language.

If you have any suggestions on how I can improve this post or the lexer, don't hesistate to send me an email (found in the footer of this site).