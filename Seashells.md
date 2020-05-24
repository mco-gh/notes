Seashells

# # Seashells

Seashells lets you *pipe output from command-line programs to the web in real-time*, even without installing any new software on your machine. You can use it to monitor long-running processes like experiments that print progress to the console. You can also use Seashells to share output with friends!

$  echo  'Hello, Seashells!'  |  [nc](http://nc110.sourceforge.net/) seashells.io 1337serving at https://seashells.io/v/{random url}

## ## Client

While you can use [netcat](http://nc110.sourceforge.net/) for convenience (because it comes preinstalled on most systems), if you use Seashells often, it's highly recommended that you install the [seashells](https://github.com/anishathalye/seashells) client. You can install it by running ``pip install seashells``.

Once you have the client installed, you can pipe output to ``seashells`` instead of piping to ``nc seashells.io 1337``. The client gives you additional features, such as showing output on stdout as well as forwarding to Seashells. Run ``seashells --help`` for more information about using the client.

## ## Examples

- - Show output on both stdout and Seashells:

$  python train.py |  seashellsserving at https://seashells.io/v/{url}
Epoch 1/1000, loss = 12.483
{...}

- - Show output on both stdout and Seashells using netcat:

$  go test -v  |  tee  >(nc seashells.io 1337)serving at https://seashells.io/v/{url}

=== RUN TestSeashellsBasic
{...}

- - Show stdout and stderr on Seashells:

$  npm install 2>&1  |  seashellsserving at https://seashells.io/v/{url}
npm WARN prefer global node-gyp@3.6.2 should be installed with -g
{...}

- - Have time to see URL before full-screen command:

$  htop  |  seashells  --delay 5serving at https://seashells.io/v/{url}
{5 second delay}
{...}

## ## Notes

- -  If you want plaintext output, replace the ``/v/{url}`` (for view) with ``/p/{url}`` (for plaintext).

- -  Seashells isn't meant for data storage: old sessions are garbage collected after a period of one day.

- -  Seashells currently doesn't have an accounts system, so each IP address is limited to 5 concurrent sessions. This will likely change soon, and you'll have access to more sessions if you're signed in and using the ``seashells`` client.

- -  Seashells is currently in beta. While we think the service is working pretty well, we recommend that you don't use Seashells for any uptime-critical applications.

- -  If you have any feedback or feature requests, please send them to [aathalye+seashells@mit.edu](https://seashells.io/mailto:aathalye+seashells@mit.edu).

## ## Acknowledgements

Created by [@anishathalye](https://github.com/anishathalye).

Seashells builds on open-source technologies. In particular, Seashells would not have been possible without the excellent [xterm.js](https://github.com/sourcelair/xterm.js).