---
name: ao-plan
description: Write an implementation plan that an Orchestrator.inc (`ao`) orchestrator can run, with one worker per step, a model and reasoning effort chosen per step, and tiered review rounds that fix defects now and track suggestions in a follow-up issue. Use when planning a feature, fix, or new project that AO workers will implement, or when the user mentions Orchestrator.inc, AO, `ao spawn`, the orchestrator, worker tiers, or wants a plan "for the orchestrator".
---

# AO tiered plans

Produce a plan file that an AO orchestrator can execute without extra instructions: it says how to run itself, and every step names the exact `ao spawn` flags for its worker.

## 1. Understand the repo

- New or existing project? For an existing one, read `CLAUDE.md` / `AGENTS.md`, `README`, and the code the change touches. Find the test command.
- Plan as you normally would (ask what you need, agree on the approach). This skill only shapes the output.
- If another planning skill is active (for example superpowers `writing-plans`), let it write the steps and their detail, then add this skill's sections and per-step fields to that same plan. Produce one plan file, not two.

## 2. Load the tiers

Look for an `## AO worker tiers` table in the user's or project's `CLAUDE.md` / `AGENTS.md`. If none exists, use [references/tiers.md](references/tiers.md). Use the agent, model, and effort values from that table exactly; never invent model IDs.

## 3. Split into steps

- One step = one worker = one pull request. A step should be reviewable on its own and leave tests passing.
- Give each step: goal, files, depends-on (step numbers or `none`), risk with a one-line reason, tier, `Worker:` line, and `Review:` line.
- Steps that touch the same files depend on each other. Everything else can run in parallel; say so.

## 4. Choose a tier per step

Choose by the riskiest thing in the step:

- **light**: mechanical, well-specified, mostly one file: docs, config, copy, a command that mirrors an existing one, tests for existing code.
- **standard**: normal features and bug fixes across a few files with a clear approach.
- **deep**: concurrency, data loss or corruption, migrations of stored data, security or auth, bugs with unclear root cause, or changes that cut across many modules.

If unsure between two, choose the higher one.

The step's tier also sets its review rounds. Each entry in the `Review:` line is the reviewer tier for one round:

| Step tier | Review |
|-----------|--------|
| light | `standard` |
| standard | `standard → deep` |
| deep | `standard → deep → deep` |

Add or drop a round when a step's risk calls for it, and say why in its risk line.

## 5. Write and save the plan

Follow [references/plan-template.md](references/plan-template.md) exactly, including the `How to run this plan` section and the tier table.

- In plan mode, present the plan for approval first. You cannot write repo files until plan mode ends.
- Once approved, save it to `docs/plans/YYYY-MM-DD-<topic>.md` in the repo (today's date, short kebab-case topic) and commit only that file: `docs: add <topic> plan`.
- The orchestrator reads the plan from the repo, so it must be committed on the branch the orchestrator works from (normally the default branch). If you are on another branch, tell the user.

## 6. Hand off

End with the line the user gives the AO orchestrator:

```
Implement docs/plans/<file>.md, following its "How to run this plan" section.
```
