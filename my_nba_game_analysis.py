#README: for checking the code go to main fuction in the end of the code
def analyse_nba_game(play_by_play_moves):
    #Opening a file with input data
    a = ""
    with open(play_by_play_moves, 'r') as inf:
        for line in inf:
            a += line

    # Defining home / away teams and finding corresponding NAMES of the players 
    home_names = []
    away_names = []

    #Creating a big list for raw data to work with
    b = a.split('\n')
    big_list = []
    big_list_2 = [] #creating the same list for the following actions
    for i in b:
        big_list.append(i.split('|'))
    for u in b:
        big_list_2.append(u.split('|'))

    #Searching all the names in home team and away team
    
    list_1 = ["makes 3-pt", "misses 3-pt", "makes 2-pt", "misses 2-pt", "makes free throw", "misses free throw"]
    list_2 = ["Offensive rebound by", "Defensive rebound by", "Personal foul by"]
    list_3 = ["assist by", "steal by", "block by"]
    
    x = 0
    for i in list_1:
        while x < len(big_list):
            if big_list[x][2] == big_list[0][4]:
                if i in big_list[x][7]:
                    big_list[x][7] = big_list[x][7].split(" ")
                    c = big_list[x][7][0] + " " + big_list[x][7][1]
                    if c not in home_names and c not in away_names:
                        home_names.append(c)
            elif big_list[x][2] == big_list[0][3]:
                if i in big_list[x][7]:
                    big_list[x][7] = big_list[x][7].split(" ")
                    c = big_list[x][7][0] + " " + big_list[x][7][1]
                    if c not in away_names and c not in home_names:
                        away_names.append(c)
            x += 1
    
    x1 = 0
    for i in list_2:
        while x1 < len(big_list):
            if big_list[x1][2] == big_list[0][4]:
                if i in big_list[x1][7]:
                    if i == "Personal foul by":
                        big_list[x1][7] = big_list[x1][7].split(" ")
                        c = big_list[x1][7][3] + " " + big_list[x1][7][4]
                        if c not in home_names and c not in away_names:
                            away_names.append(c)
                    else:
                        if c not in home_names and c not in away_names:
                            home_names.append(c)
            elif big_list[x1][2] == big_list[0][3]:
                if i in big_list[x1][7]:
                    if i == "Personal foul by":
                        big_list[x1][7] = big_list[x1][7].split(" ")
                        c = big_list[x1][7][3] + " " + big_list[x1][7][4]
                        if c not in away_names and c not in home_names:
                            home_names.append(c)
                    else:
                        if c not in away_names and c not in home_names:
                            away_names.append(c)
            x1 += 1
    
    x2 = 0
    for i in list_3:
        while x2 < len(big_list):
            if big_list[x2][2] == big_list[0][4]:
                if i in big_list[x2][7]:
                    if i == "assist by":
                        big_list[x2][7] = big_list[x2][7].split(" ")
                        c = big_list[x2][7][-2] + " " + big_list[x2][7][-1][:-1]
                        if c not in home_names and c not in away_names:
                            home_names.append(c)
                    else:
                        if c not in away_names and c not in home_names:
                            away_names.append(c)
            elif big_list[x2][2] == big_list[0][3]:
                if i in big_list[x2][7]:
                    if i == "assist by":
                        big_list[x2][7] = big_list[x2][7].split(" ")
                        c = big_list[x2][7][-2] + " " + big_list[x2][7][-1][:-1]
                        if c not in away_names and c not in home_names:
                            away_names.append(c)
                    else:
                        if c not in home_names and c not in away_names:
                            home_names.append(c)
            x2 += 1    

    j = 0
    while j < len(big_list):
    #home team
        if big_list[j][2] == big_list[0][4]:
            if "Team" in big_list[j][7]:
                j += 1
            elif "Turnover by" in big_list[j][7]:
                big_list[j][7] = big_list[j][7].split(" ")
                c = big_list[j][7][2] + " " + big_list[j][7][3]
                if c not in home_names and c not in away_names:
                    home_names.append(c)
        #away team
        elif big_list[j][2] == big_list[0][3]:
            if "Team" in big_list[j][7]:
                j += 1
            elif "Turnover by" in big_list[j][7]:
                big_list[j][7] = big_list[j][7].split(" ")
                c = big_list[j][7][2] + " " + big_list[j][7][3]
                if c not in away_names and c not in home_names:
                    away_names.append(c)   
        j += 1

    #creating main dictionaries for home and away teams
    import string #using this for creating the same dictionary for each of the home / away names
    dic_home = {}
    dic_away = {}
    for name in home_names:
        dic_home[name]={"player_name": name, "FG": [], "FGA": [], "FG%": [], "3P": [], "3PA": [], "3P%": [], "FT": [], "FTA": [], "FT%": [], "ORB": [], "DRB": [], "TRB": [], "AST": [], "STL": [], "BLK": [], "TOV": [], "PF": [], "PTS": []}

    for name in away_names:
        dic_away[name]={"player_name": name, "FG": [], "FGA": [], "FG%": [], "3P": [], "3PA": [], "3P%": [], "FT": [], "FTA": [], "FT%": [], "ORB": [], "DRB": [], "TRB": [], "AST": [], "STL": [], "BLK": [], "TOV": [], "PF": [], "PTS": []}

    #creating additional 2 dics for elements that are not in the table
    dic_home_additional_par = {}
    dic_away_additional_par = {}
    for name in home_names:
        dic_home_additional_par[name]={"2P": [], "m2P": [], "m3P": [], "mFT": []}

    for name in away_names:
        dic_away_additional_par[name]={"2P": [], "m2P": [], "m3P": [], "mFT": []}

    #creating additional 2 dics for totals at the bottom of the tables
    #totals of home team
    dic_home_totals = {}
    dic_away_totals = {}
    for name in home_names:
        dic_home_totals[name]={"player_name": None, "FG": None, "FGA": None, "FG%": None, "3P": None, "3PA": None, "3P%": None, "FT": None, "FTA": None, "FT%": None, "ORB": None, "DRB": None, "TRB": None, "AST": None, "STL": None, "BLK": None, "TOV": None, "PF": None, "PTS": None}

    for name in away_names:
        dic_away_totals[name]={"player_name": None, "FG": None, "FGA": None, "FG%": None, "3P": None, "3PA": None, "3P%": None, "FT": None, "FTA": None, "FT%": None, "ORB": None, "DRB": None, "TRB": None, "AST": None, "STL": None, "BLK": None, "TOV": None, "PF": None, "PTS": None}

    #final version of a dictionary   
    DATA_T = {"home_team": {"name": big_list[0][4], "players_data": {}}, "away_team": {"name": big_list[0][3], "players_data": {}}}

    #collecting all the data in the lists for convenience
    home_list = []
    away_list = []

    for name in home_names:
        home_list.append(dic_home[name])

    for name in away_names:
        away_list.append(dic_away[name])
    
    # stating and fulfilling the final dictionary        
    DATA_T = {"home_team": {"name": big_list[0][4], "players_data": home_list}, "away_team": {"name": big_list[0][3], "players_data": away_list}}

    #Analyzing the game description and deriving PRIMARY integer parameters
    e = 0
    while e < len(big_list_2):
        for i in home_names:
            if (i + " "+ "makes 3-pt") in big_list_2[e][7]:
                dic_home[i]["3P"].append(1)
        for u in away_names:
            if (u + " "+ "makes 3-pt") in big_list_2[e][7]:
                dic_away[u]["3P"].append(1)
        e += 1

    for name in home_names:
        dic_home[name]["3P"] = dic_home[name]["3P"].count(1)
    for name in away_names:
        dic_away[name]["3P"] = dic_away[name]["3P"].count(1)

    e1 = 0
    while e1 < len(big_list_2):
        for i in home_names:
            if (i + " "+ "makes free throw") in big_list_2[e1][7]:
                dic_home[i]["FT"].append(1)
        for u in away_names:
            if (u + " "+ "makes free throw") in big_list_2[e1][7]:
                dic_away[u]["FT"].append(1)
        e1 += 1

    for name in home_names:
        dic_home[name]["FT"] = dic_home[name]["FT"].count(1)
    for name in away_names:
        dic_away[name]["FT"] = dic_away[name]["FT"].count(1)
    
    e2 = 0
    while e2 < len(big_list_2):
        for i in home_names:
            if ("Offensive rebound by" + " " + i) in big_list_2[e2][7]:
                dic_home[i]["ORB"].append(1)
        for u in away_names:
            if ("Offensive rebound by" + " " + u) in big_list_2[e2][7]:
                dic_away[u]["ORB"].append(1)
        e2 += 1

    for name in home_names:
        dic_home[name]["ORB"] = dic_home[name]["ORB"].count(1)
    for name in away_names:
        dic_away[name]["ORB"] = dic_away[name]["ORB"].count(1)

    e3 = 0
    while e3 < len(big_list_2):
        for i in home_names:
            if ("Defensive rebound by" + " " + i) in big_list_2[e3][7]:
                dic_home[i]["DRB"].append(1)
        for u in away_names:
            if ("Defensive rebound by" + " " + u) in big_list_2[e3][7]:
                dic_away[u]["DRB"].append(1)
        e3 += 1

    for name in home_names:
        dic_home[name]["DRB"] = dic_home[name]["DRB"].count(1)
    for name in away_names:
        dic_away[name]["DRB"] = dic_away[name]["DRB"].count(1)

    e4 = 0
    while e4 < len(big_list_2):
        for i in home_names:
            if ("assist by" + " " + i) in big_list_2[e4][7]:
                dic_home[i]["AST"].append(1)
        for u in away_names:
            if ("assist by" + " " + u) in big_list_2[e4][7]:
                dic_away[u]["AST"].append(1)
        e4 += 1

    for name in home_names:
        dic_home[name]["AST"] = dic_home[name]["AST"].count(1)
    for name in away_names:
        dic_away[name]["AST"] = dic_away[name]["AST"].count(1)
    
    e5 = 0
    while e5 < len(big_list_2):
        for i in home_names:
            if ("steal by" + " " + i) in big_list_2[e5][7]:
                dic_home[i]["STL"].append(1)
        for u in away_names:
            if ("steal by" + " " + u) in big_list_2[e5][7]:
                dic_away[u]["STL"].append(1)
        e5 += 1

    for name in home_names:
        dic_home[name]["STL"] = dic_home[name]["STL"].count(1)
    for name in away_names:
        dic_away[name]["STL"] = dic_away[name]["STL"].count(1)
    
    e6 = 0
    while e6 < len(big_list_2):
        for i in home_names:
            if ("block by" + " " + i) in big_list_2[e6][7]:
                dic_home[i]["BLK"].append(1)
        for u in away_names:
            if ("block by" + " " + u) in big_list_2[e6][7]:
                dic_away[u]["BLK"].append(1)
        e6 += 1

    for name in home_names:
        dic_home[name]["BLK"] = dic_home[name]["BLK"].count(1)
    for name in away_names:
        dic_away[name]["BLK"] = dic_away[name]["BLK"].count(1)
    
    e7 = 0
    while e7 < len(big_list_2):
        for i in home_names:
            if ("Turnover by" + " " + i) in big_list_2[e7][7]:
                dic_home[i]["TOV"].append(1)
        for u in away_names:
            if ("Turnover by" + " " + u) in big_list_2[e7][7]:
                dic_away[u]["TOV"].append(1)
        e7 += 1

    for name in home_names:
        dic_home[name]["TOV"] = dic_home[name]["TOV"].count(1)
    for name in away_names:
        dic_away[name]["TOV"] = dic_away[name]["TOV"].count(1)
    
    e8 = 0
    while e8 < len(big_list_2):
        for i in home_names:
            if ("Personal foul by" + " " + i) in big_list_2[e8][7]:
                dic_home[i]["PF"].append(1)
        for u in away_names:
            if ("Personal foul by" + " " + u) in big_list_2[e8][7]:
                dic_away[u]["PF"].append(1)
        e8 += 1


    for name in home_names:
        dic_home[name]["PF"] = dic_home[name]["PF"].count(1)
    for name in away_names:
        dic_away[name]["PF"] = dic_away[name]["PF"].count(1)

    #creating additional dictionary for analyzing the game description and deriving PRIMARY integer parameters which are not in the main dictionary and calculating secondary integer parameters (on the basis of the primary parameters)  
    e9 = 0
    while e9 < len(big_list_2):
        for i in home_names:
            if (i + " " + "makes 2-pt") in big_list_2[e9][7]:
                dic_home_additional_par[i]["2P"].append(1)
        for u in away_names:
            if (u + " " + "makes 2-pt") in big_list_2[e9][7]:
                dic_away_additional_par[u]["2P"].append(1)
        e9 += 1


    for name in home_names:
        dic_home_additional_par[name]["2P"] = dic_home_additional_par[name]["2P"].count(1)
    for name in away_names:
        dic_away_additional_par[name]["2P"] = dic_away_additional_par[name]["2P"].count(1)
    
    e10 = 0
    while e10 < len(big_list_2):
        for i in home_names:
            if (i + " " + "misses 2-pt") in big_list_2[e10][7]:
                dic_home_additional_par[i]["m2P"].append(1)
        for u in away_names:
            if (u + " " + "misses 2-pt") in big_list_2[e10][7]:
                dic_away_additional_par[u]["m2P"].append(1)
        e10 += 1

    for name in home_names:
        dic_home_additional_par[name]["m2P"] = dic_home_additional_par[name]["m2P"].count(1)
    for name in away_names:
        dic_away_additional_par[name]["m2P"] = dic_away_additional_par[name]["m2P"].count(1)
    
    e11 = 0
    while e11 < len(big_list_2):
        for i in home_names:
            if (i + " " + "misses 3-pt") in big_list_2[e11][7]:
                dic_home_additional_par[i]["m3P"].append(1)
        for u in away_names:
            if (u + " " + "misses 3-pt") in big_list_2[e11][7]:
                dic_away_additional_par[u]["m3P"].append(1)
        e11 += 1

    for name in home_names:
        dic_home_additional_par[name]["m3P"] = dic_home_additional_par[name]["m3P"].count(1)
    for name in away_names:
        dic_away_additional_par[name]["m3P"] = dic_away_additional_par[name]["m3P"].count(1)

    e12 = 0
    while e12 < len(big_list_2):
        for i in home_names:
            if (i + " " + "misses free throw") in big_list_2[e12][7]:
                dic_home_additional_par[i]["mFT"].append(1)
        for u in away_names:
            if (u + " " + "misses free throw") in big_list_2[e12][7]:
                dic_away_additional_par[u]["mFT"].append(1)
        e12 += 1

    for name in home_names:
        dic_home_additional_par[name]["mFT"] = dic_home_additional_par[name]["mFT"].count(1)
    for name in away_names:
        dic_away_additional_par[name]["mFT"] = dic_away_additional_par[name]["mFT"].count(1)

    for name in home_names:
        dic_home[name]["FG"] = dic_home[name]["3P"] + dic_home_additional_par[name]["2P"] 
    for name in away_names:
        dic_away[name]["FG"] = dic_away[name]["3P"] + dic_away_additional_par[name]["2P"]
    
    for name in home_names:
        dic_home[name]["FGA"] = dic_home[name]["3P"] + dic_home_additional_par[name]["2P"] + dic_home_additional_par[name]["m3P"] + dic_home_additional_par[name]["m2P"]
    for name in away_names:
        dic_away[name]["FGA"] = dic_away[name]["3P"] + dic_away_additional_par[name]["2P"] + dic_away_additional_par[name]["m3P"] + dic_away_additional_par[name]["m2P"]
    
    for name in home_names:
        if dic_home[name]["FGA"] == 0:
            dic_home[name]["FG%"] = '{0:.3f}'.format(0)[1:5] #for rounding
        else: 
            dic_home[name]["FG%"] = '{0:.3f}'.format(dic_home[name]["FG"] / dic_home[name]["FGA"])
            if float(dic_home[name]["FG%"]) < 1: # if here is needed to format the results, e.g. 0.500 would be .500
                dic_home[name]["FG%"] = str(dic_home[name]["FG%"])[1:5]
    for name in away_names:
        if dic_away[name]["FGA"] == 0:
            dic_away[name]["FG%"] = '{0:.3f}'.format(0, 3)[1:5]
            if float(dic_away[name]["FG%"]) < 1:
                dic_away[name]["FG%"] = str(dic_away[name]["FG%"])[1:5]
        else:
            dic_away[name]["FG%"] = '{0:.3f}'.format(dic_away[name]["FG"] / dic_away[name]["FGA"])
            if float(dic_away[name]["FG%"]) < 1:
                dic_away[name]["FG%"] = str(dic_away[name]["FG%"])[1:5]
    for name in home_names:
        dic_home[name]["3PA"] = dic_home[name]["3P"] + dic_home_additional_par[name]["m3P"] 
    for name in away_names:
        dic_away[name]["3PA"] = dic_away[name]["3P"] + dic_away_additional_par[name]["m3P"]

    for name in home_names:
        if dic_home[name]["3PA"] == 0:
            dic_home[name]["3P%"] = '{0:.3f}'.format(0)[1:5]
        else:
            dic_home[name]["3P%"] = '{0:.3f}'.format(dic_home[name]["3P"] / dic_home[name]["3PA"])
            if float(dic_home[name]["3P%"]) < 1:
                dic_home[name]["3P%"] = str(dic_home[name]["3P%"])[1:5]
    for name in away_names:
        if dic_away[name]["3PA"] == 0:
            dic_away[name]["3P%"] = '{0:.3f}'.format(0)[1:5]
        else:
            dic_away[name]["3P%"] = '{0:.3f}'.format(dic_away[name]["3P"] / dic_away[name]["3PA"])
            if float(dic_away[name]["3P%"]) < 1:
                dic_away[name]["3P%"] = str(dic_away[name]["3P%"])[1:5]
    for name in home_names:
        dic_home[name]["FTA"] = dic_home[name]["FT"] + dic_home_additional_par[name]["mFT"] 
    for name in away_names:
        dic_away[name]["FTA"] = dic_away[name]["FT"] + dic_away_additional_par[name]["mFT"]
    
    for name in home_names:
        if dic_home[name]["FTA"] == 0:
            dic_home[name]["FT%"] = '{0:.3f}'.format(0)[1:5]
        else:
            dic_home[name]["FT%"] = '{0:.3f}'.format(dic_home[name]["FT"] / dic_home[name]["FTA"])
            if float(dic_home[name]["FT%"]) < 1:
                dic_home[name]["FT%"] = str(dic_home[name]["FT%"])[1:5]
    for name in away_names:
        if dic_away[name]["FTA"] == 0:
            dic_away[name]["FT%"] = '{0:.3f}'.format(0)[1:5]
        else:
            dic_away[name]["FT%"] = '{0:.3f}'.format(dic_away[name]["FT"] / dic_away[name]["FTA"])
            if float(dic_away[name]["FT%"]) < 1:
                dic_away[name]["FT%"] = str(dic_away[name]["FT%"])[1:5]

    for name in home_names:
        dic_home[name]["TRB"] = dic_home[name]["ORB"] + dic_home[name]["DRB"] 
    for name in away_names:
        dic_away[name]["TRB"] = dic_away[name]["ORB"] + dic_away[name]["DRB"]

    for name in home_names:
        dic_home[name]["PTS"] = dic_home[name]["3P"] * 3 + dic_home_additional_par[name]["2P"] * 2 + dic_home[name]["FT"] * 1 
    for name in away_names:
        dic_away[name]["PTS"] = dic_away[name]["3P"] * 3 + dic_away_additional_par[name]["2P"] * 2 + dic_away[name]["FT"] * 1

    return DATA_T

