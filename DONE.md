## 2026-11-22

- **Skills — superficie v3 en CLI y MCP (HECHO 2026-11-22 · T2 · skills)** — 34 `SKILL.md` migradas a las claves v3 (`purchases`, `templates`, `ingest`, `processing`, `tables`, `connectors`, `files`, `queries`, `processes`, `taxes`, …), con grupos anidados en CLI (`leads capture|enrich|manage`, `orders intake|tracking`, `treatments classify|convert|unify|number`) y nombres MCP `<surface_key>.<acción>` (`leads.capture.*`, `treatments.classify.*`). Cada sección `Modules` lleva clave + suite. Nuevo `scripts/check_skill_surface.py` (falla con tokens/slugs v2). Documentadas las acciones `process`/`retry` de treatments y archive. README, USER_MANUAL y este tracking actualizados. `[skills]`

# DONE

## 2026-10-19
- `administration/review-incoming-documents`: documentada la colección `templates` de `ingest` en las secciones MCP y CLI (catálogo global de sistema en solo lectura; el cliente autoriza un tipo añadiendo la plantilla del catálogo; el CLI no tiene `module create`). README/USER_MANUAL sin cambios de estructura.


## 2026-08-18
- `USER_MANUAL.md` y `README.md`: nueva sección "Setting up access (MCP and CLI)" — explica dónde obtener la guía de configuración (tutoriales de la ayuda del front, `https://app.uproc.io/help/tutorials/cli` y `/mcp`), los valores necesarios (`UPROC_API_URL` = `https://api.uproc.io`, `CUSTOMER_DOMAIN`, `CUSTOMER_API_KEY`, `CUSTOMER_USER_EMAIL`, tomados siempre de los tutoriales) y ejemplos compactos de configuración MCP (OpenCode) y CLI (instalación + `uproc applications login`).
## 2026-08-18
- Revisión completa skills vs capacidades MCP + CLI. Ningún skill documentaba el CLI (solo `Implementation via Uproc MCP`); añadida la sección `Implementation via Uproc CLI` a los 29 skills existentes con los comandos `uproc applications` dedicados o el lector genérico `module <slug> <collection>` / `module overview <slug> kpis` / `module upload` / `module webhook`, y las limitaciones por skill (CLI sin `module create`, flujos AI plan MCP-only, verbos MCP-only como `cancel_invoice`, `upload_contract_document`, `run_transfer`).
- Convenciones: `skills/AGENTS.md` obliga ahora a incluir las secciones MCP y CLI en cada `SKILL.md`; `skills/README.md` y `USER_MANUAL.md` documentan ambas vías de acceso y el catálogo actualizado.
- Nuevos skills (5): `data-operations/run-data-process-tools` (M56 data-process, MCP + CLI completos) y `administration/classify-documents` (M08), `administration/archive-documents` (M11), `administration/convert-documents` (M10), `administration/unify-documents` (M12) — los cuatro con colección `folders` (read/upload/webhook + KPIs) y nota de limitación.
- `treatments.number` (M09) integrado como sección dentro de `administration/review-incoming-documents` (misma colección `folders`).
- Skills existentes actualizados con capacidades MCP nuevas: flujos AI plan (`analyze_plan`/`execute_plan`/`get_plan`/`list_plans`/`regenerate_plan`) en `marketing/prepare-campaigns-and-audiences`, `finance/track-payments-and-overdues` (debt-track), `marketing/manage-editorial-content`, `sales/create-and-qualify-leads` (lead-intelligence); `campaigns.launch_platforms` y `sync_audience`; y normalización/smart-import de `tables` en `data-operations/load-and-sync-data`.
- `USER_MANUAL.md`: corregida la entrada de `operations/file-sync` que estaba ubicada bajo Legal; añadidas las entradas de los 5 skills nuevos.

## 2026-08-05
- Rename de marca: todas las secciones `## Implementation via Bizzmod MCP` pasan a `## Implementation via Uproc MCP` (32 ficheros: `SKILL.md`, `README.md`, `USER_MANUAL.md`, `AGENTS.md`). Solo texto de marca; el server MCP real (`bizzmod-*` en opencode.json) queda intacto.

## 2026-08-04
- `data-operations/load-and-sync-data`: actualizada la sección de integraciones — añadidas las de software contable (Xero, QuickBooks, Pandle, QuickFile, ClearBooks, Bonsai, Capium) y el concepto de grupos multi-miembro (`erp`/`accounting`) con `available=false` para las pendientes. `USER_MANUAL.md` alineado.
- `data-operations/load-and-sync-data`: añadida la integración **Postiz** (social media scheduling, categoría/grupo `social`, read-only). `USER_MANUAL.md` alineado.


## 2026-08-01
- `finance/review-invoices-and-capture` y `finance/register-purchases`: añadido el flujo de **facturas recurrentes** — colección `recurring_invoices` (leer/crear), `sales.create_recurring_from_invoice` / `purchases.create_recurring_from_invoice` (convertir existente) y `*.generate_recurring_invoice` (generar siguiente draft). Nota: los drafts generados en sales llegan como `draft` (revisión/emisión manual); en purchase como `received`.

## 2026-07-31
- `leadership/ask-data-questions`: añadidas las nuevas herramientas del data-chatbot — `queries.list_domains` (dominios/canales con preguntas de ejemplo), `queries.follow_up` (continuar conversación por `session_id`, reutilizando canal/dominio/pregunta previa) y la guía de capturar el `session_id` de `send_chat_query`. Se descartó un skill duplicado `data-operations/ask-company-data` (ya existía este skill P1 que cubre la tarea).
- `finance/register-purchases`: actualizadas las herramientas MCP del ciclo de vida de compras a las tools concretas `purchases.change_status` (validate/pay, con `item_id`+`status`+`reason`) y `purchases.assign_from_ingest` (reemplaza la referencia genérica `module.status`/`module.action`).

- `data-operations/load-and-sync-data`: añadida la capacidad de integraciones ERP (Holded / Factura Directa / Invoice Ninja, credencial propia por integración, selección de ERPs a integrar, recursos `invoices`/`purchases`/`clients`/`suppliers` → `sales`/`purchases`/`tables`) + herramientas MCP (`module.get` para `erp_integrations`, `module.action` `test_source`, `module.create` workflows ERP). `USER_MANUAL.md` actualizado.
- `finance/review-invoices-and-capture`: actualizadas las referencias MCP del módulo renombrado `invoice-generator` → `sales` (tools `sales.*`).

Completed skills work, grouped by date.

## 2026-07-31

- `finance/register-purchases`: nuevo skill del módulo `purchases` (alta directa, asignación desde invoice-ingest, estados received→validated→paid, pagos, proveedores DM). `README.md` y `USER_MANUAL.md` alineados.
- `leadership/ask-data-questions`: documentada la capacidad de follow-up del data chatbot (pasar la pregunta anterior como `context` / foundation query). `USER_MANUAL.md` alineado.

