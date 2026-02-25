---
name: reddit-ai-trend-scraper
description: Busca, extrae y resume las 10 aplicaciones de IA más en tendencia en Reddit en el último mes.
---

# Reddit AI Trend Scraper

## Objetivo
Buscar e identificar las 10 aplicaciones, herramientas o proyectos de Inteligencia Artificial que han sido más populares (trending) en Reddit durante el último mes.

## Instrucciones
1. Ejecuta el script de extracción que viene incluido en la skill:
   `python "c:/Users/UD/Desktop/Creador de Skills/reddit-ai-trend-scraper/scripts/fetch_top_ai_apps.py"`
2. El script consultará la API pública de Reddit en las comunidades clave de IA (`r/artificial`, `r/LocalLLaMA`, `r/MachineLearning`, `r/OpenAI`) y filtrará los posts principales del mes para identificar herramientas o aplicaciones.
3. Lee la salida del script. Si el script logró obtener resultados estructurados, compila la información y preséntasela al usuario en un formato agradable y fácil de leer (Markdown con viñetas o enlaces).
4. **Plan de Respaldo (Fallback)**: Si el script falla por límite de peticiones (Error 429) o no encuentra 10 aplicaciones exactas en el top 50 de Reddit, **estás obligado** a usar tu herramienta nativa `search_web` con búsquedas (por ejemplo: `site:reddit.com trending AI apps this month` o `dorks`), leer los resultados y compilar la lista manualmente usando tu habilidad de razonamiento.

## Restricciones
- **NO** inventes o alucines aplicaciones. Todo debe provenir de los datos reales de Reddit o de tu `search_web`.
- **NO** incluyas noticias genéricas o debates filosóficos sobre IA. El foco exclusivo es en **aplicaciones, herramientas, repositorios o proyectos usables**.
- Limítate a reportar un máximo de 10 elementos asombrosos.

## Ejemplos
### Caso de uso válido
Entrada del usuario: "¿Me resumes las apps de IA más virales de Reddit este mes?"
Acción del agente: 
1. Ejecuta `python "c:/Users/UD/Desktop/Creador de Skills/reddit-ai-trend-scraper/scripts/fetch_top_ai_apps.py"`.
2. Lee los resultados exitosos y redacta la lista para el usuario con el nombre de la herramienta, su función y su enlace a Reddit.
