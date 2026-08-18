# Review Log

Items needing human review: technical debt, workarounds, pending decisions, scope cuts.

## Entry Format

- Date: `YYYY-MM-DD`
- Area: short scope name
- Item: what needs review
- Reason: why it was deferred or needs attention
- Impact: functional/tech/ops impact
- Status: `pending` | `planned` | `won't_do`

## Entries

### 2026-08-18

- Date: 2026-08-18
- Area: skills catalog
- Item: `investment-analysis` (M17) no tiene representación en skills.
- Reason: el módulo no expone entities ni tools concretas en el MCP (solo acceso genérico `module.kpis`/`module.data`) y el CLI tampoco tiene comandos dedicados; un skill no tendría capacidades concretas que documentar.
- Impact: ninguna aplicación cubre análisis de inversiones vía skills hasta que el backend exponga herramientas.
- Status: `pending`

- Date: 2026-08-18
- Area: skills catalog
- Item: módulos `admin` (customers, users, credentials, tickets, usage) y `custom-dashboard` excluidos del catálogo de skills.
- Reason: son capacidades solo para staff de Killia (onboarding, credenciales, soporte interno), no tareas de trabajador final; el catálogo es worker-facing.
- Impact: el acceso a estas áreas queda documentado únicamente en CLI (`uproc applications admin ...`) y MCP (`admin.*`, `custom_dashboard.*`).
- Status: `won't_do`


