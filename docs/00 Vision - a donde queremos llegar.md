# LotLens: a dónde queremos llegar (borrador v1, 08.10.2026)

> Nombre de trabajo. Se puede cambiar.

## La idea en una frase
**Una herramienta que, dada una zona o un lote del South West de WA, te dice con datos si conviene comprar, construir, renovar o alquilar (largo plazo o turístico), cuánto rinde y qué se puede construir ahí, con un asistente de IA que lo explica y escribe el informe.**

## Para quién
1. **Vos, en los próximos 6 meses:** elegir tu lote o tu propiedad para renovar con números, no a ojo.
2. **Cualquier reclutador o hiring manager:** que en 60 segundos vea que sabés llevar datos reales a una decisión de negocio, de punta a punta.

## Las 4 preguntas que responde
1. **Mercado:** ¿dónde están subiendo los precios y los alquileres, y qué rinde más en el South West, por zona?
2. **El lote:** ¿qué puedo construir en este lote? Zonificación, códigos residenciales y tamaño mínimo, con la fuente citada.
3. **Los números:** compra + construcción o renovación + costos → ¿cuánto vale al final, cuánto renta y qué retorno da? ¿Conviene alquiler largo o turístico?
4. **La decisión:** un informe de inversión de una página, escrito por IA a partir de los datos, con riesgos y supuestos.
5. **El momento:** ¿cómo vino rindiendo cada zona en los últimos 10–20 años, en qué parte del ciclo estamos hoy (recuperación, expansión, pico, corrección) y qué dicen los indicadores: comprar ahora, esperar unos meses o vigilar?

## Momento de mercado: historia, ciclos y "¿compro hoy o espero?"
**Qué va a hacer:**
- **Historia por zona:** precios medianos, alquileres, rendimiento bruto, volumen de ventas, días en el mercado, stock en venta, vacancia de alquiler, permisos de construcción, población, tasas de interés y accesibilidad (precio / ingreso, cuota / ingreso).
- **Desempeño histórico:** crecimiento a 1, 3, 5 y 10 años, retorno total (precio + renta), caídas máximas y cuánto tardó en recuperarse cada zona. Comparación South West vs Perth vs el resto de WA.
- **Ciclos:** separar tendencia, estacionalidad y ciclo. Ver si hay ciclos repetidos (por ejemplo, el boom y la caída minera de WA, de 2008 a 2020) y cuánto duró cada fase.
- **Fase actual del ciclo:** clasificar cada zona en **recuperación / expansión / pico / corrección** con reglas explicables: momentum de precios, ventas y stock, días en el mercado, vacancia, tasas.
- **Indicadores adelantados:** los que suelen moverse antes que el precio: stock en venta, días en el mercado, vacancia, permisos, crédito, tasas.
- **Proyección con incertidumbre:** escenarios de los próximos 6 a 24 meses (base, optimista y pesimista) con rangos, no un número mágico.
- **Backtesting:** probar la señal hacia atrás ("si hubiera usado esto en 2015, 2019 o 2022, ¿qué decía y qué pasó después?"), para saber cuánto confiar en ella.
- **Señal de timing por zona:** *"Indicadores a favor de comprar ahora / esperar / vigilar"*, con el porqué, el nivel de confianza y qué dato la haría cambiar. La IA lo explica en lenguaje simple y lo suma al informe de inversión.

**Importante:** es un **indicador basado en datos, no un consejo financiero**. Muestra probabilidades y escenarios; la decisión es tuya, y conviene validarla con un asesor si hace falta.

## Lo que se va a ver al final (los entregables)
| Entregable | Qué demuestra | Habilidad |
|---|---|---|
| **Base de datos** con modelo estrella (zonas, propiedades, alquileres, permisos, costos, ocupación turística) | Modelar y consultar datos de varias fuentes | **SQL** |
| **Pipeline de datos** en Python: descarga, limpieza, validación y actualización automática | Ingeniería de datos y automatización | **Python** |
| **Motor de factibilidad** (compra + obra + financiación → valor, renta, retorno, sensibilidad) | Modelado financiero y lógica de negocio | **Python + Excel** |
| **Tablero Power BI**: mercado por zona, rendimientos, oportunidades | Comunicar datos a quien decide | **Power BI** |
| **Módulo de ciclos y timing**: series históricas, fase del ciclo, indicadores adelantados, escenarios y backtesting | Series de tiempo, estadística y forecasting | **Python + SQL + Power BI** |
| **Asistente de zonificación con IA**: le preguntás "¿puedo hacer 2 casas en este lote de 900 m²?" y responde citando las normas de WA (R-Codes) y el plan local | IA aplicada sobre documentos (RAG) | **IA aplicada** |
| **Analista con IA**: preguntas en lenguaje natural que se convierten en consultas SQL sobre la base | IA + datos (texto a SQL) | **IA + SQL** |
| **Generador de informe de inversión** por lote | IA que produce un entregable de negocio | **IA aplicada** |
| **App web simple** (Streamlit): ponés zona o lote y ves todo | Producto terminado, no solo código | **Python** |
| **GitHub con README, diagrama de arquitectura y video de 2 minutos** | Profesionalismo y documentación | Todo |

