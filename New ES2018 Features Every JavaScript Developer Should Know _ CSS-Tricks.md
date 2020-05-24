New ES2018 Features Every JavaScript Developer Should Know | CSS-Tricks

[Home](https://css-tricks.com/)  /[Articles](https://css-tricks.com/archives/)  /

# New ES2018 Features Every JavaScript Developer Should Know

[![25e546a6e2e1903d2554412d24aa57ee](../_resources/24b38985b4a7f3847c56672ef92789e7.png)](https://css-tricks.com/author/faraz-kelhini/)![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='half-circle js-evernote-checked' width='80px' height='80px' data-evernote-id='202'%3e %3cpath d='M102 4c0 27.1-21.9 49-49 49S4 31.1 4 4' data-evernote-id='2941' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)

Author
[Faraz Kelhini](https://css-tricks.com/author/faraz-kelhini/)
13 Comments

[Go to Comments![](data:image/svg+xml,%3csvg width='24' height='24' viewBox='0 0 24 24' fill='none' xmlns='http://www.w3.org/2000/svg' class='icon-arrow-right js-evernote-checked' data-evernote-id='210'%3e %3cpath d='M7 12.5L23 12.5' stroke='url(%23paint0_linear)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='211' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M1 12.5H2' stroke='url(%23paint1_linear)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='212' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M17.5 7L23 12.5L17.5 18' stroke='url(%23paint2_linear)' stroke-width='2' stroke-linecap='round' stroke-linejoin='round' data-evernote-id='213' class='js-evernote-checked'%3e%3c/path%3e %3cdefs data-evernote-id='214' class='js-evernote-checked'%3e %3clinearGradient id='paint0_linear' x1='10.7498' y1='12.5' x2='11.3447' y2='9.73465' gradientUnits='userSpaceOnUse' data-evernote-id='215' class='js-evernote-checked'%3e %3cstop stop-color='%23FF8A00' data-evernote-id='216' class='js-evernote-checked'%3e%3c/stop%3e %3cstop offset='1' stop-color='%23DA1B60' data-evernote-id='217' class='js-evernote-checked'%3e%3c/stop%3e %3c/linearGradient%3e %3clinearGradient id='paint1_linear' x1='1.23436' y1='12.5' x2='2.00945' y2='12.2748' gradientUnits='userSpaceOnUse' data-evernote-id='218' class='js-evernote-checked'%3e %3cstop stop-color='%23FF8A00' data-evernote-id='219' class='js-evernote-checked'%3e%3c/stop%3e %3cstop offset='1' stop-color='%23DA1B60' data-evernote-id='220' class='js-evernote-checked'%3e%3c/stop%3e %3c/linearGradient%3e %3clinearGradient id='paint2_linear' x1='18.789' y1='17.9995' x2='23.3162' y2='17.3419' gradientUnits='userSpaceOnUse' data-evernote-id='221' class='js-evernote-checked'%3e %3cstop stop-color='%23FF8A00' data-evernote-id='222' class='js-evernote-checked'%3e%3c/stop%3e %3cstop offset='1' stop-color='%23DA1B60' data-evernote-id='223' class='js-evernote-checked'%3e%3c/stop%3e %3c/linearGradient%3e %3c/defs%3e %3c/svg%3e)](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#comments)

Published
Jan 9, 2019
Updated
Jul 30, 2019
[es2018](https://css-tricks.com/tag/es2018/)

[[chriscoyier_fmktwo.webp](../_resources/6fc69e06baea9bfae4c0fa4d2964306c.webp)](https://synd.co/2om6Ndq)

[300x250-stateful_2x_dju61c.webp](../_resources/829ebcb4363325940519ccaf471c34f0.webp)Effortlessly add state to your apps with [FaunaDB](https://synd.co/2om6Ndq). Native GraphQL. Start free.

In-depth [front-end engineering courses](https://synd.co/2mN0zCe)

The ninth edition of the ECMAScript standard, officially known as ECMAScript 2018 (or ES2018 for short), was released in June 2018. Starting with ES2016, new versions of ECMAScript specifications are released yearly rather than every several years and add fewer features than major editions used to. The newest edition of the standard continues the yearly release cycle by adding four new `RegExp` features, rest/spread properties, asynchronous iteration, and `Promise.prototype.finally`. Additionally, ES2018 drops the syntax restriction of escape sequences from tagged templates.

These new changes are explained in the subsections that follow.

### [#](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#article-header-id-0)The Rest/Spread Properties

One of the most interesting features added to ES2015 was the spread operator. This operator makes copying and merging arrays a lot simpler. Rather than calling the `concat()` or `slice()` method, you could use the `...` operator:

JavaScript	const arr1 = [10, 20, 30];

	*// make a copy of arr1*
	const copy = [...arr1];

	console.log(copy);    *// → [10, 20, 30]*

	const arr2 = [40, 50];

	*// merge arr2 with arr1*
	const merge = [...arr1, ...arr2];

	console.log(merge);    *// → [10, 20, 30, 40, 50]*

The spread operator also comes in handy in situations where an array must be passed in as separate arguments to a function. For example:

JavaScript	const arr = [10, 20, 30]

	*// equivalent to*
	*// console.log(Math.max(10, 20, 30));*
	console.log(Math.max(...arr));    *// → 30*

ES2018 further expands this syntax by adding spread properties to object literals. With the spread properties you can copy own enumerable properties of an object onto a new object. Consider the following example:

JavaScript	const obj1 = {

	  a: 10,
	  b: 20
	};

	const obj2 = {
	  ...obj1,
	  c: 30
	};

	console.log(obj2);    *// → {a: 10, b: 20, c: 30}*

In this code, the `...` operator is used to retrieve the properties of `obj1` and assign them to `obj2`. Prior to ES2018, attempting to do so would throw an error. If there are multiple properties with the same name, the property that comes last will be used:

JavaScript	const obj1 = {

	  a: 10,
	  b: 20
	};

	const obj2 = {
	  ...obj1,
	  a: 30
	};

	console.log(obj2);    *// → {a: 30, b: 20}*

Spread properties also provide a new way to merge two or more objects, which can be used as an alternative to the `Object.assign()` method:

JavaScript	const obj1 = {a: 10};

	const obj2 = {b: 20};
	const obj3 = {c: 30};

	*// ES2018*
	console.log({...obj1, ...obj2, ...obj3});    *// → {a: 10, b: 20, c: 30}*

	*// ES2015*
	console.log(Object.assign({}, obj1, obj2, obj3));    *// → {a: 10, b: 20, c: 30}*

Note, however, that spread properties do not always produce the same result as `Object.assign()`. Consider the following code:

JavaScript	Object.defineProperty(Object.prototype, 'a', {

	  set(value) {
	    console.log('set called!');
	  }
	});

	const obj = {a: 10};

	console.log({...obj});
	*// → {a: 10}*

	console.log(Object.assign({}, obj));
	*// → set called!*
	*// → {}*

In this code, the `Object.assign()` method executes the inherited setter property. Conversely, the spread properties simply ignore the setter.

It's important to remember that spread properties only copy enumerable properties. In the following example, the `type` property won’t show up in the copied object because its `enumerable` attribute is set to `false`:

JavaScript	const car = {

	  color: 'blue'
	};

	Object.defineProperty(car, 'type', {
	  value: 'coupe',
	  enumerable: false
	});

	console.log({...car});    *// → {color: "blue"}*

Inherited properties are ignored even if they are enumerable:
JavaScript	const car = {

	  color: 'blue'
	};

	const car2 = Object.create(car, {
	  type: {
	    value: 'coupe',
	    enumerable: true,
	  }
	});

	console.log(car2.color);                      *// → blue*
	console.log(car2.hasOwnProperty('color'));    *// → false*

	console.log(car2.type);                       *// → coupe*
	console.log(car2.hasOwnProperty('type'));     *// → true*

	console.log({...car2});                       *// → {type: "coupe"}*

In this code, `car2` inherits the `color` property from `car`. Because spread properties only copy the own properties of an object, `color` is not included in the return value.

Keep in mind that spread properties can only make a shallow copy of an object. If a property holds an object, only the reference to the object will be copied:

JavaScript	const obj = {x: {y: 10}};

	const copy1 = {...obj};
	const copy2 = {...obj};

	console.log(copy1.x === copy2.x);    *// → true*

The `x` property in `copy1` refers to the same object in memory that `x` in `copy2` refers to, so the strict equality operator returns `true`.

Another useful feature added to ES2015 was rest parameters, which enabled JavaScript programmers to use `...` to represent values as an array. For example:

JavaScript	const arr = [10, 20, 30];

	const [x, ...rest] = arr;

	console.log(x);       *// → 10*
	console.log(rest);    *// → [20, 30]*

Here, the first item in `arr` is assigned to `x`, and remaining elements are assigned to the `rest` variable. This pattern, called array destructuring, became so popular that the Ecma Technical Committee decided to bring similar functionality to objects:

JavaScript	const obj = {

	  a: 10,
	  b: 20,
	  c: 30
	};

	const {a, ...rest} = obj;

	console.log(a);       *// → 10*
	console.log(rest);    *// → {b: 20, c: 30}*

This code uses the rest properties in a destructuring assignment to copy the remaining own enumerable properties into a new object. Note that rest properties must always appear at the end of the object, otherwise an error is thrown:

JavaScript	const obj = {

	  a: 10,
	  b: 20,
	  c: 30
	};

	const {...rest, a} = obj;    *// → SyntaxError: Rest element must be last element*

Also keep in mind that using multiple rest syntaxes in an object causes an error unless they are nested:

JavaScript	const obj = {

	  a: 10,
	  b: {
	    x: 20,
	    y: 30,
	    z: 40
	  }
	};

	const {b: {x, ...rest1}, ...rest2} = obj;    *// no error*

	const {...rest, ...rest2} = obj;    *// → SyntaxError: Rest element must be last element*

#### Support for Rest/Spread Properties

| Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- |
| 60  | 55  | 11.1 | No  |

| Chrome Android | Firefox Android | iOS Safari | Edge Mobile | Samsung Internet | Android Webview |
| --- | --- | --- | --- | --- | --- |
| 60  | 55  | 11.3 | No  | 8.2 | 60  |

****Node.js:****

- •8.0.0 (requires the `--harmony` runtime flag)
- •8.3.0 (full support)

### [#](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#article-header-id-1)Asynchronous Iteration

Iterating over a collection of data is an important part of programming. Prior to ES2015, JavaScript provided statements such as `for`, `for...in`, and `while`, and methods such as `map()`, `filter()`, and `forEach()` for this purpose. To enable programmers to process the elements in a collection one at a time, ES2015 introduced the iterator interface.

An object is iterable if it has a `Symbol.iterator` property. In ES2015, strings and collections objects such as `Set`, `Map`, and `Array` come with a `Symbol.iterator` property and thus are iterable. The following code gives an example of how to access the elements of an iterable one at a time:

JavaScript	const arr = [10, 20, 30];

	const iterator = arr[Symbol.iterator]();

	console.log(iterator.next());    *// → {value: 10, done: false}*
	console.log(iterator.next());    *// → {value: 20, done: false}*
	console.log(iterator.next());    *// → {value: 30, done: false}*
	console.log(iterator.next());    *// → {value: undefined, done: true}*

`Symbol.iterator` is a well-known symbol specifying a function that returns an iterator. The primary way to interact with an iterator is the `next()` method. This method returns an object with two properties: `value` and `done`. The `value` property contains the value of the next element in the collection. The `done` property contains either `true` or `false` denoting whether or not the end of the collection has reached.

By default, a plain object is not iterable, but it can become iterable if you define a `Symbol.iterator` property on it, as in this example:

JavaScript	const collection = {

	  a: 10,
	  b: 20,
	  c: 30,
	  [Symbol.iterator]() {
	    const values = Object.keys(this);
	    let i = 0;
	    return {
	      next: () => {
	        return {
	          value: this[values[i++]],
	          done: i > values.length
	        }
	      }
	    };
	  }
	};

	const iterator = collection[Symbol.iterator]();

	console.log(iterator.next());    *// → {value: 10, done: false}*
	console.log(iterator.next());    *// → {value: 20, done: false}*
	console.log(iterator.next());    *// → {value: 30, done: false}*
	console.log(iterator.next());    *// → {value: undefined, done: true}*

This object is iterable because it defines a `Symbol.iterator` property. The iterator uses the `Object.keys()` method to get an array of the object's property names and then assigns it to the `values` constant. It also defines a counter variable and gives it an initial value of 0. When the iterator is executed it returns an object that contains a `next()` method. Each time the `next()` method is called, it returns a `{value, done}` pair, with `value` holding the next element in the collection and `done` holding a Boolean indicating if the iterator has reached the need of the collection.

While this code works perfectly, it’s unnecessarily complicated. Fortunately, using a generator function can considerably simplify the process:

JavaScript	const collection = {

	  a: 10,
	  b: 20,
	  c: 30,
	  [Symbol.iterator]: function * () {
	    for (let key in this) {
	      yield this[key];
	    }
	  }
	};

	const iterator = collection[Symbol.iterator]();

	console.log(iterator.next());    *// → {value: 10, done: false}*
	console.log(iterator.next());    *// → {value: 20, done: false}*
	console.log(iterator.next());    *// → {value: 30, done: false}*
	console.log(iterator.next());    *// → {value: undefined, done: true}*

Inside this generator, a `for...in` loop is used to enumerate over the collection and yield the value of each property. The result is exactly the same as the previous example, but it’s greatly shorter.

A downside of iterators is that they are not suitable for representing asynchronous data sources. ES2018’s solution to remedy that is asynchronous iterators and asynchronous iterables. An asynchronous iterator differs from a conventional iterator in that, instead of returning a plain object in the form of `{value, done}`, it returns a promise that fulfills to `{value, done}`. An asynchronous iterable defines a `Symbol.asyncIterator` method (instead of `Symbol.iterator`) that returns an asynchronous iterator.

An example should make this clearer:
JavaScript	const collection = {

	  a: 10,
	  b: 20,
	  c: 30,
	  [Symbol.asyncIterator]() {
	    const values = Object.keys(this);
	    let i = 0;
	    return {
	      next: () => {
	        return Promise.resolve({
	          value: this[values[i++]],
	          done: i > values.length
	        });
	      }
	    };
	  }
	};

	const iterator = collection[Symbol.asyncIterator]();

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: 10, done: false}*
	}));

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: 20, done: false} *
	}));

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: 30, done: false} *
	}));

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: undefined, done: true} *
	}));

