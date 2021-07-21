import statistics as stats
import numpy as np
import scipy.stats as sp
import pandas as pd

### Main functions

def tabulate_results(list_of_result_lists):
    summary = []
    AI1_names = []
    AI2_names = []

    for result_list in list_of_result_lists:
        p1_wins = 0
        p2_wins = 0
        p1_points = []
        p2_points = []
        intervals = []
        ties = 0

        AI_name1 = result_list.pop()
        AI_name2 = result_list.pop()
        AI1_names.append(AI_name1)
        AI2_names.append(AI_name2)

        for game_result in result_list:
            p1_points.append(game_result[1])
            p2_points.append(game_result[2])
            intervals.append(game_result[1] - game_result[2])
            if game_result[0] == "player1":
                p1_wins += 1
            elif game_result[0] == "player2":
                p2_wins += 1
            else:
                ties += 1
        
        # Stats for one matchup
        average_p1_points = stats.mean(p1_points)
        average_p2_points = stats.mean(p2_points)
        average_interval = stats.mean(intervals)
        stdev_p1_points = stats.stdev(p1_points)
        stdev_p2_points = stats.stdev(p2_points)
        stdev_interval = stats.stdev(intervals)
        points_ttest_pvalue = round(sp.ttest_rel(p1_points, p2_points).pvalue, 6)
        p1_win_percentage = round((p1_wins / (p1_wins + p2_wins + ties)) * 100, 4)
        tie_percentage = round((ties / (p1_wins + p2_wins + ties)) * 100, 4)

        #                      0                    1                2                  3               4       
        #          5                   6                   7                8            9         10
        summary.append([average_p1_points, average_p2_points, average_interval, stdev_p1_points, stdev_p2_points, \
            stdev_interval, points_ttest_pvalue, p1_win_percentage, tie_percentage, AI_name1, AI_name2])

    # Remove duplicate AI names from each list
    AI1_names = list(dict.fromkeys(AI1_names))
    AI2_names = list(dict.fromkeys(AI2_names))

    # Empty df, x colnames are AI2_names, y rownames are AIa_names
    matchup_win_percentage_df = pd.DataFrame(index = AI1_names, columns = AI2_names)
    matchup_tie_percentage_df = pd.DataFrame(index = AI1_names, columns = AI2_names)

    # Stats for all matchups
    for matchup_stats in summary:
        matchup_win_percentage_df.at[matchup_stats[9], matchup_stats[10]] = matchup_stats[7]
        matchup_tie_percentage_df.at[matchup_stats[9], matchup_stats[10]] = matchup_stats[8]
    
    # Export each dataframe to their own csv
    matchup_win_percentage_df.to_csv("Matchup_win_percentages.csv")
    matchup_tie_percentage_df.to_csv("Matchup_tie_percentages.csv")

    # Write misc stats to a csv
    f = open("Matchup statistics.csv", "w")
    f.write("Player 1,Player 2,P1 Win %,Tie %,Avg P1 Points,Avg P2 Points,Avg Interval,Stdev P1 Points,Stdev \
        P2 Points,Stdev Interval,p-value between P1 and P2 points")
    for matchup_stats in summary:
        f.write("\n{0},{1},{2},{3},{4},{5},{6},{7},{8},{9},{10}".format( \
            matchup_stats[9], matchup_stats[10], matchup_stats[7], matchup_stats[8], matchup_stats[0], \
            matchup_stats[1], matchup_stats[2], matchup_stats[3], matchup_stats[4], matchup_stats[5], \
            matchup_stats[6]))
    f.close()