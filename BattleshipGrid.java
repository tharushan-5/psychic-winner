//
// Assignment 4
// Written by: Tharushan Selliah (40184870)
// For COMP 248 Section P – Fall 2020
//

//This code will simulate a game of battleship on one 8x8 grid between the user and the computer. Each side will place 6 ships and 4 grenades and take turns trying to sink the other person's ships. If a grenade is hit, then that person loses their next turn.
//This is the constructor for the driver class "BattleshipDriver"
//Letters A - H are columns; numbers 1 - 8 are rows for the grid


import java.util.Scanner;


public class BattleshipGrid {
	
	 Scanner keyin = new Scanner(System.in);
	 private char [][] board = new char[8][8];
	 private char [][] current_board = new char [8][8];
	 private int [][] grenade_board = new int [8][8];
	 private String battleship_coordinate = "";
	 private String grenade_coordinate = "";
	 private String [][] grid_position = 
		 	{{"a1","b1","c1","d1","e1","f1","g1","h1"},
			{"a2","b2","c2","d2","e2","f2","g2","h2"},
			{"a3","b3","c3","d3","e3","f3","g3","h3"},
			{"a4","b4","c4","d4","e4","f4","g4","h4"},
			{"a5","b5","c5","d5","e5","f5","g5","h5"},
			{"a6","b6","c6","d6","e6","f6","g6","h6"},
			{"a7","b7","c7","d7","e7","f7","g7","h7"},
			{"a8","b8","c8","d8","e8","f8","g8","h8"}};
	 private int ship = 0;
	 private int grenade = 0;
	 private int counter_user = 0;
	 private int counter_bot = 0;
	 private int turn_counter = 0;
	
	 
	 