Note that it’s not possible to use an iterator of promises to achieve the same result. Although a normal, synchronous iterator can asynchronously determine the values, it still needs to determine the state of "done" synchronously.

Again, you can simplify the process by using a generator function, as shown below:

JavaScript	const collection = {

	  a: 10,
	  b: 20,
	  c: 30,
	  [Symbol.asyncIterator]: async function * () {
	    for (let key in this) {
	      yield this[key];
	    }
	  }
	};

	const iterator = collection[Symbol.asyncIterator]();

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: 10, done: false}*
	}));

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: 20, done: false} *
	}));

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: 30, done: false} *
	}));

	console.log(iterator.next().then(result => {
	  console.log(result);    *// → {value: undefined, done: true} *
	}));

Normally, a generator function returns a generator object with a `next()` method. When `next()` is called it returns a `{value, done}` pair whose `value` property holds the yielded value. An async generator does the same thing except that it returns a promise that fulfills to `{value, done}`.

An easy way to iterate over an iterable object is to use the `for...of` statement, but `for...of` doesn't work with async iterables as `value` and `done` are not determined synchronously. For this reason, ES2018 provides the `for...await...of` statement. Let’s look at an example:

JavaScript	const collection = {

	  a: 10,
	  b: 20,
	  c: 30,
	  [Symbol.asyncIterator]: async function * () {
	    for (let key in this) {
	      yield this[key];
	    }
	  }
	};

	(async function () {
	  for await (const x of collection) {
	    console.log(x);
	  }
	})();

	*// logs:*
	*// → 10*
	*// → 20*
	*// → 30*

