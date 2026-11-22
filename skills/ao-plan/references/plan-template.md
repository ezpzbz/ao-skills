# Plan template

Copy this structure. Replace everything in `<angle brackets>`. Keep the `How to run this plan` section word for word except the test command.

````markdown
# <Title>

<One paragraph: what this builds and why.>

## How to run this plan

For the AO orchestrator. The project should have AO's automatic review (`autoReview`) turned off; this plan runs review itself.

### Workers

- Spawn one worker per step. Pass the step's `Worker:` flags to `ao spawn` exactly as written, plus `--name "[<tier>] <step title>"` and a prompt that contains the step's full text, the path of this file, and the worker rules below.
- Start a step only after every step in its `Depends on` has merged. Steps with no unmerged dependencies may run in parallel.
- If a step has no `Worker:` line, use the standard tier. If it has no `Review:` line, use one standard round.

Worker rules (include them in every worker's prompt):

- Put `Worker: <agent> / <model> / <effort>` from your step's `Worker:` line at the top of the PR description.
- Keep `<test command>` passing and add tests for what you change.
- On a deep-tier step, run a local code review of your diff (for example `/code-review` in Claude Code) and fix what it finds before opening the PR.
- Do not request or run PR reviews yourself; the orchestrator runs review rounds. Fix every inline review comment you receive, then push.

### Review rounds

When a step's PR is open and its worker is idle, run the rounds in its `Review:` line in order. Each entry is a tier from the table below. For each round:

1. Post a PR comment: `Review round <n>/<total>: <agent> / <model> / <effort>`.
2. Run `ao review trigger <worker-session-id> --rerun` with that tier's `--agent`, `--model` and `--effort`, and wait for the result (`ao review ls <worker-session-id>`).
3. Inline comments are defects to fix now; AO sends them to the worker. Wait until the worker has pushed its fixes and is idle.
4. Optional suggestions in the review summary are for later. Add each as a checklist item to the PR's follow-up issue, titled `Follow-ups from PR #<number>` with label `review-followup`. Create the issue on first use, then add to it. Skip items already listed.

Stop rules:

- A round with no inline comments ends review for that step; skip its remaining rounds.
- If the last round had inline comments, run one more round at the last tier after the fixes. If that round still has inline comments, stop and ask the user.
- You decide when review is done; the reviewer's verdict does not. Merging still follows the project's normal rules.

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
- Review: <reviewer tier per round, e.g. `standard → deep`>

## Step 2: <title>

...
````
