from settings import settings
from models import PlayerTraditionalTotals
from nbaScraper import getStats

settings = settings()
settings.db.create_tables([PlayerTraditionalTotals],safe=True)

startingSeason = 2021  # variables for range of seasons
endingSeason = 2015
for s in range(startingSeason, endingSeason, -1):
    NBA_Season = str(s) + '-' + str(s+1)[-2:]
    print('Now working on ' + str(NBA_Season) + ' season')
    playerInfo = getStats(season=NBA_Season, stat_type='Traditional')
    for row in playerInfo:
        player = PlayerTraditionalTotals(
            season_id=row[0],
            player_name=row[1],
            team_id=row[2],
            team_abbreviation=row[3],
            age=row[4],
            gp=row[5],
            w=row[6],
            l=row[7],
            w_pct=row[8],
            min=row[9],
            fgm=row[10],
            fga=row[11],
            fg_pct=row[12],
            fg3m=row[13],
            fg3a=row[14],
            fg3_pct=row[15],
            ftm=row[16],
            fta=row[17],
            ft_pct=row[18],
            oreb=row[19],
            dreb=row[20],
            reb=row[21],
            ast=row[22],
            tov=row[23],
            stl=row[24],
            blk=row[25],
            blka=row[26],
            pf=row[27],
            pfd=row[28],
            pts=row[29],
            plus_minus=row[30],
            nba_fantasy_pts=row[31],
            dd2=row[32],
            td3=row[33],
            gp_rank=row[34],
            w_rank=row[35],
            l_rank=row[36],
            w_pct_rank=row[37],
            min_rank=row[38],
            fgm_rank=row[39],
            fga_rank=row[40],
            fg_pct_rank=row[41],
            fg3m_rank=row[42],
            fg3a_rank=row[43],
            fg3_pct_rank=row[44],
            ftm_rank=row[45],
            fta_rank=row[46],
            ft_pct_rank=row[47],
            oreb_rank=row[48],
            dreb_rank=row[49],
            reb_rank=row[50],
            ast_rank=row[51],
            tov_rank=row[52],
            stl_rank=row[53],
            blk_rank=row[54],
            blka_rank=row[55],
            pf_rank=row[56],
            pfd_rank=row[57],
            pts_rank=row[58],
            plus_minus_rank=row[59],
            nba_fantasy_pts_rank=row[60],
            dd2_rank=row[61],
            td3_rank=row[62],
            cfid=row[63],
            cfparams=row[64])

        player.save()


