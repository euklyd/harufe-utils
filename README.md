Run with `python statcalc.py charname.json`, then use the functions in statcalc to do calculation things ð

`charname.json` holds your character's _actual_ stats: bases, levelups, promotion gains, statboosters (from shrine, scales, etc.).

`charname_meta.json` holds meta-information. These include things that you'd have to be told by Haru directly, such as your true growths (`'initial_growths'`). You can find your expected increases (`'expected_inc'`) by using `statsat(38)`.

The following are the main two functions in `statcalc.py`:

- `growths()` tallies up your levelups so far, and calculates your effective growth rates.

- `final()` displays your stats at your current level, factoring in bases, levelups, promotion, etc.

- Additionally, `statsat(lvl)` gives you your stats at level `lvl`, given your bases, promotion gains, and growth rates.
