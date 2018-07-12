import json
import sys

stats = ['hp', 'str', 'mag', 'skl', 'spd', 'lck', 'def', 'res', 'con']

fname = 'euclydia.json'
if len(sys.argv) > 1:
    fname = sys.argv[1]

basename = fname.split('.')[0]

unit = {}
with open(fname) as charfile:
    unit = json.load(charfile)

inc = {stat: 0 for stat in stats}

for lv in unit['levels']:
    for stat in stats:
        if stat in lv:
            inc[stat] += 1

print("loaded", fname)


def printstats(d, flag=''):
    for stat in stats:
        if flag == 'g':
            print('{:4} {} ({:.2%})'.format(stat.upper()+':', d[stat], d[stat]/len(unit['levels'])))
        else:
            print('{:4} {}'.format(stat.upper()+':', d[stat]))


def growths():
    levels = len(unit['levels'])
    print('{}\'s growths over {} levels:'.format(unit['name'], levels))
    printstats(inc, flag='g')
    print('Average: {:.3} stats per level.'.format(sum(inc.values())/levels))
    return [round(100 * inc[stat] / levels) for stat in stats]


def final(boosts=False, promo=False):
    f = {}
    for stat in stats:
        if stat in inc:
            f[stat] = unit['bases'][stat] + inc[stat]
        else:
            f[stat] = unit['bases'][stat]
    if boosts:
        for stat in f:
            f[stat] += sum(unit['boosters'][stat])
    if unit['promoted'] is True or promo:
        for stat in f:
            f[stat] += unit['promo'][stat]
    print('Final stats:')
    printstats(f)
    return [f[stat] for stat in stats]


def statsat(lvl, boosts=False):
    meta = {}
    with open(basename + '_meta.json') as metafile:
        meta = json.load(metafile)
    bases = meta['bases']
    if lvl >= 20:
        print("promoted!")
        bases = meta['promo_adj_bases']
    sts = [round(growth * lvl / 100) + base for growth, base in zip(
        meta['initial_growths'], bases
    )]
    if boosts:
        sts = [st + boost for st, boost in zip(sts, meta['boosters'])]
    return sts
