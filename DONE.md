# DONE


## 2026-08-18
- Revisión completa skills vs capacidades MCP + CLI. Ningún skill documentaba el CLI (solo `Implementation via Uproc MCP`); añadida la sección `Implementation via Uproc CLI` a los 29 skills existentes con los comandos `uproc applications` dedicados o el lector genérico `module <slug> <collection>` / `module overview <slug> kpis` / `module upload` / `module webhook`, y las limitaciones por skill (CLI sin `module create`, flujos AI plan MCP-only, verbos MCP-only como `cancel_invoice`, `upload_contract_document`, `run_transfer`).
- Convenciones: `skills/AGENTS.md` obliga ahora a incluir las secciones MCP y CLI en cada `SKILL.md`; `skills/README.md` y `USER_MANUAL.md` documentan ambas vías de acceso y el catálogo actualizado.
- Nuevos skills (5): `data-operations/run-data-process-tools` (M56 data-process, MCP + CLI completos) y `administration/classify-documents` (M08), `administration/archive-documents` (M11), `administration/convert-documents` (M10), `administration/unify-documents` (M12) — los cuatro con colección `folders` (read/upload/webhook + KPIs) y nota de limitación.
- `document-numbering` (M09) integrado como sección dentro de `administration/review-incoming-documents` (misma colección `folders`).
- Skills existentes actualizados con capacidades MCP nuevas: flujos AI plan (`analyze_plan`/`execute_plan`/`get_plan`/`list_plans`/`regenerate_plan`) en `marketing/prepare-campaigns-and-audiences`, `finance/track-payments-and-overdues` (debt-track), `marketing/manage-editorial-content`, `sales/create-and-qualify-leads` (lead-intelligence); `campaign-automation.launch_platforms` y `sync_audience`; y normalización/smart-import de `data-management` en `data-operations/load-and-sync-data`.
- `USER_MANUAL.md`: corregida la entrada de `operations/file-sync` que estaba ubicada bajo Legal; añadidas las entradas de los 5 skills nuevos.

## 2026-08-05
- Rename de marca: todas las secciones `## Implementation via Bizzmod MCP` pasan a `## Implementation via Uproc MCP` (32 ficheros: `SKILL.md`, `README.md`, `USER_MANUAL.md`, `AGENTS.md`). Solo texto de marca; el server MCP real (`bizzmod-*` en opencode.json) queda intacto.

## 2026-08-04
- `data-operations/load-and-sync-data`: actualizada la sección de integraciones — añadidas las de software contable (Xero, QuickBooks, Pandle, QuickFile, ClearBooks, Bonsai, Capium) y el concepto de grupos multi-miembro (`erp`/`accounting`) con `available=false` para las pendientes. `USER_MANUAL.md` alineado.
- `data-operations/load-and-sync-data`: añadida la integración **Postiz** (social media scheduling, categoría/grupo `social`, read-only). `USER_MANUAL.md` alineado.


## 2026-08-01
- `finance/review-invoices-and-capture` y `finance/register-purchases`: añadido el flujo de **facturas recurrentes** — colección `recurring_invoices` (leer/crear), `sales-invoices.create_recurring_from_invoice` / `purchase-invoices.create_recurring_from_invoice` (convertir existente) y `*.generate_recurring_invoice` (generar siguiente draft). Nota: los drafts generados en sales llegan como `draft` (revisión/emisión manual); en purchase como `received`.

## 2026-07-31
- `leadership/ask-data-questions`: añadidas las nuevas herramientas del data-chatbot — `data-chatbot.list_domains` (dominios/canales con preguntas de ejemplo), `data-chatbot.follow_up` (continuar conversación por `session_id`, reutilizando canal/dominio/pregunta previa) y la guía de capturar el `session_id` de `send_chat_query`. Se descartó un skill duplicado `data-operations/ask-company-data` (ya existía este skill P1 que cubre la tarea).
- `finance/register-purchases`: actualizadas las herramientas MCP del ciclo de vida de compras a las tools concretas `purchase-invoices.change_status` (validate/pay, con `item_id`+`status`+`reason`) y `purchase-invoices.assign_from_ingest` (reemplaza la referencia genérica `module.status`/`module.action`).

- `data-operations/load-and-sync-data`: añadida la capacidad de integraciones ERP (Holded / Factura Directa / Invoice Ninja, credencial propia por integración, selección de ERPs a integrar, recursos `invoices`/`purchases`/`clients`/`suppliers` → `sales-invoices`/`purchase-invoices`/`data-management`) + herramientas MCP (`module.get` para `erp_integrations`, `module.action` `test_source`, `module.create` workflows ERP). `USER_MANUAL.md` actualizado.
- `finance/review-invoices-and-capture`: actualizadas las referencias MCP del módulo renombrado `invoice-generator` → `sales-invoices` (tools `sales-invoices.*`).

Completed skills work, grouped by date.

## 2026-07-31

- `finance/register-purchases`: nuevo skill del módulo `purchase-invoices` (alta directa, asignación desde invoice-ingest, estados received→validated→paid, pagos, proveedores DM). `README.md` y `USER_MANUAL.md` alineados.
- `leadership/ask-data-questions`: documentada la capacidad de follow-up del data chatbot (pasar la pregunta anterior como `context` / foundation query). `USER_MANUAL.md` alineado.

