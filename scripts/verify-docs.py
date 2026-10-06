#!/usr/bin/env python3
"""
=============================================================================
CONNEX Cloud OS Documentation Portal — Zero-Defect Local Verification Harness
NEXUS LAB 126 Constitutional & 88 Master Engineering Standards Aligned (V31.0)
=============================================================================
"""

import os
import sys
import json
import re

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
BOLD = "\033[1m"
RESET = "\033[0m"

def print_header(title):
    print(f"\n{CYAN}{BOLD}{'='*80}{RESET}")
    print(f"{CYAN}{BOLD}  {title}{RESET}")
    print(f"{CYAN}{BOLD}{'='*80}{RESET}")

def print_pass(msg):
    print(f"  {GREEN}✓ PASS:{RESET} {msg}")

def print_fail(msg):
    print(f"  {RED}✗ FAIL:{RESET} {msg}")

def print_warn(msg):
    print(f"  {YELLOW}⚠ WARN:{RESET} {msg}")

def run_verification():
    root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    docs_json_path = os.path.join(root_dir, "docs.json")
    style_css_path = os.path.join(root_dir, "style.css")
    
    total_errors = 0
    total_warnings = 0

    print_header("CONNEX CLOUD OS DOCUMENTATION INTEGRITY AUDIT")

    # 1. Audit docs.json Syntax & 8-Tab Architecture
    print(f"\n{BOLD}[1/5] Auditing docs.json & 8-Tab Architecture...{RESET}")
    if not os.path.exists(docs_json_path):
        print_fail("docs.json does not exist!")
        return 1

    try:
        with open(docs_json_path, "r", encoding="utf-8") as f:
            docs_data = json.load(f)
        print_pass("docs.json is valid JSON.")
    except Exception as e:
        print_fail(f"docs.json JSON parse error: {e}")
        return 1

    nav = docs_data.get("navigation", {})
    tabs = nav.get("tabs", [])
    tab_names = [t.get("tab") if isinstance(t, dict) else t for t in tabs]
    expected_tabs = [
        "CONNEX",
        "User Guides",
        "Use Cases",
        "Pricing",
        "Security",
        "Compliance",
        "Resources",
        "Developers"
    ]
    
    if tab_names == expected_tabs:
        print_pass(f"Authoritative 8-Tab Navigation verified: {len(tab_names)} tabs intact ({', '.join(tab_names)}).")
    else:
        print_fail(f"Tab mismatch! Expected {expected_tabs}, found {tab_names}")
        total_errors += 1

    declared_pages = set()

    def extract_pages(obj):
        if isinstance(obj, dict):
            if "pages" in obj and isinstance(obj["pages"], list):
                for p in obj["pages"]:
                    if isinstance(p, str):
                        declared_pages.add(p)
                    elif isinstance(p, dict):
                        extract_pages(p)
            for k, v in obj.items():
                if k != "pages":
                    extract_pages(v)
        elif isinstance(obj, list):
            for item in obj:
                extract_pages(item)

    extract_pages(nav)
    print_pass(f"Extracted {len(declared_pages)} page routes from docs.json navigation.")

    # 2. Audit Physical MDX Files vs docs.json Registration
    print(f"\n{BOLD}[2/5] Auditing Physical MDX Files vs Navigation SSOT...{RESET}")
    physical_mdx_files = []
    for root, dirs, files in os.walk(root_dir):
        dirs[:] = [d for d in dirs if not d.startswith(".") and d not in ("scripts", "ci", "node_modules")]
        for file in files:
            if file.endswith(".mdx") and file != "index.mdx":
                rel_path = os.path.relpath(os.path.join(root, file), root_dir)
                rel_route = rel_path[:-4]  # strip .mdx
                physical_mdx_files.append(rel_route)

    missing_in_docs = [p for p in physical_mdx_files if p not in declared_pages]
    missing_on_disk = [p for p in declared_pages if not (
        os.path.exists(os.path.join(root_dir, f"{p}.mdx")) or 
        os.path.exists(os.path.join(root_dir, f"{p}.md"))
    )]

    if not missing_in_docs:
        print_pass(f"100% of physical MDX files ({len(physical_mdx_files)}) are registered in docs.json.")
    else:
        print_fail(f"Found {len(missing_in_docs)} physical files NOT registered in docs.json: {missing_in_docs}")
        total_errors += len(missing_in_docs)

    if not missing_on_disk:
        print_pass("100% of docs.json declared routes exist on disk.")
    else:
        print_fail(f"Found {len(missing_on_disk)} routes in docs.json missing from disk: {missing_on_disk}")
        total_errors += len(missing_on_disk)

    # 3. Audit style.css for Zero !important Policy (Standard 02-01)
    print(f"\n{BOLD}[3/5] Auditing style.css for Zero !important Policy (Standard 02-01)...{RESET}")
    if os.path.exists(style_css_path):
        with open(style_css_path, "r", encoding="utf-8") as f:
            css_content = f.read()
        
        important_matches = re.findall(r'!\s*important', css_content, re.IGNORECASE)
        if len(important_matches) == 0:
            print_pass("Zero !important Policy: 0 instances found in style.css.")
        else:
            print_fail(f"Zero !important Policy VIOLATION: {len(important_matches)} instances of '!important' found in style.css!")
            total_errors += len(important_matches)
    else:
        print_fail("style.css does not exist!")
        total_errors += 1

    # 4. Audit Iconography, Raw Emojis & Clean Diagram Protocols
    print(f"\n{BOLD}[4/5] Auditing Iconography, Raw Emojis & Diagram Protocols...{RESET}")
    
    emoji_pattern = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    mermaid_init_pattern = re.compile(r'%%\{init:', re.IGNORECASE)
    
    emoji_violations = 0
    mermaid_init_violations = 0

    all_mdx = physical_mdx_files + ["index"]
    for route in all_mdx:
        mdx_path = os.path.join(root_dir, f"{route}.mdx")
        if not os.path.exists(mdx_path):
            continue
        
        with open(mdx_path, "r", encoding="utf-8") as f:
            content = f.read()

        if emoji_pattern.search(content):
            print_warn(f"Raw unicode emoji detected in {route}.mdx (Standard 02-02 Ban).")
            emoji_violations += 1

        if mermaid_init_pattern.search(content):
            print_fail(f"Hardcoded %%{{init: directive found in {route}.mdx (Standard Article 7 Ban).")
            mermaid_init_violations += 1

    if mermaid_init_violations == 0:
        print_pass("Zero hardcoded Mermaid %%{init: directives found across all MDX pages.")
    else:
        total_errors += mermaid_init_violations

    if emoji_violations == 0:
        print_pass("Zero raw unicode emojis found across all MDX pages.")
    else:
        total_warnings += emoji_violations

    # 5. Summary & Verdict
    print_header("AUDIT SUMMARY & VERDICT")
    print(f"  Total Errors:   {RED if total_errors > 0 else GREEN}{total_errors}{RESET}")
    print(f"  Total Warnings: {YELLOW if total_warnings > 0 else GREEN}{total_warnings}{RESET}")
    
    if total_errors == 0:
        print(f"\n{GREEN}{BOLD}🎉 ALL DOCUMENTATION INTEGRITY CHECKS PASSED! READY FOR PUBLICATION.{RESET}\n")
        return 0
    else:
        print(f"\n{RED}{BOLD}❌ INTEGRITY CHECKS FAILED: Please fix the {total_errors} errors before releasing.{RESET}\n")
        return 1

if __name__ == "__main__":
    sys.exit(run_verification())
