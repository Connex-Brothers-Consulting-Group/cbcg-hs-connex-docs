# Rule 01: Dual-Theme Color Isolation & Zero !important Policy

## 1. Absolute Zero `!important` Policy (Standard 02-01)
- The use of `!important` is strictly forbidden across all documentation stylesheets (`style.css`).
- All specificity conflicts must be resolved through structured CSS selector specificity hierarchies.
- Example pattern:
  ```css
  /* Correct: Pure Selector Specificity Hierarchy */
  html:not(.dark) body header#navbar .navbar-link a {
    color: #0f172a;
  }
  html.dark body header#navbar .navbar-link a {
    color: #f8fafc;
  }
  ```

## 2. Strict Dual-Theme Highlight Separation
- **Light Mode (`#003DB3`)**:
  - Primary Highlight: Solid Navy Mirage (`#003DB3` / `#002f8c`)
  - Navbar Background: Pure White (`#ffffff`)
  - Accent Borders: `#e2e8f0`
  - Zero orange or amber elements are permitted in light mode.
- **Dark Mode (`#D55E08`)**:
  - Primary Highlight: CONNEX Orange (`#D55E08` / `#f97316`)
  - Navbar Background: Translucent Frost Dark Glass (`rgba(13, 10, 15, 0.85)`)
  - Accent Borders: `rgba(255, 255, 255, 0.08)`
  - Zero blue elements are permitted in dark mode.

## 3. Typography & Responsive Design
- **Font Stack**: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif.
- **Weights**: Body weight 300/400; Section headers 500/600. Avoid crude 700/800 bolding in paragraph text.
- **Line Heights**: `1.6` for long-form documentation prose; `1.4` for compact cards.
