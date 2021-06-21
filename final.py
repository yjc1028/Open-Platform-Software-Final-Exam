import pandas as pd
import nba_api
from nba_api.stats.static import teams
from nba_api.stats.static import players
from nba_api.stats import endpoints
from nba_api.stats.endpoints import PlayerCareerStats
import numpy as np
import matplotlib.pyplot as plt

print("Please input which player you want to search: ")
input_player = input()  # 輸入指定球員
player = players.get_players()
player_id = 0
for i in player:
    if i['full_name'] == input_player:
        player_id = int(i['id'])  # 球員編號
        break
if player_id == 0:  # 打錯直接結束
    print("input is not correct!!")
else:
    playercareer = PlayerCareerStats(player_id=player_id)  # 找出指定球員的生涯數據
    career = playercareer.get_data_frames()[0]  # 取出所有常規賽季的數據
    gp = career['GP']  # 出賽場次
    pts = round(career['PTS'] / career['GP'], 1)  # 場均得分(四捨五入)
    reb = round(career['REB'] / career['GP'], 1)  # 場均籃板(四捨五入)
    ast = round(career['AST'] / career['GP'], 1)  # 場均助攻(四捨五入)
    stl = round(career['STL'] / career['GP'], 1)  # 場均抄截(四捨五入)
    blk = round(career['BLK'] / career['GP'], 1)  # 場均火鍋(四捨五入)
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

    a1 = plt.subplot(511)
    plt.title('POINTS')  # 把長條圖的X軸放入年份Y軸放入得分
    plt.bar(np.array(season), np.array(season_pts))
    for x, y in enumerate(np.array(season_pts)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值

    a2 = plt.subplot(512)
    plt.title('REBOUNDS')  # 把長條圖的X軸放入年份Y軸放入籃板
    plt.bar(np.array(season), np.array(season_reb), color='yellow')
    for x, y in enumerate(np.array(season_reb)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值

    a3 = plt.subplot(513)
    plt.title('ASSISTS')  # 把長條圖的X軸放入年份Y軸放入助攻
    plt.bar(np.array(season), np.array(season_ast), color='yellow')
    for x, y in enumerate(np.array(season_ast)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值

    a4 = plt.subplot(514)
    plt.title('STEALS')  # 把長條圖的X軸放入年份Y軸放入抄截
    plt.bar(np.array(season), np.array(season_stl), color='red')
    for x, y in enumerate(np.array(season_stl)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值

    a5 = plt.subplot(515)
    plt.title('BLOCKS')  # 把長條圖的X軸放入年份Y軸放入火鍋
    plt.bar(np.array(season), np.array(season_blk), color='red')
    for x, y in enumerate(np.array(season_blk)):
        plt.text(x, y, '%s' % y, ha='center')  # 顯示數值

    plt.tight_layout()
    plt.show()


