import csv 
from utility import uprint

def extract_stat_names(dict_of_stats):
    stat_names = []
    for key, val in dict_of_stats.items():
        stat_names += [key]
    return stat_names

def parse_players(list_of_players):
    stat_names = extract_stat_names(list_of_players[0])
    f = open('data/players_raw.csv', 'w', encoding='utf8', newline='')
    w = csv.DictWriter(f, sorted(stat_names))
    w.writeheader()
    for player in list_of_players:
            w.writerow({k:str(v).encode('utf-8').decode('utf-8') for k, v in player.items()})