In this code, the `for...await...of` statement implicitly calls the `Symbol.asyncIterator` method on the collection object to get an async iterator. Each time through the loop, the `next()` method of the iterator is called, which returns a promise. Once the promise is resolved, the `value` property of the resulting object is read to the `x` variable. The loop continues until the `done` property of the returned object has a value of `true`.

Keep in mind that the `for...await...of` statement is only valid within async generators and async functions. Violating this rule results in a `SyntaxError`.

The `next()` method may return a promise that rejects. To gracefully handle a rejected promise, you can wrap the `for...await...of` statement in a `try...catch` statement, like this:

JavaScript	const collection = {

	  [Symbol.asyncIterator]() {
	    return {
	      next: () => {
	        return Promise.reject(new Error('Something went wrong.'))
	      }
	    };
	  }
	};

	(async function() {
	  try {
	    for await (const value of collection) {}
	  } catch (error) {
	    console.log('Caught: ' + error.message);
	  }
	})();

	*// logs:*
	*// → Caught: Something went wrong.*

#### Support for Asynchronous Iterators

| Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- |
| 63  | 57  | 12  | No  |

| Chrome Android | Firefox Android | iOS Safari | Edge Mobile | Samsung Internet | Android Webview |
| --- | --- | --- | --- | --- | --- |
| 63  | 57  | 12  | No  | 8.2 | 63  |

