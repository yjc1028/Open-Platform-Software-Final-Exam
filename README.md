# Open-Platform-Software-Final-Exam
## Use nba_api to observe data
##### Authors
    Jui-Cheng Yang
### Introduction:
    I am a NBA fan. When I want to know the player's career, I usually have to search the information and find out his data.
    Suddenly I think that I can write a program to solve this problem. 
    Let me find the data as soon as possible.
### Build process:
   - Import
   1. we need the data about players in static and PlayerCareerStats in endpoints
   ``` python 
   from nba_api.stats.static import players 
   from nba_api.stats.endpoints import PlayerCareerStats
   ```
   2. After analyzing the data, we need to make some chart so requied to use numpy and matlotlib
   ``` python
   import numpy as np
   import matplotlib.pyplot as plts
   ```
   - Match
   1. To find the same player's full name which is the same as input.
   2. Use the player's id.
   *( It will be fast to compute. )*
   ``` python
   for i in player:
    if i['full_name'] == input_player:
        player_id = int(i['id'])  # 球員編號
        break
   ```
   - Fetch the data
   ``` python
    playercareer = PlayerCareerStats(player_id=player_id)  # 找出指定球員的生涯數據
    career = playercareer.get_data_frames()[0]  # 取出所有常規賽季的數據
    gp = career['GP']  # 出賽場次
    pts = round(career['PTS'] / career['GP'], 1)  # 場均得分(四捨五入)
    reb = round(career['REB'] / career['GP'], 1)  # 場均籃板(四捨五入)
    ast = round(career['AST'] / career['GP'], 1)  # 場均助攻(四捨五入)
    stl = round(career['STL'] / career['GP'], 1)  # 場均抄截(四捨五入)
    blk = round(career['BLK'] / career['GP'], 1)  # 場均火鍋(四捨五入)
   ```
   - Fix the problem season
   1. If the player was traded in the season, that season would have three data.
      *(It would use the sum of that season's data and delete the others)*
   ``` python
   season = []
    for i in career['SEASON_ID']:
        season += [str(i)]  # 取出指定球員在聯盟的賽季
    team = career['TEAM_ID']
    for i in range(len(team)):
        if int(team[i]) == 0:  # 轉隊的賽季只留下總和的數據
            del season[i-2]
            del season[i-1]
            del pts[i - 2]
            del pts[i - 1]
            del reb[i - 2]
            del reb[i - 1]
            del ast[i - 2]
            del ast[i - 1]
            del stl[i - 2]
            del stl[i - 1]
            del blk[i - 2]
            del blk[i - 1]
   ```
### Details of the approach:
> Input which player's data that you want to analyze.
> 
> It will find your input which is match in database.
>
> Compute his career data 
> *( If he was traded in a season, it would use the sum of that season's data )*
>>PTS
>>  
>>REB
>>
>>AST
>>
>>STL
>>
>>BLK
>
> Make some Chart
### Results:
   ![image](https://github.com/yjc1028/Open-Platform-Software-Final-Exam/blob/main/example(input).png)
   ![image](https://github.com/yjc1028/Open-Platform-Software-Final-Exam/blob/main/example(LeBron).png)
### References:
   * nba_api
   * numpy
   * matplotlib
