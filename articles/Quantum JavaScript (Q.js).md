Quantum JavaScript (Q.js)

### [#](https://quantumjavascript.app/#Quantum,_made_easy)Quantum, made easy

Q is a quantum circuit simulator, drag-and-drop circuit editor, and powerful JavaScript library that runs right here in your web browser. There’s nothing to install and nothing to configure, so jump right in and experiment! Here’s your first quantum circuit—a[Bell state](https://en.wikipedia.org/wiki/Bell_state).	([Here’s how to make one!](https://quantumjavascript.app/tutorials.html#Create_controlled_gates)) Tap and drag the pieces around to get a feel for the Q editor. It’s easy to use on both desktop and mobile devices. Made a mistake? Just tap the Undo button.

H
X
Y
Z
S
T

⟲
⟳
C
S

↘
1
2
3
4
1
2
3
4
5
6
0
0
0
0
H

X
X
Y

This circuit is accessible in your[JavaScript console](https://quantumjavascript.app/index.html#Open_your_JavaScript_console)as `$('#example').circuit`

#### [#](https://quantumjavascript.app/#Live_probabilty_results)Live probabilty results

Edit the code above and watch the probabilty results update in realtime.
`
1 |0000⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
2 |0001⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
3 |0010⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
4 |0011⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
5 |0100⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
6 |0101⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
7 |0110⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
8 |0111⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
9 |1000⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
10 |1001⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
11 |1010⟩ ██████████░░░░░░░░░░ 50% chance
12 |1011⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
13 |1100⟩ ██████████░░░░░░░░░░ 50% chance
14 |1101⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
15 |1110⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
16 |1111⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
`

### [#](https://quantumjavascript.app/#Free_and_open-source)Free and open-source

Q is free to use, our code is open-source, and our API is heavily documented. Still a quantum novice? Each page of API documentation includes simple explanations of basic quantum concepts to get you up to speed quickly. This makes Q ideal for the classroom as well as autodidacts at home. Q just might be the most accessible quantum circuit suite in the world. Join our project on GitHub athttps://github.com/stewdio/q.jsand drop a link to Q’s website[https://quantumjavascript.app](https://quantumjavascript.app/)on social media with the hashtag[#Qjs](https://twitter.com/search?q=%23Qjs). Let’s make quantum computing accessible!

* * *

### [#](https://quantumjavascript.app/#Quantum_JavaScript)Quantum JavaScript

What does coding a quantum circuit look like?	Let’s recreate the above[Bell state](https://en.wikipedia.org/wiki/Bell_state) using**three separate circuit authoring styles**to demonstrate Q’s flexibility. For each of the three examples we’ll create a circuit that uses 2 qubit registers for 2 moments of time. We’ll place a [Hadamard](https://quantumjavascript.app/Q-Gate.html#.HADAMARD) gate at moment 1 on register 1. Then we’ll place a [Controlled-Not](https://quantumjavascript.app/Q-Gate.html#.PAULI_X) gate at moment 2, with its control component on register 1 and its target component on register 2.

##### [#](https://quantumjavascript.app/#text-as-input)1. Text as input

Q’s [text-as-input](https://quantumjavascript.app/Q-Circuit.html#.fromText) feature directly converts your text into a functioning quantum circuit. Just type your operations out as if creating a text-only circuit diagram (using “I” for[identity gates](https://quantumjavascript.app/Q-Gate.html#.IDENTITY) in the spots where no operations occur) and enclose your text block in[backticks](https://en.wikipedia.org/wiki/Grave_accent) (instead of quotation marks). Note that parentheses are not required to invoke the function call when using backticks.

	[Q](https://quantumjavascript.app/Q.html)`
		H  X#0
		I  X#1
	`

##### [#](https://quantumjavascript.app/#python-inspired)2. Python-inspired

Folks coming to Q from Python-based quantum suites may find this syntax more familiar. Here the `[Q](https://quantumjavascript.app/Q.html)` function expects the number of qubit registers to use, followed by the number of moments to use. Afterward, each single-letter quantum gate label is also a function name. For these functions the first argument is a moment index and the second is a qubit register index or array of qubit register indices.

	[Q](https://quantumjavascript.app/Q.html)( 2, 2 )
		.h( 1, 1 )
		.x( 2, [ 1, 2 ])

##### [#](https://quantumjavascript.app/#verbose-for-clarity)3. Verbose for clarity

Under the hood, Q is making more verbose declarations. You can also make direct declarations like so. (And [what are those dollar signs about?](https://quantumjavascript.app/contributing.html#Destructive_vs_non-destructive_methods))

	new [Q](https://quantumjavascript.app/Q.html).[Circuit](https://quantumjavascript.app/Q-Circuit.html)( 2, 2 )
		.[set$](https://quantumjavascript.app/Q-Circuit.html#.set$)( [Q](https://quantumjavascript.app/Q.html).[Gate](https://quantumjavascript.app/Q-Gate.html).[HADAMARD](https://quantumjavascript.app/Q-Gate.html#.HADAMARD), 1, 1 )
		.[set$](https://quantumjavascript.app/Q-Circuit.html#.set$)( [Q](https://quantumjavascript.app/Q.html).[Gate](https://quantumjavascript.app/Q-Gate.html).[PAULI_X](https://quantumjavascript.app/Q-Gate.html#.PAULI_X), 2, [ 1, 2 ])

##### [#](https://quantumjavascript.app/#More_variations)More variations

There are many ways to build a quantum circuit with Q. What feels right for you? To learn more about[Q’s text syntax](https://quantumjavascript.app/Q-Circuit.html#.fromText) and other convenience tricks, see [“Writing quantum circuits.”](https://quantumjavascript.app/Q-Circuit.html#Writing_quantum_circuits)

#### [#](https://quantumjavascript.app/#Clear,_legible_output)Clear, legible output

Whether you use Q’s drag-and-drop circuit editor interface,[text syntax](https://quantumjavascript.app/Q-Circuit.html#.fromText), Python-inspired syntax, or prefer to type out every [set$](https://quantumjavascript.app/Q-Circuit.html#.set$) command yourself, Q makes inspecting and evaluating your circuits easy.

Let’s add two commands which could directly follow any of the three examples above. Hey—deciding what to name a circuit can sometimes be difficult, so we’ll let Q choose a random name for us. Then we’ll generate an outcome probabilities report. Just add the following two lines to any of the above examples:

	.[setName$](https://quantumjavascript.app/Q-Circuit.html#.setName$)( [Q](https://quantumjavascript.app/Q.html).[getRandomName$](https://quantumjavascript.app/Q.html#.getRandomName$) )
	.[evaluate$](https://quantumjavascript.app/Q-Circuit.html#.evaluate$)()

And that combination will yield something like the following:
`Beginning evaluation for “Sapphire Shrew”
m1 m2 ┌───┐╭─────╮
r1 |0⟩─┤ H ├┤ X#0 │
└───┘╰──┬──╯
╭──┴──╮
r2 |0⟩───○──┤ X#1 │
╰─────╯
██████████░░░░░░░░░░ 50% 1 of 2
████████████████████ 100% 2 of 2
Evaluation completed for “Sapphire Shrew”
with these results:
1 |00⟩ ██████████░░░░░░░░░░ 50% chance
2 |01⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
3 |10⟩ ░░░░░░░░░░░░░░░░░░░░ 0% chance
4 |11⟩ ██████████░░░░░░░░░░ 50% chance`

* * *

### [#](https://quantumjavascript.app/#Open_your_JavaScript_console)Open your JavaScript console

You don’t have to know a thing about quantum physics or JavaScript to launch your first qubit into[superposition](https://en.wikipedia.org/wiki/Quantum_superposition). If you’re on a desktop or laptop then everything you need is already right here in front of you. First, you must open your browser’s JavaScript console. (It’s a text window for sending JavaScript commands to your browser and receiving responses from your browser in return. You text your computer, it texts back.)

This handy chart shows you what key commands will open your JavaScript console. Are you on a Mac or a Windows machine? What web browser are you using? (If you’re on Linux, join this project on[GitHub](https://github.com/stewdio/q.js).)

|     |     |     |
| --- | --- | --- |
|     | ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 600' data-evernote-id='1' class='js-evernote-checked'%3e %3cpath d='M447.372%2c316.885c0.759%2c81.719%2c71.689%2c108.913%2c72.475%2c109.26c-0.6%2c1.918-11.333%2c38.754-37.369%2c76.803 c-22.507%2c32.896-45.866%2c65.671-82.664%2c66.349c-36.157%2c0.666-47.784-21.441-89.122-21.441c-41.326%2c0-54.243%2c20.763-88.471%2c22.108 c-35.519%2c1.344-62.567-35.572-85.261-68.347c-46.372-67.042-81.811-189.446-34.226-272.071 c23.639-41.032%2c65.884-67.015%2c111.736-67.681c34.879-0.665%2c67.8%2c23.465%2c89.122%2c23.465c21.308%2c0%2c61.315-29.019%2c103.373-24.757 c17.607%2c0.733%2c67.029%2c7.112%2c98.765%2c53.565C503.173%2c215.723%2c446.759%2c248.565%2c447.372%2c316.885 M379.418%2c116.219 C398.276%2c93.393%2c410.968%2c61.617%2c407.505%2c30c-27.181%2c1.092-60.05%2c18.113-79.547%2c40.927c-17.473%2c20.202-32.775%2c52.538-28.646%2c83.529 C329.609%2c156.8%2c360.56%2c139.06%2c379.418%2c116.219' data-evernote-id='246' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)[macOS](https://www.apple.com/macos) | ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 600' data-evernote-id='2' class='js-evernote-checked'%3e %3cpath id='path5' d='M282.44%2c122.961C358.005%2c111.398%2c433.715%2c100.507%2c509.424%2c90c0.048%2c66.354%2c0%2c132.659%2c0.048%2c199.013 c-75.661%2c0.288-151.323%2c1.439-227.032%2c1.679C282.392%2c234.75%2c282.392%2c178.855%2c282.44%2c122.961L282.44%2c122.961z' data-evernote-id='249' class='js-evernote-checked'%3e%3c/path%3e %3cpath id='path7' d='M90.528%2c149.733c56.902-8.78%2c114.044-16.361%2c171.186-23.509c0.048%2c55.031%2c0.048%2c110.014%2c0.096%2c165.045 c-57.094-0.048-114.188%2c0.816-171.282%2c0.672V149.733L90.528%2c149.733z' data-evernote-id='250' class='js-evernote-checked'%3e%3c/path%3e %3cpath id='path29' d='M90.528%2c309.26c57.046-0.192%2c114.092%2c0.72%2c171.138%2c0.624c0%2c55.175%2c0.144%2c110.35%2c0.048%2c165.524 c-56.998-8.444-114.092-15.833-171.186-23.557V309.26z' data-evernote-id='251' class='js-evernote-checked'%3e%3c/path%3e %3cpath id='path31' d='M282.104%2c311.467c75.805%2c0%2c151.563%2c0%2c227.32%2c0c0.096%2c66.162%2c0%2c132.323%2c0%2c198.533 c-75.565-11.323-151.275-21.83-226.984-32.097C282.344%2c422.44%2c282.2%2c366.977%2c282.104%2c311.467z' data-evernote-id='252' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)[Windows](https://www.microsoft.com/en-us/windows) |
| ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 600' data-evernote-id='3' class='js-evernote-checked'%3e %3cpath d='M550.452%2c211.144c-11.746-27.366-35.573-56.914-54.231-66.254c13.308%2c24.956%2c22.543%2c51.757%2c27.377%2c79.451l0.049%2c0.439 c-30.565-73.784-82.396-103.534-124.728-168.316c-2.141-3.276-4.283-6.558-6.368-10.023c-1.193-1.979-2.148-3.762-2.978-5.403 c-1.756-3.292-3.109-6.771-4.032-10.367c0.003-0.344-0.262-0.634-0.614-0.675c-0.167-0.044-0.343-0.044-0.509%2c0 c-0.035%2c0-0.091%2c0.061-0.133%2c0.074c-0.042%2c0.013-0.133%2c0.074-0.195%2c0.101l0.105-0.176 c-67.902%2c38.496-90.941%2c109.761-93.061%2c145.407c3.153-0.209%2c6.292-0.466%2c9.5-0.466c49.047%2c0.087%2c94.271%2c25.659%2c118.451%2c66.977 c-19.015-12.753-42.244-18.214-65.182-15.324c97.232%2c47.046%2c71.132%2c209.176-63.606%2c203.057 c-11.998-0.477-23.855-2.692-35.175-6.571c-2.646-0.964-5.292-2.013-7.938-3.147c-1.528-0.669-3.055-1.351-4.562-2.107 c-32.985-16.52-60.272-47.749-63.675-85.664c0%2c0%2c12.478-45.027%2c89.351-45.027c8.307%2c0%2c32.064-22.456%2c32.511-28.967 c-0.105-2.127-47.151-20.254-65.496-37.753c-9.8-9.354-14.452-13.865-18.575-17.242c-2.228-1.827-4.556-3.536-6.975-5.119 c-6.16-20.876-6.422-42.97-0.76-63.978c-24.936%2c11.697-47.094%2c28.278-65.07%2c48.694h-0.126 c-10.714-13.149-9.96-56.508-9.347-65.565c-3.169%2c1.233-6.195%2c2.789-9.026%2c4.64c-9.458%2c6.536-18.3%2c13.87-26.422%2c21.916 c-9.255%2c9.086-17.708%2c18.906-25.271%2c29.358v-0.007c-17.38%2c23.858-29.708%2c50.813-36.27%2c79.309l-0.363%2c1.729 c-0.509%2c2.303-2.344%2c13.838-2.657%2c16.344c0%2c0.196-0.042%2c0.378-0.063%2c0.574c-2.366%2c11.909-3.833%2c23.969-4.387%2c36.085v1.351 c0.131%2c144.57%2c121.275%2c261.665%2c270.583%2c261.538c131.489-0.111%2c243.827-91.81%2c266.176-217.274c0.453-3.377%2c0.823-6.72%2c1.228-10.131 C573.555%2c298.073%2c567.527%2c252.872%2c550.452%2c211.144z' data-evernote-id='256' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)[Firefox](https://www.mozilla.org/firefox/) | ⌥⌘K<br>Option Command**K** | ⌃⇧K<br>Control Shift**K** |
| ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 600' data-evernote-id='4' class='js-evernote-checked'%3e %3ccircle fill='none' cx='300' cy='300' r='270' data-evernote-id='274' class='js-evernote-checked'%3e%3c/circle%3e %3cpath d='M75.169%2c150.445C123.564%2c77.836%2c206.196%2c30%2c300%2c30c98.44%2c0%2c184.576%2c52.682%2c231.753%2c131.39L300%2c160 c-76.317%2c0-138.372%2c61.065-139.969%2c136.999L75.169%2c150.445z' data-evernote-id='275' class='js-evernote-checked'%3e%3c/path%3e %3ccircle fill='none' cx='300' cy='300' r='270' data-evernote-id='276' class='js-evernote-checked'%3e%3c/circle%3e %3cpath d='M282.897%2c569.487C195.819%2c563.88%2c113.075%2c516.237%2c66.173%2c435c-49.22-85.252-46.665-186.189-2.09-266.399L178.756%2c370 c38.159%2c66.092%2c122.07%2c89.301%2c188.629%2c52.717L282.897%2c569.487z' data-evernote-id='277' class='js-evernote-checked'%3e%3c/path%3e %3ccircle fill='none' cx='300' cy='300' r='270' data-evernote-id='278' class='js-evernote-checked'%3e%3c/circle%3e %3cpath d='M541.934%2c180.068c38.684%2c78.216%2c38.795%2c173.695-8.107%2c254.932c-49.22%2c85.252-137.912%2c133.507-229.663%2c135.009L421.244%2c370 c38.159-66.092%2c16.302-150.366-48.66-189.716L541.934%2c180.068z' data-evernote-id='279' class='js-evernote-checked'%3e%3c/path%3e %3ccircle display='inline' cx='300' cy='300' r='120' data-evernote-id='280' class='js-evernote-checked'%3e%3c/circle%3e %3c/svg%3e)[Chrome](https://www.google.com/chrome/) | ⌥⌘J<br>Option Command**J** | ⌃⇧I<br>Control Shift**I** |
| ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 600' data-evernote-id='5' class='js-evernote-checked'%3e %3cpath d='M517.353%2c431.841c-7.198%2c3.765-14.622%2c7.082-22.228%2c9.933c-24.212%2c9.059-49.86%2c13.675-75.712%2c13.624 c-99.796%2c0-186.727-68.647-186.727-156.738c0.26-24.059%2c13.517-46.094%2c34.65-57.596c-90.263%2c3.796-113.462%2c97.856-113.462%2c152.963 c0%2c155.81%2c143.599%2c171.606%2c174.537%2c171.606c16.682%2c0%2c41.842-4.851%2c56.942-9.617l2.763-0.928 C446.223%2c535%2c495.76%2c495.728%2c528.573%2c443.735c2.497-3.934%2c1.332-9.146-2.602-11.643 C523.362%2c430.436%2c520.055%2c430.339%2c517.353%2c431.841z' data-evernote-id='298' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M253.017%2c539.144c-18.811-11.675-35.112-26.973-47.958-45.005c-55.429-75.941-38.8-182.438%2c37.141-237.866 c7.925-5.784%2c16.335-10.873%2c25.137-15.208c6.58-3.1%2c17.821-8.71%2c32.773-8.436c21.355%2c0.155%2c41.406%2c10.302%2c54.179%2c27.416 c8.516%2c11.371%2c13.212%2c25.148%2c13.413%2c39.353c0-0.443%2c51.585-167.873-168.717-167.873c-92.583%2c0-168.716%2c87.859-168.716%2c164.941 c-0.365%2c40.776%2c8.359%2c81.12%2c25.539%2c118.102c58.118%2c124.003%2c199.88%2c184.84%2c329.799%2c141.532 c-44.476%2c14.023-92.863%2c7.857-132.4-16.872L253.017%2c539.144z' data-evernote-id='299' class='js-evernote-checked'%3e%3c/path%3e %3cpath d='M351.294%2c343.939c-1.708%2c2.214-6.96%2c5.272-6.96%2c11.937c0%2c5.504%2c3.585%2c10.798%2c9.954%2c15.248 c30.327%2c21.09%2c87.501%2c18.306%2c87.648%2c18.306c22.471-0.054%2c44.517-6.135%2c63.838-17.61c39.66-23.158%2c64.081-65.596%2c64.176-111.522 c0.548-47.262-16.872-78.685-23.916-92.604C501.346%2c80.278%2c404.883%2c30%2c299.983%2c30C152.366%2c29.985%2c32.113%2c148.548%2c30.037%2c296.15 c1.012-77.061%2c77.61-139.297%2c168.717-139.297c7.381%2c0%2c49.476%2c0.717%2c88.576%2c21.237c34.46%2c18.095%2c52.513%2c39.944%2c65.061%2c61.603 c13.033%2c22.503%2c15.353%2c50.931%2c15.353%2c62.256C367.744%2c313.275%2c361.965%2c330.062%2c351.294%2c343.939z' data-evernote-id='300' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)[Edge](https://www.microsoft.com/en-us/edge) | ⌥⌘J<br>Option Command**J** | F12 |
| ![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 600 600' data-evernote-id='6' class='js-evernote-checked'%3e %3cpath d='M300%2c30C150.883%2c30%2c30%2c150.883%2c30%2c300s120.883%2c270%2c270%2c270s270-120.883%2c270-270S449.117%2c30%2c300%2c30z M330.797%2c329.109 L131.672%2c470.648l139.852-199.758l199.125-141.539L330.797%2c329.109z' data-evernote-id='314' class='js-evernote-checked'%3e%3c/path%3e %3c/svg%3e)[Safari](https://www.apple.com/safari/) | ⌥⌘C<br>Option Command**C** | ×   |

Now that your JavaScript console is open, copy and paste the following line into it: (Note that those are backticks on either side of the H, rather than single quotation marks.)

	[Q](https://quantumjavascript.app/Q.html)`H`.[try$](https://quantumjavascript.app/Q-Circuit.html#.prototype.try$)() ? 'tails' : 'heads'

Did you try it? You just performed a quantum coin flip! Each time you run the above code there’s a 50% chance of landing on**heads** (`0`) and a 50% chance of landing on**tails** (`1`). Try it a few more times to see how random it feels. (Just tap your “up” arrow key in the JavaScript console to recall the last command you entered without having to type it or paste it again.) When you’re ready for more, give[“Writing quantum circuits”](https://quantumjavascript.app/Q-Circuit.html#Writing_quantum_circuits)a quick read.

* * *

### [#](https://quantumjavascript.app/#Import_and_export)Import and export

Q plays well with everyone. Export your circuits as[plain text](https://quantumjavascript.app/Q-Circuit.html#.toText),[ASCII diagrams](https://quantumjavascript.app/Q-Circuit.html#.toDiagram),[interactive graphic-user-interfaces](https://quantumjavascript.app/Q-Circuit.html#.toDom),[LaTeX code](https://quantumjavascript.app/Q-Circuit.html#.toLatex), and more! Visit the [Q playground](https://quantumjavascript.app/playground.html) to experiment with converting circuits between various formats. As always, new features are in the works.[Join our project on GitHub](https://github.com/stewdio/q.js)and help us build bridges to everywhere.

* * *

**Keywords**. Q, Q.js, Qjs, quantum, quantum physics, quantum mechanics, superposition, quantum computer, quantum computer programming, quantum JavaScript, quantum computing, QC, quantum simulator, quantum computer simulator, qubit, qbit, gate, Hadamard, Bloch, Bloch Sphere, Web, Web site, website, Web browser, browser, HTML, HTML5, JavaScript, ES6, CSS.