**Node.js:**

- •8.10.0 (requires the --harmony_async_iteration flag)
- •10.0.0 (full support)

### [#](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#article-header-id-2)Promise.prototype.finally

Another exciting addition to ES2018 is the `finally()` method. Several JavaScript libraries had previously implemented a similar method, which proved useful in many situations. This encouraged the Ecma Technical Committee to add `finally()` to the specification. With this method, programmers will be able to execute a block of code regardless of the promise's fate. Let’s look at a simple example:

JavaScript	fetch('https://www.google.com')

	  .then((response) => {
	    console.log(response.status);
	  })
	  .catch((error) => {
	    console.log(error);
	  })
	  .finally(() => {
	    document.querySelector('#spinner').style.display = 'none';
	  });

The `finally()` method comes in handy when you need to do some clean up after the operation has finished regardless of whether or not it succeeded. In this code, the `finally()` method simply hides the loading spinner after the data is fetched and processed. Instead of duplicating the final logic in the `then()` and `catch()` methods, the code registers a function to be executed once the promise is either fulfilled or rejected.

You could achieve the same result by using `promise.then(func, func)` rather than `promise.finally(func)`, but you would have to repeat the same code in both fulfillment handler and rejection handler, or declare a variable for it:

JavaScript	fetch('https://www.google.com')

	  .then((response) => {
	    console.log(response.status);
	  })
	  .catch((error) => {
	    console.log(error);
	  })
	  .then(final, final);

	function final() {
	  document.querySelector('#spinner').style.display = 'none';
	}

