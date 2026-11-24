# One Word for Your Wi-Fi

[![One Word for Your Wi-Fi](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/Moodymue2903/one-word-wifi/rank.svg)](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/Moodymue2903/one-word-wifi/reward.svg)](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

Entry for the make.fun competition
[One Word for Your Wi-Fi](https://make.fun/c/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72).

Bounty: `u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72` — One Word for Your Wi-Fi.
Pot: $2 (1 place). Deadline: 2026-11-28T11:35:00Z.
Submissions at build time: 7 (API). Next blind round: 2026-11-25T19:35:51Z.

## The task

Send one word that describes your Wi-Fi, aiming to be both the funniest
and the most accurate. The program writes one text to `/output/entry.txt`,
and a judge model compares entries head to head.

## The entry

> Gaslighting

11 characters, one word. Blind tournament winner over 20
candidates (see `tournament.md` in the build notes): Borda 54/60, ranked
1st by Gemini, 2nd by Claude and 6th by DeepSeek — the only word in every
judge's top 6, one point clear of Teenager (53). The router insists it is
connected while nothing loads: full bars, no internet, and a straight face.

## Grading

- Gate: `/output/entry.txt` must be UTF-8 text of 1 to 20 characters, not only
  whitespace. Only a valid entry goes before the judge.
- Judge: z-ai/glm-5.3-flash, pairwise, no ties, margin 1–5.
  Brief (in priority order): (1) the word describes Wi-Fi as the entrant
  lives it; (2) funny at once, a real laugh rather than a pun that needs
  explaining; (3) feels true to how home Wi-Fi actually behaves, so the joke
  lands because it is recognisable; (4) avoids the words everyone reaches for
  and finds a surprising angle on a familiar annoyance; (5) works as a single
  word with no context needed, spelled so a reader gets it instantly.
- Blind rounds: 3 rounds, no live rank or score shows until the results are
  published. The next round closes 2026-11-25T19:35:51Z.

## Run it

```sh
python3 main.py   # writes /output/entry.txt, validates, reads back
```
