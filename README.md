# ao-skills

A skill for Claude Code and Codex that writes implementation plans an [Agent Orchestrator (AO)](https://github.com/OrchestratorInc/agent-orchestrator) orchestrator can run directly.

Each plan step is one worker and one pull request, and names the exact `ao spawn` flags for that worker. Cheap, mechanical steps go to a fast model; risky ones get a stronger model with more reasoning effort:

```markdown
## Step 4: Safe concurrent writes
...
- Depends on: 3
- Risk: high. Concurrency and data-loss bugs.
- Tier: deep
- Worker: `--agent claude-code --model claude-opus-5-5 --effort high`
```

The plan also carries a `How to run this plan` section, so the orchestrator needs no extra project setup.

## Install

**Claude Code**

```
/plugin marketplace add ezpzbz/ao-skills
/plugin install ao-plan@ao-skills
```

**Codex** (and other agents that read `~/.agents/skills`)

```bash
git clone https://github.com/ezpzbz/ao-skills.git
cp -R ao-skills/skills/ao-plan ~/.agents/skills/
```

## Use

1. In the repo you want to change, plan as usual (plan mode works) and mention the orchestrator, e.g. "plan this for AO workers".
2. The skill splits the work into steps, picks a tier per step, and after you approve saves the plan to `docs/plans/YYYY-MM-DD-<topic>.md` and commits it.
3. Give your AO orchestrator the line the skill prints:

   ```
   Implement docs/plans/<file>.md, following its "How to run this plan" section.
   ```

The repo must already be an AO project (`ao project add --path <repo>`).

## Tiers

| Tier | Used for | Default worker flags |
|------|----------|----------------------|
| light | docs, config, mechanical one-file changes | `--agent claude-code --model claude-sonnet-5-5 --effort medium` |
| standard | normal features and fixes | `--agent claude-code --model claude-opus-5-5 --effort medium` |
| deep | concurrency, data loss, migrations, security, unclear bugs | `--agent claude-code --model claude-opus-5-5 --effort high` |

To change them, add an `## AO worker tiers` table to your `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or a repo's `CLAUDE.md` / `AGENTS.md`. See [skills/ao-plan/references/tiers.md](skills/ao-plan/references/tiers.md). Tiers can mix agents, for example Codex for light work and Claude Code for deep work.

## Example

[examples/tasklist](examples/tasklist) is a tiny Python CLI with a ready plan in [docs/plans/](examples/tasklist/docs/plans/) covering all three tiers. To try it end to end:

```bash
cp -R examples/tasklist ~/tmp/tasklist && cd ~/tmp/tasklist
git init -b main && git add . && git commit -m "initial"
gh repo create tasklist-ao-test --private --source . --push
ao project add --path "$PWD" --id tasklist
```

Then tell the project's orchestrator: `Implement docs/plans/2026-11-20-tasklist-v1.md, following its "How to run this plan" section.` Each worker's session details should show the model and effort from its step.

## Limits

The plan is instructions, not enforcement: AO does not validate `Worker:` lines, so an orchestrator that skips one starts that worker on the project's default model.

## License

MIT
