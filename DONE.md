# DONE


## 2026-07-31
- `finance/register-purchases`: actualizadas las herramientas MCP del ciclo de vida de compras a las tools concretas `purchase-invoices.change_status` (validate/pay, con `item_id`+`status`+`reason`) y `purchase-invoices.assign_from_ingest` (reemplaza la referencia genérica `module.status`/`module.action`).

- `data-operations/load-and-sync-data`: añadida la capacidad de integraciones ERP (Holded / Factura Directa / Invoice Ninja, credencial propia por integración, selección de ERPs a integrar, recursos `invoices`/`purchases`/`clients`/`suppliers` → `sales-invoices`/`purchase-invoices`/`data-management`) + herramientas MCP (`module.get` para `erp_integrations`, `module.action` `test_source`, `module.create` workflows ERP). `USER_MANUAL.md` actualizado.
- `finance/review-invoices-and-capture`: actualizadas las referencias MCP del módulo renombrado `invoice-generator` → `sales-invoices` (tools `sales-invoices.*`).

Completed skills work, grouped by date.

## 2026-07-31

- `finance/register-purchases`: nuevo skill del módulo `purchase-invoices` (alta directa, asignación desde invoice-ingest, estados received→validated→paid, pagos, proveedores DM). `README.md` y `USER_MANUAL.md` alineados.
- `leadership/ask-data-questions`: documentada la capacidad de follow-up del data chatbot (pasar la pregunta anterior como `context` / foundation query). `USER_MANUAL.md` alineado.

