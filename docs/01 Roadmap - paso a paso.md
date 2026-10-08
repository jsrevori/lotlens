# LotLens: paso a paso (v1, 08.10.2026)

**Ritmo supuesto:** 10–15 h por semana, unas 8 semanas. Cada fase termina con algo que funciona y se puede mostrar.
**Regla de oro:** vos tenés que entender y poder explicar cada parte (te la van a preguntar en entrevistas). Yo escribo y explico; vos ejecutás, probás y decidís. Algunas piezas las escribís vos con ayuda, para practicar SQL y Python.

---

## Fase 0: Preparar el taller (1 día)
- [ ] VS Code + extensión Claude Code, abrir la carpeta `lotlens`.
- [ ] Repo en GitHub en **privado**.
- [ ] Entorno de Python (`.venv`) con las librerías base: pandas, duckdb, geopandas, scikit-learn, statsmodels, streamlit, pydeck/folium, requests.
- [ ] Power BI Desktop instalado.
- [ ] Estructura: `data/raw`, `data/processed`, `sql/`, `src/`, `notebooks/`, `app/`, `docs/`.

**Entregable:** el proyecto corre `python -m src.check` y dice "todo listo".

## Fase 1: Mapa de datos (semana 1)
Para cada cosa que necesitamos, averiguar si existe, dónde, qué tan detallada es, si es gratis y qué licencia tiene:
| Necesidad | Candidatas a verificar |
|---|---|
| Ventas con características (m² lote, m² construidos, dormitorios) | API de Domain, Landgate (valuaciones, pago), REIWA, listados públicos |
| Alquileres (largo plazo) | Censo ABS (por zona), API de Domain, reportes del gobierno de WA |
| Historia de precios y alquileres (10–20 años) | REIWA y Domain (medianas trimestrales), SQM Research, reportes regionales |
| Stock en venta, días en el mercado, vacancia | SQM Research, Domain |
| Zonificación, R-Codes y plan urbano | R-Codes de WA, plan urbano del Shire of Augusta-Margaret River y de la City of Busselton (por Dunsborough y Yallingup) |
| Zonas de incendio (Bushfire Prone Areas) | Datos abiertos de WA (DFES / data.wa.gov.au) |
| Parcelas (catastro) | Landgate / SLIP (ver qué es gratis) |
| Alquiler turístico (permisos y oferta) | Registro y políticas del Shire, listados públicos |
| Permisos de construcción, población, tasas | ABS, RBA |
| Costos de obra y renovación | Paquetes publicados por constructoras de la zona, cotizaciones, índice de ABS |

**Entregable:** `docs/02 Fuentes.md` (tabla de fuentes con disponibilidad, costo y licencia) + una descarga de prueba de cada fuente gratuita.
**Punto de decisión:** si no hay ventas propiedad por propiedad gratis, el modelo de valor arranca con una muestra armada a mano (por ejemplo, 150 a 300 propiedades de listados) y medianas por zona para el resto.

## Fase 2: Base de datos y pipeline (semana 2)  → SQL + Python
- [ ] Diseñar el modelo estrella: `dim_area`, `dim_fecha`, `dim_propiedad` · `fact_ventas`, `fact_alquileres`, `fact_stock`, `fact_permisos`, `fact_tasas`, `fact_costos_obra`.
- [ ] Base en **DuckDB** (archivo local, SQL estándar, rápida y sin servidor).
- [ ] Un script de Python por fuente: descargar → limpiar → validar → cargar.
- [ ] Validaciones automáticas (nulos, rangos, duplicados) y tests simples.
- [ ] Vistas SQL de métricas: crecimiento anual, rendimiento bruto, retorno total.
- [ ] Un comando que actualiza todo: `python -m src.pipeline`.

**Entregable:** base con al menos 3 fuentes reales y consultas SQL documentadas.

