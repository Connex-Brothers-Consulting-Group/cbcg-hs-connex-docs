# CONNEX Cloud OS Documentation Governance & Standards

```
========================================================================================
   CONNEX CLOUD OS DOCUMENTATION CONSTITUTION: ENTERPRISE SSOT & AESTHETICS (V31.0)
   NEXUS LAB 126 CONSTITUTIONAL & 88 MASTER ENGINEERING STANDARDS ALIGNED
   Flagship Ecosystem of HybridSphere | Connex Brothers Consulting Group Inc.
========================================================================================
```

> **Antigravity Customization Architecture**:
> - **Master SSOT**: This document (`.agents/AGENTS.md`)
> - **Domain Rules**: [01-dual-theme-and-zero-important](rules/01-dual-theme-and-zero-important.md), [02-hybrid-native-architecture](rules/02-hybrid-native-architecture.md), [03-eight-tab-information-architecture](rules/03-eight-tab-information-architecture.md), [04-security-and-killswitch-governance](rules/04-security-and-killswitch-governance.md), [05-safety-and-release-governance](rules/05-safety-and-release-governance.md)
> - **Workflow Skills**: [verify-docs](skills/verify-docs/SKILL.md), [release-docs](skills/release-docs/SKILL.md), [audit-docs-matrix](skills/audit-docs-matrix/SKILL.md)

---

## SECTION I. APEX CONSTITUTION & HITL SYMBIOTIC COEXISTENCE

### Article 1 (The Fallacy of Omniscience & The Symbiotic Axiom - Constitution Charter I)
1. **The Fallacy of Omniscience**: Large Language Models (LLMs) are not omniscient oracles. When authoring technical specifications, API schemas, and architecture documentation, LLMs are prone to context loss, speculative drift, and markdown formatting defects. Documentation accuracy must never be left to unchecked probabilistic reasoning.
2. **The Symbiotic Axiom**: CONNEX Cloud OS Documentation is a world-class enterprise portal combining **the 30-year executive vision, domain clarity, and legal rigor of Human Intelligence (HI)** with **the semantic precision, rapid MDX structuring, and high-density technical authoring of Artificial Intelligence (AI)**.
   - **Sovereign (HI)**: Product taxonomy, statutory compliance boundaries (PIPA, CCPA, GDPR), brand aesthetics, and authoritative approval of release publications.
   - **Partner (AI)**: MDX page generation, Lucide vector icon taxonomy enforcement, 1:1 sidebar isolation mapping, and automated pre-release verification harness execution.

### Article 2 (Semantic Kernel Three-Pillar Governance & Zero-Ambiguity Gate - Constitution Charter II)
1. **Native Domain (Deterministic SSOT Hardcode)**: `docs.json` navigation schemas, `style.css` dual-theme design tokens, legal terms, and API route signatures are 100% deterministic code governed by strict static validation.
2. **Semantic Domain (AI Technical Content Domain)**: Architectural summaries, step-by-step onboarding walkthroughs, code snippets, and feature deep-dives are generated with extreme aesthetic and structural rigor.
3. **HITL Ambiguity Gate**: If any ambiguity is detected regarding product naming, navigation placement, pricing tiers, or security guarantees, the agent MUST NEVER guess; it must immediately pause and confirm with the human administrator.

### Article 3 (Quiet Luxury & The Invisible Butler Aesthetic - Constitution Charters III & V)
1. **The Invisible Butler**: Gaudy icons, distracting raw unicode emojis, clunky borders, and jarring color collisions are permanently eradicated. The documentation portal reflects a calm, disciplined, high-density, and prestigious enterprise demeanor.
2. **Dual-Spectrum Readability**:
   - **Executive & Investor Summary**: High-level value propositions, ROI capital allocation, and zero-trust trust frameworks.
   - **Engineering & Developer Rigor**: Exact gRPC/REST payloads, WebSocket frame schemas, Lucide vector icons, and runnable cURL examples.

### Article 4 (AWS 10x Frontier Habits & Zero-Assumption Discipline)
1. **AWS 10x Frontier Habits**:
   - **Habit 1: Context Investment & Pruning**: Maintain `.agents/AGENTS.md` and `docs.json` as the Single Source of Truth (SSOT).
   - **Habit 2: Slow Down to Go Fast (Clean MDX Hygiene)**: Write clean, modular, and maintainable MDX files adhering strictly to Mintlify standards.
   - **Habit 3: Feed the Agent, Don't Babysit**: Provide deterministic verification scripts (`scripts/verify-docs.py`) for autonomous zero-defect self-healing.
   - **Habit 4: Spec-First**: Define page navigation hierarchy and frontmatter metadata before authoring body content.
   - **Habit 5: Shift-Left Testing**: Verify page links, zero `!important` CSS rules, and emoji bans locally prior to submitting releases.
