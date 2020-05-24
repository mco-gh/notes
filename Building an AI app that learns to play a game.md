Building an AI app that learns to play a game

# Building an AI app that learns to play a game

![robot-3010309_640-e1515439507681.jpg](../_resources/081b9e21182ee888d94988f1ec7f966f.jpg)

Tic Tac Toe is a very simple game for you to program a computer to play. You can write code that tells it to go in the center square if it’s available, look if the opponent has 2 in a row and block it if so, or go to a corner if one is available, making 2 in a row yourself etc.

But that’s not how YOU learned to play. Someone put a grid in front of you and started putting X’s and O’s on it. After a while you *figured out* the strategy for yourself.

So how do we make a computer emulate a human in doing this? One thing computers are very good at is remembering things, so why not create an app where the computer *remembers* how it lost a game of tic tac toe, and then *avoids* doing the same thing again.

How would that work? First of all, consider the game board — it has 9 cells, each of which has 3 states: Empty, O and X. That can be represented by a 9-digit Base-3 number. So, for example, an empty board is 000000000, and a board with an X in the middle (giving X the value 2) is 000020000 etc. This can easily be converted into an integer, and that integer can be the key in a hashmap. So, when the computer loses a game, it can look at what the board was like when it did its last move, evaluate that, and set a value in a hashmap. In future, before doing a move, it can look at what the state of the board would be if it did a particular move, and if it is present in the hashmap, it would know that it lost the game last time it did that, so this time it should do something else.

Using this methodology, *and no other strategy*, it’s possible to build an app that quickly learns how to play tic tac toe. Not only that, when you’re done, the hashmap is easily transportable — i.e. the ‘memory’ of how to play a game can be given to another computer, and it would then instantly know how to play the game. This algorithm is so naive that it will simply move in the first available space. At first it will lose — a lot — but over time it will build up a memory of where it failed, and follow an avoidance strategy. You’ll see that it very quickly learns how to play tic tac toe to a tie, just like a human would.

Here’s the game in action — watch as I take X, and the computer is O. It will always naively go to the first available position *unless* that position has previously ended in a loss. When I start in the center, then always go to the right, I continually beat the computer until it figures out what it was doing wrong, and then forces me into a tie. As I change my strategy, the computer learns:

The learning code that allows for this is incredibly simple. Here’s a snippet, showing where the computer evaluates the board, and then rewinds the human move that led to the losing state, storing the board state in the hashmap:

public void learnFromLosing(){
int losingPosition = calcBoardValue();
losingPosition-= HUMAN_VALUE * Math.pow(3, lastHumanMove);
losingGamePositions.put(losingPosition, true);
}
public int calcBoardValue(){
int boardValue = 0;
for(int nIndex=0; nIndex<9; nIndex++){
boardValue += boardValues[nIndex] * Math.pow(3, nIndex);
}
return boardValue;
}

The boardValues[] array simply holds 0,1,2 for empty, O and X, so calcBoardValue converts this into an integer by looping over them and multiplying them by 3^ their index — effectively converting the board to an integer. In learnFromLosing, the value of the last human move is subtracted from this to put the board back to the pre-loss state, and the losing position is then stored in the hashmap of losingGamePositions.

When it’s the computer’s turn to move, it loops through the board until it finds an empty position (that’s the naive part!) and then calls ‘isOKToMove’, which, if it returns true, will have the computer move to that position.

boolean computer_moved=false;
for(int nIndex=0; nIndex<9; nIndex++){
if(boardValues[nIndex]==EMPTY_VALUE){
if(isOKToMove(nIndex)){
boardValues[nIndex]=COMPUTER_VALUE;
computer_moved=true;
totalMoves++;
drawBoard();
break;
}
}
}

The isOKToMove function then takes a look at the board if the computer does this move, and checks if that board position is in the hashmap of losing positions. If it is, then it is not OK to move. If it isn’t, then the computer will do this move:

public boolean isOKToMove(int thisIndex){
int boardValue = calcBoardValue();
boardValue+=COMPUTER_VALUE * Math.pow(3, thisIndex);
if(losingGamePositions.containsKey(boardValue)){
return false;
} else {
return true;
}
}

And that’s pretty much it! For your convenience, here’s the source code for a complete Android activity that implements this code (and it’s that Android app that you see in the above video)

Next steps and food for thought:

1. How about extending the app so that a ‘false’ value in the hashmap indicates a loss for a board position, and a ‘true’ indicates a victory. That way instead of avoiding defeat by memory, the computer could also remember ways that it won previously, thus learning more quickly

2. How about serializing the results of the hashmap out, maybe to Firebase, and then initializing the app with those results, thus having a memory dump from one app to another?

3. How would you extend this concept to a more sophisticated game like Chess?
import android.content.DialogInterface;
import android.support.v7.app.AlertDialog;
import android.support.v7.app.AppCompatActivity;
import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import java.util.HashMap;

