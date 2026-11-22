"""Fail when a SKILL.md still uses the v2 CLI/MCP surface.

Checks:
- ``uproc applications <token>`` uses a v3 key/group, not a v2 slug.
- Backticked MCP tool names ``<prefix>.<action>`` use a v3 surface prefix.
- The ``## Modules`` section lists v3 keys.

The v3 map is embedded below and mirrors
``backend/contracts/platform/module_suites.json``.
"""

from __future__ import annotations

import pathlib
import re
import sys

SURFACE = {
    "ingest", "treatments", "archive", "templates", "signing", "contracts", "cases",
    "purchases", "sales", "collections", "reconciliation", "investments", "taxes",
    "leads", "campaigns", "market", "content", "tables", "processing", "connectors",
    "files", "orders", "inventory", "approvals", "processes", "support", "mail",
    "candidates", "forms", "queries", "reports",
}
INTERNAL_MODULES = {"invoice-ingest", "custom-dashboard", "data-enrichment", "invoice-generator"}

CLI_TOKENS = SURFACE | INTERNAL_MODULES | {"login", "request", "module", "modules", "summary", "interactive"}
MCP_PREFIXES = SURFACE | INTERNAL_MODULES | {"leads.capture", "leads.enrich", "leads.manage", "orders.intake", "orders.tracking",
                          "treatments.classify", "treatments.convert", "treatments.unify", "treatments.number",
                          "module", "modules", "summary", "reports"}
V2_SLUGS = {
    "purchase-invoices", "sales-invoices", "debt-track", "financial-reconciliation",
    "investment-analysis", "tax-compliance", "tax-reporting", "lead-management",
    "lead-prospecting", "lead-intelligence", "campaign-automation", "market-signals",
    "editorial-engine", "data-management", "data-process", "data-sync", "file-sync",
    "order-ingest", "order-track", "inventory-planning", "approval-management",
    "process-visibility", "customer-care", "email-assistant", "candidate-evaluation",
    "form-generator", "data-chatbot", "case-lifecycle", "contract-lifecycle",
    "document-ingest", "document-generator", "document-signing", "document-archiving",
    "document-classifier", "document-conversion", "document-unification", "document-numbering",
}


def main() -> int:
    root = pathlib.Path(__file__).resolve().parent.parent
    errors: list[str] = []
    for path in sorted(root.rglob("SKILL.md")):
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(root)
        for match in re.finditer(r"uproc applications ([a-z0-9][a-z0-9.-]*)", text):
            token = match.group(1)
            if token in V2_SLUGS:
                errors.append(f"{rel}: v2 CLI token '{token}'")
            elif token not in CLI_TOKENS:
                errors.append(f"{rel}: unknown CLI token '{token}'")
        for match in re.finditer(r"`([a-z0-9][a-z0-9-]*(?:\.[a-z0-9-]+)+)\.[a-z0-9_]+`", text):
            prefix = match.group(1)
            head = prefix.split(".")[0]
            parent = ".".join(prefix.split(".")[:2])
            if head in V2_SLUGS:
                errors.append(f"{rel}: v2 MCP prefix '{prefix}'")
            elif head not in SURFACE and head not in INTERNAL_MODULES and parent not in MCP_PREFIXES:
                errors.append(f"{rel}: unknown MCP prefix '{prefix}'")
        modules = re.search(r"## Modules\n(.*?)(?:\n## |\Z)", text, re.S)
        if modules:
            for line in modules.group(1).splitlines():
                found = re.match(r"- `([a-z0-9.-]+)`", line.strip())
                if not found:
                    continue
                module_key = found.group(1)
                if module_key in V2_SLUGS:
                    errors.append(f"{rel}: v2 module in Modules '{module_key}'")
                elif module_key not in SURFACE and module_key not in MCP_PREFIXES and module_key not in INTERNAL_MODULES:
                    errors.append(f"{rel}: unknown module in Modules '{module_key}'")
    if errors:
        print("Skill surface FAILED:")
        for error in errors:
            print(f" - {error}")
        return 1
    print("Skill surface OK.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
