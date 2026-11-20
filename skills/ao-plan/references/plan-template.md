# Plan template

Copy this structure. Replace everything in `<angle brackets>`. Keep the `How to run this plan` section word for word except the test command.

````markdown
# <Title>

<One paragraph: what this builds and why.>

## How to run this plan

For the AO orchestrator:

- Spawn one worker per step. Pass the step's `Worker:` flags to `ao spawn` exactly as written, plus `--name "[<tier>] <step title>"` and a prompt that contains the step's full text and the path of this file.
- Start a step only after every step in its `Depends on` has merged. Steps with no unmerged dependencies may run in parallel.
- If a step has no `Worker:` line, use the standard tier below.
- Every step keeps `<test command>` passing and adds tests for what it changes.

## Worker tiers

| Tier | Worker flags |
|------|--------------|
| light | `<flags>` |
| standard | `<flags>` |
| deep | `<flags>` |

## Step 1: <title>

<What to build, in enough detail that a worker who has only this step and the repo can do it.>

- Files: <paths>
- Depends on: none
- Risk: <low | medium | high>. <one-line reason>
- Tier: <light | standard | deep>
- Worker: `<flags for that tier, copied from the table>`

## Step 2: <title>

...
````
