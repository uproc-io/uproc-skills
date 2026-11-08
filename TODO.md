# TODO

Use this file to track pending skills work, partially applied requirements, blockers, and follow-ups.

All items grouped by date under each section.

## 2026-11-08

- **Skills — actualizar CLI commands deprecated (PENDIENTE · T2 · ~1-2d · skills)** — 4 commands CLI están deprecated y referenciados en 20+ ocurrencias de skills: (1) `leads` → `lead-management`; (2) `support` → `customer-care`; (3) `cases` → `case-lifecycle`; (4) `candidate` → `candidate-evaluation`. Además, la sintaxis genérica `module <slug> <collection>` se usa con path incorrecto en varios skills (ej. `module lead-intelligence leads` debería ser `module collection lead-intelligence leads`, `module data-management entities` es inválido, `module purchase-invoices invoices` debería usar `invoice-ingest list-invoices`). **Alcance**: (1) reemplazar todos los `uproc applications leads/` por `uproc applications lead-management/` y análogos; (2) corregir sintaxis `module` genérica o redirigir al command específico del módulo cuando exista; (3) verificar que cada CLI command referenciado existe y es funcional; (4) los skills donde el módulo no tiene verbos business deben documentar explícitamente que se usa el fallback genérico. [skills]

## Active

### 2026-10-31

- **Skills — Campaign Automation: newsletter interno omnicanal (PENDIENTE · complejidad: T1 · ~0.5d · skills · plan: `../backend/docs/plans/campaign-automation-internal-newsletter.md`)** — Cuando back/front cierren F1–F9, revisar y actualizar las skills de worker (marketing/sales/operations) para reflejar el flujo completo: setup de canal/proveedor → campaña recurrente → contenido IA → aprobación → programación → tracking/rebotes/SMS. Documentar qué es externo vs interno y qué evidencias debe recoger el worker. [skills]

## Planned

No planned skills items recorded yet.

## Blocked

No blocked skills items recorded yet.