As with `then()` and `catch()`, the `finally()` method always returns a promise, so you can chain more methods. Normally, you want to use `finally()` as the last chain, but in certain situations, such as when making a HTTP request, it’s a good practice to chain another `catch()` to deal with errors that may occur in `finally()`.

#### Support for Promise.prototype.finally

| Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- |
| 63  | 58  | 11.1 | 18  |

| Chrome Android | Firefox Android | iOS Safari | Edge Mobile | Samsung Internet | Android Webview |
| --- | --- | --- | --- | --- | --- |
| 63  | 58  | 11.1 | No  | 8.2 | 63  |

**Node.js:**
10.0.0 (full support)

### [#](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#article-header-id-3)New RegExp Features

ES2018 adds four new features to the `RegExp` object, which further improves JavaScript’s string processing capabilities. These features are as follows:

- •s (dotAll) flag
- •Named capture groups
- •Lookbehind assertions
- •Unicode property escapes

#### s (dotAll) Flag

The dot (`.`) is a special character in a regular expression pattern that matches any character except line break characters such as line feed (`\n`) or carriage return (``). A workaround to match all characters, including line breaks, is to use a character class with two opposite shorthands such as `[\d\D]`. This character class tells the regular expression engine to find a character that’s either a digit (`\d`) or a non-digit (`\D`). As a result, it matches any character:

