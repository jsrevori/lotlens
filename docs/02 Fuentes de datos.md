# Fase 1: mapa de fuentes de datos (08.10.2026)

Región: Margaret River y alrededores, de Dunsborough a Augusta (sin Busselton ni Vasse).
Estado: ✅ probado y funciona · 🟡 existe pero requiere registro o una prueba más · 💲 pago · ❌ no disponible.

## Resumen
| # | Necesidad | Fuente | Estado | Detalle / nivel | Licencia / costo |
|---|---|---|---|---|---|
| 1 | **Alquileres reales** | **WA Rental Bonds** (cada contrato nuevo: fecha, localidad, código postal, alquiler semanal) | ✅ | Mensual desde **mar-2023**. **2.243 contratos** en la región; mediana regional $600 (2023) → $750 (2026). Sin tipo de vivienda. | CC-BY, gratis |
| 2 | **Zonificación** | DPLH Local Planning Scheme: Zones & Reserves (SLIP, servicio público) | ✅ | Polígonos con zona, uso y esquema, consultables por coordenadas | Datos DPLH: uso no comercial (portfolio OK) |
| 3 | **R-Codes (densidad)** | DPLH Local Planning Scheme: R Codes (SLIP, servicio público) | ✅ | Polígonos R15/R20/R30/R40… del esquema Augusta-Margaret River | Igual que el 2 |
| 4 | **Lotes (catastro)** | Landgate Cadastre (sin atributos) en SLIP | ✅ | Forma de cada lote → **m² de lote calculable**; 2.948 lotes solo en el centro de MR | Público |
| 5 | **Zonas de incendio** | OBRM Bush Fire Prone Areas (SLIP, servicio público) | ✅ (servicio) / 🟡 (descarga completa con login gratis) | Polígonos de zona propensa a incendios. El rating BAL exacto por lote no es público (lo hace un consultor). | Público |
| 6 | **Límites de localidades y municipio** | Landgate Localities / LGA (SLIP) | ✅ | Para agrupar todo por zona en el mapa | Público |
| 7 | **Censo 2021** | ABS Data API (G02 medianas, G36 tipo de vivienda, G37 tenencia, G40 alquileres) por **localidad (SAL)** | ✅ | Ingresos, alquiler y cuota medianos, viviendas, % alquiler, % vacías (casas de fin de semana) | Gratis |
| 8 | **Permisos de construcción** | ABS Building Approvals por SA2 / LGA (mensual, desde 2011) | ✅ | Oferta nueva por zona → indicador adelantado | Gratis |
| 9 | **Crédito para vivienda** | ABS Lending Indicators (housing finance) | ✅ | Indicador adelantado del ciclo (nivel WA) | Gratis |
| 10 | **Tasas de interés** | RBA F1 (cash rate desde 1990) | ✅ | Descargado | Gratis |
| 11 | **Precios de venta e historia por zona** | **Domain API** `suburbPerformanceStatistics` | 🟡 | Serie por suburbio: mediana vendida, percentiles, cantidad de ventas, listados en venta, alquiler pedido, días en el mercado. **Ideal para ciclos.** Requiere registrarte gratis en developer.domain.com.au; ver límites del plan gratuito. | Plan gratuito a confirmar |
| 12 | **Foto actual del mercado por zona** | REIWA (perfil por suburbio) | ✅ (lectura) | MR hoy: casa mediana **$1.0M**, terreno **$380k** (chico $300k / grande $475k), alquiler casa **$780/sem**, 17 días en el mercado, +12,8% anual. Gráfico de 10 años. | Uso manual o con permiso; no scrapear masivo |
| 13 | **Ventas propiedad por propiedad con m² y características** | Landgate Sales Evidence / reportes por suburbio | 💲 | Datos oficiales desde 1988, hasta las últimas 3 ventas de cada propiedad. Reporte por suburbio en Excel (ver muestra). | Pago (a cotizar) |
| 14 | **Alquiler turístico** | Registro STRA de WA (dashboard Power BI público, mensual) | 🟡 | Registros por municipio, tipo y hosted/unhosted. **Augusta-Margaret River: ~871 registradas.** No hay descarga ni datos por dirección; la API es solo para plataformas de reservas. | Público (lectura) |
| 15 | **Reglas de alquiler turístico** | Shire AMR: política y enmienda del esquema (Scheme Amendment 61), "Holiday House" hasta 6 huéspedes | ✅ | PDFs para el asistente con IA | Público |
| 16 | **R-Codes (texto)** | State Planning Policy 7.3 (Residential Design Codes) + Local Planning Scheme AMR | ✅ (a descargar) | PDFs para el asistente de zonificación (RAG) | Público |
| 17 | **Costos de obra y renovación** | Paquetes y diseños publicados por constructoras de la zona + cotizaciones + índice ABS | 🟡 | A relevar a mano (fase 4) | Público / propio |

## Lo que esto significa
- **Ya podemos armar casi todo gratis:** alquileres reales, zonificación, R-Codes, tamaño de cada lote, zonas de incendio, censo, permisos, crédito y tasas.
- **El punto débil son las ventas con características** (m² construidos, dormitorios, etc.):
  - **Opción A (gratis):** Domain API (series por zona) + REIWA (foto actual) + una muestra armada a mano de listados para el modelo de valor.
  - **Opción B (pago):** reportes de ventas de Landgate para las ~12 localidades. Es el dato oficial, el mejor para el modelo hedónico.
- **Ciclos e historia:** Domain API (desde ~2015 según el ejemplo) + RBA + ABS (permisos y crédito desde 2011) + rental bonds (desde 2023).

## Lo que necesito de vos
1. **Registrarte en developer.domain.com.au** (es tuyo, yo no puedo crear cuentas). Después creamos una API key y la guardamos en un archivo `.env` que **no** se sube a GitHub.
2. Decidir si cotizamos los **reportes de ventas de Landgate** (opción B).
3. Más adelante: charlar con 2 o 3 constructoras por costos por m².
