import game_auto, itertools, AI, analysis, os
from multiprocessing import Pool

### Helpers

def simulate_games(player1, player2, rounds_to_simulate = 1000):
    current_round = 0
    result_list = []
    while current_round != rounds_to_simulate:
        result_list.append(game_auto.briscola_auto(player1, player2))
        current_round += 1
    return result_list

def output_human_tsv(result_list, AI_name1, AI_name2):
    player1_wins = 0
    player2_wins = 0
    ties = 0
    for result in result_list:
        if result[0] == "player1":
            player1_wins += 1
        elif result[0] == "player2":
            player2_wins += 1
        else:
            ties += 1

    try:
        os.mkdir("Raw_tsvs")
    except:
        pass
    if os.name == 'nt':
        filename = "Raw_tsvs\\" + AI_name1 + "_vs_" + AI_name2 + ".tsv"
    else:
        filename = "Raw_tsvs/" + AI_name1 + "_vs_" + AI_name2 + ".tsv"

    output_file = open(filename, 'w')
    output_file.write("Game number\tWinner\tPlayer 1 Score\tPlayer 2 Score\n")
    game_number = 1
    for result in result_list:
        string_to_write = str(game_number) + "\t" + str(result[0]) + "\t" + str(result[1]) + "\t" + str(result[2]) + "\n"
        output_file.write(string_to_write)
        game_number += 1
    output_file.write("\n")
    output_file.write("Player 1 Wins:\t" + str(player1_wins) + "\n")
    output_file.write("Player 2 Wins:\t" + str(player2_wins) + "\n")
    output_file.write("Ties:\t" + str(ties))
    output_file.close()

def output_results_for_machine(result_list, AI_name1, AI_name2):

    try:
        os.mkdir("Machine_data")
    except:
        pass
    if os.name == 'nt':
        filename = "Machine_data\\" + AI_name1 + "_vs_" + AI_name2 + ".tsv"
    else:
        filename = "Machine_data/" + AI_name1 + "_vs_" + AI_name2 + ".tsv"
        
    output_file = open(filename, 'w')
    output_file.write(str(result_list))
    output_file.write("\n")
    output_file.write(AI_name1)
    output_file.write("\n")
    output_file.write(AI_name2)
    output_file.close()


### Main functions to run

def main_pipeline(AI_list1, AI_list2, rounds_per_matchup = 1000):
    AI_list_names1 = []
    AI_list_names2 = []
    for AI in AI_list1:
        AI_list_names1.append(AI.AI_name())
    for AI in AI_list2:
        AI_list_names2.append(AI.AI_name())
    print("Starting the simulation pipeline with the AIs:", ", ".join(list(set(AI_list_names1 + AI_list_names2))))

    all_possible_combinations = list(itertools.product(AI_list1, AI_list2))
    list_of_result_lists = []
    for matchup in all_possible_combinations:
        print("\nStarting to simulate " + str(matchup[0].AI_name()) + " vs " + str(matchup[1].AI_name()))
        result_list = simulate_games(matchup[0], matchup[1], rounds_per_matchup)
        print("\tFinished simulating games, now exporting...")
        output_human_tsv(result_list, matchup[0].AI_name(), matchup[1].AI_name())
        output_results_for_machine(result_list, matchup[0].AI_name(), matchup[1].AI_name())
        result_list.append(matchup[1].AI_name())
        result_list.append(matchup[0].AI_name())
        list_of_result_lists.append(result_list)
    
    print("\nFinished simulating all matchups, starting analysis")

    analysis.tabulate_results(list_of_result_lists)
    print("\n Finished analysis")
    
    




### THIS DOESN'T WORK YET
def main_pipeline_speed(AI_list1, AI_list2, rounds_per_matchup = 1000):
    AI_list_names1 = []
    AI_list_names2 = []
    for AI in AI_list1:
        AI_list_names1.append(AI.AI_name())
    for AI in AI_list2:
        AI_list_names2.append(AI.AI_name())
    print("Starting the simulation pipeline with the AIs:", ", ".join(list(set(AI_list_names1 + AI_list_names2))))

    all_possible_combinations = list(itertools.product(AI_list1, AI_list2))

    def sub_simulate(matchup_list, rounds_to_simulate):
        result_list = simulate_games(matchup_list[0], matchup_list[1], rounds_per_matchup)
        output_human_tsv(result_list, matchup_list[0].AI_name(), matchup_list[1].AI_name())
        output_results_for_machine(result_list, matchup_list[0].AI_name(), matchup_list[1].AI_name())

    pool = Pool()
    pool.starmap(sub_simulate, zip(all_possible_combinations, itertools.repeat(rounds_per_matchup)))
    pool.close()
    
    print("\n\tFinished simulating all matchups")