# Rule 03: Eight-Tab Information Architecture & 1:1 Isolated Sidebars

## 1. Canonical 8-Tab Navigation Structure (`docs.json`)
The platform documentation is organized across exactly 8 authoritative top-level navigation tabs:
1. **`CONNEX`**:
   - `Get Started`: Platform Overview, Quickstart, System Architecture
   - `Core Engines`: L1 Front-Door Gatekeeper, Tiki-Taka Ultra-Low Latency, Dynamic API Mining, Agentic RCAG
2. **`User Guides`**:
   - `Core User Manuals`: Workspace Management, AI Agent Manual, CoWorx Collaboration, Brain X Memory, Studio VFS
3. **`Use Cases`**:
   - `Enterprise Solutions`: Business & Management, Legal & Tax, R&D & Patents, Education, Healthcare
4. **`Pricing`**:
   - `Plans & Capital Allocation`: Subscription Plans, Pay-As-You-Go, Token Capital Allocation
5. **`Security`**:
   - `Trust & Data Sovereignty`: SOC 2 Type II Controls, Multi-Region Data Sovereignty, Zero-Trust Authentication, Cloud Security & Kill Switch
6. **`Compliance`**:
   - `Legal & Terms`: Terms of Service, Privacy Policy, Billing & Refund Policy, Marketing Policy
7. **`Resources`**:
   - `Support & Operations`: Documentation Center Guide, 24/7 Enterprise Support Desk, Platform Notices, Frequently Asked Questions, Release Notes
8. **`Developers`**:
   - `Public APIs & Protocols`: REST API Reference, WebSocket Streaming, Webhooks
   - `Model Context Protocol (MCP)`: MCP Server Architecture, Tools & Resources, Enterprise MCP Client

## 2. 1:1 Clean Sidebar Isolation
- **No Cross-Tab Group Duplication**: Sidebars must never replicate groups across tabs. Selecting a tab displays exclusively that tab's dedicated content.
- **Flush Left-Alignment**: All sidebar navigation links must align flush to the left; avoid isolated frontmatter `icon` declarations on individual sub-pages that create awkward indentation offsets.
