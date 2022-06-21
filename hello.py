from flask import Flask, redirect, render_template, request, flash
from flask_bootstrap import Bootstrap
from sudoku import SudokuSolver, SudokuDriver, PrintSudoku

app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'PfLGZ7kom3'

@app.route('/', methods = ["GET"])
def index():
	solvedboard = [[" " for x in range(9)] for y in range(9)]

	if (request.args.to_dict(flat=False)): # If the dictionary is not empty, i.e. if there has been input
		boardstring = ""
		for i in sorted(request.args.to_dict(flat=False)):
			if request.args.get(i) == "Solve":
				break
			elif request.args.get(i) == "":
				boardstring += "."
			else:
				boardstring += request.args.get(i)
		#print(boardstring)

		i = 0
		split_strings = [0 for x in range(9)]
		for c in range(0, 81, 9):
			newstring = boardstring[c : c + 9]
			colarray = [newstring[x] for x in range(9)]
			split_strings[i] = colarray
			i += 1
		solvable, solvedboard = SudokuSolver(split_strings)

		if not solvable:
			flash("The board is not solvable with the numbers you input. Please try again.")


	return render_template("index.html", solvedboard = solvedboard)