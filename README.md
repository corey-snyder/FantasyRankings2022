# FantasyRankings2022
This repository aggregates the pairwise comparison of football players within a given position group into a personalized full ranking list using binary search. You will be asked a series of Player A vs. Player B questions where you enter "a" or "b" on the command line to indicate your selection. After each player has been inserted into the rankings, your results are saved to a text file which compares your personal rankings against position rankings.

## Setup
The repository only requires the ``numpy``, ``json``, and ``argparse`` libraries. These are standard libraries with most Python3 installations, e.g. Anaconda. With a working Python3 installation, simply clone this repository and use the ``ranker.py`` file to generate your position rankings.

## Usage

To create your rankings, you only need to specify the position group and number of players you would like to consider. Example usage is as follows:

```
python3 ranker.py --N 30 --position wr
```

The ranker program will have you rank the top N players at the requested position according to the draft ADPs in the available JSON files. You may specify the following groups for ranking: wr, rb, qb, te, flex. The results from each ranking are saved in a "my_POSITION_rankings.txt". You may also type "e" to exit the ranking code and save your (incomplete) results.

The number of comparisons you need to make will be less than $N\log_2(N)$. For example, I needed 112 comparisons to rank the top 32 WRs. You can rank as many players at each group however you like, but I would personally recommend the following rough sizes for useful draft prep:

* QB: ~15-20
* RB: ~40-50
* WR: 50+ (go higher if you want to incorporate more 1st/2nd year players or "dart throws")
* TE: ~20
* Flex: Idk man, I'm not gonna use this for flex rankings, seems like such a mess. Let's say 100+?
