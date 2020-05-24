James Stanley - Hiding messages in chess games

James Stanley - Hiding messages in chess games
![](../_resources/57f3557c4a85d8664b50c475c9d5529e.png)
https://incoherency.co.uk/blog/stories/chess-steg.html

James Stanley Hiding messages in chess games Tue 9 October 2018 Tagged: chess , steganography I designed a steganography system that encodes data as a chess game. A convenient way to communicate chess games is PGN , but any means of communicating the moves of the game would work, as the information is encoded conceptually in the moves themselves, rather than taking advantage of any redundancy in the PGN format. You can play with it here: Chess Steganography . The code is on github . There is also a perl implementation of the same concept, but the encoding is incompatible because it was easier that way.