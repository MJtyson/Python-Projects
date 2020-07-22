from itertools import combinations
import random

team1 = ['Rory Burns', 'Dominic Sibley', 'Joe Denly', 'Zak Crawley', 'Ben Stokes (c)', 'Ollie Pope', 'Jos Buttler (wk)',
         'Dominic Bess', 'Jofra Archer', ' Mark Wood', 'James Anderson']
team2 = ['John Campbell', 'Kraigg Brathwaite', 'Shamarh Brooks', 'Shai Hope', 'Roston Chase', 'Jermaine Blackwood',
         'Shane Dowrich (wk)', 'Jason Holder (c)', 'Alzarri Joseph', 'Kemar Roach', 'Shannon Gabriel']


def generate_random_players():
    return list(combinations(team1 + team2, 11))


def display_players(team):
    return random.choice(team)


def generate_combo():
    n = 0
    teams = []
    for i in generate_random_players():
        while n < 5:
            teams.append(i)
        n += 1
    return teams


def check_combo(team):
    team1_players = 0
    team2_players = 0
    players_list = random.choice(team)

    for i in range(len(players_list)):
        print(players_list[i].strip())
        if players_list[i] in team1:
            team1_players += 1
        else:
            team2_players += 1

    return team1_players, team2_players


def get_combo_of_player(team, combo):
    team1_, team2_ = combo

    if team1_ == 6 or team2_ == 6:
        print(team)


print(generate_combo())
