---
name: verify-docs
description: "Autonomous local verification harness for CONNEX Cloud OS documentation portal"
---

# verify-docs Skill

Execute the complete documentation verification suite to guarantee zero-defect integrity before requesting review or releasing.

## Verification Checklist

1. **Python-Based Verification Harness**:
   ```bash
   python3 scripts/verify-docs.py
   ```
   Verifies:
   - `docs.json` valid JSON syntax
   - 8-Tab navigation hierarchy (`CONNEX`, `User Guides`, `Use Cases`, `Pricing`, `Security`, `Compliance`, `Resources`, `Developers`)
   - 100% two-way synchronization between physical `.mdx` files and `docs.json` routes
   - Zero `!important` declarations in `style.css`
   - Zero raw unicode emojis across all MDX pages
   - Zero hardcoded Mermaid `%%{init:` directives

2. **Pre-Release Quality Audit Gate**:
   ```bash
   ./scripts/pre-release-check.sh
   ```

3. **Autonomous Self-Healing**:
   - If missing pages are detected, register them in `docs.json` under the appropriate tab/group.
   - If `!important` is detected in `style.css`, refactor using high-specificity selector hierarchy.
   - If raw emojis are found, replace them with official Lucide vector icons (`<Icon icon="..." />` or component `icon="..."`).
