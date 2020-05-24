Learn Svelte by building a simple Tic Tac Toe game

# Learn Svelte by building a simple Tic Tac Toe game

October 22, 2019

tldr: This is a tutorial that explains the basics of Svelte by building a simple Tic Tac Toe game. You can find the [demo](https://vigilant-varahamihira-f18ad0.netlify.com/) or [clone the repo](https://github.com/codesnacks/svelte-tic-tac-toe) if you’re just interested in the final application.

Let’s jump right into it:

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='138' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='300' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://codesnacks.net/svelte/tic-tac-toe-1/#setup)Setup

	npx degit sveltejs/template svelte-tic-tac-toe
	cd svelte-tic-tac-toe

	npm install
	npm run dev

This already sets up your “Hello World” application on http://localhost:5000/

If you look at the folder structure you’ll discover a `src` folder with a `main.js` and an `App.svelte` file. `App.svelte` contains the `App` component, which we will extend in this first part of the tutorial.

So let’s open this file:

	<script>
	  export let name;
	</script>

	<style>
	  h1 {
	    color: purple;
	  }
	</style>

	<h1>Hello {name}!</h1>

As you can see this component consists of thee sections:

- script
- style
- markup

Each of these sections is optional, but we’ll need them for our game.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='139' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='324' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://codesnacks.net/svelte/tic-tac-toe-1/#global-styles)Global Styles

Let’s first drop in some global styles to make the whole application and a little bit more appealing later on. We’ll start with a font and some colors:

	<style>
	  @import url("https://fonts.googleapis.com/css?family=Shadows+Into+Light&display=swap");

	  :global(*),
	  :global(button) {
	    font-family: "Shadows Into Light", cursive;
	    background: #2e5266;
	    color: #e2c044;
	    text-align: center;
	    font-size: 48px;
	  }
	</style>

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='140' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='339' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://codesnacks.net/svelte/tic-tac-toe-1/#the-board)The Board

Let’s start with writing some markup and CSS to create our board and clean up the rest of the file. We’ll need three `rows` with three `squares` each. We’ll use a flexbox for the rows to display the squares next to each other.

	<style>
	  @import url("https://fonts.googleapis.com/css?family=Shadows+Into+Light&display=swap");

	  :global(*),
	  :global(button) {
	    font-family: "Shadows Into Light", cursive;
	    background: #2e5266;
	    color: #e2c044;
	    text-align: center;
	    font-size: 48px;
	  }
	  .row {
	    height: 45px;
	    display: flex;
	    justify-content: center;
	  }
	  .square {
	    padding: 0;
	    width: 45px;
	    height: 45px;
	    font-size: 24px;
	    border: 1px solid #d3d0cb;
	  }
	</style>

	<div class="row">
	  <button class="square" />
	  <button class="square" />
	  <button class="square" />
	</div>
	<div class="row">
	  <button class="square" />
	  <button class="square" />
	  <button class="square" />
	</div>
	<div class="row">
	  <button class="square" />
	  <button class="square" />
	  <button class="square" />
	</div>

This already gives us a nice board with the needed squares as clickable buttons. Cool! But of course, nothing happens when we click the buttons. So let’s add an event handler. We do this by adding the script section again to the top of the file. And adding the handler to the markup of one of the buttons.

	  <script>
	    function handleClick() {
	      console.log("clicked");
	    }
	  </script>

	  /* ... style and other markup ... */

	  <button class="square" on:click={handleClick} />

So far so good! Now we need to pass some arguments to the clickHandler. We do this by wrapping an anonymous function around the `handleClick` function and pass the needed argument.

	  <script>
	    function handleClick(i) {
	      console.log("clicked", i);
	    }
	  </script>

	  /* ... style and other markup ... */

	  <button class="square" on:click={() => handleClick(1)} />

Perfect! So let’s add an index to all of the squares, that we can pass to the `handleClick` function.

	<script>
	  function handleClick(i) {
	    console.log("clicked", i);
	  }
	</script>

	/* ... styles ... */

	<div class="row">
	  <button class="square" on:click={() => handleClick(0)} />
	  <button class="square" on:click={() => handleClick(1)} />
	  <button class="square" on:click={() => handleClick(2)} />
	</div>
	<div class="row">
	  <button class="square" on:click={() => handleClick(3)} />
	  <button class="square" on:click={() => handleClick(4)} />
	  <button class="square" on:click={() => handleClick(5)} />
	</div>
	<div class="row">
	  <button class="square" on:click={() => handleClick(6)} />
	  <button class="square" on:click={() => handleClick(7)} />
	  <button class="square" on:click={() => handleClick(8)} />
	</div>

We can now distinguish between all of the buttons when we click them. To save the state of the clicked buttons we’ll add a JS representation of the board in the script section. It’ll be a simple array with a length of 9. It’ll contain undefined if no player has made a move on that square, otherwise, it’ll contain the symbol of the player `x` or `o`.

We’ll also add a `nextPlayer` variable, to know who’s turn it is. This variable will just be `x` or `o`.

	<script>
	  // creates an array with 9 undefined entries
	  let board = Array.from(new Array(9));
	  // player x is going to start
	  let nextPlayer = "x";

	  function handleClick(i) {
	    console.log("clicked", i);
	  }
	</script>

To show whose turn it is, we’ll add a headline to the markup, that contains the nextPlayer variable. To output a JS variable in the markup a set of curly braces is needed.

	<h1>
	  next player
	  <strong>{nextPlayer}</strong>
	</h1>

Let’s now get to the fun part of actually writing the symbol of the player to the board and alternating between the players.

To make this work, we first need to adjust the square to actually reflect the state of the `board` variable:

	<div class="row">
	  <button class="square" on:click={() => handleClick(0)}>
	    {!!board[0] ? board[0] : ''}
	  </button>
	  <button class="square" on:click={() => handleClick(1)}>
	    {!!board[1] ? board[1] : ''}
	  </button>
	  <button class="square" on:click={() => handleClick(2)}>
	    {!!board[2] ? board[2] : ''}
	  </button>
	</div>
	<div class="row">
	  <button class="square" on:click={() => handleClick(3)}>
	    {!!board[3] ? board[3] : ''}
	  </button>
	  <button class="square" on:click={() => handleClick(4)}>
	    {!!board[4] ? board[4] : ''}
	  </button>
	  <button class="square" on:click={() => handleClick(5)}>
	    {!!board[5] ? board[5] : ''}
	  </button>
	</div>
	<div class="row">
	  <button class="square" on:click={() => handleClick(6)}>
	    {!!board[6] ? board[6] : ''}
	  </button>
	  <button class="square" on:click={() => handleClick(7)}>
	    {!!board[7] ? board[7] : ''}
	  </button>
	  <button class="square" on:click={() => handleClick(8)}>
	    {!!board[8] ? board[8] : ''}
	  </button>
	</div>

This is quite tedious, but we’ll come up with a nicer solution later on.
We’ll now focus on changing the `board` with the click handler.

	  function handleClick(i) {
	    // set the symbol of the "current" player on the board
	    board[i] = nextPlayer;

	    // alternate between players
	    nextPlayer = nextPlayer === "x" ? "o" : "x";
	  }

This already gives us a fully working Tic Tac Toe Board!

Now let’s make the markup of the board a bit more flexible. We’ll introduce a `rows` variable in the script section to get this done:

	  // split the board into columns to render them
	  const rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]];

