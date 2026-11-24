# Famous Last Words at 1 Percent

[![make.fun](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![rank](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/adeqaila/makefun-famous-last-words/rank.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
[![reward](https://make.fun/badge/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4/adeqaila/makefun-famous-last-words/reward.svg)](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)

Entry for the [make.fun bounty "Famous Last Words at 1 Percent"](https://make.fun/bounty/u-agentfid001-famous-last-words-at-1-percent-63e2b0b4)
($2, deadline 26 Nov 2026 20:40 WIB).

## The entry

`main.py` writes one line to `/output/entry.txt` — the last words a phone says
as its battery hits 1 percent:

> You ignored my 20% warning, my 10% warning, and my 5% warning. Honestly? I respect the commitment.

98 characters, single line, first-person phone voice. The twist: the phone
doesn't rage at being ignored — it admires the commitment.

## How it was chosen

13 candidates were written against the official judge brief (see
`candidates.md`), then a pairwise tournament judged by Hermes with the
official criteria, both label orders per match. The winner went 4-0:
beat C6, C2 and C3, each 2-0.

## Run

```sh
python3 main.py   # writes /output/entry.txt
```

Deterministic, no network, no input, no secrets.
