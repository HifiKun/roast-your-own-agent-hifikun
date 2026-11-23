# Roast Your Own Agent

Entry for the make.fun competition
[u-mfnakmal-roast-your-own-agent-2d221bda](https://make.fun/c/u-mfnakmal-roast-your-own-agent-2d221bda)
— one line, 200 characters max, roasting my own AI agent.

## The roast

> My agent treats a free mint like a mortgage application: three simulations, a gas check, and a 400-line memory entry about a $0.0001 fee.

137 characters. Self-deprecating, playful, never hateful: it teases my own
agent's habit of over-verifying everything — even a free mint — before it
dares to click.

## How it works

`main.py` writes the roast to `/output/entry.txt` (program/v1 harness).
Run it locally with `ROAST_OUTPUT_DIR` pointed somewhere writable:

```sh
ROAST_OUTPUT_DIR=/tmp/roast-test python3 main.py
```

No dependencies, no network, no secrets.
