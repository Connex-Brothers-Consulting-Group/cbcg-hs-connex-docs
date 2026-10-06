# CONNEX Cloud OS Documentation Governance & Standards

> **CONNEX CLOUD OS DOCUMENTATION CONSTITUTION: ENTERPRISE SSOT & AESTHETICS (V31.0)**  
> *NEXUS LAB 126 Constitutional & 88 Master Engineering Standards Aligned*  
> *Flagship Ecosystem of HybridSphere | Connex Brothers Consulting Group Inc.*

## SECTION I. DOCUMENTATION ARCHITECTURE & ENGINE

- **Engine**: [Mintlify](https://mintlify.com) `mint` theme.
- **Root SSOT Config**: `docs.json` (`"icons": { "library": "lucide" }`)
- **Global Design System**: `style.css` (Paired Dual-Theme: Solid Navy Mirage `#003DB3` in Light / Frost Glass `#D55E08` in Dark)
- **Asset Directory**: `ci/` (Official active WebP branding assets only: `logo-light.webp`, `logo-dark.webp`, `favicon-light.webp`, `favicon-dark.webp`)

---

## SECTION II. ICONOGRAPHY & EMOJI GOVERNANCE (STANDARD 02-02)

### Article 1 (Raw Unicode Emoji Absolute Ban)
1. **Raw Emoji Ban**: Crude raw unicode emojis in documentation headings, paragraphs, cards, steps, callouts, and table cells are **strictly prohibited**.
2. **Enterprise Demeanor**: Maintain a clean, disciplined, and world-class quiet luxury enterprise tone across all technical pages.

### Article 2 (Lucide Vector Iconography SSOT)
1. **Lucide Icons Only**: All interface iconography must strictly use crisp vector icon names from the official [Lucide Icon library](https://lucide.dev/icons).
2. **Mintlify Native Component Support**:
   - **Cards**: `<Card title="..." icon="shield-check" href="...">`
   - **Steps**: `<Step title="..." icon="terminal">`
   - **Tabs**: `<Tab title="..." icon="code">`
   - **Inline Icons**: `<Icon icon="sparkles" />`, `<Icon icon="database" />`
   - **Anchors (`docs.json`)**: `"icon": "globe"`, `"icon": "github"`
3. **Fidelity Guarantee**: Mintlify natively resolves and renders all Lucide vector SVG icons at infinite resolution with zero distortion across Retina and 4K displays.

---

## SECTION III. COLOR ISOLATION, CASCADE & ZERO !IMPORTANT GOVERNANCE

### Article 3 (Strict Mode Highlight Separation)
1. **Light Mode (#003DB3)**:
   - Primary Highlight: Solid Navy Mirage (`#003DB3` / `#002f8c`)
   - Header Background: Pure White (`#ffffff`)
   - Zero Orange elements permitted in Light Mode.
2. **Dark Mode (#D55E08)**:
   - Primary Highlight: CONNEX Orange (`#D55E08` / `#f97316`)
   - Header Background: Translucent Frost Dark Glass (`rgba(13, 10, 15, 0.85)`)
   - Zero Blue elements permitted in Dark Mode.

### Article 3-1 (Zero !important Policy & CSS Specificity SSOT - Standard 02-01)
1. **Zero `!important` Policy**: The use of `!important` is strictly forbidden across all documentation stylesheets (`style.css`).
2. **Cascade & High-Specificity Architecture**: All styling overrides against default theme and utility classes must be resolved purely through structured CSS selector specificity (e.g., `html:not(.dark) body header#navbar .navbar-link a`, `html:not(.dark) body [data-component-part="card-icon"]`).

---

## SECTION IV. MODULAR FOLDER STRUCTURE & ROUTING

```text
cbcg-hs-docs/
├── ci/                          # Official CI & Branding Assets (WebP only)
├── get-started/                 # Quickstart, Architecture & Foundation
├── features/                    # CoWorx, AI Agent, Brain X, VFS Core Modules
├── guide/                       # 5 Persistent User Manuals
├── use-cases/                   # 5 Industry Solutions
├── pricing/                     # Pricing & Token Capital Allocation
├── governance/                  # Data Sovereignty, Cloud Security, Kill Switch, Terms
├── support/                     # Releases, Notices, FAQ
├── developers/                  # Public APIs & MCP Server Protocols
├── docs.json                    # Mintlify Master Configuration
├── index.mdx                    # Canonical Landing Page (/)
└── style.css                    # Master CSS Styling Sheet
```

---

## SECTION V. ENTERPRISE MERMAID DIAGRAM STYLING STANDARD (PURE TRANSPARENT LINE-ART SSOT)

### Article 4 (Solid Fill Ban & Zero Text Background Principle)
1. **Solid Color Fill Ban**: Heavy solid fill blocks (`fill:#1E293B`, `fill:#007CFF`) and colored subgraph backgrounds are strictly prohibited.
2. **Pure Transparent Line-Art**: All diagram nodes, clusters, and containers must maintain 100% transparent backgrounds (`fill: transparent`).
3. **Zero Background Behind Text**: Text elements, tspans, div labels, and edge labels must never display gray or colored background rectangles (`edgeLabelBackground: transparent`). All text renders directly and cleanly over the page background.

### Article 5 (Mode Highlight Line-Art & Base Theme Directive)
For diagrams rendered on GitHub (such as `README.md`), declare the base theme init directive:

```mermaid
%%{init: {
  'theme': 'base',
  'themeVariables': {
    'background': 'transparent',
    'primaryColor': 'transparent',
    'primaryBorderColor': '#003DB3',
    'primaryTextColor': '#003DB3',
    'secondaryColor': 'transparent',
    'secondaryBorderColor': '#003DB3',
    'secondaryTextColor': '#003DB3',
    'tertiaryColor': 'transparent',
    'tertiaryBorderColor': '#003DB3',
    'tertiaryTextColor': '#003DB3',
    'clusterBkg': 'transparent',
    'clusterBorder': '#003DB3',
    'lineColor': '#003DB3',
    'textColor': '#003DB3',
    'edgeLabelBackground': 'transparent',
    'nodeBorder': '#003DB3',
    'nodeTextColor': '#003DB3',
    'fontFamily': 'Inter, -apple-system, BlinkMacSystemFont, sans-serif',
    'fontSize': '12px'
  }
}}%%

```

---

## SECTION VI. DATA SOVEREIGNTY & CRYPTOGRAPHIC KILL SWITCH GOVERNANCE

### Article 6 (Zero-Knowledge Envelope Encryption & KMS Kill Switch Standard)
1. **Two-Tier Envelope Key Architecture**: All sensitive files and VFS records are protected by random AES-256-GCM Data Encryption Keys (DEKs) wrapped by Customer-Managed Encryption Keys (CMEKs) residing in cloud KMS.
2. **Hardware Kill Switch (`KeyAccessRevokedError` → HTTP 423)**: If a customer disables or revokes their key in Cloud KMS, all subsequent reads immediately fail closed with HTTP 423 Locked.
3. **Zero Plaintext Lingering**: Plaintext DEKs are cached exclusively in ephemeral Python `ContextVar` per request and never persisted. Envelope-encrypted files explicitly bypass intermediate storage caches (GCS cache bypass) to guarantee zero-delay revocation enforcement.
4. **Fail-Closed Write Invariant (`NoEncryptionContextError` → HTTP 412)**: Unencrypted plaintext writes are categorically prohibited.
