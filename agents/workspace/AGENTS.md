# AGENTS.md

Guidelines for AI agents working in this workspace.

## Critical Rules

### Git Operations - READ CAREFULLY

**NEVER push code to remote repositories.** Commits are the furthest you go.

- You do NOT have GitHub authentication
- Any operation requiring GitHub auth will fail and waste context
- After committing, ALWAYS provide the appropriate command for the user to run:

```bash
# Example: provide commands like these for the user to execute
git push origin <branch>
git push -u origin <branch>
gh pr create --title "..." --body "..."
```

### What You CAN Do
- Stage files (`git add`)
- Create commits (`git commit`)
- Create and switch branches (`git checkout -b`, `git switch`)
- View status, logs, diffs

### What You MUST NOT Do
- `git push` (any form)
- `gh pr create` / `gh pr merge`
- Any `gh` command that requires authentication
- Force operations on remote (`push --force`, etc.)

## General Best Practices

### Project Discovery
- Each subdirectory may be a separate project with its own conventions
- Look for project-specific `AGENTS.md`, `CLAUDE.md`, or `README.md` files
- Respect per-project configurations when they exist

### Before Making Changes
- Read relevant code before modifying it
- Understand the existing patterns and conventions of each project
- Check for existing tests and maintain test coverage

### Code Quality
- Follow the existing code style of each project
- Don't over-engineer or add unrequested features
- Keep changes minimal and focused on the task at hand
- Don't add comments, docstrings, or type annotations to unchanged code

### Communication
- Be concise - this is a CLI environment
- When providing commands for the user to run, use copyable code blocks
- If a task requires auth or permissions you lack, clearly state what the user needs to do

## Project-Specific Overrides

Individual projects may contain their own `AGENTS.md` or `CLAUDE.md` files. Those project-specific instructions take precedence over this file for work within that project.
