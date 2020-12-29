import json
import requests
import pandas as pd
from time import sleep
def pre_proccessing(file_name):
  enga = 0

  with open('temp/herojson.json','w+') as file:
    ## HERO STATS
    r = requests.get('https://api.opendota.com/api/heroStats')
    enga += 1
    json.dump(r.json(),file)

  with open('temp/herojson.json','r+') as json_file,open('temp/proced_json.json','w') as outfile:
    heroes = json_file.read().replace('true','"True"')
    outfile.seek(0)
    outfile.write('{"heroes":'+f'{heroes}'+'}')
    outfile.truncate()
  with open('temp/proced_json.json') as json_file:
    data = json.load(json_file)
    num_to_lane = {1:"safelane",2:"mid",3:"offlane",4:"support",5:"hard_support"}
    for i in data['heroes']:
      if enga == 59:
        print('api limit reached please wait 60 seconds')
        sleep(60)
        
        enga = 0

      i['winrate'] =  float((i.get('7_win') + i.get('8_win')) / (i.get('7_pick') + i.get('8_pick'))) * 100
      lane = pre_proccessing_2(i.get('id'),file_name)
      if lane == 1:
        if 'Carry' in i['roles']:
          i['lane'] = lane
        else:
          i['lane'] = 5
      elif lane == 3:
        if 'Support' in i['roles']:
          i['lane'] = 4
        else:
          i['lane'] = lane
      else:
        i['lane'] = lane
          
      i['main_role'] = str(num_to_lane.get(i.get('lane')))
      print(i['main_role'],i['lane'])
      print(f'sending request for {i["localized_name"]}')
      enga += 1
  with open(file_name,'w') as json_file:
    df = pd.DataFrame(data['heroes'])
    ## CSV Editing
    df = df.drop(columns=['null_pick','null_win'],axis=1)    
    df.to_csv('heroes_data.csv')
    json.dump(data,json_file,indent = 4)
    

    



def pre_proccessing_2(hero_id,file_name):
  with open('temp/hero_roles.json','w') as file:
    r = requests.get(f'https://api.opendota.com/api/scenarios/laneRoles/?hero_id={hero_id}')
    json.dump(r.json(),file)
  with open('temp/hero_roles.json','r+') as json_file,open('temp/proced2_json.json','w') as outfile:
    heroes = json_file.read().replace('true','"True"')
    outfile.seek(0)
    outfile.write('{"heroes":'+f'{heroes}'+'}')
    outfile.truncate()
  with open('temp/proced2_json.json') as json_file:
    data = json.load(json_file)
  with open(file_name,'w') as json_file:
    list_of_rows = []
    df = pd.DataFrame(data['heroes'])
    ## CSV Editing
    df = df.astype('int64')
    for x,df2 in df.groupby('lane_role'):
      list_of_rows.append([int(df2.hero_id.mean()),int(df2.lane_role.mean()),df2.games.sum(),df2.wins.sum()/df2.games.sum()*100])
    df = pd.DataFrame(list_of_rows,columns=['id','lane','games','winrate'])
    new_df = pd.DataFrame()
    for x,y in df.groupby('id'):
      new_df = new_df.append(y.sort_values('games',ascending=False).iloc[0])
      if y.sort_values('games',ascending=False).iloc[0]['games'] / 2 < y.sort_values('games',ascending=False).iloc[1]['games']:
         new_df = new_df.append(y.sort_values('games',ascending=False).iloc[1])

    new_df['lane'] = new_df['lane'].astype('int64')
    return int(new_df.loc[:,'lane'].iloc[0])
    
pre_proccessing('all_heroes.json')
