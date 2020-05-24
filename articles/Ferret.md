Ferret

 ![](../_resources/4a18bed4c159d31d337b68af91dce985.png)

#  Ferret

##  a web scraping system

aiming to simplify data extraction from the web

 [Get started](https://www.montferret.dev/docs/getting-started/)  [Download](https://github.com/MontFerret/ferret/releases)

### Declarative

ferret has a declarative query language that makes it easy to focus on a data that you need to get.

### Dynamic pages support

ferret has the ability to scrape JS rendered pages, handle all page events and emulate user interactions.

### Embeddable

ferret was designed as a library from the ground up. it can be easily embedded into any Go application.

* * *

### Hello, Ferret!

ferret helps you to focus on the data you need using an easy to learn declarative language

	LET doc = DOCUMENT('https://github.com/topics')

	FOR el IN ELEMENTS(doc, '.py-4.border-bottom')
	    LIMIT 10
	    LET url = ELEMENT(el, 'a')
	    LET name = ELEMENT(el, '.f3')
	    LET desc = ELEMENT(el, '.f5')

	    RETURN {
	        name: TRIM(name.innerText),
	        description: TRIM(desc.innerText),
	        url: 'https://github.com' + url.attributes.href
	    }

* * *

	LET doc = DOCUMENT('https://soundcloud.com/charts/top', {
	    driver: 'cdp'
	})

	WAIT_ELEMENT(doc, '.chartTrack__details', 5000)

	LET tracks = ELEMENTS(doc, '.chartTrack__details')

	FOR track IN tracks
	    RETURN {
	        artist: TRIM(INNER_TEXT(track, '.chartTrack__username')),
	        track: TRIM(INNER_TEXT(track, '.chartTrack__title'))
	    }

### Dynamic pages handled easily

ferret uses Chrome/Chromium via Chrome Devtools Protocol to handle dynamically rendered web pages

* * *

### Simple extensibility

ferret is extremeley extensible - creating custom functions and types is super easy

	transform := func(ctx context.Context, args ...core.Value) (core.Value, error) {
	    str := args[0].(values.String)

	    return values.NewString(strings.ToUpper(str.String() + "_ferret")), nil
	}

	query := `
	    FOR el IN ["foo", "bar", "qaz"]
	        RETURN TRANSFORM(el)
	`

	comp := compiler.New()

	if err := comp.RegisterFunction("transform", transform); err != nil {
	    return nil, err
	}

	program, err := comp.Compile(query)