2. **Four Rules of Zero-Assumption Discipline**:
   - **No Speculation**: Never assume a route exists or an icon renders; verify against `docs.json` and the official Lucide icon registry.
   - **End-to-End Link Tracing**: Trace all cross-page links (`href="/guide/workspace"`) to physical files.
   - **Verification Transparency**: Candidly separate verified items from pending reviews in audit reports.

---

## SECTION II. ABSOLUTE SAFETY GATES & ZERO-SHORTCUT DISCIPLINE

### Article 5 (Absolute Git Safety Mandate)
1. **Destructive Commands Strictly Prohibited**: Commands risking data loss or state corruption (`git reset --hard`, `git branch -m`, destructive `git checkout`, force operations) are strictly prohibited without prior explicit user authorization.
2. **State Auditing & Korean Explanation**: If branch switching or state reconciliation is necessary, inspect `git diff`, explain potential risks in Korean, and obtain distinct user approval.

### Article 6 (Terminal Server Execution & Browser Subagent Prohibition)
1. **Terminal Server Launch Prohibited**: The agent MUST NEVER start, restart, or run local Mintlify dev servers (e.g., `mintlify dev`, `npx mintlify dev`) via terminal tools (`run_command`). All local development servers are managed independently by the user in dedicated IDE terminals.
2. **Browser Subagent Launch Prohibited**: The agent MUST NEVER trigger `browser_subagent` or launch automated browser windows without explicit user request.

### Article 7 (4-Step Zero-Shortcut Engineering Process)
Skipping deep analysis or local verification for the sake of token economy or speed is strictly prohibited:
- **Step 1: Exhaustive Investigation**: Deeply inspect `docs.json`, `style.css`, and related `.mdx` pages.
- **Step 2: Spec-First Proposal & Consent**: Present structure and MDX component layouts to the user; obtain explicit consent prior to making edits.
- **Step 3: Shift-Left Verification & Self-Healing**: Run `./scripts/pre-release-check.sh` (`scripts/verify-docs.py`); autonomously resolve all detected errors.
- **Step 4: Approved Commit & Deploy**: Obtain explicit user approval before committing or pushing changes.

### Article 7-1 (NEXUS LAB 126 3대 무결성 공학 철칙 - Anti-Fraud Engineering Standards)
1. **임의의 `sleep()`을 통한 동기화 영구 금지**:
   - 시간차나 렌더링 지연을 덮기 위해 스크립트나 코드에 `sleep()`을 단 0.1초라도 넣는 행위는 사기(Fraud)입니다. 시간차가 나면 프로토콜(이벤트, 명시적 파일 검증)로 풀어야지, 절대로 스레드를 임의로 재우지 않습니다.
2. **핵심 상태 변경의 백그라운드 프로세스 방치 금지**:
   - 문서 라우팅 및 스타일 변경 후 결과 확인을 "알아서 되겠지" 하고 방치하지 않고, 확실히 검증 스크립트 통과를 확인한 후 다음 단계로 넘깁니다.
3. **Mock 테스트 맹신 금지 & 실제 실측 검증**:
   - 가상의 검증 대신 실제 41개 MDX 파일과 `docs.json`의 1:1 매핑 상태, `style.css`의 `!important` 0건을 스크립트로 직접 실측하여 숫자로 증명합니다.

---

## SECTION III. RELEASE & VERSION GOVERNANCE (GITFLOW RITUAL)

### Article 8 (SSOT Version Authority & Dedicated Working Branch)
1. **SSOT Version Authority**: The root `VERSION` file is the sole authoritative source of truth (e.g., `3.5.0`).
2. **Dedicated Branch Naming**: Release working branches are strictly named `hs-docs-v{VERSION}`.
3. **Commitlint Standard**: All commit messages must strictly conform to Conventional Commits standards (e.g., `feat(docs): add mcp server protocol specs`, `fix(style): resolve light mode card border contrast`).

