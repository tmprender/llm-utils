# AGENTS.md – Workspace‑wide rules

## Sub‑agent discovery
- The **continue** plugin will automatically look inside `llm-utils/agents/` for folders that each contain an `AGENTS.md`.
- Read `AGENTS.md` files for sub-agent instructions.

## Project‑specific AGENTS.md
- Any subdirectory of the workspace may ship its own `AGENTS.md`.  
- Rules defined in a sub‑project’s `AGENTS.md` are merged with these workspace rules; project rules take precedence.
- To override a workspace rule in a particular project, add a `# rules` section to the project’s `AGENTS.md` and define the rule there.

```bash
# Example – add a project‑specific rule in `tlp-dev/AGENTS.md`
#   ├─ tmp-dev/
#   │   └─ AGENTS.md
#   │       # rules
#   │       export LLM_MODEL=gpt-4o-mini-16k
```

```md
- If a project does **not** need a custom rule, simply omit the `# rules` section – the workspace defaults will apply.