JavaScript`console.log(/one[\d\D]two/.test('one\ntwo'));    *// → true*`

ES2018 introduces a mode in which the dot can be used to achieve the same result. This mode can be activated on per-regex basis by using the `s` flag:

JavaScript	console.log(/one.two/.test('one\ntwo'));     *// → false*

	console.log(/one.two/s.test('one\ntwo'));    *// → true*

The benefit of using a flag to opt in to the new behavior is backwards compatibility. So existing regular expression patterns that use the dot character are not affected.

#### Named Capture Groups

In some regular expression patterns, using a number to reference a capture group can be confusing. For example, take the regular expression `/(\d{4})-(\d{2})-(\d{2})/` which matches a date. Because date notation in American English is different from British English, it’s hard to know which group refers to the day and which group refers to the month:

JavaScript	const re = /(\d{4})-(\d{2})-(\d{2})/;

	const match= re.exec('2019-01-10');

	console.log(match[0]);    *// → 2019-01-10*
	console.log(match[1]);    *// → 2019*
	console.log(match[2]);    *// → 01*
	console.log(match[3]);    *// → 10*

ES2018 introduces named capture groups which uses the `(?<name>...)` syntax. So, the pattern to match a date can be written in a less ambiguous manner:

JavaScript	const re = /(?<year>\d{4})-(?<month>\d{2})-(?<day>\d{2})/;

	const match = re.exec('2019-01-10');

	console.log(match.groups);          *// → {year: "2019", month: "01", day: "10"}*
	console.log(match.groups.year);     *// → 2019*
	console.log(match.groups.month);    *// → 01*
	console.log(match.groups.day);      *// → 10*

You can recall a named capture group later in the pattern by using the `\k<name>` syntax. For example, to find consecutive duplicate words in a sentence, you can use `/\b(?<dup>\w+)\s+\k<dup>\b/`:

JavaScript	const re = /\b(?<dup>\w+)\s+\k<dup>\b/;

	const match = re.exec('Get that that cat off the table!');

	console.log(match.index);    *// → 4*
	console.log(match[0]);       *// → that that*

To insert a named capture group into the replacement string of the `replace()` method, you will need to use the `$<name>` construct. For example:

JavaScript	const str = 'red & blue';

	console.log(str.replace(/(red) & (blue)/, '$2 & $1'));
	*// → blue & red*

	console.log(str.replace(/(?<red>red) & (?<blue>blue)/, '$<blue> & $<red>'));
	*// → blue & red*

#### Lookbehind Assertions

ES2018 brings lookbehind assertions to JavaScript, which have been available in other regex implementations for years. Previously, JavaScript only supported lookahead assertions. A lookbehind assertion is denoted by `(?<=...)`, and enables you to match a pattern based on the substring that precedes the pattern. For example, if you want to match the price of a product in dollar, pound, or euro without capturing the currency symbol, you can use `/(?<=\$|£|€)\d+(\.\d*)?/`:

JavaScript	const re = /(?<=\$|£|€)\d+(\.\d*)?/;

	console.log(re.exec('199'));
	*// → null*

	console.log(re.exec('$199'));
	*// → ["199", undefined, index: 1, input: "$199", groups: undefined]*

	console.log(re.exec('€50'));
	*// → ["50", undefined, index: 1, input: "€50", groups: undefined]*

There is also a negative version of lookbehind, which is denoted by `(?<!...)`. A negative lookbehind allows you to match a pattern only if it is not preceded by the pattern within the lookbehind. For example, the pattern `/(?<!un)available/` matches the word available if it does not have a "un" prefix:

JavaScript	const re = /(?<!un)available/;

	console.log(re.exec('We regret this service is currently unavailable'));
	*// → null*

	console.log(re.exec('The service is available'));
	*// → ["available", index: 15, input: "The service is available", groups: undefined]*

#### Unicode Property Escapes

