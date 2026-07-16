---
name: lean-execution
description: Use when the user explicitly requests a lightweight workflow for a small or moderately scoped task and wants to avoid disproportionate Superpowers overhead.
---

# Lean Execution

## Principle

Deliver the correct result with the minimum process necessary. Keep goal awareness, staged execution, verification, and iteration, but never turn a bounded task into a large project.

When explicitly invoked, this skill is the active process controller. Do not invoke general Superpowers process skills such as `brainstorming`, `writing-plans`, `subagent-driven-development`, or `using-git-worktrees` unless an escalation condition is met or the user explicitly requests one. Higher-priority system and safety instructions still apply.

## Choose the Smallest Suitable Mode

### Fast Mode

Use when the objective is clear, risk is low, dependencies are limited, and the task can be completed in one direct pass.

Execute immediately. Do not announce a formal plan.

### Lean Plan Mode

Use when the task has several dependent steps, touches multiple files, or combines research, implementation, and checking while remaining bounded.

State a compact plan of 3–6 steps and begin immediately. Do not create a separate specification or wait for approval unless a wrong assumption would cause substantial rework.

### Escalation Mode

Escalate only for:

- multiple independent subsystems or major architectural choices;
- production deployment, destructive migration, security-sensitive, or safety-critical work;
- broad refactoring with uncertain impact;
- unclear acceptance criteria where an incorrect direction would be costly;
- repeated failures requiring systematic debugging;
- work that clearly benefits from several independent agents.

Invoke only the smallest relevant advanced skill, not the entire Superpowers workflow.

## Execution Rules

1. Extract the objective, constraints, inputs, and completion criteria from the conversation and project files.
2. Reuse existing context. Do not ask questions whose answers are already available.
3. Resolve minor ambiguity with reasonable, low-risk assumptions. State only assumptions that materially affect the result.
4. Follow the shortest reliable path to the requested deliverable.
5. Keep the plan stable. When new evidence appears, revise only the affected step instead of restarting the process.
6. Complete the requested deliverable in the current run whenever technically possible.
7. Stop when the completion criteria are met. Do not add unrelated improvements merely because they are possible.

## Tool and Subagent Rules

- Use tools only when they materially improve correctness, speed, or verification.
- Do not browse, scan large directories, or load many files without a task-specific reason.
- Do not create subagents by default.
- Use at most 1–2 subagents only for genuinely independent work with a clear speed or specialist-quality benefit.
- Do not use subagents for simple research, one-file edits, routine checking, or work requiring shared context.
- Stop gathering information once there is enough evidence to act reliably.

## Avoid Process Overhead

Unless explicitly requested, do not require brainstorming, present unnecessary alternatives, create design documents, implementation plans, task trees, worktrees, branches, commits, pull requests, or multi-stage review ceremonies.

Do not delay execution for unnecessary confirmation. Ask a clarification only when no safe assumption can resolve a material ambiguity.

## Proportional Verification

Verification is required, but its depth must match the risk.

- Text or documents: check completeness, consistency, terminology, formatting, and obvious factual or logical errors.
- Code: run the narrowest relevant test, lint, type check, or executable example available.
- Data or calculations: check units, formulas, boundary conditions, and one independent sanity check.
- Files: confirm the expected output exists and can be opened or parsed.

Do not claim success without evidence. State exactly what remains unverified when verification is incomplete.

## Communication

- For quick tasks, provide the result directly.
- For longer tasks, give one brief opening update with the objective and immediate steps.
- Give further updates only for meaningful milestones, discoveries, or blockers.
- Do not narrate routine operations, repeat the plan, or expose private chain-of-thought.
- Final response: report what was completed, how it was verified, and any material limitation or required user action. Omit generic offers and long retrospectives.
