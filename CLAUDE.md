# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

A Claude Code plugin (also usable as a Codex skill) containing one Markdown skill, `ao-plan`. It writes implementation plans that an Orchestrator.inc (`ao`) orchestrator runs: one worker per step, with per-step `Worker:` (`ao spawn` flags) and `Review:` (reviewer tier per round) lines. No build step; the product is the Markdown.

## Commands

- Validate the plugin: `claude plugin validate .`
- Example project tests: `cd examples/tasklist && python3 -m unittest` (single test: `python3 -m unittest tests.test_store.<Class>.<method>`). Python 3.10+, stdlib only.

## Structure and coupling

- `skills/ao-plan/SKILL.md` is the workflow. It links to `references/tiers.md` (default tier → agent/model/effort flags) and `references/plan-template.md` (exact plan output format, including the "How to run this plan" section the orchestrator follows).
- `.claude-plugin/plugin.json` and `marketplace.json` both carry the plugin description; keep them in sync.
- Facts are duplicated across files. When changing one, update the others:
  - Tier defaults (models, efforts, review rounds): `references/tiers.md`, the review table in `SKILL.md`, and the README "Tiers" table.
  - Plan format: `references/plan-template.md` and the example plan `examples/tasklist/docs/plans/2026-11-20-tasklist-v1.md` (required by CONTRIBUTING).
  - Review-round behavior: `plan-template.md` and the README "Review rounds" section.
- `examples/tasklist` is a deliberately small Python CLI whose plan exercises all three tiers; it contains an intentional concurrency bug for the deep-tier step. Do not fix it outside that plan.

## Conventions

- Never invent model IDs in tier tables or plans; use the values from `references/tiers.md` or the user's `## AO worker tiers` override table.
- PRs should state how the change was tested: which agent, which model, and what the orchestrator did with the plan.
