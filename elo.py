BASE_ELO = 1600
MAX_ADJUST = 32 # tweak this to your desire


def compare_games(game1, game2):
    """
    Returns -1 if the first game happened before the 2nd, 0 if they are the same, 1 if it happened after
    The input here is our games tuple (y, w, t1, s1, t2, s2)
    :param game1:
    :param game2:
    :return:
    """
    if game1[0] == game2[0]:
        # fallback to week
        if game1[1] < game2[1]: return -1
        if game1[1] == game2[1]: return 0
        if game1[1] > game2[1]: return 1
        pass
    else:
        if game1[0] < game2[0]: return -1
        if game1[0] > game2[0]: return 1

def process_games_data():
    """
    Take the games.csv and spit the data back out into a more useful python format
    Output format will be an array of tuples of the following format (year, week, team_one, score_one, team_two, score_two)
    We will also sort the games into the correct order before spitting them back out
    :return:
    """
    TEAM_ONE_INDEX = 6
    SCORES_INDEX = 7 # this will give us both scores in the format <one>-<two>
    TEAM_TWO_INDEX = 8
    YEAR_INDEX = 0
    WEEK_INDEX = 2
    games_file = 'games.csv'
    games = [] # an empty variable to hold the game tuples
    with open(games_file) as f: # open the file
        games_data = f.readlines() # read all the games into a list so we can loop through them

    for game in games_data: # for each game in the file
        data = game.strip('"') # remove the quotaion marks on both sides
        data = data.split(' ') # split the line on all of the spaces
        year = data[YEAR_INDEX]
        week = data[WEEK_INDEX]
        team_one = data[TEAM_ONE_INDEX]
        team_two = data[TEAM_TWO_INDEX]
        scores = data[SCORES_INDEX]
        scores = scores.split('-') # split the scores data on the minues sign
        score_one = scores[0]
        score_two = scores[1]
        games.append((year, week, team_one, score_one, team_two, score_two)) # Add the data into the array

    # Now we sort the games
    games.sort(compare_games)

    return games

def get_starting_elo():
    """
    Reads in the starting elo's from a file, useful for getting the ELO info after a previous run into it with new games without having to process every game every time
    Not implemented yet, for now returns an empty dictionary
    :return:
    """
    return {}

def get_team_elo(elo, team_name):
    """
    Returns the teams elo rating, if the team doesn't exist inserts them in the dictionary and returns the base ELO
    :param elo:
    :param team_name:
    :return:
    """
    if team_name not in elo:
        elo[team_name] = BASE_ELO
    return elo[team_name]

def adjust_elo(elo, winner, loser):
    """
    Adjusts each teams value in the elo dictionary
    :param elo:
    :param winner:
    :param loser:
    :return:
    """
    k = MAX_ADJUST
    r_winner = elo[winner]
    r_loser = elo[loser]
    q_winner = pow(10.0, (r_winner/400.0))
    q_loser = pow(10.0, (r_loser/400.0))
    e_winner = q_winner / (q_winner+q_loser)
    e_loser = q_loser / (q_winner+q_loser)
    elo[winner] = r_winner + k*(1-e_winner)
    elo[loser] = r_loser + k*(0-e_loser)

elo = get_starting_elo()
games = process_games_data()
for game in games:
    team_one = game[2]
    team_two = game[4]
    team_one_elo = get_team_elo(elo, team_one)
    team_two_elo = get_team_elo(elo, team_two)
    if game[3] > game[5]:
        # Team one won
        adjust_elo(elo, winner=team_one, loser=team_two)
    elif game[3] < game[5]:
        # Team two won
        adjust_elo(elo, winner=team_two, loser=team_one)
    else:
        #a tie happened, do nothing for now
        pass

output = []
for team, score in elo.iteritems():
    team_result = "%s - %s" % (team, str(int(score)))
    output.append(team_result)
    print team_result

with open('results.txt', 'w') as f: # open the file
    f.writelines("%s\n" % l for l in output)