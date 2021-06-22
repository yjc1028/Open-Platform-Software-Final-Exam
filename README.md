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
      *( It would use the sum of that season's data and delete the others )*
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
   - Make chart
   1. Create list
   *( List is used by chart )*
   ``` python
   season_pts = []
    for i in pts:
        season_pts += [i]  # 取出指定球員在聯盟的場均得分
    season_reb = []
    for i in reb:
        season_reb += [i]  # 取出指定球員在聯盟的場均籃板
    season_ast = []
    for i in ast:
        season_ast += [i]  # 取出指定球員在聯盟的場均助攻
    season_stl = []
    for i in stl:
        season_stl += [i]  # 取出指定球員在聯盟的場均抄截
    season_blk = []
    for i in blk:
        season_blk += [i]  # 取出指定球員在聯盟的場均火鍋
   ```
   2. Make season points chart
   ``` python
    a1 = plt.subplot(511) # 放在指定位置
    plt.title('POINTS')  # 把長條圖的X軸放入年份Y軸放入得分
    plt.bar(np.array(season), np.array(season_pts))
    for x, y in enumerate(np.array(season_pts)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值
   ```
   3. Make season rebounds chart
   ``` python
    a2 = plt.subplot(512)
    plt.title('REBOUNDS')  # 把長條圖的X軸放入年份Y軸放入籃板
    plt.bar(np.array(season), np.array(season_reb), color='yellow')
    for x, y in enumerate(np.array(season_reb)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值
   ```
   4. Make season assists chart
   ``` python
    a3 = plt.subplot(513)
    plt.title('ASSISTS')  # 把長條圖的X軸放入年份Y軸放入助攻
    plt.bar(np.array(season), np.array(season_ast), color='yellow')
    for x, y in enumerate(np.array(season_ast)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值
   ```
   5. Make season steals chart
   ``` python
    a4 = plt.subplot(514)
    plt.title('STEALS')  # 把長條圖的X軸放入年份Y軸放入抄截
    plt.bar(np.array(season), np.array(season_stl), color='red')
    for x, y in enumerate(np.array(season_stl)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值
   ```
   6. Make season blocks chart
   ``` python
    a5 = plt.subplot(515)
    plt.title('BLOCKS')  # 把長條圖的X軸放入年份Y軸放入火鍋
    plt.bar(np.array(season), np.array(season_blk), color='red')
    for x, y in enumerate(np.array(season_blk)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值
   ```
  - Output
    ``` python
    plt.tight_layout()
    plt.show()
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
