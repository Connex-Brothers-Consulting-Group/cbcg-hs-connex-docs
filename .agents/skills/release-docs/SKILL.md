---
name: release-docs
description: "SOC 2 Type II compliant documentation release and gitflow protocol"
---

# release-docs Skill

Governs git commit, Pull Request, and live deployment workflows for the documentation repository.

## Release Workflows

### 1. Working Branch Routine Push (Zero Build Trigger)
For iterative edits, formatting, and drafts:
```bash
./scripts/git-release.sh "docs(guide): update workspace management walkthrough" push
```

### 2. Pull Request Gate (Human-In-The-Loop)
When changes are ready for human administrator review:
```bash
./scripts/git-release.sh "feat(security): document hardware kill switch error codes" pr
```
- Executes `pre-release-check.sh`
- Creates GitHub PR to `main`
- Displays clickable PR review link in chat prompt

### 3. Production Live Deployment Gate (Explicit Approval Required)
Only upon explicit user instruction to deploy live to Mintlify:
```bash
./scripts/git-release.sh "feat(security): document hardware kill switch error codes" main
```
- Merges to `main`
- Creates release tag `v{VERSION}`
- Pushes to `origin/main` for live portal synchronization
