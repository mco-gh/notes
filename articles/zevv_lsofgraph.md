zevv/lsofgraph

# zevv/lsofgraph

 Lua

###  README.md

A small utility to convert Unix `lsof` output to a graph showing FIFO and UNIX interprocess communication.

Generate graph:
sudo lsof -n -F | ./lsofgraph | dot -Tjpg > /tmp/a.jpg
or add `unflatten` to the chain for a better layout:
sudo lsof -n -F | ./lsofgraph | unflatten -l 1 -c 6 | dot -T jpg > /tmp/a.jpg
[(L)](https://github.com/zevv/lsofgraph/blob/master/example.jpg)

[![example output](../_resources/a1deb3454d01de1b00fa2531d12ecf77.jpg)](https://github.com/zevv/lsofgraph/blob/master/example.jpg)