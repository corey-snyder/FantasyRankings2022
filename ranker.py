import json
import argparse
import numpy as np

parser = argparse.ArgumentParser()
parser.add_argument('--position', type=str, help='Position to rank. One of: wr, rb, qb, te, flex')
parser.add_argument('--N', type=str, help='Include top-N players by ADP at this position')
args = parser.parse_args()

position = args.position
N = int(args.N)

if position not in ['wr', 'rb', 'qb', 'te', 'flex']:
    raise ValueError('Please specify position as one of: wr, rb, qb, te, flex')

position_json = '{}_adp_2022.json'.format(position)
with open(position_json, 'r') as f:
    position_data = json.load(f)[:N]

available_players = [player['Name'] for player in position_data]
adp = {player['Name']: player['PositionRank'] for player in position_data}

# rank two initial players
initial_players = np.random.choice(available_players, 2, replace=False)
c = None
while c not in ['a', 'b']:
    c = input('(a) {} vs. (b) {}: who do you prefer? Type a or b and press Enter: '.format(initial_players[0], initial_players[1]))
    if c not in ['a', 'b']:
        print('Please type a or b for your selection')
if c == 'a':
    ranked_players = [initial_players[0], initial_players[1]]
else:
    ranked_players = [initial_players[1], initial_players[0]]

# iteratively rank
available_players.remove(initial_players[0])
available_players.remove(initial_players[1])
np.random.shuffle(available_players)
n_comparisons = 1
for p in available_players:
    start, end = 0, len(ranked_players)
    while start < end:
        c = None
        midpoint = int((start+end)/2)
        while c not in ['a', 'b', 'e']:
            c = input('(a) {} vs. (b) {}: who do you prefer? Type a or b and press Enter: '.format(p, ranked_players[midpoint]))
            if c not in ['a', 'b', 'e']:
                print('Please type a or b for your selection or e to exit and save your current rankings')
            if c == 'a':
                end = midpoint
                n_comparisons += 1
            elif c == 'b':
                start = midpoint+1
                n_comparisons += 1
            else:
                break
        if c == 'e':
            break
    if c == 'e':
        break
    ranked_players.insert(start, p)

with open('my_{}_rankings.txt'.format(position), 'w') as f:
    f.write('(Consensus Ranking) Your Ranking: Player name\n')
    for i, p in enumerate(ranked_players):
        f.write('({}) {}: {}\n'.format(adp[p], i+1, p))
print('{} comparisons made'.format(n_comparisons))
print('Ranking saved to my_{}_rankings.txt'.format(position))
