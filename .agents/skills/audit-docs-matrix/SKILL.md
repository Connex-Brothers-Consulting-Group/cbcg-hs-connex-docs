---
name: audit-docs-matrix
description: "Comprehensive 41-page MDX architecture and navigation audit skill"
---

# audit-docs-matrix Skill

Performs deep matrix auditing across all 41 MDX documentation pages, ensuring design system compliance, component syntax correctness, and link integrity.

## Audit Matrix

| Dimension | Verification Target | Standard |
| :--- | :--- | :--- |
| **Information Architecture** | 8 Canonical Tabs | Exact mapping in `docs.json` |
| **Sidebar Isolation** | 1:1 Tab-to-Group Mapping | Zero duplicate user guides across tabs |
| **Component Standard** | Native Mintlify Components | `<Steps>`, `<CardGroup>`, `<Tabs>`, `<AccordionGroup>` |
| **Iconography** | Vector Lucide Icons | Official Lucide names, 0 raw emojis |
| **Theme Symmetry** | Light (`#003DB3`) / Dark (`#D55E08`) | Zero `!important`, high-specificity selectors |
| **Security Guarantees** | Envelope Encryption & Kill Switch | AES-256-GCM, HTTP 423, HTTP 412, PIPA/GDPR isolation |

## Audit Execution
```bash
python3 scripts/verify-docs.py
```
