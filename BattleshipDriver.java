//
// Assignment 4
// Written by: Tharushan Selliah (40184870)
// For COMP 248 Section P – Fall 2020
//

//This code will simulate a game of battleship on one 8x8 grid between the user and the computer. Each side will place 6 ships and 4 grenades and take turns trying to sink the other person's ships. If a grenade is hit, then that person loses their next turn.
//This is the Driver class for the constructor class "BattleshipGrid"
//Letters A - H are columns; numbers 1 - 8 are rows for the grid

public class BattleshipDriver {

	public static void main(String[] args) {
			boolean counter_user = false; //to check if user will win
			boolean counter_bot = false; //To check if bot will win
			char [][] current_board2 = new char[8][8]; //create basic 8x8 grid
			
			BattleshipGrid grid = new BattleshipGrid(); //create class for the grid
			
			grid.createGrid(current_board2); //generate a 8x8 board filled with '_'
			
			System.out.println("Hello! Let's play BattleShip!\n");
			
			//user ships are 's'
			grid.shipCoordinates(); //Asks the user to place their ships
			
			//user grenades are 'g'
			grid.grenadeCoordinates(); //Asks the user to place their grenades
			
			//Computer's ships are 'S'
			grid.shipsBot(); //Randomly places computer's ships in an unoccupied space
			
			//Computer grenades are 'G'
			grid.grenadesBot(); //randomly places computer's grenades in an unoccupied space
			
			System.out.println("\n\n\nOK, the computer placed its ships and grenades at random. Let's play!");
			
			//print empty board filled with '_'
			grid.currentBoard(current_board2);
			
			
			//Simulates the game between user and bot. Whoever has 6 ship sunk will be declared the winner
			
			while(counter_user == false || counter_bot == false) {
				//the user will choose which coordinate to attack
				grid.userAttacks();
				//checks if the user has won the game (and appropriate message)
				counter_user = grid.checkEndResult(counter_user); //counter_user will become true once all 6 enemy ships are hit
				if (counter_user == true)
					break;
				if(counter_bot == true)
					break;
				//the bot will attack a random coordinate in the grid
				grid.botAttacks();
				//checks if the bot wins the game (and appropriate message)
				counter_bot = grid.checkEndResult(counter_bot); //counter_bot will become true once all 6 user ships are hit
				if (counter_user == true)
					break;
				if(counter_bot == true)
					break;
			}
	}
}
