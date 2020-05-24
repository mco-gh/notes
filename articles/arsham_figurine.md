arsham/figurine

###    README.md

# [(L)](https://github.com/arsham/figurine#figurine)Figurine

[[68747470733a2f2f676f7265706f7274636172642e636f6d2f62616467652f6769746875622e636f6d2f61727368616d2f6669677572696e65](../_resources/d44fec0bdd61765720e0a381fdf75da3.bin)](https://opensource.org/licenses/Apache-2.0)[[68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4c6963656e73652d417061636865253230322e302d626c75652e737667](../_resources/910356e190dee6a2626038b2492f9a57.bin)](http://godoc.org/github.com/arsham/figurine)[[68747470733a2f2f676f646f632e6f72672f6769746875622e636f6d2f61727368616d2f6669677572696e653f7374617475732e737667](../_resources/6ac4d9948bd755f8116f3a3192a36819.bin)](https://goreportcard.com/report/github.com/arsham/figurine)

Print your name in style

[![figurine.png](../_resources/03e2da28b9fe9db3893d3d43e53dae4c.png)](https://github.com/arsham/figurine/blob/master/docs/figurine.png?raw=true)

### [(L)](https://github.com/arsham/figurine#table-of-contents)Table of Contents

1. [Installation](https://github.com/arsham/figurine#installation)
2. [Usage](https://github.com/arsham/figurine#usage)
3. [See Also](https://github.com/arsham/figurine#see-also)
4. [License](https://github.com/arsham/figurine#license)

## [(L)](https://github.com/arsham/figurine#installation)Installation

You can download the latest binary from[here](https://github.com/arsham/figurine/releases), or you can compile from source:

$ go get github.com/arsham/figurine

## [(L)](https://github.com/arsham/figurine#usage)Usage

Every time the application is called, it chooses a random font for rendering the message. Pass the message you want to decorate as arguments.

$ figurine Some Text
You can print available fonts:
$ figurine -l
$ figurine -l -s
To set a font:
$ figurine -f "Poison.flf" Some Text
To get a list of available arguments:
$ figurine -h

This application is very light weight, so feel free to add it to your .zshrc/.bashrc file, so each time you open a new shell it shows you a nice message.

## [(L)](https://github.com/arsham/figurine#see-also)See Also

See also [Rainbow](https://github.com/arsham/rainbow), which is the library that colours the output.

## [(L)](https://github.com/arsham/figurine#license)License

Use of this source code is governed by the Apache 2.0 license. License that can be found in the [LICENSE](https://github.com/arsham/figurine/blob/master/LICENSE) file.