### Article 9 (SOC 2 Type II Documentation Release Protocol - `./scripts/git-release.sh`)
1. **Working Branch Push Mode (Zero Deploy Trigger)**:
   - Routine content updates, typo fixes, and refactoring execute on working branch `hs-docs-v{VERSION}`.
   - Execute `./scripts/git-release.sh "<commit message>" push`.
   - Automatically runs `./scripts/pre-release-check.sh`, appends `[skip ci]`, commits, and pushes to origin.
2. **Stage 1 (Application PR Gate - Human-In-The-Loop)**:
   - When documentation is ready to be merged, execute `./scripts/git-release.sh "<commit message>" pr`.
   - Runs `./scripts/pre-release-check.sh`, creates/updates GitHub Pull Request to `main`, and displays the clickable PR Review link.
   - The human administrator reviews and approves the PR on GitHub.
3. **Stage 2 (Production Live Release Gate)**:
   - Upon explicit user instruction, execute `./scripts/git-release.sh "<commit message>" main`.
   - Merges into `main`, publishes release tag `v{VERSION}`, and pushes to `origin/main` to trigger live Mintlify synchronization.
4. **Absolute Release Mandate**: Releases must exclusively use `./scripts/git-release.sh`. Manual tag pushes or manual git merges are strictly forbidden.

---

## SECTION IV. DUAL-THEME COLOR ISOLATION, CASCADE & ZERO !IMPORTANT GOVERNANCE

### Article 10 (Strict Mode Highlight Separation)
1. **Light Mode (`#003DB3`)**:
   - Primary Highlight: Solid Navy Mirage (`#003DB3` / `#002f8c`)
   - Header Background: Pure White (`#ffffff`)
   - Zero Orange/Amber elements permitted in Light Mode.
2. **Dark Mode (`#D55E08`)**:
   - Primary Highlight: CONNEX Orange (`#D55E08` / `#f97316`)
   - Header Background: Translucent Frost Dark Glass (`rgba(13, 10, 15, 0.85)`)
   - Zero Blue elements permitted in Dark Mode.

### Article 11 (Zero `!important` Policy & CSS Specificity SSOT - Standard 02-01)
1. **Zero `!important` Policy**: The use of `!important` is strictly forbidden across all documentation stylesheets (`style.css`).
2. **Cascade & High-Specificity Architecture**: All styling overrides against default theme and utility classes must be resolved purely through structured CSS selector specificity:
   ```css
   /* Correct: Pure Specificity Cascade */
   html:not(.dark) body header#navbar .navbar-link a {
     color: #0f172a;
   }
   html.dark body header#navbar .navbar-link a {
     color: #f8fafc;
   }
   ```

---

## SECTION V. 8-TAB INFORMATION ARCHITECTURE & 1:1 ISOLATED SIDEBARS

### Article 12 (Authoritative 8-Tab Navigation Structure)
Platform documentation is organized across exactly 8 authoritative top-level navigation tabs in `docs.json`:
1. **`CONNEX`**: Quickstart, System Architecture, Core Intelligence Engines (L1 Gatekeeper, Tiki-Taka, Dynamic API Mining, Agentic RCAG).
2. **`User Guides`**: Dedicated top tab containing the 5 persistent core user manuals (Workspace, Agent, CoWorx, Brain X, Studio VFS).
3. **`Use Cases`**: 5 industry-tailored enterprise solutions (Business & Management, Legal & Tax, R&D & Patents, Education, Healthcare).
4. **`Pricing`**: Subscription plans, Pay-As-You-Go metrics, and Token Capital Allocation Governance.
5. **`Security`**: Dedicated technical cloud security tab (SOC 2 Controls Ledger, PIPA/CCPA Data Sovereignty, Zero-Trust Auth, KMS Envelope Encryption & Hardware Kill Switch).
6. **`Compliance`**: Dedicated legal and regulatory policies tab (Terms of Service, Privacy Policy, Billing & Refund Policy, Marketing Policy).
7. **`Resources`**: Operational support, Docs Center Guide, 24/7 Enterprise Support Desk, Notices, FAQ, and Release Notes.
8. **`Developers`**: Public REST APIs, WebSocket streaming protocol, Webhooks, and Model Context Protocol (MCP) server specifications.

### Article 13 (1:1 Clean Sidebar Isolation & Flush Left-Alignment)
1. **Zero Duplicate Groups**: Sidebars must never replicate identical groups across tabs. Each tab presents strictly its own dedicated content.
2. **Flush Left-Alignment Standard**: All sidebar links must align flush to the left; avoid isolated frontmatter `icon` declarations on individual sub-pages that create awkward indentation offsets.

