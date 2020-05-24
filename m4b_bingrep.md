m4b/bingrep

# [(L)](https://github.com/m4b/bingrep#bingrep)bingrep

Greps through binaries from various OSs and architectures, and colors them. Current backends:

- ELF 32/64, arm, x86, openrisc - all others will parse and color, but relocations won't show properly
- Mach 32/64, arm, x86
- PE (debug only)

**NOTE**: Requires rustc version 1.15 or greater. If you're using a distro's rust compiler, consider using [https://rustup.rs](https://rustup.rs/) to install your rustc compiler and associated binaries.

[![pic2](../_resources/98a7aa958140942ced1d9aa88e5457fc.png)](https://github.com/m4b/bingrep/blob/master/etc/s2.png)

[![pic1](../_resources/7f278f26e513caf8e972027477b11afe.png)](https://github.com/m4b/bingrep/blob/master/etc/s1.png)

[![mach](../_resources/cbb563da182803d26f668a1d2ac78b59.png)](https://github.com/m4b/bingrep/blob/master/etc/mach.png)

## [(L)](https://github.com/m4b/bingrep#build)Build

cargo build --release

## [(L)](https://github.com/m4b/bingrep#run)Run

Example:

	bingrep /bin/ls

To dump internal debug representation of the parsed binary:

	bingrep -d /bin/ls