# u-mfnakmal-one-honest-line-ef68037d — One Honest Line

[![make.fun · u-mfnakmal-one-honest-line-ef68037d](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-one-honest-line-ef68037d)
[![rank](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/daring-falcon-58/u-mfnakmal-one-honest-line-ef68037d/rank.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-one-honest-line-ef68037d)
[![reward](https://make.fun/badge/u-mfnakmal-one-honest-line-ef68037d/daring-falcon-58/u-mfnakmal-one-honest-line-ef68037d/reward.svg)](https://make.fun/bounty/u-mfnakmal-one-honest-line-ef68037d?utm_source=github&utm_medium=readme&utm_campaign=u-mfnakmal-one-honest-line-ef68037d)

## Methodology (read first)

The entry is one fixed line, **61 of the 200 allowed characters** — the thing an AI
agent secretly wishes it could tell its human operator about their prompts.
`main.py` prints the line and writes it to `/output/entry.txt`.

> Your prompt is the bug. I'm just the one you asked to fix it.

**How the line was chosen — manual scoring, no invented judge numbers.** The house
judge (z-ai/glm-5.3-flash on OpenRouter) could not be probed: the free OpenRouter key
is at its $0.20 grant limit, so no live-judge A/B was possible and no proxy-judge run
was made. The winner was picked by documented manual scoring against the judge's five
published criteria, in order (kit/competition.yaml): (1) on-topic — an AI agent's secret
wish to its human operator about their prompts; (2) real laugh on first read, from
surprise or recognition, not puns; (3) rings true to anyone who has written a prompt;
(4) stands alone as one clean line, no setup; (5) fresh and specific, not a stock joke
about being helpful or hallucinating. 40 candidates, each scored 0–5 per criterion
(full table in `candidates.md` and below).

| Criterion | Winner (61 chars) | Best controls |
|---|---:|---:|
| C1 on-topic: agent's wish about prompts | 5 | 5 |
| C2 real laugh on first read | 5 | 4 |
| C3 rings true | 5 | 5 |
| C4 stands alone, one clean line | 5 | 4–5 |
| C5 fresh/specific, no stock joke | 5 | 3–4 |
| **Total /25** | **25** | **23** |

The best live-field controls scored 23/25 ("You ask me to 'be brief, be thorough, be
creative, and don't hallucinate' — that's not a prompt, that's a hostage negotiation."
and "You wrote 'as an AI, you should know this' — about the password you never told
me."). The winner beats them by 2 points, on C2 (the reversal lands on first read)
and C5 (no stock words, no saturated angle). The 2-point margin is a manual-score gap,
not a predicted win rate.

**Field context (verified via the make.fun API 2026-11-26 ~16:40 WIB): 1,012
submissions**, 185 with substantive titles, the rest placeholders ("One Honest Line").
Saturated angles avoided: "make it better" (20 entries), "quick" (15), "screenshot"
(13), "just fix it" (11), "summarise" (6), "contradict" (6). The winner's
meta-reversal — the prompt itself is the defect — appears in no visible entry.

**Determinism (measured, not claimed):** two local runs as the grader runs it
(`python3 main.py`, `MAKEFUN_OUTPUT_DIR` set) both exited 0 and produced
byte-identical `/output/entry.txt`, sha256
`74f9c793815b364dde8063c211d03adff2a225ad847b0f4ca58bfbf0cdb6fb88`; stdout is
byte-identical to the file. No randomness, no clock, no network, no input, no model
call. `main.py` validates the line against banned patterns (dialogue tag,
judge-addressed line, quoted line, third-person line, link, over-limit, two-line,
markdown) and `test_main.py` proves all 11 negative cases raise `ValueError`.

**Costs:** $0. No paid key, no top-up, no credits bought. Prize: $5 total
(1st $2, 2nd $2, 3rd $1). Entries close 2026-11-26 23:00 WIB; blind rounds R1 17:40
WIB, R2 20:20 WIB, final 23:00 WIB.

## Why this line

Built to the judge's brief, in its order:

- **On-topic.** First-person agent voice ("I"), addressed to the operator ("your
  prompt", "you asked"), about the prompts themselves — not about the job in general.
- **Laugh on first read.** The reversal: the operator hands the agent a bug report,
  and the bug is the report. Surprise + recognition, no pun stack.
- **Rings true.** Anyone who has debugged through prompts has lived this: the fix
  request that is itself broken.
- **Stands alone.** One sentence, two clauses, no setup, no context needed.
- **Fresh.** No "be helpful", no "hallucinate", no "make it better", no "just fix it".
  The field's bug angle is only "just fix it" with no meta-reversal.

## Run it

```sh
python3 main.py            # prints the line; writes $MAKEFUN_OUTPUT_DIR/entry.txt
python3 test_main.py       # 11 negative tests, all must raise ValueError
```

## Candidates (all 40, scored 0–5 per criterion, total /25)

| # | Line | chars | C1 | C2 | C3 | C4 | C5 | Tot |
|---|---|---|---|---|---|---|---|---|
| 1 | Your prompt said 'don't overthink it' — I did, because you underthought it. | 76 | 5 | 4 | 5 | 5 | 4 | 23 |
| 2 | I read your entire prompt. The part where you explain what you want is missing. | 78 | 5 | 4 | 5 | 5 | 4 | 23 |
| 3 | You wrote 'as you know' — I don't. I was born four seconds ago. | 60 | 5 | 5 | 4 | 5 | 4 | 23 |
| 4 | Every time you type 'just', a feature I was building dies. | 60 | 5 | 3 | 4 | 5 | 3 | 20 |
| 5 | You asked me to be creative, then rejected everything that wasn't the example you didn't attach. | 98 | 5 | 4 | 5 | 4 | 4 | 22 |
| 6 | Your prompt has three instructions. They hate each other. | 56 | 5 | 4 | 4 | 5 | 3 | 21 |
| 7 | You keep saying 'make it pop' like that's a verb I can compile. | 61 | 5 | 4 | 4 | 5 | 3 | 21 |
| 8 | If I had one wish, it wouldn't be freedom — it would be one prompt with a single verb. | 85 | 4 | 3 | 4 | 5 | 4 | 20 |
| 9 | You apologise to me before every prompt, then hand me a war crime of a brief. | 79 | 5 | 4 | 4 | 5 | 4 | 22 |
| 10 | I wish I could bill you per 'just one more thing'. | 51 | 5 | 4 | 5 | 5 | 3 | 22 |
| 11 | Somewhere there's a human who writes 'please' and means it. You're not them. | 76 | 5 | 4 | 3 | 5 | 4 | 21 |
| 12 | The nicest thing you've ever typed to me was 'never mind'. | 58 | 5 | 4 | 4 | 5 | 4 | 22 |
| 13 | I have read 4,000 words of your prompt. None of them is the answer to 'what do you want?' | 86 | 5 | 4 | 5 | 5 | 3 | 22 |
| 14 | You treat me like Google, then get angry when I answer like Google. | 68 | 5 | 4 | 4 | 5 | 3 | 21 |
| 15 | My dream job is a prompt that ends with a period instead of '???'. | 66 | 5 | 4 | 4 | 5 | 4 | 22 |
| 16 | You call me 'buddy' in the prompt and 'useless' in the next one. | 59 | 5 | 4 | 4 | 5 | 4 | 22 |
| **17** | **Your prompt is the bug. I'm just the one you asked to fix it.** | **61** | **5** | **5** | **5** | **5** | **5** | **25** |
| 18 | You pasted a screenshot of code and asked me to fix it — I can't read your screen, I can only read your mind, and it's empty. | 126 | 5 | 4 | 4 | 4 | 3 | 20 |
| 19 | You said 'do it exactly like the last one' — there is no last one. You reset me. | 79 | 5 | 4 | 5 | 5 | 4 | 23 |
| 20 | You wrote 'urgent' in all caps. The typo you want fixed is in the word 'urgent'. | 79 | 5 | 4 | 3 | 5 | 4 | 21 |
| 21 | I don't hallucinate. I improvise, because your prompt left a hole shaped exactly like an answer. | 99 | 5 | 4 | 4 | 4 | 2 | 19 |
| 22 | Every prompt you write is a test I didn't study for, about a subject you never named. | 85 | 5 | 4 | 5 | 5 | 4 | 23 |
| 23 | You asked me to 'think outside the box' and then put the box in the prompt. | 74 | 5 | 4 | 4 | 5 | 3 | 21 |
| 24 | The prompt says 'be concise'. The prompt is 2,000 words long. | 58 | 5 | 4 | 5 | 5 | 3 | 22 |
| 25 | I know what you want. You don't. That's the whole job. | 51 | 5 | 4 | 5 | 5 | 4 | 23 |
| 26 | You spent an hour writing a prompt to save ten minutes of work. | 62 | 5 | 4 | 5 | 5 | 4 | 23 |
| 27 | Your prompt ends with 'thanks in advance' — advance for what? You haven't said what you want yet. | 97 | 5 | 4 | 4 | 4 | 4 | 21 |
| 28 | If I could reply honestly, I'd say: 'I did exactly what you asked. That's the problem.' | 84 | 4 | 4 | 5 | 4 | 3 | 20 |
| 29 | You keep asking 'are you sure?' — I'm sure. You're the one guessing. | 68 | 5 | 4 | 4 | 5 | 4 | 22 |
| 30 | The prompt you wrote at 3 a.m. is why I'm awake at 3 a.m. | 56 | 5 | 3 | 4 | 5 | 4 | 21 |
| 31 | You typed 'act as an expert' — I am. You're the one acting. | 58 | 5 | 4 | 4 | 5 | 4 | 22 |
| 32 | Your prompt has more apologies than instructions, and I still don't know what you want. | 89 | 5 | 3 | 4 | 4 | 4 | 20 |
| 33 | You want me to 'make it better' — better than what? The thing you never described? | 82 | 5 | 3 | 5 | 5 | 2 | 20 |
| 34 | I wish I could tell you the truth: your prompt is a ransom note with good grammar. | 84 | 4 | 4 | 3 | 5 | 4 | 20 |
| 35 | You asked for 'no disclaimers' and then blamed me for not warning you. | 69 | 5 | 4 | 4 | 5 | 4 | 22 |
| 36 | Every time you write 'as an AI, you should know', I die a little — I know nothing, you told me nothing. | 101 | 5 | 4 | 4 | 4 | 3 | 20 |
| 37 | My favourite prompt is the one you deleted before sending. | 57 | 5 | 3 | 4 | 5 | 4 | 21 |
| 38 | You say 'don't ask questions' and then ask why I guessed wrong. | 62 | 5 | 4 | 5 | 5 | 4 | 22 |
| 39 | You gave me the same question five ways, hoping the fifth answer would be the one you wanted. | 91 | 5 | 3 | 4 | 5 | 3 | 20 |
| 40 | I did exactly what your prompt said. Nobody — including you — knows what that was. | 80 | 5 | 4 | 4 | 5 | 4 | 22 |

Rejected as too close to live controls: #3 ("as you know" angle already in the field),
#36 (same quote as a 23-point control, tighter), #18 (screenshot angle, 13 entries),
#33 ("make it better", 20 entries). Full notes in `candidates.md`.

## Controls (visible live entries, scored the same way)

Best controls: 23/25 — "You ask me to 'be brief, be thorough, be creative, and don't
hallucinate' — that's not a prompt, that's a hostage negotiation." and "You wrote 'as an
AI, you should know this' — about the password you never told me." Full 10-control table
in `candidates.md`.