public class MainActivity extends AppCompatActivity implements View.OnClickListener{

int[] buttonIDs = new int[] {R.id.btn1, R.id.btn2, R.id.btn3, R.id.btn4, R.id.btn5, R.id.btn6, R.id.btn7, R.id.btn8, R.id.btn9};

Button[] buttons = new Button[9];
int[] boardValues = new int[9];
int lastHumanMove=0;
int totalMoves=0;
public static final int EMPTY_VALUE=0;
public static final int COMPUTER_VALUE=1;
public static final int HUMAN_VALUE=2;
public static final String COMPUTER_CHARACTER="O";
public static final String HUMAN_CHARACTER="X";
public static final String EMPTY_CHARACTER="";
public static final String NOBODY="NOBODY";
HashMap<Integer, Boolean> losingGamePositions = new HashMap<>();
@Override
protected void onCreate(Bundle savedInstanceState) {
super.onCreate(savedInstanceState);
setContentView(R.layout.activity_main);
final Button tmpButton;
for(int nIndex=0; nIndex<9; nIndex++) {
buttons[nIndex] = (Button) findViewById(buttonIDs[nIndex]);
buttons[nIndex].setOnClickListener(this);
}
drawBoard();
}
@Override
public void onClick(View v){
if(v instanceof Button){
Button thisButton = (Button) v;
int index = Integer.parseInt(thisButton.getTag().toString());
if(boardValues[index]==EMPTY_VALUE){
boardValues[index]=HUMAN_VALUE;
lastHumanMove=index;
drawBoard();
totalMoves++;
if(checkWinner(HUMAN_VALUE)){
learnFromLosing();
showWinner(HUMAN_CHARACTER);
} else {
if(totalMoves==9)
{
showWinner(NOBODY);
} else {
doComputerTurn();
}
}
}
}
}
public void showWinner(String playerID){
AlertDialog alertDialog = new AlertDialog.Builder(MainActivity.this).create();
alertDialog.setTitle("Game Over");
if(playerID==NOBODY){
alertDialog.setMessage("It's a tie!");
} else {
alertDialog.setMessage("The Winner is " + playerID);
}
alertDialog.setButton(AlertDialog.BUTTON_NEUTRAL, "OK",
new DialogInterface.OnClickListener() {
public void onClick(DialogInterface dialog, int which) {
dialog.dismiss();
for(int nIndex=0; nIndex<9; nIndex++){
buttons[nIndex].setText(EMPTY_CHARACTER);
boardValues[nIndex]=EMPTY_VALUE;
totalMoves=0;
}
}
});
alertDialog.show();
}
public boolean checkWinner(int playerID){

if((boardValues[0]==playerID && boardValues[1]==playerID && boardValues[2]==playerID) ||

(boardValues[0]==playerID && boardValues[3]==playerID && boardValues[6]==playerID) ||

(boardValues[0]==playerID && boardValues[4]==playerID && boardValues[8]==playerID) ||

(boardValues[1]==playerID && boardValues[4]==playerID && boardValues[7]==playerID) ||

(boardValues[2]==playerID && boardValues[4]==playerID && boardValues[6]==playerID) ||

(boardValues[2]==playerID && boardValues[5]==playerID && boardValues[8]==playerID) ||

(boardValues[3]==playerID && boardValues[4]==playerID && boardValues[5]==playerID) ||

(boardValues[6]==playerID && boardValues[7]==playerID && boardValues[8]==playerID))

return true;
else
return false;
}
public void doComputerTurn(){
boolean computer_moved=false;
for(int nIndex=0; nIndex<9; nIndex++){
if(boardValues[nIndex]==EMPTY_VALUE){
if(isOKToMove(nIndex)){
boardValues[nIndex]=COMPUTER_VALUE;
computer_moved=true;
totalMoves++;
drawBoard();
break;
}
}
}
if (checkWinner(COMPUTER_VALUE)) {
showWinner(COMPUTER_CHARACTER);
} else {
if(!computer_moved) {
// There are no moves, so let's flag this as a bad board position
learnFromLosing();
// Just do any move, and lose
for(int nIndex=0; nIndex<9; nIndex++){
if(boardValues[nIndex]==EMPTY_VALUE){
boardValues[nIndex]=COMPUTER_VALUE;
computer_moved=true;
drawBoard();
break;
}
}
}
}
}
public boolean isOKToMove(int thisIndex){
int boardValue = calcBoardValue();
boardValue+=COMPUTER_VALUE * Math.pow(3, thisIndex);
if(losingGamePositions.containsKey(boardValue)){
return false;
} else {
return true;
}
}
public void learnFromLosing(){
int losingPosition = calcBoardValue();
losingPosition-= HUMAN_VALUE * Math.pow(3, lastHumanMove);
losingGamePositions.put(losingPosition, true);
}
public int calcBoardValue(){
int boardValue = 0;
for(int nIndex=0; nIndex<9; nIndex++){
boardValue += boardValues[nIndex] * Math.pow(3,nIndex);
}
return boardValue;
}
public void drawBoard(){
for(int nIndex=0; nIndex<9; nIndex++){
switch(boardValues[nIndex]){
case HUMAN_VALUE:
buttons[nIndex].setText(HUMAN_CHARACTER);
break;
case COMPUTER_VALUE:
buttons[nIndex].setText(COMPUTER_CHARACTER);
break;
default:
buttons[nIndex].setText(EMPTY_CHARACTER);
}
}
}
}

(Image is CC0 on Pixabay: https://pixabay.com/en/robot-woman-face-cry-sad-3010309/)