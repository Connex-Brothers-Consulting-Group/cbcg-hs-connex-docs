# CONNEX Cloud OS Documentation Governance & Standards

```
========================================================================================
   CONNEX CLOUD OS DOCUMENTATION CONSTITUTION: ENTERPRISE SSOT & AESTHETICS (V31.0)
   NEXUS LAB 126 CONSTITUTIONAL & 88 MASTER ENGINEERING STANDARDS ALIGNED
========================================================================================
```

## SECTION I. DOCUMENTATION ARCHITECTURE & ENGINE

- **Engine**: [Mintlify](https://mintlify.com) `mint` theme.
- **Root SSOT Config**: `docs.json`
- **Global Design System**: `style.css` (Paired Dual-Theme: Solid Navy Mirage `#003DB3` in Light / Frost Glass `#D55E08` in Dark)
- **Asset Directory**: `ci/` (Official active WebP branding assets only: `logo-light.webp`, `logo-dark.webp`, `favicon-light.webp`, `favicon-dark.webp`)

---

## SECTION II. ICONOGRAPHY & EMOJI GOVERNANCE (STANDARD 02-02)

### Article 1 (Raw Unicode Emoji Absolute Ban)
1. **Raw Emoji Ban**: Crude raw unicode emojis (🚀, 💡, 🔄, 🔒, 📊, ⚡, ⚠️, etc.) in documentation headings, paragraphs, cards, steps, callouts, and table cells are **strictly prohibited**.
2. **Enterprise Demeanor**: Maintain a clean, disciplined, and world-class quiet luxury enterprise tone across all technical pages.

### Article 2 (Lucide Vector Iconography SSOT)
1. **Lucide Icons Only**: All interface iconography must strictly use crisp vector icon names from the official [Lucide Icon library](https://lucide.dev/icons).
2. **Mintlify Native Component Support**:
   - **Cards**: `<Card title="..." icon="shield-check" href="...">`
   - **Steps**: `<Step title="..." icon="terminal">`
   - **Tabs**: `<Tab title="..." icon="code">`
   - **Inline Icons**: `<Icon icon="sparkles" />`, `<Icon icon="database" />`
   - **Anchors (`docs.json`)**: `"icon": "globe"`, `"icon": "shield-check"`
3. **Fidelity Guarantee**: Mintlify natively resolves and renders all Lucide vector SVG icons at infinite resolution with zero distortion across Retina and 4K displays.

---

## SECTION III. COLOR ISOLATION & DUAL-THEME SYMMETRY

### Article 3 (Strict Mode Highlight Separation)
1. **Light Mode (#003DB3)**:
   - Primary Highlight: Solid Navy Mirage (`#003DB3` / `#002f8c`)
   - Header Background: Pure White (`#ffffff`)
   - Zero Orange elements permitted in Light Mode.
2. **Dark Mode (#D55E08)**:
   - Primary Highlight: CONNEX Orange (`#D55E08` / `#f97316`)
   - Header Background: Translucent Frost Dark Glass (`rgba(13, 10, 15, 0.85)`)
   - Zero Blue elements permitted in Dark Mode.

---

## SECTION IV. MODULAR FOLDER STRUCTURE & ROUTING

```text
cbcg-hs-docs/
├── ci/                          # Official CI & Branding Assets (WebP only)
├── get-started/                 # Quickstart, Architecture & Foundation
├── features/                    # CoWorx, AI Agent, VFS Core Modules
├── governance/                  # Data Sovereignty, Zero-Trust Auth, Compliance
├── support/                     # Releases, Notices, FAQ
├── docs.json                    # Mintlify Master Configuration
├── index.mdx                    # Canonical Landing Page (/)
└── style.css                    # Master CSS Styling Sheet
```
