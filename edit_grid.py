import json,sys
import _USER_DATA
import pandas as pd
print(_USER_DATA.dota2_account_id)



favorite_heroes = [1]
all_heroes = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 119, 120, 121, 123, 126, 128, 129]
def create_hero_grid(grid_name,sort_by):
  with open(_USER_DATA.dota2_account_id + "/hero_grid_config.json") as json_file,open('heroes_data.csv','r') as hero_json:
      pos = False
      data = json.load(json_file)
      df = pd.read_csv(hero_json)
      for i,x in zip(data['configs'],range(1000)):
        if i['config_name'] == grid_name:
          pos = x
          break
        else:
          continue
      if pos == False:
        data['configs'].append({"config_name":grid_name,'categories':[]})
        pos = -1
          

      it = -1
      data['configs'][pos] = {'config_name':grid_name,'categories':[]}
      min_win = int(min(df[sort_by])) - 1
      df = df.set_index('id')

      for x in range(0,1100,63):
        for y in range(0,510,83):
          it+=1
          if it>119:
            break
          df = df.sort_values(sort_by,ascending=False)
          now_hero = df.iloc[it]
          category_name = int(now_hero[sort_by])
          hero = str(now_hero.name)
          
          data['configs'][pos].get('categories').append({'category_name':int(category_name),"x_position":x,"y_position":y,"width":6*(category_name - min_win),"height":7*(category_name - min_win),"hero_ids":[hero]})

      
  with open(_USER_DATA.dota2_account_id + "/hero_grid_config.json",'w') as json_file:
    json.dump(data,json_file,indent=4)
    

def role_grid(grid_name,heroes):
  with open(_USER_DATA.dota2_account_id + "/hero_grid_config.json") as json_file,open('heroes_data.csv','r') as hero_json:
      pos = False
      df = pd.read_csv(hero_json)
      num_to_lane = {1:"safelane",2:"mid",3:"offlane",4:"jungle"}
      data = json.load(json_file)

      for i,x in zip(data['configs'],range(1000)):

        if i['config_name'] == grid_name:
          pos = x
          break
        else:
          continue
      if pos == False:
        data['configs'].append({"config_name":grid_name,'categories':[]})
        pos = -1

      h = iter(heroes)
      it = -1
      roles = list(df['lane'].unique())

      data['configs'][pos] = {'config_name':grid_name,'categories':[]}
      for x in range(0,1100,int(1100)):
        for y in range(0,510,int(510/len(roles))-1):
          it+=1
          if it+1>len(roles):
            break
          data['configs'][pos].get('categories').append({'category_name':num_to_lane.get(roles[it]),"x_position":x,"y_position":y,"width":1100,"height":100,"hero_ids":list(df[df['lane'] == roles[it]]['id'])})
  with open(_USER_DATA.dota2_account_id + "/hero_grid_config.json",'w') as json_file:
    json.dump(data,json_file,indent=4)
    
role_grid('Hero_roles',all_heroes)
create_hero_grid('best_heroes','winrate')