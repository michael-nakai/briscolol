A set of functions that allows for high-repetition simulation of two AIs playing the card game "Briscola". Uses the Python built-in modules along with scipy, numpy, and pandas.

AIs are located in AI.py, along with necessary methods per AI class.

A quick demonstration of how to use the main simulation function can be found in `test.py`, but briefly:
* Create multiple variables, each which is assigned an AI class
* Create two lists, one which holds all AIs designated as Player 1 (goes first), and the other for all Player 2 AIs (goes second)
* Run the main pipeline with: `main_pipeline(Player_1_list, Player_2_list, Number_of_games_per_matchup)`. For reference, on a machine with 16GB of RAM and a clock speed of 3.7GHz, a 100,000 game simulation took ~10 seconds on average.
* Examine the output, available as:
    + Raw output (a record of all games played, available both as a tabulated dataset or Pythonic list)
    + Pre-analysed tabulated output (a tabulated dataset of win/loss/tie matrices, or matchup charts)