## Por qué suma para cualquier puesto, no solo inmobiliario
- **BA / implementación:** requisitos, modelo de datos, flujo de punta a punta, documentación.
- **Analista de datos / BI:** SQL, Python, Power BI, calidad de datos.
- **IA aplicada / automatización:** RAG, agentes, texto a SQL, generación de informes.
- **Real estate / PropTech:** factibilidad, rendimientos, zonificación.
- **Construcción:** costos de obra y renovación, lo que ya conocés.

La historia que contás en una entrevista: *"Quería comprar un lote, así que me construí la herramienta para decidir."*

## Principios
- **Datos reales y públicos** (o tuyos, como Magma). Nada inventado, nada de scrapear sitios que lo prohíben.
- **Primero algo chico que funcione de punta a punta**, después se agranda.
- **Todo explicable:** cada número con su fuente y cada respuesta de IA con su cita.

## Fuentes de datos candidatas (se verifican en la fase 1)
- ABS: censo (alquiler y precio medianos por zona), permisos de construcción por municipio, índice de costos de construcción. Gratis.
- RBA: tasas de interés. Gratis.
- Normas de WA: R-Codes (códigos residenciales) y los planes urbanos de Busselton y de Augusta-Margaret River. PDFs públicos, para el asistente con IA.
- Landgate / SLIP (datos geográficos y de parcelas de WA): ver qué es gratis.
- Ventas y alquileres por zona: ver si la API de Domain tiene plan gratuito; si no, los reportes públicos.
- Alquiler turístico: tus datos de Magma como caso real, más lo público que exista para el South West.
- Costos de obra: tus referencias de construcción y el índice de ABS.
- **Series históricas (para ciclos y timing):** medianas trimestrales por zona (REIWA y los reportes de Domain), vacancia y stock por código postal (SQM Research, ver qué es gratis), tasa del RBA desde los 90, permisos y crédito de vivienda (ABS), población y migración interna (ABS). Los índices de Cotality y PropTrack son pagos; ver si publican resúmenes regionales gratis.

## Fases (propuesta)
1. **Destino y datos (esta semana):** cerrar la visión, verificar qué datos existen de verdad y armar el diagrama.
2. **Base + pipeline:** SQL + Python con 2 o 3 fuentes, de punta a punta.
3. **Factibilidad:** el motor de números, probado con un caso real.
4. **Power BI + ciclos:** el tablero de mercado, la historia por zona, la fase del ciclo y la señal de timing (con backtesting).
5. **IA:** asistente de zonificación, analista y generador de informes.
6. **App + GitHub + video:** dejarlo presentable y publicarlo en LinkedIn.

## Decisiones tomadas (08.10.2026)
1. **Universal por diseño, Margaret River primero.**
   - Todo se arma por geografía (zona, código postal, coordenadas) y la región es un parámetro. Sumar otra zona = agregar datos, no reescribir.
   - **Primera región:** Margaret River y alrededores (≈ 45 km, **sin Busselton ni Vasse**): Margaret River, Prevelly, Gnarabup, Cowaramup, Gracetown, Witchcliffe, Karridale, Augusta, Yallingup, Dunsborough, Quindalup y Eagle Bay.
   - **Mapa interactivo:** te movés por el mapa y cada zona se pinta según rendimiento, crecimiento, fase del ciclo y señal de timing ("por acá sí / por acá no / vigilar"). Hacés clic en una zona o un lote y ves el detalle y el informe.
2. **Analiza las 3 estrategias y las compara:** (a) comprar lote y construir, (b) comprar propiedad establecida, (c) comprar para renovar. Pregunta central: *¿es buen negocio comprar hoy, y con qué estrategia?*
3. **Costos de obra:** de constructoras y oficios de la zona (Magma no sirve: está en Indonesia).
4. **GitHub privado.** Se hace público cuando esté presentable, si querés.

## Qué le da valor a una propiedad (a investigar y medir con datos)
Se va a medir con un **modelo de precios hedónico**: cuánto suma cada característica al precio y a la renta. Es machine learning explicable, y también sirve para cualquier puesto de datos. Variables candidatas:
- **Terreno:** m² de lote, frente, forma, pendiente, esquina, zonificación y R-Code (**¿se puede subdividir o hacer 2 viviendas?**), servicios (cloacas vs pozo séptico).
- **Construcción:** m² construidos, dormitorios y baños, antigüedad, estado, materiales, garaje, eficiencia energética.
- **Ubicación:** distancia a playa, centro, escuelas y servicios; vistas; calle tranquila vs principal.
- **Riesgos y restricciones** (clave en Margaret River): **zona de incendio y rating BAL** (encarece la obra y el seguro), inundación, vegetación protegida, **permisos para alquiler turístico** (el municipio los limita).
- **Mercado:** días en el mercado, descuento sobre el precio pedido, demanda de alquiler y ocupación turística.

## Costos de obra y renovación (cómo los conseguimos)
- **Precios publicados por constructoras de la zona:** paquetes casa + terreno y diseños con precio y m² (Dale Alcock SW, Celebration Homes, Ventura, Summit, etc.) → costo por m² según tipo y calidad.
- **Constructoras chicas a medida** (Cape Constructions, Bluewater, Nick Goode, Holst): rangos por m² pidiendo cotización o charlando. Es networking que también sirve para tu búsqueda.
- **Renovación:** costos típicos por rubro (cocina, baño, techo, pintura, pisos) de oficios locales y guías públicas.
- **Sobrecostos de la zona:** BAL por incendio, pozo séptico, accesos, distancia desde Perth.
- **Índice de costos de construcción de ABS** para actualizar los números en el tiempo.
