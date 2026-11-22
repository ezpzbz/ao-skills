# Contributing

Thanks for helping. This repo is small on purpose: Markdown skills, no build step.

## Layout

- `skills/<name>/SKILL.md`: the skill, with YAML frontmatter (`name`, `description`).
- `skills/<name>/references/`: files the skill links to.
- `.claude-plugin/`: Claude Code plugin and marketplace manifests.
- `examples/`: sample repos with ready plans.

## Before opening a PR

- Run `claude plugin validate .` if you have Claude Code. CI runs it and the example tests on every PR.
- If you change anything under `skills/`, bump `version` in `.claude-plugin/plugin.json`. Installed plugins only update when it changes.
- If you change `references/plan-template.md`, update the example plan in `examples/tasklist/docs/plans/` to match.
- Describe how you tested it: which agent, which model, and what the orchestrator did with the plan.

## Reporting a run

Real runs are the most useful issues. Include the plan (or its step lines), the agent and models used, and what the orchestrator or workers did differently from the plan.
