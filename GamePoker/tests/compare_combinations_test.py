import sys
sys.path.append('C:\\Users\\Xiaomi\\Desktop\\Projects\\Python\\PythonCourse\\GamePoker')

from poker import *
from test_data import *


combinations = [
    HighCard([cardAc, card6c, card3h, card3c, card2c]), # special rule
    HighCard([cardKc, card10c, card3h, card3c, card2c]),
    HighCard([cardAh, card10c, card3h, card3c, card2c]),
    Pair([card6h, card6c]),
    Pair([cardAh, cardAc]),
    DoublePair([card6c, card6h, card3c, card3h]),
    DoublePair([cardAs, cardAc, card6h, card6c]),
    Triplet([card6s, card6d, card6c]),
    Triplet([cardAs, cardAd, cardAc]),
    Straight([card5c, card4d, card3h, card2c, cardAh]),
    Straight([cardAh, cardKc, cardQc, cardJc, card10c]),
    Flush([cardAc, card6c, card4c, card3c, card2c]), # special rule
    Flush([cardKc, card6c, card4c, card3c, card2c]),
    Flush([cardAc, cardJc, card4c, card3c, card2c]),
    FullHouse([card6c, card6d, card6s, card3c, card3h]),
    FullHouse([cardKc, cardKs, card6c, card6d, card6s]),
    Quads([card6s, card6c, card6d, card6h]),
    Quads([cardAs, cardAc, cardAd, cardAh]),
    StraightFlush([card5c, card4c, card3c, card2c, cardAc]),
    StraightFlush([cardAc, cardKc, cardQc, cardJc, card10c]),
    RoyalFlush([cardAc, cardKc, cardQc, cardJc, card10c])
]


def test_order():
    for i, comb_i in enumerate(combinations):
        for j, comb_j in enumerate(combinations):
            if i == j:
                expected = 0
            elif i > j:
                expected = 1
            else:
                expected = 2
            
            actual = compare_combinations(comb_i, comb_j)

            sign = ['=', '>', '<']
            error_message = f'''
                actual:   {comb_i} {sign[actual]} {comb_j}, 
                expected: {comb_i} {sign[expected]} {comb_j}
            '''
            assert actual == expected, error_message