Space Invaders

# Space Invaders

- [Disassembled Code as Z80 opcodes](http://www.computerarcheology.com/Arcade/SpaceInvaders/Code.html)
- [RAM Usage](http://www.computerarcheology.com/Arcade/SpaceInvaders/RAMUse.html)
- [Hardware Info](http://www.computerarcheology.com/Arcade/SpaceInvaders/Hardware.html)

# Related Projects

Mikael Agren patched the original ROMs to add a [high-score table](http://myprojectsweblog.blogspot.com/2011/09/space-invaders-high-score-list-hack.html). Check out his project blog and demo movie.

# The Space Invaders System

Space Invaders [as described on the Wikipedia](http://en.wikipedia.org/wiki/Space_Invaders) was one of the very first video arcade games. Released in 1978 by Taito, it ushered in the Golden Age of Arcade Games. Most video games before SI used dedicated circuit boards without a CPU. SI uses an 8080 CPU (the primitive forerunner of the Z80). The CPU board carried forward into several other games.

SI uses a black-and-white raster display (grid of pixels). Interestingly, vector graphics like in Atari Asteroids did not hit the market until 1979. In SI the hardware paints the monitor in the usual way: from left to right and top to bottom with a vertical retrace at the end. But the monitor is rotated counterclockwise 90 degrees counter-clockwise in the game cabinet. The rotation makes the code comments and screen coordinates a bit confusing. Here and in the code comments I'll use the terms "rotated" and "non-rotated" to help.

The game uses colored transparencies that overlay certain areas of the monitor. The player's area is green and the flying saucer line is red. The overlays are obvious when you see shots changing colors at the top and bottom of the screen.

Screen memory is organized as one-pixel-per-bit -- eight pixels per byte. All sprites in the game are one byte wide but many rows long (on the rotated screen they are all 8 bits tall but 8, 16, or more bits wide). Rarely does a game sprite align perfectly to a byte boundary in screen memory. Most of the time the image pixels have to be shifted. Some of the pixels fall in the first byte of screen memory and some spill over into the next byte. The 8080 instruction-set lacks multi-bit shifts to make sprite rendering practical. But the SI hardware includes a 2-byte shift register mapped into port memory. The sprite drawing hardware runs all images through the shift register for a very fast bit-mapping.

The Space Invaders sounds are all discrete analog circuitry. Opamps and decaying RC networks create an eerie realism that digital sound chips fall short of today. The individual sound circuits are triggered by bits in two output ports.

In the early eighties you would have found the Space Invaders cabinet in an arcade right next to the pinball machines. So a "tilt" switch, like you would find in a pinball machine, would not have seemed as strange as it does today. If you shake, slap, or otherwise physically abuse an SI cabinet you will get a TILT message and your game will end.

# General Code Structure

The assembly code is filled with lots of questionable structures. In general, there are lots and lots of NOP instructions. Some are executed in the code flow, but most are used as padding between code sections. I suspect that the value 00 was the default written to empty areas instead of the more common FF. For an EEPROM an erased memory byte contains "FF" and you have to burn the 0's in.

I added "%%" to comments in the code that you can search for to find these questionable areas. I'll note a few really strange code spots in passing:

The code at 0456 reads a two byte value from memory, increments it, and writes it back. But the code only increments the LSB. The upper byte never changes and is never accessed anywhere else in the code.

0456: 2A 8F 20 LD HL,($208F) ; Increments with every shot ...
0459: 2C INC L ; ... but only LSB ** ...
045A: 22 8F 20 LD ($208F),HL ; ... used for saucer direction

A common shortcut in assembly is to replace a CALL followed by a RET with just a JUMP to the subroutine. At 09AA the shortcut jumps to the very next line of code. An even shorter cut would be to take the jump out completely.

09A5: 23 INC HL ; Load ...
09A6: 7E LD A,(HL) ; ... the ...
09A7: 23 INC HL ; ... screen ...
09A8: 66 LD H,(HL) ; ... coordinates ...
09A9: 6F LD L,A ; ... to HL
09AA: C3 AD 09 JP $09AD ; ** Usually a good idea, but wasted here
;##-Print4Digits
; Print 4 digits in DE
09AD: 7A LD A,D ; Get first 2 digits of BCD or hex
09AE: CD B2 09 CALL $09B2 ; Print them
09B1: 7B LD A,E ; Get second 2 digits of BCD or hex (fall into print)
;##-DrawHexByte
; Display 2 digits in A to screen at HL
09B2: D5 PUSH DE ; Preserve
09B3: F5 PUSH AF ; Save for later

Assembly programmers do all kinds of "unstructured flow" tricks with the stack. Some of it is confusing and potentially error prone. The code at 0x01A2 breaks out of a routine when D reaches 0. But it doesn't return to the caller -- it discards a slot on the stack returns to the caller's caller (the grand-caller?)! The code makes some dangerous assumptions about who is calling it.

;##-MoveRefAlien

; The "reference alien" is the bottom left. All other aliens are drawn relative to this

; reference. This routine moves the reference alien (the delta is set elsewhere) and toggles

; the animation frame number between 0 and 1.
;
01A1: 15 DEC D ; This decrements with each call to move

01A2: CA CD 01 JP Z,$01CD ; Return out of TWO call frames (only used if no aliens left)

01A5: 21 06 20 LD HL,$2006 ; Set current alien ...
...
;##-ReturnTwo

; If there are no aliens left on the screen then MoveDrawAlien comes here which returns from the

; caller's stack frame.
;
01CD: E1 POP HL ; Drop return to caller
01CE: C9 RET ; Return to caller's caller

At 0x0A01 the value of A is stuffed into location 0x2067. The very next instruction loads A from 0x2067. This might make sense if any other line of code jumped to 0x0A04. But nobody does.

0A00: F1 POP AF ; Restore ...
0A01: 32 67 20 LD ($2067),A ; ... current player number

0A04: 3A 67 20 LD A,($2067) ; ** Why load this again? Nobody ever jumps to 0A04?

0A07: 67 LD H,A ; To H

The count-aliens routine at 0x15F3 sets the location 0x206B to 1 if there is only one alien left. Nobody every reads the flag from 0x206B. Maybe it was used at one time? At any rate the instructions at 0x160B and 0x160E could have been replaced with just "LD ($2067),A" to save some time and space.

;##-CountAliens

; Count number of aliens remaining in active game and return count 2082 holds the current count.

; If only 1, 206B gets a flag of 1 ** but ever nobody checks this
15F3: CD 11 16 CALL $1611 ; Get active player descriptor
15F6: 01 00 37 LD BC,$3700 ; B=55 aliens to check?
15F9: 7E LD A,(HL) ; Get byte
15FA: A7 AND A ; Is it a zero?
15FB: CA FF 15 JP Z,$15FF ; Yes ... don't count it
15FE: 0C INC C ; Count the live aliens
15FF: 23 INC HL ; Next alien
1600: 05 DEC B ; Count ...
1601: C2 F9 15 JP NZ,$15F9 ; ... all alien indicators
1604: 79 LD A,C ; Get the count
1605: 32 82 20 LD ($2082),A ; Hold it
1608: FE 01 CP $01 ; Just one?
160A: C0 RET NZ ; No keep going
160B: 21 6B 20 LD HL,$206B ; Set flag if ...
160E: 36 01 LD (HL),$01 ; ... only one alien left
1610: C9 RET ; Out

There is a huge empty area in the ROM between 0x0C00 and 0x13FF (2K bytes but not on a 2K ROM chip boundary, which would have saved the cost of a chip). That's 1/4th of the ROM empty, which leaves a lot of space for expansion. And yet it appears the developers felt they were running out of space! (Update ... this area was for a diagnostics routine that got dropped)

The end of ROM beginning at 0x1E00 contains an 8x8 pixel character set used to draw text on the screen. The area is filled out completely with 64 characters, but some of them were not used in messages by the game. The developers reclaimed the space of these unused characters for other purposes (see 0x1F50) rather than using the plentiful space at 0x0C00. Very strange.

# Hidden Message (Easter Egg)

There is a hidden message in the Space Invaders code. You can get the message "TAITO COP", with no "R" as in "CORP", to appear at the top of the screen during the demo play. Wait for the demo play to start and hold down "2 Start", "1 Fire", "1 Left", and "1 Right". The order you press them and the timing does not matter as long as you get all the buttons down at the same time eventually.

That's the first sequence. Then you have to hold down the second sequence: "1 Start", "1 Fire", "1 Left". Again the timing does not matter. An easy way is to hold down the first sequence and just switch start buttons and let up on "1 Right". You will see the message at the top of the screen in the "Flying Saucer" area (in red). The message will be erased when the demo finishes and you will have to reenter it every demo.

The MAME emulator has trouble with these simultaneous button presses. I was unable to reproduce the sequences in the emulator. I did patch the code to make a simpler sequence: "2 Start" then "1 Start".

;##-CheckHiddenMes

; There is a hidden message "TAITO COP" (with no "R") in the game. It can only be ; displayed in the demonstration game during the splash screens. You must enter

; 2 seqences of buttons. Timing is not critical. As long as you eventually get all

; the buttons up/down in the correct pattern then the game will register the
; sequence.
;
; 1st: 2start(down) 1start(up) 1fire(down) 1left(down) 1right(down)
; 2nd: 2start(up) 1start(down) 1fire(down) 1left(down) 1right(up)
;

; Unfortunately MAME does not deliver the simultaneous button presses correctly. You can see the message in

; MAME by changing 19A6 to 02 and 19B1 to 02. Then the 2start(down) is the only sequence. ;

199A: 3A 1E 20 LD A,($201E) ; Has the 1st "hidden-message" sequence ...
199D: A7 AND A ; ... been registered?
199E: C2 AC 19 JP NZ,$19AC ; Yes ... go look for the 2nd sequence
19A1: DB 01 IN A,($01) ; Get player inputs
19A3: E6 76 AND $76 ; 0111_0110 Keep 2Pstart, 1Pstart, 1Pshot, 1Pleft, 1Pright
19A5: D6 72 SUB $72 ; 0111_0010 1st sequence: 2Pstart, 1Pshot, 1Pleft, 1Pright
19A7: C0 RET NZ ; Not first sequence ... out
19A8: 3C INC A ; Flag that 1st sequence ...
19A9: 32 1E 20 LD ($201E),A ; ... has been entered
19AC: DB 01 IN A,($01) ; Check inputs for 2nd sequence
19AE: E6 76 AND $76 ; 0111_0110 Keep 2Pstart, 1Pstart, 1Pshot, 1Pleft, 1Pright

19B0: FE 34 CP $34 ; 0011_0100 2nd sequence: 1Pstart, 1Pshot, 1Pleft 19B2: C0 RET NZ ; If not second sequence ignore

19B3: 21 1B 2E LD HL,$2E1B ; Screen coordinates
19B6: 11 F7 0B LD DE,$0BF7 ; Message = "TAITO COP" (no R)
19B9: 0E 09 LD C,$09 ; Message length
19BB: C3 F3 08 JP $08F3 ; Print message and out

# Code Bug

There is a bug in the code, but it is very subtle. Here is a quick way to see it:

Shoot all the aliens but the one in the upper left. Try and stay to the left side of the screen as much as possible because you want to keep the aliens from shooting as much of your right shield as you can. Wait for this last alien to wiggle down the screen. Move to the far right side of the screen under the right edge of your right shield. The alien will turn green as it crosses the screen going from right to left above your shields. Just as it hits the left side of the screen and turns to eat your shields fire a shot into your shield. The game will think your shot hit the last alien and the next round will begin.

The timing is very critical, and it might take you several tries to see the bug. The best way to reproduce it is to play invaders in MAME and press Shift+F7 when there is only one alien left. That will save the state of your game, and you can press F7 to reload that state if you miss the timing. Eventually you will see it.

The bug is documented in the code at 0x1504, but I'll explain it in detail here.

The aliens are all drawn relative to the bottom left alien in the rack. This is the "reference alien". Even if it has been shot it continues to move as the origin for all the others (see discussion on The Aliens below).

There is an algorithm in the code to convert a screen point to a column/row coordinate within the alien rack. Rows go from 0 (the bottom row) up to 4 (the top row). Columns go from 0 (the left column) up to 10 (the right column). The code uses a "count the 16s" algorithm to see how many 16-pixels to add to the reference alien to get to (or just past) the target point. There are separate counts for X and Y. Each alien consumes a 16x16 pixel area on the screen. If the player's shot hits any pixel within the alien rack, this algorithm will find the row/column coordinate of the alien that was hit.

The "count the 16s" algorithm does NOT do boundary checking at all. The caller must assure that the target point is within the alien rack or unexpected values will result. If the target point is far to the right of the reference then the algorithm will produce a column number greater than the maximum 11th column. If the target point is left of the reference the results are a bit strange (see the code) and incorrect. Thus it is very important for the caller to make sure the target point is actually inside the alien rack.

The player-shot-collision code appears, at first glance, to check the boundary conditions correctly with some logical assumptions as follows:

The code first checks to see if the player's shot hit the saucer or exited the top of the screen. Next the code checks to see if the player's shot is above the Y coordinate of the reference alien. If the player's shot hits something below the saucer's zone and above the lowest alien point then it has to be inside the alien's 11x5 grid. What else could it be? No alien shots can be on the left or right of the grid. They can't be above it. Because the player's shot hit SOMETHING above the lowest alien point it must be a hit within the alien rack. Thus the "count 16s" algorithm will function correctly.

This assumption is the bug in the code. When the alien rack is down in the player's shield area then the player's shot can hit something outside the rack square -- the shields.

Start a new game and watch the full alien rack as it hits the right side of the screen and moves left. Move so you are peaking out of the right edge of the right shield. Position yourself so your shots will just miss the edge of your shield. Notice that when the aliens turn at the left side of the screen your shots are missing the alien rack but would be hitting an extra column of aliens if there were one.

The key point here is that the right edge of the player's right shield is in the 12th (invalid) column when the alien rack turns on the left side of the screen.

Now imagine all the aliens are dead except for the upper left. This alien is in row 4. Rows are numbered from 0 to 4 from bottom to top. This alien is in column 0. Columns are numbered from 0 to 10 from left to right.

The alien wiggles around and you shoot the right edge of your right shield when it makes its turn on the left into your screen row. The Y coordinate of your shot is below the alien. The game correctly calculates your shot hit row 3 (one below 4). The shot is outside the alien rack, but the code calculates the column anyway. It gets 11 (the 12th column).

Aliens are numbered sequentially from 0 to 54 (11*55 = 55 aliens). The code converts row/column numbers to an index with this formula: ROW*11 + COLUMN. For examples, the alien at row=0, column=0 is index 0*11+0 = 0. The alien at row=4, column=10 is index 4*11+10 = 54.

Our upper left alien is at index 4*11+0 = 44. The game converts the shot row/column to an index of 3*11+11 = 44. The indices are the same and the game thinks the shot hit the last alien. The column overflow effectively moves the shot to the start of the next row.

# Game Timing

The game-play timing is based on an interrupt from the video system. Actually there are two interrupts. When the video rendering reaches the middle of the screen an RST 1 (jumps to 0x0008) is generated. When the rendering reaches the end of the screen (when vertical blanking begins) an RST 2 (jumps to 0x0010) is generated.

The separate interrupts allow the code to keep out of the way of the monitor's electron beam. If an object is moved in memory while the rendering hardware is drawing from the same memory then part of the image will be drawn at the old place and part at the new. This makes a very brief visual glitch that could, in theory, be noticed by the player. The flickers accumulate in the players mind over time.

Objects at the top of the screen are drawn after the mid-screen interrupt. Objects at the bottom of the screen are drawn after the end-screen interrupt. Thus the code and hardware work on different halves of the screen. I'll talk more about the mechanics of this in Game Objects below.

The screen refresh rate is 60Hz. So each interrupt is executed 60 times a second. Each interrupt has a list of chores to perform described below.

# End of Screen Interrupt

The end-screen interrupt checks the tilt switch. It counts the credits as coins are inserted. The limit is 99 stored as a byte of binary-coded-decimal. After that coins are just ignored (an overflow would wipe out $25 of quarters).

This interrupt decreases a general-purpose counter at 0x20C0. This counter is used to time small delays in the attract mode. The print-text code sets this timer and waits for it to reach zero before moving to the next letter. Thus the letters appear on the screen in a slow, steady beat.

This interrupt also counts the aliens and changes the rate of the "step" sound. The sound rate is independent of the actual steps, as I'll explain below in The Aliens.

There are three different alien shots, each with a different picture. The end-screen interrupt sets a flag to keep all three in sync so that only one shot is processed per screen refresh.

This interrupt code draws exactly one alien every interrupt. This interrupt code keeps up with the time between flying saucers.

And most importantly, this interrupt (like the mid-screen interrupt) gives all five game objects a chance to run. Each object decides which interrupt to use based on which half of the screen it is on. I'll discuss this in detail in Game Objects below.

# Mid Screen Interrupt

The mid-screen interrupt handles attract-mode tasks. In the attract mode there are two different animations to amuse a potential player passing by the cabinet. The first is an upside down "Y" in the message "PLAY" above "SPACE INVADERS". The small alien drags the letter off the screen and brings back the correct one. The second is an extra "C" in "INSERT CCOIN". The small alien shoots the extra "C". These animations happen every-other pass through the attract mode and not on the first pass.

The mid-screen interrupt advances the "next alien" cursor for the draw-alien process managed by the end-screen interrupt. See The Aliens below.

And most importantly again, this interrupt (like the end-screen interrupt) gives all five game objects a chance to run. Each object decides which interrupt to use based on which half of the screen it is on. I'll discuss this in detail in Game Objects below.

# Game Objects

There are five game objects processed by the interrupt routines. They are (1) the player at the bottom of the screen, (2) the player's shot, and (3) (4) (5) three different alien shots. The Flying Saucer that appears briefly at the top of the screen uses the (5) alien shot. Only one of these objects (saucer or shot) can be on the screen at the same time.

Each task has a 16 byte data structure. The first three bytes of each structure are timers that the system uses to decide how often to run a task. It is up to the task to reset its timer once it runs. The three bytes are organized as one two-byte timer and a second one-byte timer. If the first two-bytes are zero then the task manager moves to the third byte.

A single two-byte timer would have been sufficient. I suspect, based on some evidence in the code, that the first two-byte timer was meant for the initial startup time of the object. The player's object uses this timer to delay for two seconds at the start of the game. The second timer was meant to delay between handlings once the object gets started. The alien shots use this timer to slow them down.

The next two bytes in each structure are a pointer to the task's code. This reminds me of a modern day object-oriented virtual function pointer table!

0263: 5E LD E,(HL) ; Get handler address LSB
0264: 23 INC HL ; xx04
0265: 56 LD D,(HL) ; Get handler address MSB
0266: E5 PUSH HL ; Remember pointer to MSB
0267: EB EX DE,HL ; Handler address to HL
0268: E5 PUSH HL ; Now to stack (making room for indirect call)
0269: 21 6F 02 LD HL,$026F ; Return address to 026F
026C: E3 EX (SP),HL ; Return address (026F) now on stack. Handler in HL.
026D: D5 PUSH DE ; Push pointer to data struct (xx04) for handler to use
026E: E9 JP (HL) ; Run object's code (will return to next line)
026F: E1 POP HL ; Restore pointer to xx04

0270: 11 0C 00 LD DE,$000C ; Offset to next ... 0273: 19 ADD HL,DE ; ... game task (C+4=10)

0274: C3 4B 02 JP $024B ; Do next game task
The remaining bytes in each object structure are object-specific data.

Each object has an X,Y coordinate in its specific data. The upper bit of the Y coordinate defines which half of the non-rotated screen the sprite is on. If the upper bit is 0 then the Y value is 0-127. If the upper bit is 1 then the Y value is 128-255 (223 is the screen limit). The first thing the interrupts do is set a bit identifying which one is running. Both interrupts call the task routines, but the routines only run in the context of one of them based on their Y coordinate.

The routine at 0x1A06 compares the upper bit of the Y coordinate to the interrupt-id. If the beam is on the other half of the screen then the C flag is set, which allows the task to run in the current context. If the beam is on the same half of the screen then the task routine returns and is executed by the "other" interrupt when the beam has moved on. For instance, here is the check for an alien shot:

; Move the alien shot
05C1: 11 7C 20 LD DE,$207C ; Alien-shot Y coordinate
05C4: CD 06 1A CALL $1A06 ; Compare to beam position
05C7: D0 RET NC ; Not the right ISR for this shot

## Game Object 0: Move/draw Player

The player object is unique in that code only calls it with the mid-screen interrupt no matter which half of the screen the player is on. Remember that on the non-rotated screen the player moves up and down on the left side of the screen. The end-screen interrupt specifically skips this object, and the object code does not compare its Y coordinate to the interrupt id like the others do.

The player runs every screen refresh. That's as fast as it can be. But the code appears to be designed to make the player run slower. There is a line of code that sets the second-byte-timer that would slow the player down -- if it were non-zero.

Here are the last lines few lines of the player's object code:
; Draw player sprite
036F: 21 18 20 LD HL,$2018 ; Active player descriptor
0372: CD 3B 1A CALL $1A3B ; Load 5 byte sprite descriptor in order: EDLHB
0375: CD 47 1A CALL $1A47 ; Convert HL to screen coordinates
0378: CD 39 14 CALL $1439 ; Draw player

037B: 3E 00 LD A,$00 ; Clear the task timer. Nobody changes this but it could have ...

037D: 32 12 20 LD ($2012),A ; ... been speed set for the player with a value other than 0 (not XORA)

0380: C9 RET ; Out

This code first draws the sprite then sets the one-byte timer at 0x2012. Notice that the value loaded into A to set this timer is 00. The timer is already at 00 or this task would never have run. In fact, this is the only place in the code that writes to this memory location.

Notice that the instruction to set A to 00 is the two-byte indirect instruction "LD A,$00". A faster, smaller way is to use the one-byte instruction "XOR A" that exclusive-ORs the register with itself. This "fast zero" is used all over the code. In fact, the less efficient instruction "LD A,$00" is only used twice in the entire code: here and at 0x00CD. At 0x00CD it was specifically chosen because it does not affect the flags, which are passed to the next instruction.

00CB: FE FE CP $FE ; Moving left?

00CD: 3E 00 LD A,$00 ; Value of 0 for rack-moving-right (not XOR so flags are unaffected)

00CF: C2 D3 00 JP NZ,$00D3 ; Not FE ... keep the value 0 for right

I suspect at one time the "LD A" had a non-zero value. But a delay of any kind was probably too slow for play.

I suspect the task was originally designed to pick an interrupt based on Y like the other objects. Why was the task changed to run at only mid-screen? I suspect -- and this is pure speculation -- that the pick-a-half-of-the-screen algorithm produced an undesirable visual effect. The mid-screen interrupt happens at scan-line 96. But the code asserts it happens at scan-line 128 by using the Y coordinate's upper bit. There is a 32 byte discrepancy near the middle of the screen, and the player moving left and right at the mid screen may have made this difference obvious with the flicker it was trying to avoid. I need to burn a new set of ROMs to test this theory since it would not appear in the MAME emulator which drives a faster monitor.

The player task code is straight forward. If the player is blowing up then the code flips back and forth between two images for half a second. If the game is in player-mode then the buttons translate to left or right.

; Draw player sprite
036F: 21 18 20 LD HL,$2018 ; Active player descriptor
0372: CD 3B 1A CALL $1A3B ; Load 5 byte sprite descriptor in order: EDLHB
0375: CD 47 1A CALL $1A47 ; Convert HL to screen coordinates
0378: CD 39 14 CALL $1439 ; Draw player

037B: 3E 00 LD A,$00 ; Clear the task timer. Nobody changes this but it could have ...

037D: 32 12 20 LD ($2012),A ; ... been speed set for the player with a value other than 0 (not XORA)

0380: C9 RET ; Out
;##-MovePlayerRight
; Handle player moving right
0381: 78 LD A,B ; Player coordinate
0382: FE D9 CP $D9 ; At right edge?
0384: CA 6F 03 JP Z,$036F ; Yes ... ignore this
0387: 3C INC A ; Bump X coordinate
0388: 32 1B 20 LD ($201B),A ; New X coordinate
038B: C3 6F 03 JP $036F ; Draw player and out

The player's fire button is read and debounced in the main game loop at 1618. In demo mode the player always fires, and when the player shot is removed from play a new demo command is read from an 11 byte table. The change of direction in the demo thus depends on the shot exploding, which is somewhat non periodic.

## Game Object 1: Move/draw Player's Shot

The player's shot uses the Y coordinate and interrupt id to decide when to run. The shot can be in several states: just starting, moving up screen, blowing up because of hitting an alien, or blowing because of hitting something else.

The shot's deltaY (rotated screen) is a constant 4-pixels per interrupt. The shot covers the entire screen at a rate of 60Hz*4 pixels = 240 pixels/sec. The shot image itself is just a single byte -- a four-pixel line.

The sprite drawing algorithm checks the bits on the screen as it writes new bits. If a bit overlaps then a collision detection flag is set. If the player's shot is drawn over anything on the screen then a flag is set and checked at 190A in the main game loop.

## Game Object 2, 3, and 4: Alien Shots

There are three different alien shots in the game, and each has a unique picture. Object 2 is the "Rolling" shot. It spirals a bit as it falls. Object 3 is the "Plunger" shot. It reminds me of a bathroom plunger falling down the screen. Object 4 is the "Squiggly" shot. It looks like a turning zig-zag line much like a resistor circuit symbol.

The byte timer from Object 2 is used to synchronize the three shots so that only one shot is processed per screen. The objects can't synchronize directly from the timer byte at 2032 since its decrement depends on which half of the screen it is on. Instead the timer byte is copied to a sync-flag at 0x2080 where it remains constant for all the shots between end and mid screen interrupts.

The code uses a common routine to handle all three shots. Each shot task copies its data structure to a common area, calls the handler, and then copies the changed data back to its personal area.

The common handler is responsible for moving each shot. The normal delta Y for the shots is a constant 4 pixels down per step. A shot makes a step every 3 frames. (4*60/3 = 80 pixels per second). But when there are 8 or fewer aliens on the screen the delta changes up to 5 pixels per step (5*60/3 = 100 pixels per second).

The common handler also initiates the alien shots. Each shot has a move-counter that starts when the shot is dropped and counts up with each step as it falls. The game keeps a constant reload rate that determines how fast the aliens can fire. The game takes the smallest count of the other two shots and compares it to the reload rate. If it is too soon since the last shot then no shot is fired.

The reload rate gets faster as the game progresses. The code uses the upper two digits of the player's score as a lookup into the table at 1AA1 and sets the reload rate to the value in the table at 1CB8. The reload rate for anything below 0x0200 is 0x30. From 0x0200 to 0x1000 the delay drops to 0x10, then 0x0B at from 0x1000 to 0x2000. From 0x2000 to 0x3000 the rate is 8 and then maxes out above 0x3000 at 7. With a little flying-saucer-luck you will reach 0x3000 in 2 or 3 racks.

The "rolling" shot (object 2) drops right over the player when it falls. The other two shots use pointers into a table of columns at 0x1D00. The pointers advance very predictably. You can see from the table that the "squiggly" shot will fall first in column 11 and then 1, 6, and 3.

When there is only one alien left on the screen the plunger shot is disabled. Only the "rolling" (tracking) and squiggly shots are active, which means the tracking shot gets fired more often.

## Flying Saucer

The flying saucer shares the object-task with the "squiggly" shot. Only one of them can be on the screen at a time. The main loop keeps up with the time-until-saucer.

;##-TimeToSaucer
0913: 3A 09 20 LD A,($2009) ; Reference alien's X coordinate
0916: FE 78 CP $78 ; Don't process saucer timer ... ($78 is 1st rack Yr)
0918: D0 RET NC ; ... unless aliens are closer to bottom
0919: 2A 91 20 LD HL,($2091) ; Time to saucer
091C: 7D LD A,L ; Is it time ...
091D: B4 OR H ; ... for a saucer
091E: C2 29 09 JP NZ,$0929 ; No ... skip flagging
0921: 21 00 06 LD HL,$0600 ; Reset timer to 600 game loops
0924: 3E 01 LD A,$01 ; Flag a ...
0926: 32 83 20 LD ($2083),A ; ... saucer sequence
0929: 2B DEC HL ; Decrement the ...
092A: 22 91 20 LD ($2091),HL ; ... time-to-saucer
092D: C9 RET ; Done

Game task 4 checks the "time for saucer" flag. If it isn't time or if there is already a squiggly shot going then it handles the squiggly shot. If there are 8 or more aliens on the screen then a saucer begins its journey across the screen.

The flying saucer's direction is linked to the player's shot count. The lowest bit of the count determines which side of the screen the saucer comes from. If the saucer appears after an even number of player shots then it comes from the right. After an odd number it comes from the left. The saucer object structure is re-initialized every time the player's shot blows up. Here is the code in Object 1 (player fire):

045D: 3A 84 20 LD A,($2084) ; Is saucer ...
0460: A7 AND A ; ... on screen?
0461: C0 RET NZ ; Yes ... don't reset it
;
; Setup saucer direction for next trip
0462: 7E LD A,(HL) ; Shot counter
0463: E6 01 AND $01 ; Lowest bit set?
0465: 01 29 02 LD BC,$0229 ; Xr delta of 2 starting at Xr=29
0468: C2 6E 04 JP NZ,$046E ; Yes ... use 2/29
046B: 01 E0 FE LD BC,$FEE0 ; No ... Xr delta of -2 starting at Xr=E0
046E: 21 8A 20 LD HL,$208A ; Saucer descriptor
0471: 71 LD (HL),C ; Store Xr coordinate
0472: 23 INC HL ; Point to ...
0473: 23 INC HL ; ... delta Xr
0474: 70 LD (HL),B ; Store delta Xr
0475: C9 RET ; Done

The score for shooting the saucer ranges from 50 to 300, and the exact value depends on the number of player shots fired. The table at 0x1D54 contains 16 score values, but a bug in the code at 0x044E treats the table as having 15 values. The saucer data starts out pointing to the first entry. Every time the player's shot blows up the pointer is incremented and wraps back around. Here is the table. You have to append a trailing "0" to every value to get the three digit score.

; 208D points here to the score given when the saucer is shot. It advances ; every time the player-shot is removed. The code wraps after 15, but there

; are 16 values in this table. This is a bug in the code at 044E (thanks to
; Colin Dooley for finding this).
;
; Thus the one and only 300 comes up every 15 shots (after an initial 8).
1D54: 10 05 05 10 15 10 10 05 30 10 10 10 05 15 10 05

There are five entries of 050, eight entries of 100, two 150s, and only one 300. The 300 score comes up every 15 shots (after an initial eight). It should come up every 16, but again -- the code has a bug.

Eric Furrer discovered the pattern long ago to get 300 points for the saucer every time. The algorithm can be more easily described once you've seen the code:

At the start of every level keep a count of the shots you make as they explode -- whether they hit anything or not. Count to 8 and start over. From then on count to 15 and start over. You want the 15th shot to be the one that hits the saucer (or the first 8th if you can manage it).

## The Aliens

There are 5 rows of 11 aliens in Space Invaders. There are three types of aliens. Each type has two pictures that flip to make animation with each "step".

The lower left alien of the rack is the "reference" alien. The game keeps up with the reference alien's coordinates and all the others are drawn relative to it. Each player has a 55 byte table that tracks the living/dead state of each alien.

The end-screen interrupt draws precisely one alien each screen painting. The lower left alien moves left or right 2 pixels and the code redraws it. On the next pass (interrupt) the alien to the right of the reference moves. The wave continues each screen refresh (60 times a second) from left to right and bottom to top. Once all live aliens have been drawn the process starts again. When the rack hits the left or right side of the screen the direction reverses and the reference alien is dropped 8 pixels.

The more aliens there are on the screen the longer it takes to get back around to moving the reference alien. At the start of the round there are 55 aliens. That's 55 interrupts or almost 1 second to move the entire rack. At the end of the round there is only one alien left. It moves 2 pixels left or right 60 times a second. That's about two seconds from side to side.

The game does a nasty trick to the timing when there is one alien left. Instead of moving 2 pixels both directions the alien moves 2 pixels at a time to the left but 3 pixels at a time to the right. The last little alien is faster going right than it is going left. This changes the timing up just enough to make it difficult to lead the advancing alien with a shot.

The speed of the fleet tones does NOT match the actual speed of the alien rack. The delay-between-tones is read from a table and depends on how many aliens are left in play.

; Alien delay lists. First list is the number of aliens. The second list is the corresponding delay.

; This delay is only for the rate of change in the fleet's sound.

; The check takes the first num-aliens-value that is lower or the same as the actual num-aliens on screen.

;

; The game starts with 55 aliens. The aliens are move/drawn one per interrupt which means it

; takes 55 interrupts. The first delay value is 52 ... which is almost in sync with the number

; of aliens. It is a tad faster and you can observe the sound and steps getting out of sync.

;
1A11: 32 2B 24 1C 16 11 0D 0A 08 07 06 05 04 03 02 01

1A21: 34 2E 27 22 1C 18 15 13 10 0E 0D 0C 0B 09 07 05 1A31: FF ; ** Needless terminator. The list value "1" catches everything.

The first value in the table is a delay of 52 interrupts between sounds when there are 50 or more aliens. When there are 55 aliens the step sounds are faster than the rack. When there are 50 aliens the step sounds are slower than the rack.

When there are 43 aliens the step speed changes to 46 interrupts between changes. Again, the sounds are faster than the aliens. When there is only 1 alien left the delay minimizes to 5 interrupts between changes. Anything faster sounds unpleasing.

Even though the alien racks speeds up very smoothly as they die, the step sounds take sudden changes. If you wait a bit between killings you can hear the sudden changes -- especially at the beginning of the game when the deltas in the table are large.

The table at 1DA3 gives the starting Y (rotated) coordinates for the alien rack with each new round.

;##-AlienStartTable

; Starting Y coordinates for aliens at beginning of rounds. The first round is initialized to $78 at 07EA.

; After that this table is used for 2nd, 3rd, 4th, 5th, 6th, 7th, 8th, and 9th. The 10th starts over at

; 1DA3 (60).
1DA3: 60 1DA4: 50 1DA5: 48 1DA6: 48 1DA7: 48 1DA8: 40 1DA9: 40 1DAA: 40

The first wave starts at Y=78 (hex). The next wave starts 16 pixels (one row of the rack) lower at Y=50. Then the rack holds at 48 for three rounds and then 40 for three rounds. The value Y=40 is just above the player's shields.

Round 7 is as hard as the game gets. By that time the player's score is above 3000, which means the aliens reload their shots at the fastest rate. The aliens never start out lower than Y=40. If you can manage the game at level 7 you can play forever.

# Corrections

Thanks to Colin Dooley for correcting the comments around 1D15. He pointed out the "rolling" shot tracks the player ... not the "plunger" shot as originally commented.

Thanks to Colin Dooley for correcting the comments around the saucer-score-table at 0x1D54. He pointed out that the code at 0x044E wraps after 15 values and not 16. This brings the code in line with the guides that say the 300 value comes up every 15 shots (instead of 16).

Thanks to Glen Hewlett for correcting the comments above 0x0A93. He points out the length is in C and not B.

Thanks to Adrian Torres for pointing out that hexidecimal values in the write-up should be prefixed with '0x'. He also corrected 'RST 8' and 'RST 10' pointing out that they are really 'RST 1 (jumps to 0x0008)' and 'RST 2 (jumps to 0x0010)'.

Thanks to Elliot Roush for correcting the alien-shot-screen-deltas. The correct values are -4 (normally) and -5 (when less than 8 aliens).