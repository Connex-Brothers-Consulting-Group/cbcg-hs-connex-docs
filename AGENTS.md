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

---

## SECTION V. ENTERPRISE MERMAID DIAGRAM STYLING STANDARD (METHOD 1 classDef SSOT)

### Article 4 (Unstyled Raw Diagrams Strictly Prohibited)
1. **Raw Default Mermaid Ban**: Unstyled Mermaid diagrams that fall back to default pastel purple/lavender palettes (`#ECECFF`) are strictly prohibited in official documentation.
2. **Quiet Luxury Enterprise Palette**: All architecture, sequence, and workflow diagrams must explicitly encode CONNEX design system tokens to ensure uniform aesthetic harmony across GitHub preview and Mintlify production.

### Article 5 (Standard classDef Palette & Semantic Tokens)
All `graph TD` and `graph LR` flowcharts must declare and bind the following standardized `classDef` tokens:

```mermaid
classDef primary fill:#007CFF,stroke:#0056B3,stroke-width:1.5px,color:#FFFFFF;
classDef enterprise fill:#1E293B,stroke:#334155,stroke-width:1.5px,color:#F8FAFC;
classDef accent fill:#0D9488,stroke:#0F766E,stroke-width:1.5px,color:#FFFFFF;
classDef storage fill:#334155,stroke:#475569,stroke-width:1.5px,color:#F1F5F9;
classDef ai fill:#6366F1,stroke:#4F46E5,stroke-width:1.5px,color:#FFFFFF;
classDef warning fill:#D97706,stroke:#B45309,stroke-width:1.5px,color:#FFFFFF;
```

- **`primary` (`#007CFF`, Cobalt)**: Client UIs, triggers, webhooks, ingress entry points, primary highlights.
- **`enterprise` (`#1E293B`, Solid Navy)**: Core API gateways, backend thin orchestrators, session handlers.
- **`accent` (`#0D9488`, Emerald/Teal)**: Event buses, Pub/Sub channels, SSE streams, broadcast routers.
- **`storage` (`#334155`, Slate/Charcoal)**: Regional Firestore (`accounts-kr`/`accounts-us`), Redis clusters, KMS CMEK, GCS.
- **`ai` (`#6366F1`, Indigo)**: Semantic Kernel, Gemini Flash/Pro LLMs, Agentic reasoning loops.
- **`warning` (`#D97706`, Amber)**: Fallback searches, failovers, contingency notifications.

### Article 6 (Sequence Diagram Theme Directive Standard)
For `sequenceDiagram` blocks where `classDef` is not supported, the `%%{init}%%` directive must be prefixed:

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'actorBkg': '#1E293B',
    'actorBorder': '#007CFF',
    'actorTextColor': '#FFFFFF',
    'actorLineColor': '#64748B',
    'signalColor': '#007CFF',
    'signalTextColor': '#F8FAFC',
    'labelBoxBkgColor': '#1E293B',
    'labelBoxBorderColor': '#007CFF',
    'labelTextColor': '#FFFFFF',
    'noteBkgColor': '#0F172A',
    'noteBorderColor': '#007CFF',
    'noteTextColor': '#F8FAFC',
    'sequenceNumberColor': '#FFFFFF'
  }
}}%%
```
