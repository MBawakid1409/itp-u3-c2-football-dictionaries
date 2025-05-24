def players_as_dictionaries(squads_list):
    result = []
    keys = [
        'number',
        'position',
        'name',
        'date_of_birth',
        'caps',
        'club',
        'country',
        'club_country',
        'year'
    ]
    
    for player in squads_list:
        player_dict = {}
        for i, value in enumerate(player):
            player_dict[keys[i]] = value
        result.append(player_dict)
    
    return result

# or with zip function

# def players_as_dictionaries(squads_list):
#     keys = [
#         'number',
#         'position',
#         'name',
#         'date_of_birth',
#         'caps',
#         'club',
#         'country',
#         'club_country',
#         'year'
#     ]
#     return [dict(zip(keys, player)) for player in squads_list]
