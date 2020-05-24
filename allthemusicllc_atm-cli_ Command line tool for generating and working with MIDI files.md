allthemusicllc/atm-cli: Command line tool for generating and working with MIDI files.

# [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='60'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='843' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/allthemusicllc/atm-cli#atm-cli)atm-cli

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='61'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='845' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/allthemusicllc/atm-cli#overview)Overview

`atm-cli` is a command line tool for generating and working with MIDI files. It was purpose-built for All the Music, LLC to assist in its mission to enable musicians to make all of their music without the fear of frivolous copyright lawsuits. All code is released into the public domain via the [Creative Commons Attribute 4.0 International License](http://creativecommons.org/licenses/by/4.0/). If you're looking for a Rust library to generate and work with MIDI files, check out[the `libatm` project](https://github.com/allthemusicllc/libatm), on which this tool relies. For more information on All the Music, check out [allthemusic.info](http://allthemusic.info/). For more detailed information about the code, check out the crate documentation [here](https://allthemusicllc.github.io/atm-cli/atm/index.html).

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='62'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='848' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/allthemusicllc/atm-cli#installation)Installation

`atm-cli` is written in [Rust](https://www.rust-lang.org/), and thus requires the Rust toolchain to compile. Follow the instructions at https://www.rust-lang.org/tools/install to install the toolchain. Once that is complete, clone the repo and compile the tool:

$ git clone https://github.com/allthemusicllc/atm-cli.git
$ cd atm-cli
$ git submodule update --init
$ cargo build --release
$ cargo run --release -- -h # show usage

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='63'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='855' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/allthemusicllc/atm-cli#getting-started)Getting Started

To generate a single MIDI file from a melody, use the `single` directive:
atm single -n 'C:4,D:4,E:4,F:4,G:4,A:4,B:4,C:5' -t test.mid

To brute-force a range of melodies with a given length, generated from a given input note sequence, use the `batch` directive:

atm batch -n 'C:4,D:4,E:4,F:4,G:4,A:4,B:4,C:5' -L 8 -b 20 -p 2 -t C4_D4_E4_F4_G4_A4_B4_C5.tar

After brute-force generating a range of melodies with the `batch` command, lookup the output batch for note sequence with the `partition` directive:

atm partition -n 'C:4,C:4,C:4,C:4,C:4,C:4,C:4,C:5' -p 2

You can download an existing dataset containing all 10-note melodies containing the 8 major keys in the Middle C octave from:

https://allthemusic.s3.amazonaws.com/datasets/20190727.C4_D4_E4_F4_G4_A4_B4_C5.L10.tar

## [![](data:image/svg+xml,%3csvg xmlns='http://www.w3.org/2000/svg' class='octicon octicon-link js-evernote-checked' viewBox='0 0 16 16' version='1.1' width='16' height='16' aria-hidden='true' data-evernote-id='64'%3e%3cpath fill-rule='evenodd' d='M4 9h1v1H4c-1.5 0-3-1.69-3-3.5S2.55 3 4 3h4c1.45 0 3 1.69 3 3.5 0 1.41-.91 2.72-2 3.25V8.59c.58-.45 1-1.27 1-2.09C10 5.22 8.98 4 8 4H4c-.98 0-2 1.22-2 2.5S3 9 4 9zm9-3h-1v1h1c1 0 2 1.22 2 2.5S13.98 12 13 12H9c-.98 0-2-1.22-2-2.5 0-.83.42-1.64 1-2.09V6.25c-1.09.53-2 1.84-2 3.25C6 11.31 7.55 13 9 13h4c1.45 0 3-1.69 3-3.5S14.5 6 13 6z' data-evernote-id='874' class='js-evernote-checked'%3e%3c/path%3e%3c/svg%3e)](https://github.com/allthemusicllc/atm-cli#usage)Usage

atm 0.2.0
All The Music, LLC

Tools for generating and working with MIDI files. This app was created as part of an effort to generate by brute-force

billions of melodies, and is tailored for that use case.
USAGE:
atm [SUBCOMMAND]
FLAGS:
-h, --help Prints help information
-V, --version Prints version information
SUBCOMMANDS:

batch Generate by brute-force MIDI files containing permutations of a sequence of MIDI pitches help Prints this message or the help of the given subcommand(s)

partition Generate the output path from the 'batch' directive for a given MIDI pitch sequence

single Generate single MIDI file from provided MIDI pitch sequence