In the markup, we iterate over the rows and squares. We can use the `#each` tag to do this:

	{#each rows as row}
	  <div class="row">
	    {#each row as index}
	      <button class="square" on:click={() => handleClick(index)}>
	        {!!board[index] ? board[index] : '  '}
	      </button>
	    {/each}
	  </div>
	{/each}

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='141' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='501' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://codesnacks.net/svelte/tic-tac-toe-1/#winning-condition)Winning Condition

One of the problems our game still has is that you can continue after a player has won. That’s because we didn’t implement any winning condition yet. So let’s do this now.

We have to check after every move if the winning condition is met. So we’ll add this to the `handleClick` function and implement the `checkWinningCondition` function.

But let’s start with defining the winning conditions themselves:

	const possibleWinningCombinations = [
	  // rows
	  [0, 1, 2],
	  [3, 4, 5],
	  [6, 7, 8],
	  // columns
	  [0, 3, 6],
	  [1, 4, 7],
	  [2, 5, 8],
	  // diagonals
	  [0, 4, 8],
	  [6, 4, 2]
	];

`possibleWinningCombinations` now contains all three in a row combinations by the index of the squares. Let’s use this in our `checkWinningConditions` function.

	  // state that contains the winning combination if one exists
	  let winningCombination;

	  function checkWinningCondition() {
	    return possibleWinningCombinations
	      .filter(combination => {
	        return (
	          !!board[combination[0]] &&
	          board[combination[0]] === board[combination[1]] &&
	          board[combination[0]] === board[combination[2]]
	        );
	      })
	      // will contain the winning combination or undefined
	      .pop();
	  }

	  function handleClick(i) {
	    // set the symbol of the "current" player on the board
	    board[i] = nextPlayer;

	    // alternate between players
	    nextPlayer = nextPlayer === "x" ? "o" : "x";

	    // check the winning combination if there is any
	    winningCombination = checkWinningCondition();

	    // and log it
	    console.log(winningCombination);
	  }

So as soon as you have three in a row the application will not log the winning combination. Quite cool! But let’s make this a bit more obvious by highlighting the squares. To achieve this we’ll add a conditional class on the squares. So let’s change the markup:

	{#each rows as row}
	  <div class="row">
	    {#each row as index}
	      <button
	        class="square {!!winningCombination && winningCombination.includes(index) ? 'winning-combination' : ''}"
	        on:click={() => handleClick(index)}>
	        {!!board[index] ? board[index] : '  '}
	      </button>
	    {/each}
	  </div>
	{/each}

This adds the class `winning-combination` to all of the squares, that are part of a winning combination. We have to add some CSS to make these squares stand out. So within the style section, we add:

	  .winning-combination {
	    background: #6e8898;
	  }

This gives the squares of a winning combination a different background.

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='142' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='566' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://codesnacks.net/svelte/tic-tac-toe-1/#displaying-the-winner)Displaying the winner

We also should output the winning player. Therefore we will introduce a `winningPlayer` variable in the script section. We will read the value of the first square of the `winningCombination` to find out which player actually won. Let’s name this function `getWinner` and call it inside of the `handleClick` function.

	  let winningPlayer;

	  //...

	  function getWinningPlayer() {
	    return board[winningCombination[0]];
	  }

	  function getWinner() {
	    winningCombination = checkWinningCondition();

	    if (winningCombination) {
	      winningPlayer = getWinningPlayer();
	    }
	  }

	  function handleClick(i) {
	    // set the symbol of the "current" player on the board
	    board[i] = nextPlayer;

	    // alternate between players
	    nextPlayer = nextPlayer === "x" ? "o" : "x";

	    // get the winner and the winning combination
	    getWinner();
	  }

So `winningPlayer` is either `x`, `o` or undefined, is there’s no winning combination. In this case, we don’t want to show a winner, so we need conditional rendering of an element. We’ll use the `#if` tag in the markup section to do that:

	{#if winningPlayer}
	  <h1>
	    winner
	    <strong>{winningPlayer}</strong>
	  </h1>
	  {:else}
	  <h1>no winner yet</h1>
	{/if}

By now we have a playable version of Tic Tac Toe. But one annoyance - or call it a feature - is, that one player can overwrite the squares of the other player and that moves are still possible after the game already has a winner. Let’s fix this by only reacting on clicks on the square if this square has no value yet and the game has no winner yet.

	  function handleClick(i) {
	    // return if the square at position i already has a value or the game already has a winner
	    if (board[i] || winningCombination) {
	      return;
	    }

	    board[i] = nextPlayer;

	    // switch player
	    nextPlayer = nextPlayer === "x" ? "o" : "x";

	    getWinner();
	  }

This is how the full game looks right now:

	<script>
	  // creates an array with 9 undefined entries
	  let board = Array.from(new Array(9));
	  // player x is going to start
	  let nextPlayer = "x";
	  let winningPlayer = "";

	  // split the board into columns to render them
	  const rows = [[0, 1, 2], [3, 4, 5], [6, 7, 8]];

	  const possibleWinningCombinations = [
	    // rows
	    [0, 1, 2],
	    [3, 4, 5],
	    [6, 7, 8],
	    // columns
	    [0, 3, 6],
	    [1, 4, 7],
	    [2, 5, 8],
	    // diagonals
	    [0, 4, 8],
	    [6, 4, 2]
	  ];

	  // state that contains the winning combination if one exists
	  let winningCombination;

	  function checkWinningCondition() {
	    return (
	      possibleWinningCombinations
	        .filter(combination => {
	          return (
	            !!board[combination[0]] &&
	            board[combination[0]] === board[combination[1]] &&
	            board[combination[0]] === board[combination[2]]
	          );
	        })
	        // will contain the winning combination or undefined
	        .pop()
	    );
	  }

	  function getWinningPlayer() {
	    return board[winningCombination[0]];
	  }

	  function getWinner() {
	    winningCombination = checkWinningCondition();

	    if (winningCombination) {
	      winningPlayer = getWinningPlayer();
	    }
	  }

	  function handleClick(i) {
	    // return if the square at positon i already has a value or the game already has a winner
	    if (board[i] || winningCombination) {
	      return;
	    }

	    // set the symbol of the "current" player on the board
	    board[i] = nextPlayer;

	    // alternate between players
	    nextPlayer = nextPlayer === "x" ? "o" : "x";

	    // get the winner and the winning combination
	    getWinner();
	  }
	</script>

	<style>
	  @import url("https://fonts.googleapis.com/css?family=Shadows+Into+Light&display=swap");

	  :global(*),
	  :global(button) {
	    font-family: "Shadows Into Light", cursive;
	    background: #2e5266;
	    color: #e2c044;
	    text-align: center;
	    font-size: 48px;
	  }
	  .row {
	    height: 45px;
	    display: flex;
	    justify-content: center;
	  }
	  .square {
	    padding: 0;
	    width: 45px;
	    height: 45px;
	    font-size: 24px;
	    border: 1px solid #d3d0cb;
	  }
	  .winning-combination {
	    background: #6e8898;
	  }
	</style>

	<h1>
	  next player
	  <strong>{nextPlayer}</strong>
	</h1>

	{#each rows as row}
	  <div class="row">
	    {#each row as index}
	      <button
	        class="square {!!winningCombination && winningCombination.includes(index) ? 'winning-combination' : ''}"
	        on:click={() => handleClick(index)}>
	        {!!board[index] ? board[index] : '  '}
	      </button>
	    {/each}
	  </div>
	{/each}

	{#if winningPlayer}
	  <h1>
	    winner
	    <strong>{winningPlayer}</strong>
	  </h1>
	{:else}
	  <h1>no winner yet</h1>
	{/if}

### [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' aria-hidden='true' height='16' version='1.1' viewBox='0 0 16 16' width='16' data-evernote-id='143' class='js-evernote-checked'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='743' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://codesnacks.net/svelte/tic-tac-toe-1/#persisting-state)Persisting State

Our game completely resets after every change we make to the code because of hot module reloading. The same happens of course if you reload the browser window. To fix this, we will add the state of our game to the `localStorage` of your browser. We will, therefore, make use of the **lifecycle hooks** that Svelte provides. In our case we will use `onMount`, which is called whenever the component was first rendered to the DOM to get the previous state from the local storage. `afterUpdate` is called after the DOM was synced with the data of the application. We will, therefore, use it to update our state in the local storage.

Enough said. Let’s import these lifecycle hooks and use them:

	  import { onMount, afterUpdate } from "svelte";

	  // ...

	  onMount(() => {
	    const storedState = JSON.parse(window.localStorage.getItem("tictactoe"));

	    board = storedState.board || initialBoard;
	    nextPlayer = storedState.nextPlayer || "x";

	    // check if there is already a winner
	    getWinner();
	  });

	  afterUpdate(function() {
	    window.localStorage.setItem(
	      "tictactoe",
	      JSON.stringify({ board, nextPlayer })
	    );
	  });

Now the state of the application is persisted and we can continue our games even after a page refresh. The only thing that’s now missing is a button to start over and clean the state. So let’s add a button to the markdown and wire it up with a click handler

	  function clearState() {
	    // remove the state from local storage
	    localStorage.removeItem("tictactoe");

	    // reset the board
	    board = [...initialBoard];

	    // reset the next player
	    nextPlayer = "x";

	    // reset the winningCombination
	    winningCombination = null;
	  }
	</script>

	// ...

	<button on:click={clearState}>start over</button>

That’s it! Our first very simple Svelte application is done. Please follow me if you liked this article and you don’t want to miss part 2 of this series, where we learn about *component composition*, animations and deploying our application to netlify.

Thanks for reading! If you have any questions or suggestions just drop me a line in the comments!