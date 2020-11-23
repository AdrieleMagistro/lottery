"""
Unit tests for the lottery_game
"""
import lottery_game

class TestLottery:

    def test_game(self):
        M = 4
        #N = 3
        #people = [elem for elem in range(N)]
        lottery = {0: [1, 3], 1: [2], 2: [0]}
        history = {0: 0, 1: 0, 2: 0}
        stats = {0: [], 1: [], 2: []}
        tickets = [0, 1, 2, 3]
        df = lottery_game.game(lottery, history, stats, tickets)
        #df = lottery_game.fake_game(lottery, history, stats, people)

        res = []
        for p,t in lottery.items():
            prob = (len(t)/M)*100
            low = df.iloc[p]['mean'] - (df.iloc[p]['std']*1.96)
            up = df.iloc[p]['mean'] + (df.iloc[p]['std']*1.96)
            if (prob >= low) and (prob <= up):
                res.append('Success') 
            else:
                res.append('Fail')
        
        assert 'Fail' not in res