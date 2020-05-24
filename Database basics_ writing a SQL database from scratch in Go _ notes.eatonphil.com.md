Database basics: writing a SQL database from scratch in Go | notes.eatonphil.com

 [↩Notes](https://notes.eatonphil.com/)

## March 6, 2020

# Database basics: writing a SQL database from scratch in Go

[database](https://notes.eatonphil.com/tags/database.html)[golang](https://notes.eatonphil.com/tags/golang.html)[parsing](https://notes.eatonphil.com/tags/parsing.html)

 [**](https://github.com/eatonphil)  [**](https://twitter.com/phil_eaton)  [**](https://notes.eatonphil.com/rss.xml)  [Subscribe](https://docs.google.com/forms/d/e/1FAIpQLSchaYjB6mq0SHmFL_J1wbB7E4SwUk23Dja2K7mfjtYH5o48fw/viewform?usp=sf_link)

Next in database basics:

 [Database basics (2): binary expressions and WHERE filters](https://notes.eatonphil.com/database-basics-expressions-and-where.html)

In this series we'll write a rudimentary database from scratch in Go. Project source code is available on[Github](https://github.com/eatonphil/gosql).

In this first post we'll build enough of a parser to run some simple`CREATE`, `INSERT`, and `SELECT`queries. Then we'll build an in-memory backend supporting `TEXT` and `INT` types and write a basic REPL.

We'll be able to support the following interaction:

	$ go run *.go
	Welcome to gosql.
	# CREATE TABLE users (id INT, name TEXT);
	ok
	# INSERT INTO users VALUES (1, 'Phil');
	ok
	# SELECT id, name FROM users;
	| id | name |
	====================
	| 1 |  Phil |
	ok
	# INSERT INTO users VALUES (2, 'Kate');
	ok
	# SELECT name, id FROM users;
	| name | id |
	====================
	| Phil |  1 |
	| Kate |  2 |
	ok

The first stage will be to map a SQL source into a list of tokens (lexing). Then we'll call parse functions to find individual SQL statements (such as `SELECT`). These parse functions will in turn call their own helper functions to find patterns of recursively parseable chunks, keywords, symbols (like parenthesis), identifiers (like a table name), and numeric or string literals.

Then, we'll write an in-memory backend to do operations based on an AST. Finally, we'll write a REPL to accept SQL from a CLI and pass it to the in-memory backend.

This post assumes a basic understanding of parsing concepts. We won't skip any code, but also won't go into great detail on why we structure the way we do.

For a simpler introduction to parsing and parsing concepts, see [this post on parsing JSON](https://notes.eatonphil.com/writing-a-simple-json-parser.html).

### Lexing

The lexer is responsible for finding every distinct group of characters in source code: tokens. This will consist primarily of identifiers, numbers, strings, and symbols.

What follows is a second, more orthodox pass at lexing. The first pass took a number of shortcuts and couldn't handle spaces in strings, for example.

 [Here is the relevant pull request in gosql if you are curious.](https://github.com/eatonphil/gosql/pull/2)

The gist of the logic will be to pass control to a helper function for each kind of token. If the helper function succeeds in finding a token, it will return true and the location for the lexer to start at next. It will continue doing this until it reaches the end of the source.

First off, we'll define a few types and constants for use in `lexer.go`:

	package gosql

	import (
	    "fmt"
	    "strings"
	)

	type location struct {
	    line uint
	    col  uint
	}

	type keyword string

	const (
	    selectKeyword keyword = "select"
	    fromKeyword   keyword = "from"
	    asKeyword     keyword = "as"
	    tableKeyword  keyword = "table"
	    createKeyword keyword = "create"
	    insertKeyword keyword = "insert"
	    intoKeyword   keyword = "into"
	    valuesKeyword keyword = "values"
	    intKeyword    keyword = "int"
	    textKeyword   keyword = "text"
	)

	type symbol string

	const (
	    semicolonSymbol  symbol = ";"
	    asteriskSymbol   symbol = "*"
	    commaSymbol      symbol = ","
	    leftparenSymbol  symbol = "("
	    rightparenSymbol symbol = ")"
	)

	type tokenKind uint

	const (
	    keywordKind tokenKind = iota
	    symbolKind
	    identifierKind
	    stringKind
	    numericKind
	)

	type token struct {
	    value string
	    kind  tokenKind
	    loc   location
	}

	type cursor struct {
	    pointer uint
	    loc     location
	}

	func (t *token) equals(other *token) bool {
	    return t.value == other.value && t.kind == other.kind
	}

	type lexer func(string, cursor) (*token, cursor, bool)

Next we'll write out the main loop:

	func lex(source string) ([]*token, error) {
	    tokens := []*token{}
	    cur := cursor{}

	lex:
	    for cur.pointer < uint(len(source)) {
	        lexers := []lexer{lexKeyword, lexSymbol, lexString, lexNumeric, lexIdentifier}
	        for _, l := range lexers {
	            if token, newCursor, ok := l(source, cur); ok {
	                cur = newCursor

	                // Omit nil tokens for valid, but empty syntax like newlines
	                if token != nil {
	                    tokens = append(tokens, token)
	                }

	                continue lex
	            }
	        }

	        hint := ""
	        if len(tokens) > 0 {
	            hint = " after " + tokens[len(tokens)-1].value
	        }
	        return nil, fmt.Errorf("Unable to lex token%s, at %d:%d", hint, cur.loc.line, cur.loc.col)
	    }

	    return tokens, nil
	}

Then we'll write a helper for each kind of fundemental token.

#### Analyzing numbers

Numbers are the most complex. So we'll refer to the [PostgreSQL documentation (section 4.1.2.6)](https://www.postgresql.org/docs/current/sql-syntax-lexical.html)for what constitutes a valid number.

	func lexNumeric(source string, ic cursor) (*token, cursor, bool) {
	    cur := ic

	    periodFound := false
	    expMarkerFound := false

	    for ; cur.pointer < uint(len(source)); cur.pointer++ {
	        c := source[cur.pointer]
	        cur.loc.col++

	        isDigit := c >= '0' && c <= '9'
	        isPeriod := c == '.'
	        isExpMarker := c == 'e'

	        // Must start with a digit or period
	        if cur.pointer == ic.pointer {
	            if !isDigit && !isPeriod {
	                return nil, ic, false
	            }

	            periodFound = isPeriod
	            continue
	        }

	        if isPeriod {
	            if periodFound {
	                return nil, ic, false
	            }

	            periodFound = true
	            continue
	        }

	        if isExpMarker {
	            if expMarkerFound {
	                return nil, ic, false
	            }

	            // No periods allowed after expMarker
	            periodFound = true
	            expMarkerFound = true

	            // expMarker must be followed by digits
	            if cur.pointer == uint(len(source)-1) {
	                return nil, ic, false
	            }

	            cNext := source[cur.pointer+1]
	            if cNext == '-' || cNext == '+' {
	                cur.pointer++
	                cur.loc.col++
	            }

	            continue
	        }

	        if !isDigit {
	            break
	        }
	    }

	    // No characters accumulated
	    if cur.pointer == ic.pointer {
	        return nil, ic, false
	    }

	    return &token{
	        value: source[ic.pointer:cur.pointer],
	        loc:   ic.loc,
	        kind:  numericKind,
	    }, cur, true
	}

#### Analyzing strings

Strings must start and end with a single apostrophe. They can contain a single apostophe if it is followed by another single apostrophe. We'll put this kind of character delimited lexing logic into a helper function so we can use it again when analyzing identifiers.

	func lexCharacterDelimited(source string, ic cursor, delimiter byte) (*token, cursor, bool) {
	    cur := ic

	    if len(source[cur.pointer:]) == 0 {
	        return nil, ic, false
	    }

	    if source[cur.pointer] != delimiter {
	        return nil, ic, false
	    }

	    cur.loc.col++
	    cur.pointer++

	    var value []byte
	    for ; cur.pointer < uint(len(source)); cur.pointer++ {
	        c := source[cur.pointer]

	        if c == delimiter {
	            // SQL escapes are via double characters, not backslash.
	            if cur.pointer+1 >= uint(len(source)) || source[cur.pointer+1] != delimiter {
	                return &token{
	                    value: string(value),
	                    loc:   ic.loc,
	                    kind:  stringKind,
	                }, cur, true
	            } else {
	                value = append(value, delimiter)
	                cur.pointer++
	                cur.loc.col++
	            }
	        }

	        value = append(value, c)
	        cur.loc.col++
	    }

	    return nil, ic, false
	}

	func lexString(source string, ic cursor) (*token, cursor, bool) {
	    return lexCharacterDelimited(source, ic, '\'')
	}

#### Analyzing symbols and keywords

Symbols and keywords come from a fixed set of strings, so they're easy to compare against. Whitespace should be thrown away.

	func lexSymbol(source string, ic cursor) (*token, cursor, bool) {
	    c := source[ic.pointer]
	    cur := ic
	    cur.loc.col++
	    cur.pointer++

	    switch c {
	    // Syntax that should be thrown away
	    case '\n':
	        cur.loc.line++
	        cur.loc.col = 0
	        fallthrough
	    case '\t':
	        fallthrough
	    case ' ':
	        return nil, cur, true

	    // Syntax that should be kept
	    case ',':
	        fallthrough
	    case '(':
	        fallthrough
	    case ')':
	        fallthrough
	    case ';':
	        fallthrough
	    case '*':
	        break

	    // Unknown character
	    default:
	        return nil, ic, false
	    }

	    return &token{
	        value: string(c),
	        loc:   ic.loc,
	        kind:  symbolKind,
	    }, cur, true
	}

#### Analyzing identifiers

An identifier is either a double-quoted string or a group of characters starting with an alphabetical character and possibly containing numbers and underscores.

	func lexIdentifier(source string, ic cursor) (*token, cursor, bool) {
	    // Handle separately if is a double-quoted identifier
	    if token, newCursor, ok := lexCharacterDelimited(source, ic, '"'); ok {
	        return token, newCursor, true
	    }

	    cur := ic

	    c := source[cur.pointer]
	    // Other characters count too, big ignoring non-ascii for now
	    isAlphabetical := (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')
	    if !isAlphabetical {
	        return nil, ic, false
	    }
	    cur.pointer++
	    cur.loc.col++

	    value := []byte{c}
	    for ; cur.pointer < uint(len(source)); cur.pointer++ {
	        c = source[cur.pointer]

	        // Other characters count too, big ignoring non-ascii for now
	        isAlphabetical := (c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')
	        isNumeric := c >= '0' && c <= '9'
	        if isAlphabetical || isNumeric || c == '$' || c == '_' {
	            value = append(value, c)
	            cur.loc.col++
	            continue
	        }

	        break
	    }

	    if len(value) == 0 {
	        return nil, ic, false
	    }

	    return &token{
	        // Unquoted dentifiers are case-insensitive
	        value: strings.ToLower(string(value)),
	        loc:   ic.loc,
	        kind:  identifierKind,
	    }, cur, true
	}

And that's it for the lexer! If you copy[lexer_test.go](https://github.com/eatonphil/gosql/blob/master/lexer_test.go)from the main project, the tests should now pass.

### AST model

At the highest level, an AST is a collection of statements:

	package main

	type Ast struct {
	    Statements []*Statement
	}

A statement, for now, is one of `INSERT`,`CREATE`, or `SELECT`:

	type AstKind uint

	const (
	    SelectKind AstKind = iota
	    CreateTableKind
	    InsertKind
	)

	type Statement struct {
	    SelectStatement      *SelectStatement
	    CreateTableStatement *CreateTableStatement
	    InsertStatement      *InsertStatement
	    Kind                 AstKind
	}

#### INSERT

An insert statement, for now, has a table name and a list of values to insert:

	type InsertStatement struct {
	    table  token
	    values *[]*expression
	}

An expression is a literal token or (in the future) a function call or inline operation:

	type expressionKind uint

	const (
	    literalKind expressionKind = iota
	)

	type expression struct {
	    literal *token
	    kind    expressionKind
	}

#### CREATE

A create statement, for now, has a table name and a list of column names and types:

	type columnDefinition struct {
	    name     token
	    datatype token
	}

	type CreateTableStatement struct {
	    name token
	    cols *[]*columnDefinition
	}

#### SELECT

A select statement, for now, has a table name and a list of column names:

	type SelectStatement struct {
	    item []*expression
	    from token
	}

And that's it for the AST.

### Parsing

The `Parse` entrypoint will take a list of tokens and attempt to parse statements, separated by a semi-colon, until it reaches the last token.

In general our strategy will be to increment and pass around a cursor containing the current position of unparsed tokens. Each helper will return the new cursor that the caller should start from.

	package main

	import (
	    "errors"
	    "fmt"
	)

	func tokenFromKeyword(k keyword) token {
	    return token{
	        kind:  keywordKind,
	        value: string(k),
	    }
	}

	func tokenFromSymbol(s symbol) token {
	    return token{
	        kind:  symbolKind,
	        value: string(s),
	    }
	}

	func expectToken(tokens []*token, cursor uint, t token) bool {
	    if cursor >= uint(len(tokens)) {
	        return false
	    }

	    return t.equals(tokens[cursor])
	}

	func helpMessage(tokens []*token, cursor uint, msg string) {
	    var c *token
	    if cursor < uint(len(tokens)) {
	        c = tokens[cursor]
	    } else {
	        c = tokens[cursor-1]
	    }

	    fmt.Printf("[%d,%d]: %s, got: %s\n", c.loc.line, c.loc.col, msg, c.value)
	}

	func Parse(source string) (*Ast, error) {
	    tokens, err := lex(source)
	    if err != nil {
	        return nil, err
	    }

	    a := Ast{}
	    cursor := uint(0)
	    for cursor < uint(len(tokens)) {
	        stmt, newCursor, ok := parseStatement(tokens, cursor, tokenFromSymbol(semicolonSymbol))
	        if !ok {
	            helpMessage(tokens, cursor, "Expected statement")
	            return nil, errors.New("Failed to parse, expected statement")
	        }
	        cursor = newCursor

	        a.Statements = append(a.Statements, stmt)

	        atLeastOneSemicolon := false
	        for expectToken(tokens, cursor, tokenFromSymbol(semicolonSymbol)) {
	            cursor++
	            atLeastOneSemicolon = true
	        }

	        if !atLeastOneSemicolon {
	            helpMessage(tokens, cursor, "Expected semi-colon delimiter between statements")
	            return nil, errors.New("Missing semi-colon between statements")
	        }
	    }

	    return &a, nil
	}

#### Parsing statements

Each statement will be one of `INSERT`,`CREATE`, or `SELECT`. The`parseStatement` helper will call a helper on each of these statement types and return `true` if one of them succeeds in parsing.

	func parseStatement(tokens []*token, initialCursor uint, delimiter token) (*Statement, uint, bool) {
	    cursor := initialCursor

	    // Look for a SELECT statement
	    semicolonToken := tokenFromSymbol(semicolonSymbol)
	    slct, newCursor, ok := parseSelectStatement(tokens, cursor, semicolonToken)
	    if ok {
	        return &Statement{
	            Kind:            SelectKind,
	            SelectStatement: slct,
	        }, newCursor, true
	    }

	    // Look for a INSERT statement
	    inst, newCursor, ok := parseInsertStatement(tokens, cursor, semicolonToken)
	    if ok {
	        return &Statement{
	            Kind:            InsertKind,
	            InsertStatement: inst,
	        }, newCursor, true
	    }

	    // Look for a CREATE statement
	    crtTbl, newCursor, ok := parseCreateTableStatement(tokens, cursor, semicolonToken)
	    if ok {
	        return &Statement{
	            Kind:                 CreateTableKind,
	            CreateTableStatement: crtTbl,
	        }, newCursor, true
	    }

	    return nil, initialCursor, false
	}

#### Parsing select statements

Parsing `SELECT` statements is easy. We'll look for the following token pattern:

1. `SELECT`
2. `$expression [, ...]`
3. `FROM`
4. `$table-name`
Sketching that out we get:

	func parseSelectStatement(tokens []*token, initialCursor uint, delimiter token) (*SelectStatement, uint, bool) {
	    cursor := initialCursor
	    if !expectToken(tokens, cursor, tokenFromKeyword(selectKeyword)) {
	        return nil, initialCursor, false
	    }
	    cursor++

	    slct := SelectStatement{}

	    exps, newCursor, ok := parseExpressions(tokens, cursor, []token{tokenFromKeyword(fromKeyword), delimiter})
	    if !ok {
	        return nil, initialCursor, false
	    }

	    slct.item = *exps
	    cursor = newCursor

	    if expectToken(tokens, cursor, tokenFromKeyword(fromKeyword)) {
	        cursor++

	        from, newCursor, ok := parseToken(tokens, cursor, identifierKind)
	        if !ok {
	            helpMessage(tokens, cursor, "Expected FROM token")
	            return nil, initialCursor, false
	        }

	        slct.from = *from
	        cursor = newCursor
	    }

	    return &slct, cursor, true
	}

The `parseToken` helper will look for a token of a particular token kind.

	func parseToken(tokens []*token, initialCursor uint, kind tokenKind) (*token, uint, bool) {
	    cursor := initialCursor

	    if cursor >= uint(len(tokens)) {
	        return nil, initialCursor, false
	    }

	    current := tokens[cursor]
	    if current.kind == kind {
	        return current, cursor + 1, true
	    }

	    return nil, initialCursor, false
	}

The `parseExpressions` helper will look for tokens separated by a comma until a delimiter is found. It will use existing helpers plus `parseExpression`.

	func parseExpressions(tokens []*token, initialCursor uint, delimiters []token) (*[]*expression, uint, bool) {
	    cursor := initialCursor

	    exps := []*expression{}
	outer:
	    for {
	        if cursor >= uint(len(tokens)) {
	            return nil, initialCursor, false
	        }

	        // Look for delimiter
	        current := tokens[cursor]
	        for _, delimiter := range delimiters {
	            if delimiter.equals(current) {
	                break outer
	            }
	        }

	        // Look for comma
	        if len(exps) > 0 {
	            if !expectToken(tokens, cursor, tokenFromSymbol(commaSymbol)) {
	                helpMessage(tokens, cursor, "Expected comma")
	                return nil, initialCursor, false
	            }

	            cursor++
	        }

	        // Look for expression
	        exp, newCursor, ok := parseExpression(tokens, cursor, tokenFromSymbol(commaSymbol))
	        if !ok {
	            helpMessage(tokens, cursor, "Expected expression")
	            return nil, initialCursor, false
	        }
	        cursor = newCursor

	        exps = append(exps, exp)
	    }

	    return &exps, cursor, true
	}

The `parseExpression` helper (for now) will look for a numeric, string, or identifier token.

	func parseExpression(tokens []*token, initialCursor uint, _ token) (*expression, uint, bool) {
	    cursor := initialCursor

	    kinds := []tokenKind{identifierKind, numericKind, stringKind}
	    for _, kind := range kinds {
	        t, newCursor, ok := parseToken(tokens, cursor, kind)
	        if ok {
	            return &expression{
	                literal: t,
	                kind:    literalKind,
	            }, newCursor, true
	        }
	    }

	    return nil, initialCursor, false
	}

And that's it for parsing a `SELECT` statement!

#### Parsing insert statements

We'll look for the following token pattern:
1. `INSERT`
2. `INTO`
3. `$table-name`
4. `VALUES`
5. `(`
6. `$expression [, ...]`
7. `)`
With the existing helpers, this is straightforward to sketch out:

	func parseInsertStatement(tokens []*token, initialCursor uint, delimiter token) (*InsertStatement, uint, bool) {
	    cursor := initialCursor

	    // Look for INSERT
	    if !expectToken(tokens, cursor, tokenFromKeyword(insertKeyword)) {
	        return nil, initialCursor, false
	    }
	    cursor++

	    // Look for INTO
	    if !expectToken(tokens, cursor, tokenFromKeyword(intoKeyword)) {
	        helpMessage(tokens, cursor, "Expected into")
	        return nil, initialCursor, false
	    }
	    cursor++

	    // Look for table name
	    table, newCursor, ok := parseToken(tokens, cursor, identifierKind)
	    if !ok {
	        helpMessage(tokens, cursor, "Expected table name")
	        return nil, initialCursor, false
	    }
	    cursor = newCursor

	    // Look for VALUES
	    if !expectToken(tokens, cursor, tokenFromKeyword(valuesKeyword)) {
	        helpMessage(tokens, cursor, "Expected VALUES")
	        return nil, initialCursor, false
	    }
	    cursor++

	    // Look for left paren
	    if !expectToken(tokens, cursor, tokenFromSymbol(leftparenSymbol)) {
	        helpMessage(tokens, cursor, "Expected left paren")
	        return nil, initialCursor, false
	    }
	    cursor++

	    // Look for expression list
	    values, newCursor, ok := parseExpressions(tokens, cursor, []token{tokenFromSymbol(rightparenSymbol)})
	    if !ok {
	        return nil, initialCursor, false
	    }
	    cursor = newCursor

	    // Look for right paren
	    if !expectToken(tokens, cursor, tokenFromSymbol(rightparenSymbol)) {
	        helpMessage(tokens, cursor, "Expected right paren")
	        return nil, initialCursor, false
	    }
	    cursor++

	    return &InsertStatement{
	        table:  *table,
	        values: values,
	    }, cursor, true
	}

And that's it for parsing an `INSERT` statement!

#### Parsing create statements

Finally, for create statements we'll look for the following token pattern:
1. `CREATE`
2. `$table-name`
3. `(`
4. `[$column-name $column-type [, ...]]`
5. `)`
Sketching that out with a new `parseColumnDefinitions`helper we get:

	func parseCreateTableStatement(tokens []*token, initialCursor uint, delimiter token) (*CreateTableStatement, uint, bool) {
	    cursor := initialCursor

	    if !expectToken(tokens, cursor, tokenFromKeyword(createKeyword)) {
	        return nil, initialCursor, false
	    }
	    cursor++

	    if !expectToken(tokens, cursor, tokenFromKeyword(tableKeyword)) {
	        return nil, initialCursor, false
	    }
	    cursor++

	    name, newCursor, ok := parseToken(tokens, cursor, identifierKind)
	    if !ok {
	        helpMessage(tokens, cursor, "Expected table name")
	        return nil, initialCursor, false
	    }
	    cursor = newCursor

	    if !expectToken(tokens, cursor, tokenFromSymbol(leftparenSymbol)) {
	        helpMessage(tokens, cursor, "Expected left parenthesis")
	        return nil, initialCursor, false
	    }
	    cursor++

	    cols, newCursor, ok := parseColumnDefinitions(tokens, cursor, tokenFromSymbol(rightparenSymbol))
	    if !ok {
	        return nil, initialCursor, false
	    }
	    cursor = newCursor

	    if !expectToken(tokens, cursor, tokenFromSymbol(rightparenSymbol)) {
	        helpMessage(tokens, cursor, "Expected right parenthesis")
	        return nil, initialCursor, false
	    }
	    cursor++

	    return &CreateTableStatement{
	        name: *name,
	        cols: cols,
	    }, cursor, true
	}

The `parseColumnDefinitions` helper will look column names followed by column types separated by a comma and ending with some delimiter:

	func parseColumnDefinitions(tokens []*token, initialCursor uint, delimiter token) (*[]*columnDefinition, uint, bool) {
	    cursor := initialCursor

	    cds := []*columnDefinition{}
	    for {
	        if cursor >= uint(len(tokens)) {
	            return nil, initialCursor, false
	        }

	        // Look for a delimiter
	        current := tokens[cursor]
	        if delimiter.equals(current) {
	            break
	        }

	        // Look for a comma
	        if len(cds) > 0 {
	            if !expectToken(tokens, cursor, tokenFromSymbol(commaSymbol)) {
	                helpMessage(tokens, cursor, "Expected comma")
	                return nil, initialCursor, false
	            }

	            cursor++
	        }

	        // Look for a column name
	        id, newCursor, ok := parseToken(tokens, cursor, identifierKind)
	        if !ok {
	            helpMessage(tokens, cursor, "Expected column name")
	            return nil, initialCursor, false
	        }
	        cursor = newCursor

	        // Look for a column type
	        ty, newCursor, ok := parseToken(tokens, cursor, keywordKind)
	        if !ok {
	            helpMessage(tokens, cursor, "Expected column type")
	            return nil, initialCursor, false
	        }
	        cursor = newCursor

	        cds = append(cds, &columnDefinition{
	            name:     *id,
	            datatype: *ty,
	        })
	    }

	    return &cds, cursor, true
	}

And that's it for parsing! If you copy[parser_test.go](https://github.com/eatonphil/gosql/blob/master/parser_test.go)from the main project, the tests should now pass.

### An in-memory backend

Our in-memory backend should conform to a general backend interface that allows a user to create, select, and insert data:

	package main

	import "errors"

	type ColumnType uint

	const (
	    TextType ColumnType = iota
	    IntType
	)

	type Cell interface {
	    AsText() string
	    AsInt() int32
	}

	type Results struct {
	    Columns []struct {
	        Type ColumnType
	        Name string
	    }
	    Rows [][]Cell
	}

	var (
	    ErrTableDoesNotExist  = errors.New("Table does not exist")
	    ErrColumnDoesNotExist = errors.New("Column does not exist")
	    ErrInvalidSelectItem  = errors.New("Select item is not valid")
	    ErrInvalidDatatype    = errors.New("Invalid datatype")
	    ErrMissingValues      = errors.New("Missing values")
	)

	type Backend interface {
	    CreateTable(*CreateTableStatement) error
	    Insert(*InsertStatement) error
	    Select(*SelectStatement) (*Results, error)
	}

This leaves us room in the future for a disk-backed backend.

#### Memory layout

Our in-memory backend should store a list of tables. Each table will have a list of columns and rows. Each column will have a name and type. Each row will have a list of byte arrays.

	package main

	import (
	    "bytes"
	    "encoding/binary"
	    "fmt"
	    "strconv"
	)

	type MemoryCell []byte

	func (mc MemoryCell) AsInt() int32 {
	    var i int32
	    err := binary.Read(bytes.NewBuffer(mc), binary.BigEndian, &i)
	    if err != nil {
	        panic(err)
	    }

	    return i
	}

	func (mc MemoryCell) AsText() string {
	    return string(mc)
	}

	type table struct {
	    columns     []string
	    columnTypes []ColumnType
	    rows        [][]MemoryCell
	}

	type MemoryBackend struct {
	    tables map[string]*table
	}

	func NewMemoryBackend() *MemoryBackend {
	    return &MemoryBackend{
	        tables: map[string]*table{},
	    }
	}

#### Implementing create table support

When creating a table, we'll make a new entry in the backend tables map. Then we'll create columns as specified by the AST.

	func (mb *MemoryBackend) CreateTable(crt *CreateTableStatement) error {
	    t := table{}
	    mb.tables[crt.name.value] = &t
	    if crt.cols == nil {

	        return nil
	    }

	    for _, col := range *crt.cols {
	        t.columns = append(t.columns, col.name.value)

	        var dt ColumnType
	        switch col.datatype.value {
	        case "int":
	            dt = IntType
	        case "text":
	            dt = TextType
	        default:
	            return ErrInvalidDatatype
	        }

	        t.columnTypes = append(t.columnTypes, dt)
	    }

	    return nil
	}

#### Implementing insert support

Keeping things simple, we'll assume the value passed can be correctly mapped to the type of the column specified.

We'll reference a helper for mapper values to internal storage,`tokenToCell`.

	func (mb *MemoryBackend) Insert(inst *InsertStatement) error {
	    table, ok := mb.tables[inst.table.value]
	    if !ok {
	        return ErrTableDoesNotExist
	    }

	    if inst.values == nil {
	        return nil
	    }

	    row := []MemoryCell{}

	    if len(*inst.values) != len(table.columns) {
	        return ErrMissingValues
	    }

	    for _, value := range *inst.values {
	        if value.kind != literalKind {
	            fmt.Println("Skipping non-literal.")
	            continue
	        }

	        row = append(row, mb.tokenToCell(value.literal))
	    }

	    table.rows = append(table.rows, row)
	    return nil
	}

The `tokenToCell` helper will write numbers as binary bytes and will write strings as bytes:

	func (mb *MemoryBackend) tokenToCell(t *token) MemoryCell {
	    if t.kind == numericKind {
	        buf := new(bytes.Buffer)
	        i, err := strconv.Atoi(t.value)
	        if err != nil {
	            panic(err)
	        }

	        err = binary.Write(buf, binary.BigEndian, int32(i))
	        if err != nil {
	            panic(err)
	        }
	        return MemoryCell(buf.Bytes())
	    }

	    if t.kind == stringKind {
	        return MemoryCell(t.value)
	    }

	    return nil
	}

#### Implementing select support

Finally, for select we'll iterate over each row in the table and return the cells according to the columns specified by the AST.

	func (mb *MemoryBackend) Select(slct *SelectStatement) (*Results, error) {
	    table, ok := mb.tables[slct.from.table]
	    if !ok {
	        return nil, ErrTableDoesNotExist
	    }

	    results := [][]Cell{}
	    columns := []struct {
	        Type ColumnType
	        Name string
	    }{}

	    for i, row := range table.rows {
	        result := []Cell{}
	        isFirstRow := i == 0

	        for _, exp := range slct.item {
	            if exp.kind != literalKind {
	                // Unsupported, doesn't currently exist, ignore.
	                fmt.Println("Skipping non-literal expression.")
	                continue
	            }

	            lit := exp.literal
	            if lit.kind == identifierKind {
	                found := false
	                for i, tableCol := range table.columns {
	                    if tableCol == lit.value {
	                        if isFirstRow {
	                            columns = append(columns, struct {
	                                Type ColumnType
	                                Name string
	                            }{
	                                Type: table.columnTypes[i],
	                                Name: lit.value,
	                            })
	                        }

	                        result = append(result, row[i])
	                        found = true
	                        break
	                    }
	                }

	                if !found {
	                    return nil, ErrColumnDoesNotExist
	                }

	                continue
	            }

	            return nil, ErrColumnDoesNotExist
	        }

	        results = append(results, result)
	    }

	    return &Results{
	        Columns: columns,
	        Rows:    results,
	    }, nil
	}

### The REPL

At last, we're ready to wrap the parser and in-memory backend in a REPL. The most complex part is displaying the table of results from a select query.

	package main

	import (
	    "bufio"
	    "fmt"
	    "os"
	    "strings"

	    "github.com/eatonphil/gosql"
	)

	func main() {
	    mb := gosql.NewMemoryBackend()

	    reader := bufio.NewReader(os.Stdin)
	    fmt.Println("Welcome to gosql.")
	    for {
	        fmt.Print("# ")
	        text, err := reader.ReadString('\n')
	        text = strings.Replace(text, "\n", "", -1)

	        ast, err := gosql.Parse(text)
	        if err != nil {
	            panic(err)
	        }

	        for _, stmt := range ast.Statements {
	            switch stmt.Kind {
	            case gosql.CreateTableKind:
	                err = mb.CreateTable(ast.Statements[0].CreateTableStatement)
	                if err != nil {
	                    panic(err)
	                }
	                fmt.Println("ok")
	            case gosql.InsertKind:
	                err = mb.Insert(stmt.InsertStatement)
	                if err != nil {
	                    panic(err)
	                }

	                fmt.Println("ok")
	            case gosql.SelectKind:
	                results, err := mb.Select(stmt.SelectStatement)
	                if err != nil {
	                    panic(err)
	                }

	                for _, col := range results.Columns {
	                    fmt.Printf("| %s ", col.Name)
	                }
	                fmt.Println("|")

	                for i := 0; i < 20; i++ {
	                    fmt.Printf("=")
	                }
	                fmt.Println()

	                for _, result := range results.Rows {
	                    fmt.Printf("|")

	                    for i, cell := range result {
	                        typ := results.Columns[i].Type
	                        s := ""
	                        switch typ {
	                        case gosql.IntType:
	                            s = fmt.Sprintf("%d", cell.AsInt())
	                        case gosql.TextType:
	                            s = cell.AsText()
	                        }

	                        fmt.Printf(" %s | ", s)
	                    }

	                    fmt.Println()
	                }

	                fmt.Println("ok")
	            }
	        }
	    }
	}

Putting it all together:

	$ go run *.go
	Welcome to gosql.
	# CREATE TABLE users (id INT, name TEXT);
	ok
	# INSERT INTO users VALUES (1, 'Phil');
	ok
	# SELECT id, name FROM users;
	| id | name |
	====================
	| 1 |  Phil |
	ok
	# INSERT INTO users VALUES (2, 'Kate');
	ok
	# SELECT name, id FROM users;
	| name | id |
	====================
	| Phil |  1 |
	| Kate |  2 |
	ok

And we've got a very simple SQL database!
Next up we'll get into filtering, sorting, and indexing.

#### Further reading

- [Writing a simple JSON parser](https://notes.eatonphil.com/writing-a-simple-json-parser.html)
    - This post goes into a little more detail about the theory and basics of parsing.
- [Database Systems: A Practical Approach to Design, Implementation and Management](https://www.goodreads.com/book/show/617120.Database_Systems)
    - A giant book, but an excellent and very easy introduction to database theory.

#### Comments

Please reply on Twitter with questions or comments.

 [**](https://github.com/eatonphil)  [**](https://twitter.com/phil_eaton)  [**](https://notes.eatonphil.com/rss.xml)  [Subscribe](https://docs.google.com/forms/d/e/1FAIpQLSchaYjB6mq0SHmFL_J1wbB7E4SwUk23Dja2K7mfjtYH5o48fw/viewform?usp=sf_link)