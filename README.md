# skills

This directory contains end-user skills organized by worker profile and day-to-day task.

## Design rules

- The primary entry point is the worker profile, not the Bizzmod module name.
- Each skill is named after a real task the worker wants to complete.
- Module names are documented inside each skill as implementation detail.
- Skills reflect the backend reality: most modules support reading, KPIs, uploads, and webhooks; generic create operations are currently rare.
- In this catalog, `form-generator` is the canonical name used for forms.

## Structure

```text
skills/
  AGENTS.md
  README.md
  administracion/
    revisar-documentos-entrantes/
      SKILL.md
```

## Priority model

- `P0`: immediate value for common worker workflows.
- `P1`: important area-specific workflows.
- `P2`: advanced or more specialized workflows.

## Catalog

### administracion

- `P0` `administracion/revisar-documentos-entrantes`
- `P0` `administracion/validar-facturas-recibidas`
- `P1` `administracion/gestionar-aprobaciones-pendientes`

### finanzas

- `P1` `finanzas/revisar-facturas-y-captura`
- `P0` `finanzas/conciliar-movimientos`
- `P0` `finanzas/seguir-cobros-y-impagos`
- `P1` `finanzas/preparar-reporting-fiscal`

### soporte

- `P0` `soporte/gestionar-incidencias`
- `P0` `soporte/redactar-respuestas-a-clientes`
- `P1` `soporte/seguir-pedidos-y-avisar-incidencias`

### ventas

- `P0` `ventas/crear-y-cualificar-leads`
- `P0` `ventas/preparar-propuesta-comercial`
- `P1` `ventas/enviar-propuesta-y-hacer-seguimiento`
- `P1` `ventas/revisar-prospeccion-y-priorizar`

### operaciones

- `P1` `operaciones/revisar-pedidos-entrantes`
- `P2` `operaciones/coordinar-stock-y-demanda`
- `P2` `operaciones/monitorizar-procesos`

### legal

- `P0` `legal/revisar-contratos-vigentes-y-vencimientos`
- `P1` `legal/preparar-firma-documental`

### rrhh

- `P1` `rrhh/revisar-candidaturas`
- `P1` `rrhh/seguir-proceso-de-seleccion`

### marketing

- `P2` `marketing/preparar-campanas-y-audiencias`
- `P2` `marketing/gestionar-contenido-editorial`

### direccion

- `P0` `direccion/consultar-kpis-y-resumen-ejecutivo`
- `P1` `direccion/hacer-preguntas-al-dato`

### operaciones-de-datos

- `P2` `operaciones-de-datos/cargar-y-sincronizar-datos`
- `P2` `operaciones-de-datos/revisar-senales-y-activaciones`

## Backend notes

- Most backend-exposed capabilities are `read_kpis`, `list_collections`, `read_collection_data`, `upload_files`, and `receive_webhooks`.
- Generic external `create_collection_data` is currently available for `lead-management.leads`.
- `lead-management` also exposes special actions for proposal generation, proposal sending, and rerunning lead intelligence.
- Some internal backend flows support more than the generic MCP layer exposes, so skills must distinguish between direct action and assisted recommendation.

## Working in this directory

- Add one directory per skill.
- Keep each `SKILL.md` short, operational, and worker-facing.
- When backend capabilities change, update the affected skills and this catalog in the same change set.