def print_nba_game_stats(team_dict):
    import collections #needed to sum all the values by keys of several dictionaries
    
    home_list = team_dict["home_team"]["players_data"]
    away_list = team_dict["away_team"]["players_data"]

    dic_home_totals = team_dict["home_team"]["players_data"]
    counter = collections.Counter()
    
    for d in dic_home_totals:
        counter.update(d)
    dic_home_totals_1 = dict(counter) #dic_home_totals_1

    #dic_away_totals_1
    dic_away_totals = team_dict["away_team"]["players_data"]
    counter = collections.Counter()
    for d in dic_away_totals:
        counter.update(d)
    dic_away_totals_1 = dict(counter)

    header = "Players FG FGA FG% 3P 3PA 3P% FT FTA FT% ORB DRB TRB AST STL BLK TOV PF PTS\n"
    answer_final = header

    #last line formation
    # for home table
    last_line_home = []

    last_line_home.append(dic_home_totals_1['FG'])
    last_line_home.append(dic_home_totals_1['FGA'])
    prm = dic_home_totals_1['FG'] / dic_home_totals_1['FGA']
    if prm < 1:
        prm = str(prm)[1:5]
        last_line_home.append(prm)
    else:
        last_line_home.append('{0:.3f}'.format(dic_home_totals_1['FG'] / dic_home_totals_1['FGA']))
    last_line_home.append(dic_home_totals_1['3P'])
    last_line_home.append(dic_home_totals_1['3PA'])
    prm = dic_home_totals_1['3P'] / dic_home_totals_1['3PA']
    if prm < 1:
        prm = str(prm)[1:5]
        last_line_home.append(prm)
    else:
        last_line_home.append('{0:.3f}'.format(dic_home_totals_1['3P'] / dic_home_totals_1['3PA']))
    last_line_home.append(dic_home_totals_1['FT'])
    last_line_home.append(dic_home_totals_1['FTA'])
    prm = dic_home_totals_1['FT'] / dic_home_totals_1['FTA']
    if prm < 1:
        prm = str(prm)[1:5]
        last_line_home.append(prm)
    else:
        last_line_home.append('{0:.3f}'.format(dic_home_totals_1['FT'] / dic_home_totals_1['FTA']))
    last_line_home.append(dic_home_totals_1['ORB'])
    last_line_home.append(dic_home_totals_1['DRB'])
    last_line_home.append(dic_home_totals_1['TRB'])
    last_line_home.append(dic_home_totals_1['AST'])
    last_line_home.append(dic_home_totals_1['STL'])
    last_line_home.append(dic_home_totals_1['BLK'])
    last_line_home.append(dic_home_totals_1['TOV'])
    last_line_home.append(dic_home_totals_1['PF'])
    last_line_home.append(dic_home_totals_1['PTS'])

    last_line_home_str = ""
    for i in last_line_home:
        last_line_home_str += str(i) + " "

    # similar for away table
    last_line_away = []

    last_line_away.append(dic_away_totals_1['FG'])
    last_line_away.append(dic_away_totals_1['FGA'])
    prm = dic_away_totals_1['FG'] / dic_away_totals_1['FGA']
    if prm < 1:
        prm = str(prm)[1:5]
        last_line_away.append(prm)
    else:
        last_line_away.append('{0:.3f}'.format(dic_away_totals_1['FG'] / dic_away_totals_1['FGA']))
    last_line_away.append(dic_away_totals_1['3P'])
    last_line_away.append(dic_away_totals_1['3PA'])
    prm = dic_away_totals_1['3P'] / dic_away_totals_1['3PA']
    if prm < 1:
        prm = str(prm)[1:5]
        last_line_away.append(prm)
    else:
        last_line_away.append('{0:.3f}'.format(dic_away_totals_1['3P'] / dic_away_totals_1['3PA']))
    last_line_away.append(dic_away_totals_1['FT'])
    last_line_away.append(dic_away_totals_1['FTA'])
    prm = dic_away_totals_1['FT'] / dic_away_totals_1['FTA']
    if prm < 1:
        prm = str(prm)[1:5]
        last_line_away.append(prm)
    else:
        last_line_away.append('{0:.3f}'.format(dic_away_totals_1['FT'] / dic_away_totals_1['FTA']))
    last_line_away.append(dic_away_totals_1['ORB'])
    last_line_away.append(dic_away_totals_1['DRB'])
    last_line_away.append(dic_away_totals_1['TRB'])
    last_line_away.append(dic_away_totals_1['AST'])
    last_line_away.append(dic_away_totals_1['STL'])
    last_line_away.append(dic_away_totals_1['BLK'])
    last_line_away.append(dic_away_totals_1['TOV'])
    last_line_away.append(dic_away_totals_1['PF'])
    last_line_away.append(dic_away_totals_1['PTS'])

    last_line_away_str = ""
    for i in last_line_away:
        last_line_away_str += str(i) + " "

    home_table = []
    m = 0
    while m < len(home_list):
        home_table.append(home_list[m]['player_name'])
        home_table.append(home_list[m]['FG'])
        home_table.append(home_list[m]['FGA'])
        home_table.append(home_list[m]['FG%'])
        home_table.append(home_list[m]['3P'])
        home_table.append(home_list[m]['3PA'])
        home_table.append(home_list[m]['3P%'])
        home_table.append(home_list[m]['FT'])
        home_table.append(home_list[m]['FTA'])
        home_table.append(home_list[m]['FT%'])
        home_table.append(home_list[m]['ORB'])
        home_table.append(home_list[m]['DRB'])
        home_table.append(home_list[m]['TRB'])
        home_table.append(home_list[m]['AST'])
        home_table.append(home_list[m]['STL'])
        home_table.append(home_list[m]['BLK'])
        home_table.append(home_list[m]['TOV'])
        home_table.append(home_list[m]['PF'])
        home_table.append(home_list[m]['PTS'])
        m += 1

    '''
    Printing the results for the Task 2
    '''
    
    didi = []
    i = 0
    j = 19
    while i <= len(home_table) and j <= len(home_table): #adding every 18th element to the list
        didi.append(home_table[i:j])
        i += 19
        j += 19

    gogo = []
    for i in didi:
        list_str = map(str, i) #splitting
        gogo.append(list(list_str))

    yandex = []
    for i in gogo: #connecting with space between the signs
        yandex.append(" ".join(i))

    y = 1
    while y < len(yandex): #inserting newline between each element of the list
        yandex.insert(y, '\n')
        y += 2

    answer = ""
    for i in yandex: 
        answer += i
    total_answer = answer_final + answer + '\n' + "Team Totals" + " " + last_line_home_str

    # SECOND TABLE_AWAY
    away_table = []
    m2 = 0
    while m2 < len(away_list):
        away_table.append(away_list[m2]['player_name'])
        away_table.append(away_list[m2]['FG'])
        away_table.append(away_list[m2]['FGA'])
        away_table.append(away_list[m2]['FG%'])
        away_table.append(away_list[m2]['3P'])
        away_table.append(away_list[m2]['3PA'])
        away_table.append(away_list[m2]['3P%'])
        away_table.append(away_list[m2]['FT'])
        away_table.append(away_list[m2]['FTA'])
        away_table.append(away_list[m2]['FT%'])
        away_table.append(away_list[m2]['ORB'])
        away_table.append(away_list[m2]['DRB'])
        away_table.append(away_list[m2]['TRB'])
        away_table.append(away_list[m2]['AST'])
        away_table.append(away_list[m2]['STL'])
        away_table.append(away_list[m2]['BLK'])
        away_table.append(away_list[m2]['TOV'])
        away_table.append(away_list[m2]['PF'])
        away_table.append(away_list[m2]['PTS'])
        m2 += 1

    didi2 = []
    i2 = 0
    j2 = 19
    while i2 <= len(away_table) and j2 <= len(away_table):
        didi2.append(away_table[i2:j2])
        i2 += 19
        j2 += 19

    yandex2 = []
    gogo2 = []
    for i in didi2:
        list_str2 = map(str, i)
        gogo2.append(list(list_str2))

    for i in gogo2:
        yandex2.append(" ".join(i))

    y2 = 1
    while y2 < len(yandex2):
        yandex2.insert(y2, '\n')
        y2 += 2

    answer2 = ""
    for i in yandex2:
        answer2 += i
    
    total_answer2 = answer_final + answer2 + '\n' + "Team Totals" + " " + last_line_away_str

    #printing home and away tables  
    ANSWER = total_answer + '\n' + '\n' +  total_answer2

    #Task 2 answer
    return ANSWER
    
def main():
    play_by_play_moves = "NBA_Game_1.txt"
    team_dict = analyse_nba_game(play_by_play_moves)
    table = print_nba_game_stats(team_dict)
    #print(team_dict) 
    #the above is TASK 1 check 
    print(table) # TASK 2 check
    #play_by_play_moves = "NBA_Game_2.txt"
    #the above is the second doc for checking the code    

if __name__ == "__main__":
    main()