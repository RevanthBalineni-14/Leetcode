class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort(reverse= True)
        trainers.sort(reverse= True)
        pp, tp = 0, 0
        while pp<len(players) and tp<len(trainers):
            if players[pp]<=trainers[tp]:
                pp+=1
                tp+=1
            else:
                pp+=1
        return tp