Kramnik And AlphaZero: How To Rethink Chess - Chess.com

 ![25110.9393953a.668x375o.a45c29993d36.png](../_resources/6a65da467b7e5be20a72109638aafb1d.png)

 The legendary 14th world chess champion Vladimir Kramnik writes about an exciting way to make chess more interesting.

# Kramnik And AlphaZero: How To Rethink Chess‎

 [![68294742.8a353c1a.35x35o.8e688c290799.jpeg](../_resources/4a68636a07ed0d50210c8e47fb3f25ff.jpg)](https://www.chess.com/member/vladimirkramnik)

 [GM](https://www.chess.com/members/titled-players)  [VladimirKramnik](https://www.chess.com/member/vladimirkramnik)

 [(L)](https://www.chess.com/membership?c=flair)

  Updated: Dec 2, 2019, 8:40 AM   |
 c
 588  |  [Opening Theory](https://www.chess.com/articles/opening-theory)

M
 English‎
<

**For chess to flourish, we need a new challenge.**

The increasing strength of chess engines, the millions of **[computer games](http://www.chess.com/ccc)** and the volumes of **[opening theory](https://www.chess.com/openings)** available to every player are making top-level chess less imaginative. Decisive games in super-tournaments have declined, while the number of games with what I'd call "creative" content is also on the slide.

The 2018 world championship match between[** Magnus Carlsen**](https://www.chess.com/players/magnus-carlsen) and [**Fabiano Caruana**](https://www.chess.com/players/fabiano-caruana), for example, ended with zero decisive classical games. (Carlsen defended his world title by winning a [rapid-game playoff](https://www.chess.com/news/view/carlsen-wins-2018-world-chess-championship-in-playoff).)

This is not the players’ fault, but the reality they face. It would be strange to expect them to deliberately decrease their chances of a positive outcome by taking unreasonable risks for the sake of playing more “entertaining” games. From my own experience, I know how difficult it has become to force a complex and interesting fight if your opponent wants to play it safe. As soon as one side chooses a relatively sterile line of play, the opponent is forced to follow suit, leading to an unoriginal game and an inevitably drawish outcome.

Of course, there are still some fascinating top-level games being played, but to keep chess alive, I believe we must reverse this trend before the game’s spirit fades away.

**Working with DeepMind:**

So I started thinking, if the outcome is always the same, perhaps there’s something we can do to reinvigorate the game. I spoke with **Demis Hassabis**, the founder and CEO of the artificial intelligence lab **[DeepMind](https://deepmind.com/).** Hassabis was once one of the strongest junior chess players in the United Kingdom and is still a devoted chess aficionado. I was granted an opportunity to test my theory with the famous machine-learning chess engine [**AlphaZero**](https://www.chess.com/news/view/updated-alphazero-crushes-stockfish-in-new-1-000-game-match).

Working with DeepMind researchers **Ulrich Paquet** and **Nenad Tomasev**, we used AlphaZero as a petri dish to test different variations and see how the game might unfold. Ultimately, our mission was to find an **adjustment to the rules **to allow more space for human creativity.

Tweaking the rules of chess is not a new idea. One of the most widely played variants is **Fischer Random**, also known as Chess960. The recent **[World Fischer Random Chess Championship](https://www.frchess.com/)** drew quite a bit of attention and resulted in **Wesley So’s** triumph over Carlsen in the finals.

![phpAe15o5.jpeg](../_resources/687c2bece00355908fc9dcb7c060ed83.jpg)

HWesley So wins the Fischer Random World Championship over Magnus Carlsen. Photo: Lennart Ootes / Chess.com.

Fischer Random is an interesting format, but it has its drawbacks. In particular, the nontraditional starting positions make it difficult for many amateurs to enjoy the game until more familiar positions are achieved. The same is true for world-class players, as many have confessed to me privately. Finally, it also seems to lack an aesthetic quality found in traditional chess, which makes it less appealing for both players and viewers, even if it does occasionally result in an exciting game.

[phptRkxWJ.webp](../_resources/b2558688c65f0ae600df7a4c5c434ab6.webp)
**No-castling chess:**

My aim was to find a chess variant that would not only have the potential to bring the excitement and decisive victories back to chess, but is also aesthetically pleasing. The goal was to reignite interest and introduce players and audiences to the immense complexity and creativity of the original game of chess.

To begin, we tasked AlphaZero with exploring **a**  **variant that prevented either side from castling**, trying different opening moves from both sides. The outcome was beyond our expectations!

We let AlphaZero learn how to play "no-castling chess" from scratch, allowing the program to incrementally learn how to master the game through a process of trial and error, similar to how it taught itself to play classical chess. After playing millions of games, AlphaZero became a no-castling expert, allowing us to analyze how it plays and assess the overall game balance.

The win/loss percentages for both White and Black are similar to classical chess, suggesting that the no-castling variant should be quite playable without favoring a particular player. Preventing the king from retreating to a safe distance means that all of the pieces have to engage in the melee, making the play more dynamic and entertaining, with a number of original patterns.

AlphaZero_NoCastle_100s_per_m vs. AlphaZero_NoCastle_100s_per_m

1/2-1/2  |Computer Match, selfplay from move 4 pg  /London, UK  /25 Sep 2019

8
7
6
5
4
3
2
1

a
b
c
d
e
f
g
h

*I have had a great time analyzing this game in detail and would like to share my findings with the readers, I am sure you will enjoy it as well!*  1.  e4    c6   2.  d4    d5   *the last book move*  3.  Nc3    dxe4   4.  Nxe4    Nf6   5.  Nc3   *It feels like we are back to the ancient times in terms of the opening theory when chess players had to think about the best ways to set up their pieces as early as move five, instead of blitzing out the first 20 moves as it often happens nowadays... It will take us a long time to understand why AZ have chosen this move and why it is (possibly) the best try in this position.*  5...  e6   6.  Be3    Qc7   *God knows why those moves have been played but considering the strength of the machine we can be sure it is one of the best ways of treating the Caro-Kann for both sides under the new circumstances...*  7.  h4 !  *I have noticed that it becomes a typical motif, a sort of a useful opening move, preparing the activation of the rook from h1 via h3 or sometimes by the means of h5, Rh4. The king then often moves to f1 or g1*  7...  Nbd7

(7...  h5   *is another typical response to h4 as I have noticed while studying the games, as you will see in the next example*)

8.  a4   *I suppose white decides that it is important to stop b5*
(8.  h5    b5 )

8...  h6   *looks strange to hurry with this, but maybe it is very deep prophylactics against g4, who knows...*

(8...  b6   9.  g4   *might be interesting*)

9.  Nf3    a6   *preparing c5 probably*  10.  Bc4    Bd6   11.  Kf1    b6   12.  Qe2    Bb7   13.  Re1   *both sides have been playing logical developing moves and now another typical opening maneuver is coming!*  13...  Ke7 !  *In "normal" chess both sides would have castled short, black would then push c5 and the game would take a standard positional path. But in "no-castle" chess kings are never fully safe and it makes the game sharp and entertaining*  14.  Bd2 !

(14.  Rh3    Rhe8   *should be perfectly fine*)
14...  Rhe8   15.  g4 !  *only chance to fight for the initiative*
(*after*  15.  Ne5    c5 !  *white has to be careful to equalize already*)
15...  c5 !

(15...  Nxg4   16.  Rg1   *is in white's favor*  16...  Ndf6   (16...  h5   17.  Ng5 )  17.  Ne5 )

16.  d5    Kf8   17.  dxe6    b5 !

(17...  Qc6 !?  *was another interesting move*  18.  Qd3 !   Ne5 !  19.  Nxe5    Qg2+ !  (19...  Bxe5   20.  Rg1    Bh2   *would have been strong if not for the amazing resource*  21.  Bf4 !!   Bxf4   22.  g5   *and white is better, for example*  22...  hxg5   23.  hxg5    Bxg5   24.  Rxg5    Qh1+   25.  Rg1    Bg2+   26.  Ke2    Qh2   27.  Kd1 !   b5   (27...  Re7 )  28.  Rxg2    bxc4   29.  Rxh2    cxd3   30.  e7+ !   Kg8   31.  cxd3 )  20.  Ke2    Bxe5   21.  Rhg1 !  (21.  Reg1    Qc6  ∓  22.  g5    Rad8   23.  e7+    Kxe7   24.  gxf6+    Kf8 )  21...  Qh2 !  22.  g5 !  (22.  Kd1    fxe6 )  (22.  exf7    Re7   23.  Kd1    b5 !  24.  g5 !   bxc4   25.  Qg6    Qxh4   26.  gxh6    Qh5+   27.  Kc1    Qxg6   28.  Rxg6    Nd7   29.  Bg5    Bf4+ !  30.  Bxf4    Rxe1+   31.  Kd2    Ne5 ! ⩱)  22...  hxg5   23.  Bxg5    fxe6   *with a complicated position assessed as equal by machine*  24.  Qg6   (24.  Qe3 ))

18.  axb5    Nb6   19.  g5 !

(19.  Rh3    Nxc4  ⩱  20.  Qxc4    axb5   21.  Nxb5   (21.  Qd3    c4   22.  Qf5    Rxe6   23.  Nxb5    Rxe1+   24.  Nxe1    Qc6   25.  Nxd6    Qxd6   26.  Bc3    Bc8   27.  Qf3    Ra1   *is equal*)  21...  Qb6 )

19...  Nxc4   20.  Qxc4

(20.  gxf6   *is not working*  20...  Bxf3   21.  Qxc4    Bxh1   22.  Qg4    fxe6 )

20...  Bxf3   21.  Rg1    hxg5   22.  hxg5    Ng8   *the best by far, everything else is bad, even if it might be hard to understand why with our human brains. Here is the answer:*

(22...  Nd7   23.  Qh4 !   fxe6   24.  g6 !   Nf6   25.  Bg5    Ng8   26.  Qh3    Bb7   27.  b6 !   Qd7   28.  Rg4 !)

(22...  Nh5   23.  Qd3 !   Bb7   24.  b6 !  *for some reason*  24...  Qc6   25.  Qh7 )

23.  Re3    Bh5   *the players are in a fighting mood!*

(23...  axb5   *leads to a holdable endgame*  24.  Nxb5    Ra1+   25.  Be1    Qa5 !  26.  Nxd6    Rxe6   27.  b4 !   Qxb4   28.  Qxb4    cxb4   29.  Rxe6    fxe6   30.  Rg3    Bd5   31.  Ke2    Rb1 )

24.  Rh1    Bg6

(24...  g6 ?  *is losing*  25.  Rxh5    gxh5   26.  b6 !   Qb7   27.  g6 !  *hats off!*)

25.  Rf3    Re7   *only move again*  26.  Nd5

(26.  Rh8   *was quite a serious alternative*  26...  axb5   *playing for more*  (26...  Qb7   *leads to a draw in most of the lines, the main one is quite amazing*  27.  exf7    Rxf7   28.  Ne4 !!   Re8   29.  Nf6 !   gxf6   30.  gxf6    Re4 !  31.  bxa6 !   Qc6   32.  Qa2 !   Qb5+   33.  Kg1    Rg4+   34.  Rg3    Qe2 !  35.  Qd5    Qd1+   36.  Kg2    Rxg3+   37.  fxg3    Qe2+   38.  Kg1    Qd1+   39.  Kg2 )  27.  Nxb5    Qc6   (27...  Qb7   28.  Ra3  ∞)  28.  exf7    Rxf7   *important*  (28...  Ra1+   *is inferior because of the obvious*  29.  Kg2    Rxf7   30.  Nd4 !   Qe4   31.  Rh4 !   Qa8   32.  Bf4 !!   Rxf4   33.  Ne6+    Ke7   34.  Nxf4    Bf7   35.  Qc3   *and white is somewhat better here*)  29.  Re3 !  (29.  Nd4    Qa4 ! -+)  29...  Ra1+   30.  Be1    Rd1 !  31.  Qe2    Rf5 !  *with a small but pleasant plus*)

26...  Qb7   27.  exf7    Rxf7   28.  Bf4 !   Be7 !

(*after*  28...  Bxf4   29.  Qxc5+    Ke8   30.  Rh8    Rf8   31.  c4 !  (31.  Rxf4    Qxb5+   32.  Qxb5+    axb5   33.  Nc7+    Kd7   34.  Nxa8    Rxf4   35.  Rxg8    Rf7   *black holds easily*)  31...  axb5   32.  Rxg8    Rxg8   33.  Rxf4    Bd3+   34.  Ke1    Ra7 !  35.  cxb5   *white is tiny better*)

29.  b6 !   Rd8   *only move again*  30.  Nc7 !

(30.  Nxe7    Rxe7  ∓  31.  Rhh3    Bh5 !  32.  Bd6+    Bxf3   33.  Bxe7+    Kxe7   34.  Qxc5+    Ke8 )

30...  Qxf3   *the perpetual was already unstoppable*  31.  Ne6+    Ke8   32.  Nc7+    Kf8   33.  Ne6+    Ke8   *DeepMind's technical comment. A draw! When AlphaZero plays against itself at full strength over longer time controls, as we see here, it is a very dynamic but equal match. When AlphaZero plays itself in training at a fraction of a second per move, with additional noise injected into its decision making process to aid learning, there is more margin for error. In training white wins 33% of games, black wins 23% of games, and 44% of games are drawn.*    1/2-1/2

white

black

result

round

year

AlphaZero_NoCastle_100s_per_m

AlphaZero_NoCastle_100s_per_m

1/2-1/2

2019
AlphaZero_NoCastle_100s_per_m

AlphaZero_NoCastle_100s_per_m

1/2-1/2

2019

*Two AlphaZero no-castling games annotated by Kramnik.*

The advantages do not stop there. The no-castling restriction means that players cannot rely on memorized patterns; they are forced to think creatively from the beginning. Even if a player wants to force a draw, it is nearly impossible to control everything. Plus, this variant makes it practically impossible to play it safe, even as White, because it is so much harder to find a completely secure place for the king.

Finally, it also levels the playing field, so that amateur players have a better chance at playing against more seasoned opponents, who often memorise opening theory.

**Old boundaries, new creativity:**

A tournament using this variant will definitely see a significant increase in the number of decisive games—far beyond 50 percent, I estimate—along with an explosion of creative and unexpected ideas.

There are still many details to investigate. For example, the openings seem to be more complicated in the AlphaZero no-castling games, meaning that new opening theory has to be developed and players will need to explore new approaches to king safety. But none of this should prevent the chess community from trying this game.

**I highly recommend that organizers of upcoming tournaments and chess lovers across the world give this variant a try.**

No-castling has the potential to reset the clock, making creativity and depth of thought more important than just memorizing patterns and spending preparation time pressing the spacebar to get the next computer-engine move. By adjusting our limits, we can harness a new generation of players, original ideas and a future of exciting, decisive and creative chess.

**Would you play no-castling chess? Let us know in the comments.**
**More on Vladimir Kramnik:**

- [Chess.com interview: 'I'm Not Afraid To Lose'‎](https://www.chess.com/article/view/vladimir-kramnik-interview-im-not-afraid-to-lose)
- [Chess.com biography](https://www.chess.com/players/vladimir-kramnik)

**More on AlphaZero:**

- [AlphaZero's surprise debut](https://www.chess.com/news/view/google-s-alphazero-destroys-stockfish-in-100-game-match)
- [AlphaZero beats Stockfish again](https://www.chess.com/news/view/updated-alphazero-crushes-stockfish-in-new-1-000-game-match)
- [Official AlphaZero resources](https://deepmind.com/research/open-source/alphazero-resources)
- [*Game Changer: AlphaZero's Groundbreaking Chess Strategies and the Promise of AI *by Matthew Sadler and Natasha Regan](https://shop.chess.com/game-changer/)
- 10 more unannotated AlphaZero-vs-AlphaZero no-castling games (below)

AlphaZero_NoCastle vs. AlphaZero_NoCastle

1/2-1/2  |Computer Match, selfplay from move 3 pgn_3368567873508361830_0  /London, UK  /25 Sep 2019  | Round: -

8
7
6
5
4
3
2
1

a
b
c
d
e
f
g
h

1.  d4   *book*  1...  d5   *book*  2.  Nc3   *book*  2...  Nf6   3.  Bf4    a6   4.  Nf3    e6   5.  e3    c5   6.  Bd3    Nc6   7.  Kf1    h5   8.  dxc5    Bxc5   9.  Qe1    h4   10.  h3    Rh5   11.  e4    Bb4   12.  Rd1    Bd7   13.  e5    d4   14.  exf6    Qxf6   15.  Bg5    Rxg5   16.  Ne4    Qxf3   17.  gxf3    Bxe1   18.  Nxg5    Bb4   19.  a3    Be7   20.  f4    Bd6   21.  Rg1    Bxf4   22.  Rg4    e5   23.  Rxh4    Ke7   24.  Ne4    b6   25.  Re1    Be6   26.  Ng3    b5   27.  Be4    Kd6   28.  Ne2    Bc4   29.  b3    Bxe2+   30.  Kxe2    Rc8   31.  Rg1    Bh6   32.  Rh5    Ne7   33.  f4    Bxf4   34.  Rxg7    Rc3   35.  Kf2    Re3   36.  Bb7    Rc3   37.  Be4    Re3   38.  Bb7    Rc3   39.  Be4     1/2-1/2

white

black

result

round

year

AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1-0

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019
AlphaZero_NoCastle

AlphaZero_NoCastle

1/2-1/2

-

2019