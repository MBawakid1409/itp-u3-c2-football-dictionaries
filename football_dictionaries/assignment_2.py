def players_by_position(squads_list):
    players = players_as_dictionaries(squads_list)
    positions_dict = {}
    for player in players:
        position = player['position']
        if position not in positions_dict:
            positions_dict[position] = []
        positions_dict[position].append(player)
    return positions_dict

players_by_position(SQUADS_DATA_DICT)
