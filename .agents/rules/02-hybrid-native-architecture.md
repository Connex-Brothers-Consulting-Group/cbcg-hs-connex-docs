# Rule 02: Hybrid Native Architecture & Lucide Iconography Standard

## 1. Mintlify Native Components First (Stripe & Anthropic Standard)
- Express system topologies, data flows, infrastructure pipelines, and feature walkthroughs using Mintlify native components:
  - **Multi-Step Workflows**: `<Steps>` with child `<Step title="..." icon="...">`
  - **Structured Grids**: `<CardGroup cols={2}>` with child `<Card title="..." icon="..." href="...">`
  - **Multi-Language / Tabbed Context**: `<Tabs>` with child `<Tab title="..." icon="...">`
  - **Collapsible Deep Dives**: `<AccordionGroup>` with child `<Accordion title="..." icon="...">`
  - **Inline Highlights**: `<Icon icon="..." />`

## 2. Iconography & Raw Unicode Emoji Absolute Ban (Standard 02-02)
- **Raw Unicode Emojis Banned**: Never use emojis (🚀, 💡, 🛡️, ⚙️, etc.) in MDX page titles, section headings, card titles, step titles, or tables.
- **Lucide Vector Icons SSOT**: Always use official Lucide icon names (`shield-check`, `cpu`, `database`, `server`, `globe`, `lock`, `brain`, `key`, `terminal`, `layers`, `file-text`, `sparkles`).
- **Mintlify Native Guarantee**: Lucide vector icons automatically adapt to active light/dark theme colors with infinite resolution across Retina and 4K displays.

## 3. Sequence & State Diagrams (Mermaid Protocol)
- Use standard Mermaid syntax (`sequenceDiagram`, `stateDiagram`) for sequential API handshakes (e.g., ticket exchanges) or state machines.
- **Zero `%%{init: ...}%%` Directives**: Never hardcode static theme init directives inside MDX files to preserve runtime theme reactivity.
