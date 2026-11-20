# Default worker tiers

Used when neither the user's nor the project's `CLAUDE.md` / `AGENTS.md` has an `## AO worker tiers` table.

| Tier | Worker flags |
|------|--------------|
| light | `--agent claude-code --model claude-sonnet-5-5 --effort medium` |
| standard | `--agent claude-code --model claude-opus-5-5 --effort medium` |
| deep | `--agent claude-code --model claude-opus-5-5 --effort high` |

## Overriding

Copy this table under an `## AO worker tiers` heading into `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md`, or a repo's `CLAUDE.md` / `AGENTS.md`, and change the flags. A project table wins over a user table. Any agent `ao spawn --agent` accepts works, and tiers may mix agents, for example:

```markdown
## AO worker tiers

| Tier | Worker flags |
|------|--------------|
| light | `--agent codex --model gpt-5.6-sol --effort low` |
| standard | `--agent claude-code --model claude-opus-5-5 --effort medium` |
| deep | `--agent claude-code --model claude-opus-5-5 --effort high` |
```

Run `ao agent ls` to see installed agents. Model IDs and effort values must be ones that agent accepts, or the spawn fails.
