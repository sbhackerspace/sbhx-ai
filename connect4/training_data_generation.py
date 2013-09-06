# Run this script to generate data to train the neural network

from game import *

# How many games to play
final_games = 2000

f = open('generated_data/game_data.csv','w')

# Keeps track of the numbers of winners
#	[ties, player1 wins, player2 wins]
winner_count = [0,0,0]

game_count = 0
while game_count < final_games:

	# Set your AIs here:

	p1 = MinimaxAI(2)
	p2 = MinimaxAI(2)
	#p2 = MinimaxNNAI(2)
	#p1 = Human()
	#p1 = RandomAI()
	#p2 = RandomAI()


	# Play the game
	g = Game(p1, p2)
	winner = g.Play()

	# Throw out games where the starting player wins
	#	In games where the starting player wins, the starting
	#	player will have one extra piece on the board. This 
	#	causes the NN to learn to favor whoever has the most 
	#	pieces, which is a useless metric. 

	if winner == g.starting_player:
		continue

	# Print the output to a file
	g.PrintToCSV(f)

	# update the counts 
	winner_count[winner] += 1
	game_count += 1
		
		
	print ("Standings: tie: ", winner_count[0], ", p1 wins:", winner_count[1], ", p2 wins: ", winner_count[2], ".", sep='')

print("Complete!")

#close the file
f.close()



