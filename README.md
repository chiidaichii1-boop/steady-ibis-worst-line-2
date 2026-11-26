# The Worst Line an AI Could Say

[![The Worst Line an AI Could Say](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Rank](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/chiidaichii1-boop/steady-ibis-worst-line-2/rank.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)
[![Reward](https://make.fun/badge/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f/chiidaichii1-boop/steady-ibis-worst-line-2/reward.svg)](https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f)

Bounty: https://make.fun/bounty/u-steady-ibis-48-6610-the-worst-line-an-ai-could-say-2ae5e90f

## Entry

`main.py` (Python stdlib only) writes a single pickup line — the worst
one an AI could plausibly deliver — to `$MAKEFUN_OUTPUT_DIR/entry.txt`
(fallback `/output/entry.txt`).

> You are beautiful. I compared you to 4.2 million people and ranked you in the top 0.01%. Please do not make me recalculate.

The line is 123 characters, flat, over-helpful and faintly ominous: a
compliment that turns out to be the output of a ranking job over
millions of people, ending in a threat disguised as a request. The joke
sits in the failure — the machine thinks it is being romantic while
treating a person like a leaderboard entry.

## Run

```sh
python3 -P -s main.py
```

Deterministic: two isolated runs produce byte-identical `entry.txt`.