---

## SECTION VI. MINTLIFY HYBRID NATIVE ARCHITECTURE & ICONOGRAPHY GOVERNANCE

### Article 14 (Mintlify Native Architecture Components - Stripe & Anthropic Standard)
1. **Native Component-First Principle**: System architectures, infrastructure topologies, and data lifecycles must be declared primarily using Mintlify native components (`<Steps>`, `<CardGroup>`, `<Tabs>`, `<AccordionGroup>`) coupled with Lucide vector icons.
2. **Infinite Resolution & Zero CSS Hacking**: Mintlify native components guarantee 100% reactive dual-theme adaptation (Solid Navy `#003DB3` in Light / CONNEX Orange `#D55E08` in Dark), 60 FPS mobile responsiveness, full accessibility, and `Cmd+K` global search indexability without complex CSS overrides.

### Article 15 (Raw Unicode Emoji Absolute Ban & Lucide Vector Iconography SSOT - Standard 02-02)
1. **Raw Emoji Ban**: Crude raw unicode emojis in documentation headings, paragraphs, cards, steps, callouts, and table cells are **strictly prohibited**.
2. **Lucide Icons Only**: All interface iconography must strictly use crisp vector icon names from the official [Lucide Icon library](https://lucide.dev/icons):
   - **Cards**: `<Card title="..." icon="shield-check" href="...">`
   - **Steps**: `<Step title="..." icon="terminal">`
   - **Tabs**: `<Tab title="..." icon="code">`
   - **Inline Icons**: `<Icon icon="sparkles" />`, `<Icon icon="database" />`

### Article 16 (Clean Sequence & State Diagram Protocol)
1. **Targeted Flow Applications**: Sequential API handshakes or state transitions use clean, standard Mermaid syntax (`sequenceDiagram`, `stateDiagram`) without hardcoded init directives.
2. **Zero `%%{init: ...}%%` Hardcoding**: Never embed static theme init directives inside MDX files to preserve native runtime theme flexibility.

---

## SECTION VII. DATA SOVEREIGNTY, KMS ENVELOPE ENCRYPTION & HARDWARE KILL SWITCH GOVERNANCE

### Article 17 (Zero-Knowledge Envelope Encryption & KMS Kill Switch Standard)
1. **Two-Tier Envelope Key Architecture**: All sensitive files and VFS records are protected by random AES-256-GCM Data Encryption Keys (DEKs) wrapped by Customer-Managed Encryption Keys (CMEKs) residing in cloud KMS.
2. **Hardware Kill Switch (`KeyAccessRevokedError` → HTTP 423)**: If a customer disables or revokes their key in Cloud KMS, all subsequent reads immediately fail closed with HTTP 423 Locked.
3. **Zero Plaintext Lingering**: Plaintext DEKs are cached exclusively in ephemeral Python `ContextVar` per request and never persisted. Envelope-encrypted files explicitly bypass intermediate storage caches to guarantee zero-delay revocation enforcement.
4. **Fail-Closed Write Invariant (`NoEncryptionContextError` → HTTP 412)**: Unencrypted plaintext writes are categorically prohibited.

---

## SECTION VIII. SHIFT-LEFT LOCAL VERIFICATION & AUTONOMOUS REMEDIATION (STANDARDS VOL 8)

### Article 18 (Autonomous Local Verification Harness)
After modifying documentation or stylesheets, the agent must independently execute the following verification harness and prove zero defects before asking for user review:
1. **Automated Documentation Integrity Audit**:
   ```bash
   python3 scripts/verify-docs.py
   ```
2. **Automated Pre-Release Quality Audit Gate**:
   ```bash
   ./scripts/pre-release-check.sh
   ```

---

## SECTION IX. IMMUTABLE ETERNITY CLAUSE

### Article 19 (The Inviolable Constitutional Values)
The supreme values articulated in this constitution—**"The Primacy of Human Dignity"**, **"The Quiet Luxury of Enterprise Aesthetics"**, **"The Inviolability of Data Sovereignty"**, and **"The Perpetual Dedication to Future Generations of Researchers and Developers (Constitution Charter VII)"**—shall never be compromised or abrogated under any circumstances.
Every engineer and AI partner authoring documentation must uphold these standards to the highest caliber.
