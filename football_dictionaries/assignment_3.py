from squads_data import SQUADS_DATA
from football_dictionaries.assignment_2.py import players_as_dictionaries

def players_by_country_and_position(squads_list):
    players = players_as_dictionaries(squads_list)
    country_dict = {}   
    for player in players:
        country = player['country']
        position = player['position']
        
        # Initialize country if not present
        if country not in country_dict:
            country_dict[country] = {}
        
        # Initialize position list if not present
        if position not in country_dict[country]:
            country_dict[country][position] = []
        country_dict[country][position].append(player)
    
    return country_dict
