from edit_grid import hero_grid

# print(help(hero_grid()))

# remove above # for documentation on how to edit this file


a = hero_grid('D:/Games/Steam',443187988)
#                   ^               ^
#        steam location here   dota2 id here


#important: you can add parentheses before a.collect_data() so you dont have to collect data everytime you launch, collecting data takes times
a.collect_data()


a.execute_defaults()

print('executed successfully')

## The Above function is the same as these functions below. Combined

# a.role_grid('Rolegrid','winrate','all')   
# a.role_grid('Rolegrid: SORTED BY MATCH PLAYED','personal_match_played','played')

# a.create_hero_grid('ALL_HEROES_SORTED_BY_WINRATE','winrate','all')
# a.create_hero_grid('YOUR HEROES SORTED_BY_WINRATE','winrate','played')
