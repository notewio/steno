# plover-phrasing
My personal phrasing system for plover

Largely based off of [Jade-GG's system](https://github.com/Jade-GG/plover_phrasing) with a couple of changes

- uses the number bar for the unique starters
- conjugation aware
- middles/enders that make more sense to me
- two-stroke phrases

`verb.txt` taken from [Nodebox Linguistics Extended](https://github.com/RensaProject/nodebox_linguistics_extended/tree/master/nodebox_linguistics_extended/verb)

## usage

Install the plover python dictionary plugin and add `phrasing.py` as a dictionary

Changing starters or middles can be done in `phrasing.py`. To change enders, modify them in `generate.py`, then run it and copy the output to `phrasing.py`. (not a pretty solution, but loading external files broke in some update recently so everything has to be in one python file)

## system

| Starters | |
| --- | --- |
| I | `#R` |
| you | `#HR` |
| he | `#PR` |
| she | `#PHR` |
| it | `#THR` |
| we | `#TR` |
| they | `#TPR` |
| (nothing) | `#TPHR` |

| Middles | |
| --- | --- |
| can | `A` |
| \<past\> | `E` |
| will | `U` |
| could | `AE` |
| would | `EU` |
| be doing | `AU` |
| should | `AEU` |

`O` can be added to negate the middle, i.e. can (`A`) -> can't (`AO`)

Enders can be found in `generate.py`