	//generate the basic board filled with '_'
	public char[][] createGrid(char[][]board) {
		
		//Create starting grid 
		for(int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				board [i][j] = '_'; 	
			}
		}
		current_board = duplicate(board); //get a copy for the current board
		this.board = duplicate(board); //get a copy for the actual board
		return board;
	}
	
	//duplicate the board whenever needed so we do not have to keep creating a new board when we need a board
	public char[][] duplicate(char[][] board2) {
		char[][] theCopy = new char[board2.length][board2.length];
		for (int i = 0; i < board2.length; i++) {
			for( int j= 0; j < board2.length; j++) { 
				theCopy[i][j] = board2[i][j];
			}
		}
		return theCopy;
	}
	
	//Enter the ship coordinates of player and put on board
	public void shipCoordinates(){
		for (int i = 0; i < 6; i++) { //6 ships so this will loop 6 times total
			ship = i + 1;
			System.out.print("Enter the coordinates of ship #" + ship + ": ");
			battleship_coordinate = keyin.next();
			check_validity_ships(); //Checks if the ships are inside the quadrant or if the position was already called before
			locationShips();	
		}
	}
		
	//If the user puts an incorrect coordinate, ask the user to put in another coordinate
	public  void check_validity_ships() {
		
		
		
		//Check if coordinate was previously stated. If stated, then ask for another coordinate
		for( int i = 0; i < 8; i++)
			for(int j = 0; j < 8; j++) {
				if (grid_position[i][j].equalsIgnoreCase(battleship_coordinate)) {
					if(board[i][j] == 's') {
						System.out.println("Sorry, coordinates already in use. Try again");
						System.out.print("Enter the coordinates of ship #" + ship + ": ");	
						battleship_coordinate = keyin.next();
						i = 0;
						j = -1; //this is to reset the for loop so the program will check every coordinate again
					}
					
				}
			}
		//Check if coordinate is outside of board from user input
		while (!battleship_coordinate.equalsIgnoreCase("a1") && !battleship_coordinate.equalsIgnoreCase("a2") && !battleship_coordinate.equalsIgnoreCase("a3") && !battleship_coordinate.equalsIgnoreCase("a4") && !battleship_coordinate.equalsIgnoreCase("a5") && !battleship_coordinate.equalsIgnoreCase("a6") && !battleship_coordinate.equalsIgnoreCase("a7") && !battleship_coordinate.equalsIgnoreCase("a8") &&
				!battleship_coordinate.equalsIgnoreCase("b1") && !battleship_coordinate.equalsIgnoreCase("b2") && !battleship_coordinate.equalsIgnoreCase("b3") && !battleship_coordinate.equalsIgnoreCase("b4") && !battleship_coordinate.equalsIgnoreCase("b5") && !battleship_coordinate.equalsIgnoreCase("b6") && !battleship_coordinate.equalsIgnoreCase("b7") && !battleship_coordinate.equalsIgnoreCase("b8") &&
				!battleship_coordinate.equalsIgnoreCase("c1") && !battleship_coordinate.equalsIgnoreCase("c2") && !battleship_coordinate.equalsIgnoreCase("c3") && !battleship_coordinate.equalsIgnoreCase("c4") && !battleship_coordinate.equalsIgnoreCase("c5") && !battleship_coordinate.equalsIgnoreCase("c6") && !battleship_coordinate.equalsIgnoreCase("c7") && !battleship_coordinate.equalsIgnoreCase("c8") &&
				!battleship_coordinate.equalsIgnoreCase("d1") && !battleship_coordinate.equalsIgnoreCase("d2") && !battleship_coordinate.equalsIgnoreCase("d3") && !battleship_coordinate.equalsIgnoreCase("d4") && !battleship_coordinate.equalsIgnoreCase("d5") && !battleship_coordinate.equalsIgnoreCase("d6") && !battleship_coordinate.equalsIgnoreCase("d7") && !battleship_coordinate.equalsIgnoreCase("d8") &&
				!battleship_coordinate.equalsIgnoreCase("e1") && !battleship_coordinate.equalsIgnoreCase("e2") && !battleship_coordinate.equalsIgnoreCase("e3") && !battleship_coordinate.equalsIgnoreCase("e4") && !battleship_coordinate.equalsIgnoreCase("e5") && !battleship_coordinate.equalsIgnoreCase("e6") && !battleship_coordinate.equalsIgnoreCase("e7") && !battleship_coordinate.equalsIgnoreCase("e8") &&
				!battleship_coordinate.equalsIgnoreCase("f1") && !battleship_coordinate.equalsIgnoreCase("f2") && !battleship_coordinate.equalsIgnoreCase("f3") && !battleship_coordinate.equalsIgnoreCase("f4") && !battleship_coordinate.equalsIgnoreCase("f5") && !battleship_coordinate.equalsIgnoreCase("f6") && !battleship_coordinate.equalsIgnoreCase("f7") && !battleship_coordinate.equalsIgnoreCase("f8") &&
				!battleship_coordinate.equalsIgnoreCase("g1") && !battleship_coordinate.equalsIgnoreCase("g2") && !battleship_coordinate.equalsIgnoreCase("g3") && !battleship_coordinate.equalsIgnoreCase("g4") && !battleship_coordinate.equalsIgnoreCase("g5") && !battleship_coordinate.equalsIgnoreCase("g6") && !battleship_coordinate.equalsIgnoreCase("g7") && !battleship_coordinate.equalsIgnoreCase("g8") &&
				!battleship_coordinate.equalsIgnoreCase("h1") && !battleship_coordinate.equalsIgnoreCase("h2") && !battleship_coordinate.equalsIgnoreCase("h3") && !battleship_coordinate.equalsIgnoreCase("h4") && !battleship_coordinate.equalsIgnoreCase("h5") && !battleship_coordinate.equalsIgnoreCase("h6") && !battleship_coordinate.equalsIgnoreCase("h7") && !battleship_coordinate.equalsIgnoreCase("h8")) {
			System.out.println("Sorry, coordinates outside grid. Try again");
			System.out.print("Enter the coordinates of ship #" + ship + ": ");	
			battleship_coordinate = keyin.next();
			check_validity_ships();
		}
		
	}
	

	//Designate ship coordinates from user commands
	public  void locationShips(){

		duplicate(board); //Use this version of the board without affecting the original
		for( int i = 0; i < 8; i++)
			for(int j = 0; j < 8; j++) {
				//Assigns users coordinates of battleships to the board. The users ships are 's'
				if (grid_position[i][j].equalsIgnoreCase(battleship_coordinate)) {
					board[i][j] = 's';
				}
				
			}
	}
	
	//coordinates of grenades from user
	public void grenadeCoordinates() {
		for (int i = 0; i < 4; i++) {
			grenade = i + 1;
			System.out.print("Enter the coordinates of grenade #" + grenade + ": ");
			grenade_coordinate = keyin.next();
			check_validity_grenades(); //Checks if the grenade coordinates are inside the grid and there is not already assigned
			locationGrenades(); //places the grenades onto the grid
			
		}
	}
	
	//If the user puts an incorrect coordinate, ask the user to put in another coordinate
	public  void check_validity_grenades() {
		//Check if coordinate was previously stated. If stated, then ask for another coordinate
		for( int i = 0; i < 8; i++)
			for(int j = 0; j < 8; j++) {
				if (grid_position[i][j].equalsIgnoreCase(grenade_coordinate)) {
					if(board[i][j] == 's' || board[i][j] == 'g') { //if the position called already has a ship or grenade on the grid, then call another coordinate
						System.out.println("Sorry, coordinates already in use. Try again");
						System.out.print("Enter the coordinates of grenade #" + grenade + ": ");	
						grenade_coordinate = keyin.next();
						i = 0;
						j = -1; //Reset the for loop to check every coordinate again
					}
					
				}
			}
		//Check if coordinate is outside of board from user input
		while (!grenade_coordinate.equalsIgnoreCase("a1") && !grenade_coordinate.equalsIgnoreCase("a2") && !grenade_coordinate.equalsIgnoreCase("a3") && !grenade_coordinate.equalsIgnoreCase("a4") && !grenade_coordinate.equalsIgnoreCase("a5") && !grenade_coordinate.equalsIgnoreCase("a6") && !grenade_coordinate.equalsIgnoreCase("a7") && !grenade_coordinate.equalsIgnoreCase("a8") &&
				!grenade_coordinate.equalsIgnoreCase("b1") && !grenade_coordinate.equalsIgnoreCase("b2") && !grenade_coordinate.equalsIgnoreCase("b3") && !grenade_coordinate.equalsIgnoreCase("b4") && !grenade_coordinate.equalsIgnoreCase("b5") && !grenade_coordinate.equalsIgnoreCase("b6") && !grenade_coordinate.equalsIgnoreCase("b7") && !grenade_coordinate.equalsIgnoreCase("b8") &&
				!grenade_coordinate.equalsIgnoreCase("c1") && !grenade_coordinate.equalsIgnoreCase("c2") && !grenade_coordinate.equalsIgnoreCase("c3") && !grenade_coordinate.equalsIgnoreCase("c4") && !grenade_coordinate.equalsIgnoreCase("c5") && !grenade_coordinate.equalsIgnoreCase("c6") && !grenade_coordinate.equalsIgnoreCase("c7") && !grenade_coordinate.equalsIgnoreCase("c8") &&
				!grenade_coordinate.equalsIgnoreCase("d1") && !grenade_coordinate.equalsIgnoreCase("d2") && !grenade_coordinate.equalsIgnoreCase("d3") && !grenade_coordinate.equalsIgnoreCase("d4") && !grenade_coordinate.equalsIgnoreCase("d5") && !grenade_coordinate.equalsIgnoreCase("d6") && !grenade_coordinate.equalsIgnoreCase("d7") && !grenade_coordinate.equalsIgnoreCase("d8") &&
				!grenade_coordinate.equalsIgnoreCase("e1") && !grenade_coordinate.equalsIgnoreCase("e2") && !grenade_coordinate.equalsIgnoreCase("e3") && !grenade_coordinate.equalsIgnoreCase("e4") && !grenade_coordinate.equalsIgnoreCase("e5") && !grenade_coordinate.equalsIgnoreCase("e6") && !grenade_coordinate.equalsIgnoreCase("e7") && !grenade_coordinate.equalsIgnoreCase("e8") &&
				!grenade_coordinate.equalsIgnoreCase("f1") && !grenade_coordinate.equalsIgnoreCase("f2") && !grenade_coordinate.equalsIgnoreCase("f3") && !grenade_coordinate.equalsIgnoreCase("f4") && !grenade_coordinate.equalsIgnoreCase("f5") && !grenade_coordinate.equalsIgnoreCase("f6") && !grenade_coordinate.equalsIgnoreCase("f7") && !grenade_coordinate.equalsIgnoreCase("f8") &&
				!grenade_coordinate.equalsIgnoreCase("g1") && !grenade_coordinate.equalsIgnoreCase("g2") && !grenade_coordinate.equalsIgnoreCase("g3") && !grenade_coordinate.equalsIgnoreCase("g4") && !grenade_coordinate.equalsIgnoreCase("g5") && !grenade_coordinate.equalsIgnoreCase("g6") && !grenade_coordinate.equalsIgnoreCase("g7") && !grenade_coordinate.equalsIgnoreCase("g8") &&
				!grenade_coordinate.equalsIgnoreCase("h1") && !grenade_coordinate.equalsIgnoreCase("h2") && !grenade_coordinate.equalsIgnoreCase("h3") && !grenade_coordinate.equalsIgnoreCase("h4") && !grenade_coordinate.equalsIgnoreCase("h5") && !grenade_coordinate.equalsIgnoreCase("h6") && !grenade_coordinate.equalsIgnoreCase("h7") && !grenade_coordinate.equalsIgnoreCase("h8")) {
			System.out.println("Sorry, coordinates outside grid. Try again");
			System.out.print("Enter the coordinates of grenade #" + grenade + ": ");	
			grenade_coordinate = keyin.next();
			check_validity_grenades(); //check the same method again to see if new coordinate has already been called or not
		}
		
	}
	
	//Places the grenades onto the map if it is a valid coordinate
	public  void locationGrenades() {
		duplicate(board);
		for( int i = 0; i < 8; i++)
			for(int j = 0; j < 8; j++) {
				//Assigns users coordinates of grenades to the board, denoted as 'g'
				if (grid_position[i][j].equalsIgnoreCase(grenade_coordinate)) {
					board[i][j] = 'g';
				}	
			}
	}
	
	
	//Print the current version of the board with added inputs from user and from computer. This will be used during the attacking portion of the user and the bot
	public  char [][] currentBoard(char [][] current_board){
		for(int i = 0; i < 8; i++) {
			for (int j = 0; j < 8; j++) {
				System.out.print(current_board[i][j] + " ");
			}
				System.out.println();	
		}
		return current_board;
	}
	
	
	//Assign random ship coordinate for computer
	public  void shipsBot(){
		//Generates a random number generated between [0,8), then take the floor of that and use that as an index. 
		duplicate(board);
		int random_num1 = 9;
		int random_num2 = 9;
		for(int i = 0; i < 6; i++) {
			//since the Math.random() method * 10 will create an int between 0 to 9, we do not want 8 or 9 so we have to keep generating random ints that is not 8 or 9. We also do not want the coordinate to already be called by a previous coordinate
			while(random_num1 == 8 || random_num1 == 9 || random_num2 == 8 || random_num2 == 9 || board[random_num1][random_num2] == 's' || board[random_num1][random_num2] == 'g' || board[random_num1][random_num2] == 'S') {
				random_num1 = (int) (Math.random() * 10);
				random_num2 = (int) (Math.random() * 10);
			}
		
			board[random_num1][random_num2] = 'S'; //the bot's ships are denoted by 'S'
		}
	}
	
	//Assign random grenade coordinate for computer
	public  void grenadesBot() {
		//lets have a random number generated between [0,8), then take the floor of that and use that as an index
		duplicate(board);
		int random_num1 = 9;
		int random_num2 = 9;
		for(int i = 0; i < 4; i++) {
			//This is because the Math.random() method * 10 will create an int between 0 to 9. We do not want 8 or 9 so we have to keep generating random ints that is not 8 or 9
			while(random_num1 == 8 || random_num1 == 9 || random_num2 == 8 || random_num2 == 9 || board[random_num1][random_num2] == 's' || board[random_num1][random_num2] == 'g' || board[random_num1][random_num2] == 'S' || board[random_num1][random_num2] == 'G') {
				random_num1 = (int) (Math.random() * 10);
				random_num2 = (int) (Math.random() * 10);
			}
			board[random_num1][random_num2] = 'G';
		}
	
	}
	
	//This method will cause the user to attack
	//Take in input from users to attack enemy ships and display on the board
	public  void userAttacks() {
		System.out.print("\nPosition of your rocket: ");
		String rocket_coordinate = keyin.next();
		
		//check if it is a valid coordinate and ask again if it is invalid
		while (!rocket_coordinate.equalsIgnoreCase("a1") && !rocket_coordinate.equalsIgnoreCase("a2") && !rocket_coordinate.equalsIgnoreCase("a3") && !rocket_coordinate.equalsIgnoreCase("a4") && !rocket_coordinate.equalsIgnoreCase("a5") && !rocket_coordinate.equalsIgnoreCase("a6") && !rocket_coordinate.equalsIgnoreCase("a7") && !rocket_coordinate.equalsIgnoreCase("a8") &&
				!rocket_coordinate.equalsIgnoreCase("b1") && !rocket_coordinate.equalsIgnoreCase("b2") && !rocket_coordinate.equalsIgnoreCase("b3") && !rocket_coordinate.equalsIgnoreCase("b4") && !rocket_coordinate.equalsIgnoreCase("b5") && !rocket_coordinate.equalsIgnoreCase("b6") && !rocket_coordinate.equalsIgnoreCase("b7") && !rocket_coordinate.equalsIgnoreCase("b8") &&
				!rocket_coordinate.equalsIgnoreCase("c1") && !rocket_coordinate.equalsIgnoreCase("c2") && !rocket_coordinate.equalsIgnoreCase("c3") && !rocket_coordinate.equalsIgnoreCase("c4") && !rocket_coordinate.equalsIgnoreCase("c5") && !rocket_coordinate.equalsIgnoreCase("c6") && !rocket_coordinate.equalsIgnoreCase("c7") && !rocket_coordinate.equalsIgnoreCase("c8") &&
				!rocket_coordinate.equalsIgnoreCase("d1") && !rocket_coordinate.equalsIgnoreCase("d2") && !rocket_coordinate.equalsIgnoreCase("d3") && !rocket_coordinate.equalsIgnoreCase("d4") && !rocket_coordinate.equalsIgnoreCase("d5") && !rocket_coordinate.equalsIgnoreCase("d6") && !rocket_coordinate.equalsIgnoreCase("d7") && !rocket_coordinate.equalsIgnoreCase("d8") &&
				!rocket_coordinate.equalsIgnoreCase("e1") && !rocket_coordinate.equalsIgnoreCase("e2") && !rocket_coordinate.equalsIgnoreCase("e3") && !rocket_coordinate.equalsIgnoreCase("e4") && !rocket_coordinate.equalsIgnoreCase("e5") && !rocket_coordinate.equalsIgnoreCase("e6") && !rocket_coordinate.equalsIgnoreCase("e7") && !rocket_coordinate.equalsIgnoreCase("e8") &&
				!rocket_coordinate.equalsIgnoreCase("f1") && !rocket_coordinate.equalsIgnoreCase("f2") && !rocket_coordinate.equalsIgnoreCase("f3") && !rocket_coordinate.equalsIgnoreCase("f4") && !rocket_coordinate.equalsIgnoreCase("f5") && !rocket_coordinate.equalsIgnoreCase("f6") && !rocket_coordinate.equalsIgnoreCase("f7") && !rocket_coordinate.equalsIgnoreCase("f8") &&
				!rocket_coordinate.equalsIgnoreCase("g1") && !rocket_coordinate.equalsIgnoreCase("g2") && !rocket_coordinate.equalsIgnoreCase("g3") && !rocket_coordinate.equalsIgnoreCase("g4") && !rocket_coordinate.equalsIgnoreCase("g5") && !rocket_coordinate.equalsIgnoreCase("g6") && !rocket_coordinate.equalsIgnoreCase("g7") && !rocket_coordinate.equalsIgnoreCase("g8") &&
				!rocket_coordinate.equalsIgnoreCase("h1") && !rocket_coordinate.equalsIgnoreCase("h2") && !rocket_coordinate.equalsIgnoreCase("h3") && !rocket_coordinate.equalsIgnoreCase("h4") && !rocket_coordinate.equalsIgnoreCase("h5") && !rocket_coordinate.equalsIgnoreCase("h6") && !rocket_coordinate.equalsIgnoreCase("h7") && !rocket_coordinate.equalsIgnoreCase("h8")) {
			System.out.println("Sorry, coordinates outside grid. Try again");
			System.out.print("Position of your rocket: ");	
			rocket_coordinate = keyin.next();
		}
		
		
		//Display correct board and message after an attack is made
		for (int i = 0; i < 8; i++)
			for (int j = 0; j < 8; j++) 
				if(grid_position[i][j].equalsIgnoreCase(rocket_coordinate)) { //checks the coordinate of the board that the user inputted
					
					//when the user hits the enemy ship
					if(board[i][j] == 'S') {
						if(current_board[i][j] == 'S'){ //if the position was called already, the board is unchanged
							System.out.println("Position already called.");
						}
						else {
							current_board[i][j] = 'S'; //if the position was not previously called, change the board accordingly with the coordinate equals 'S'
							System.out.println("Ship hit!");
						}
						currentBoard(current_board);
					}
					
					//when you hit enemy grenade, lose a turn
					else if(board[i][j] == 'G') {
						if(current_board[i][j] == 'G') { //if the position was called already, the board is unchanged
								System.out.println("Position already called.");
								currentBoard(current_board);
							}
						
						else {
							current_board[i][j] = 'G'; //if the position was not previously called, change the board accordingly with the coordinate equals 'G'
						
							if(current_board[i][j] == 'G') {
								
								if(grenade_board[i][j] >= 1) { //if the grenade was already hit before, the player will not lose a turn again
									System.out.println("grenade has already been hit");
									currentBoard(current_board);
									continue; //escape the current iteration of the for loop and move on with the game
								}
								turn_counter = 0;
								turn_counter++;
								grenade_board[i][j] = turn_counter;
								if(grenade_board[i][j] == 1) { //the player will lose a turn (the bot will have their turn)
									System.out.println("BOOM! Grenade!");
									currentBoard(current_board);
									botAttacks(); //The bot will attack
								}
							}
						}
						
					}
					//hitting own grenade
					else if(board[i][j] == 'g') {
						if(current_board[i][j] == 'g'){ //if the position was called already, the board is unchanged
							System.out.println("Position already called.");
						}
						else {
							current_board[i][j] = 'g'; //if the position was not previously called, change the board accordingly with the coordinate equals 'g'
							System.out.println("You hit your own grenade");
						}
						currentBoard(current_board);
					}
					
					//hitting own ship
					else if(board[i][j] == 's') {
						if(current_board[i][j] == 's'){ //if the position was called already, the board is unchanged
							System.out.println("Position already called.");
						}
						else {
							current_board[i][j] = 's'; //if the position was not previously called, change the board accordingly with the coordinate equals 's'
							System.out.println("You sank a friendly ship");
							}
						currentBoard(current_board);
					}
					
					//hitting blank spot
					else if(board[i][j] == '_') {
						if(current_board[i][j] == '*') { //if the position was called already, the board is unchanged
							System.out.println("Position already called.");
							currentBoard(current_board);
						}
						else {
							current_board[i][j] = '*'; //if the position was not previously called, change the board accordingly with the coordinate equals '*'
							System.out.println("Nothing");
							currentBoard(current_board);
						}
					}	
				}
			}
		
	
	
	
	//Computer will randomly attack one of your ships
	public  void botAttacks() {
		//Generate a random int between 0 and 7
		int random_num1 = 9;
		int random_num2 = 9;
		//This is because the Math.random() method * 10 will create an int between 0 to 9. We do not want 8 or 9 so we have to keep generating random ints that is not 8 or 9
		while(random_num1 == 8 || random_num1 == 9 || random_num2 == 8 || random_num2 == 9 || board[random_num1][random_num2] == 'S' || board[random_num1][random_num2] == 'G') { //The bot will not accidently shoot their own ship and grenade
			random_num1 = (int) (Math.random() * 10);
			random_num2 = (int) (Math.random() * 10);
		}
		//Display message for bot attack
		System.out.print("\nPosition of my rocket: " + grid_position[random_num1][random_num2] + "\n");
		//Display correct board and message after the bot did their attack
		for (int i = 0; i < 8; i++)
			for (int j = 0; j < 8; j++) {
				if(i == random_num1 && j == random_num2)	
					
					//if hit enemy ship
					if(board[i][j] == 's') {
						if(current_board[i][j] == 's') //if the position was called already, the board is unchanged
							System.out.println("Position already called.");
						else {
							current_board[i][j] = 's'; //if the position was not previously called, change the board accordingly with the coordinate equals 's'
							System.out.println("Ship hit!");
						}
						currentBoard(current_board);
					}
					//if hit enemy grenade, lose a turn
					else if(board[i][j] == 'g') {
						//if the position was called already
						if(current_board[i][j] == 's')
							System.out.println("Position already called.");
						else { 
							current_board[i][j] = 'g'; //if the position was not previously called, change the board accordingly with the coordinate equals 'g'
							
							if(current_board[i][j] == 'g') { //check if the grenade was already called or not
								if(grenade_board[i][j] >= 1) {
									System.out.println("grenade has already been hit");
									currentBoard(current_board);
									continue;
								}
								//If the grenade was not previously called, the bot will lose their next turn and so the user can attack twice in a row
								turn_counter = 0;
								turn_counter++;
								grenade_board[i][j] = turn_counter;
								if(grenade_board[i][j] == 1) {
									System.out.println("BOOM! Grenade!");
									currentBoard(current_board);
									userAttacks();
								}
							}
						}
					}
				//This code is commented out as the computer will not hit their own ships or grenades. However, if this mechanic woould be introduced, this piece of code can be added but would need to change the while condition on line 348
				/*
				//if hit own grenade
					else if(board[i][j] == 'G') {
						//if the position was called already
						if(current_board[i][j] == 'G')
							System.out.println("Position already called.");
						else {
							current_board[i][j] = 'G';
							System.out.println("You hit your own grenade");
						}
						currentBoard(current_board);
					}
				//if hit own ship
					else if(board[i][j] == 'S') {
						//if the position was called already
						if(current_board[i][j] == 'S')
							System.out.println("Position already called.");
						else {
							current_board[i][j] = 'S';
							System.out.println("You sank a friendly ship");
						}
						currentBoard(current_board);
					}
					
					*/
				
				//if hit nothing
					else if(board[i][j] == '_') {
						if(current_board[i][j] == '*') { //if the position was called already, the board is unchanged
							System.out.println("Position already called.");
							currentBoard(current_board);
						}
						else {
							current_board[i][j] = '*'; //if the position was not previously called, change the board accordingly with the coordinate equals '*'
							System.out.println("Nothing");
							currentBoard(current_board);
						}
					}
			}
	}
	

	
	
	//Check end result and declare the winner of the game
	//Include two counters, one for each user. When one counter reaches 6, the game is done. Once all 6 ships have been counted for on either side, the boolean becomes true and will break the while loop in the driver class
	public boolean checkEndResult(boolean lose_win) {
		lose_win = false;
		counter_user = 0;
		counter_bot = 0;
		
		for (int i = 0; i < 8; i++)
			for(int j = 0; j < 8; j++) {
				if (current_board[i][j] == 'S') {
					counter_user++; //Increase the counter depending on how many bot ships were destroyed
				}
				if(current_board[i][j] == 's') {
					counter_bot++; //Increase the counter depending on how many user ships were destroyed
				}
				
			}
		
		//if the user sinks 6 ships you win
		if (counter_user == 6) {
			System.out.println("\n\n\nYOU WIN!!\n");
			lose_win = true;
			currentBoard(board);	
		}
		//if the comp sinks 6 ship they win
		if(counter_bot == 6) {
			System.out.println("\n\n\nYou lose!\n");
			lose_win = true;
			currentBoard(board);
		}
		return lose_win;
	}	
}