ES2018 provides a new type of escape sequence known as Unicode property escape, which provides support for full Unicode in regular expressions. Suppose you want to match the Unicode character ㉛ in a string. Although ㉛ is considered a number, you can’t match it with the `\d` shorthand character class because it only supports ASCII [0-9] characters. Unicode property escapes, on the other hand, can be used to match any decimal number in Unicode:

JavaScript	const str = '㉛';

	console.log(/\d/u.test(str));    *// → false*
	console.log(/\p{Number}/u.test(str));     *// → true*

Similarly, if you want to match any Unicode (word) alphabetic character, you can use `\p{Alphabetic}`:

JavaScript	const str = 'ض';

	console.log(/\p{Alphabetic}/u.test(str));     *// → true*

	*// the \w shorthand cannot match ض*
	  console.log(/\w/u.test(str));    *// → false*

There is also a negated version of `\p{...}`, which is denoted by `\P{...}`:
JavaScript	console.log(/\P{Number}/u.test('㉛'));    *// → false*

	console.log(/\P{Number}/u.test('ض'));    *// → true*

	console.log(/\P{Alphabetic}/u.test('㉛'));    *// → true*
	console.log(/\P{Alphabetic}/u.test('ض'));    *// → false*

In addition to Alphabetic and Number, there are several more properties that can be used in Unicode property escapes. You can find a list of supported Unicode properties in the [current specification proposal](https://tc39.github.io/proposal-regexp-unicode-property-escapes/#sec-static-semantics-unicodematchproperty-p).

#### Support for New RegExp Features

|     | Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- | --- |
| s (dotAll) Flag | 62  | No  | 11.1 | No  |
| Named Capture Groups | 64  | No  | 11.1 | No  |
| Lookbehind Assertions | 62  | No  | No  | No  |
| Unicode Property Escapes | 64  | No  | 11.1 | No  |

|     | Chrome (Android) | Firefox (Android) | iOS Safari | Edge Mobile | Samsung Internet | Android Webview |
| --- | --- | --- | --- | --- | --- | --- |
| s (dotAll) Flag | 62  | No  | 11.3 | No  | 8.2 | 62  |
| Named Capture Groups | 64  | No  | 11.3 | No  | No  | 64  |
| Lookbehind Assertions | 62  | No  | No  | No  | 8.2 | 62  |
| Unicode Property Escapes | 64  | No  | 11.3 | No  | No  | 64  |

**Node.js:**

- •8.3.0 (requires the --harmony runtime flag)
- •8.10.0 (support for s (dotAll) flag and lookbehind assertions)
- •10.0.0 (full support)

### [#](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#article-header-id-4)Template Literal Revision

When a template literal is immediately preceded by an expression, it is called a tagged template literal. A tagged template comes in handy when you want to parse a template literal with a function. Consider the following example:

JavaScript	function fn(string, substitute) {

	  if(substitute === 'ES6') {
	    substitute = 'ES2015'
	  }
	  return substitute + string[1];
	}

	const version = 'ES6';
	const result = fn`${version} was a major update`;

	console.log(result);    *// → ES2015 was a major update*

In this code, a tag expression — which is a regular function — is invoked and passed the template literal. The function simply modifies the dynamic part of the string and returns it.

Prior to ES2018, tagged template literals had syntactic restrictions related to escape sequences. A backslash followed by a certain sequence of characters were treated as special characters: a `\x` interpreted as a hex escape, a `\u` interpreted as a unicode escape, and a `\` followed by a digit interpreted as an octal escape. As a result, strings such as `"C:\xxx\uuu"` or `"\ubuntu"` were considered invalid escape sequences by the interpreter and would throw a `SyntaxError`.

ES2018 removes these restrictions from tagged templates and instead of throwing an error, represents invalid escape sequences as `undefined`:

JavaScript	function fn(string, substitute) {

	  console.log(substitute);    *// → escape sequences:*
	  console.log(string[1]);     *// → undefined*
	}

	const str = 'escape sequences:';
	const result = fn`${str} \ubuntu C:\xxx\uuu`;

Keep in mind that using illegal escape sequences in a regular template literal still causes an error:

JavaScript	const result = `\ubuntu`;

	*// → SyntaxError: Invalid Unicode escape sequence*

#### Support for Template Literal Revision

| Chrome | Firefox | Safari | Edge |
| --- | --- | --- | --- |
| 62  | 56  | 11  | No  |

| Chrome Android | Firefox Android | iOS Safari | Edge Mobile | Samsung Internet | Android Webview |
| --- | --- | --- | --- | --- | --- |
| 62  | 56  | 11  | No  | 8.2 | 62  |

**Node.js:**

- •8.3.0 (requires the --harmony runtime flag)
- •8.10.0 (full support)

### [#](https://css-tricks.com/new-es2018-features-every-javascript-developer-should-know/#article-header-id-5)Wrapping up

We’ve taken a good look at several key features introduced in ES2018 including asynchronous iteration, rest/spread properties, `Promise.prototype.finally()`, and additions to the `RegExp` object. Although some of these features are not fully implemented by some browser vendors yet, they can still be used today thanks to JavaScript transpilers such as Babel.

ECMAScript is rapidly evolving and new features are being introduced every so often, so check out the [list of finished proposals](https://github.com/tc39/proposals/blob/master/finished-proposals.md) for the full scope of what’s new. Are there any new features you’re particularly excited about? Share them in the comments!

[[frontend-masters-600_coga4x.webp](../_resources/abcf7707ee3356129236bd188825c339.webp)](https://synd.co/2lxkwwp)

[Avatar_qr6vy9.webp](../_resources/829ebcb4363325940519ccaf471c34f0.webp)Take your JavaScript to the next level and find out what it's fully capable of with the JavaScript path on [Frontend Masters](https://synd.co/2lxkwwp).

[[600xDigitalOcean_Agencies_bfkeb2.webp](../_resources/a604a0e77109b7d665340af9a813496a.webp)](https://ad.doubleclick.net/ddm/trackclk/N7439.1063086.CSS-TRICKS.COM/B7043538.237730278;dc_trk_aid=434779083;dc_trk_cid=110714071;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=)

![B7043538.237730278;dc_trk_aid=434779083;dc_trk_cid=110714071;ord=1572722425;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=](../_resources/f168ac97bb4ba703127f0f220705dd0d.webp)[Wufoo](https://ad.doubleclick.net/ddm/clk/303181152;128762502;s) powers all our web forms here at CSS-Tricks, and has for over a decade!

[0619_White_OnlineForms_2_600x500_zfqkk2.webp](../_resources/d89746888da2d9510b64a9f031eaecd5.gif)

[[CSS_Tricks_Sidebar_banner_2.1_zgad1c.webp](../_resources/03ff268b6559fd8c89eaa44a0c602e23.webp)](https://ad.doubleclick.net/ddm/trackclk/N1131812.3091281BUYSELLADS/B23132710.257468488;dc_trk_aid=453266502;dc_trk_cid=122672822;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=)

Grow your agency with [DigitalOcean](https://ad.doubleclick.net/ddm/trackclk/N1131812.3091281BUYSELLADS/B23132710.257468488;dc_trk_aid=453266502;dc_trk_cid=122672822;dc_lat=;dc_rdid=;tag_for_child_directed_treatment=;tfua=) by joining a global developer community. Start saving time & resources today!

[(L)](https://synd.co/2YTMxgF)

[monday.com](https://synd.co/2YTMxgF), award-winning management tool, lets you easily manage multiple projects, track progress, and collaborate in one visual place.

[![1572540442-Large_Image_260x200_v2.jpg](../_resources/1e4da5bcb947fd92adfb07383a25b1ff.jpg)](https://srv.carbonads.net/ads/click/x/GTND42QUCVSI4KQYCEYLYKQMCA7DP5QWC67DPZ3JCWSI62QYCVBIV2JKC6BI5KJUCVYI6K3EHJNCLSIZ?segment=placement:csstrickscom;)[CloudBees Jenkins Distribution. Rock-Solid & Secure. Always free. Download Now.](https://srv.carbonads.net/ads/click/x/GTND42QUCVSI4KQYCEYLYKQMCA7DP5QWC67DPZ3JCWSI62QYCVBIV2JKC6BI5KJUCVYI6K3EHJNCLSIZ?segment=placement:csstrickscom;)