## Fase 3: Historia, ciclos y "¿compro hoy?" (semana 3)  → Python + estadística
- [ ] Desempeño por zona: crecimiento a 1, 3, 5 y 10 años, retorno total, caídas máximas y tiempo de recuperación.
- [ ] Descomposición: tendencia / estacionalidad / ciclo.
- [ ] Fase del ciclo por zona (recuperación / expansión / pico / corrección) con reglas explicables.
- [ ] Indicadores adelantados y escenarios a 6–24 meses con rangos.
- [ ] **Backtesting** de la señal.

**Entregable:** notebook + módulo `src/cycles.py` + tabla de "señal de timing" por zona (indicador, no consejo).

## Fase 4: Qué le da valor + factibilidad (semana 4)  → Python + ML + finanzas
- [ ] Base de costos de obra y renovación (constructoras de la zona; costo por m² según tipo y calidad; sobrecostos por BAL y pozo séptico).
- [ ] **Modelo hedónico:** cuánto suma cada característica (m² de lote, m² construidos, distancia a la playa, BAL, R-Code, permiso de alquiler turístico...). Explicable (coeficientes / SHAP).
- [ ] **Motor de factibilidad** para las 3 estrategias: lote + construir, establecida, renovar. Costos de compra, impuestos, obra, financiación, valor final, renta (larga o turística), retorno y sensibilidad.

**Entregable:** `src/valuation.py`, `src/feasibility.py` y un caso real probado con números.

## Fase 5: Power BI (semana 5)
- [ ] Modelo conectado a los datos procesados.
- [ ] Páginas: **Mapa del mercado** · **Detalle por zona** · **Ciclos y timing** · **Comparador de estrategias**.
- [ ] Medidas DAX bien hechas (crecimiento, rendimiento, YoY).

**Entregable:** `.pbix` + capturas + PDF para el portfolio.

## Fase 6: IA aplicada (semana 6)
- [ ] **Asistente de zonificación (RAG):** lee los R-Codes, el plan urbano local y la política de incendios; responde citando la fuente ("¿puedo hacer 2 viviendas en un lote de 900 m² R20?").
- [ ] **Analista con IA (texto a SQL):** preguntas en castellano o inglés que se convierten en consultas sobre la base.
- [ ] **Generador de informe de inversión** de una página por zona o lote: números + señal de timing + zonificación + riesgos.
- [ ] **Evaluación:** 20 preguntas de prueba con respuesta conocida para medir qué tan bien responde. Esto suma muchísimo en entrevistas de IA.

**Entregable:** `src/ai/` con los tres componentes y su evaluación.

## Fase 7: App con mapa (semana 7)  → Python + Streamlit
- [ ] Mapa interactivo: zonas coloreadas por rendimiento, crecimiento, fase del ciclo y señal ("por acá sí / no / vigilar").
- [ ] Clic en una zona → métricas, gráfico histórico, comparador de estrategias e informe con IA.
- [ ] Publicar una demo (Streamlit Community Cloud o similar).

**Entregable:** app funcionando + link de demo.

## Fase 8: Presentación y lanzamiento (semana 8)
- [ ] README en inglés con diagrama de arquitectura, capturas, resultados y "cómo correrlo".
- [ ] Video de 2 minutos ("quería comprar un lote, así que me construí la herramienta").
- [ ] Proyecto en el CV, en LinkedIn (sección Destacados) y en la búsqueda laboral.
- [ ] Decidir si el repo pasa a público.

**En paralelo, todas las semanas:** un post corto en LinkedIn con un hallazgo real ("en qué zona de Margaret River conviene más el alquiler turístico", "cuánto suma un lote subdividible"). Construye red en el rubro de datos inmobiliarios mientras avanza el proyecto.

---

## Cómo trabajamos cada sesión
1. Arrancás con "sigamos con LotLens, fase X".
2. Te propongo el paso, lo hacemos y te explico el porqué.
3. Probás vos, hacemos commit y anotamos lo aprendido en `docs/bitacora.md`.
