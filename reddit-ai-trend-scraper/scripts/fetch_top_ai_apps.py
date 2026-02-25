import urllib.request
import json
import ssl

def fetch_reddit():
    # URL de la API pública de Reddit para el top mensual de comunidades de IA
    url = "https://www.reddit.com/r/artificial+LocalLLaMA+MachineLearning+OpenAI/top.json?t=month&limit=100"
    
    # User-Agent personalizado obligatorio para evitar bloqueos por defecto de Reddit
    req = urllib.request.Request(
        url, 
        data=None, 
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)'
        }
    )
    
    # Ignorar errores de certificado local si existieran
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    try:
        response = urllib.request.urlopen(req, context=ctx)
        data = json.loads(response.read().decode('utf-8'))
        
        posts = data.get('data', {}).get('children', [])
        
        print("=== RESULTADOS DE REDDIT (ÚLTIMO MES) ===")
        count = 0
        
        # Palabras clave heurísticas para detectar si un post trata de una herramienta o app
        keywords = ['app', 'tool', 'release', 'project', 'launch', 'github', 'introducing', 'open source', 'framework', 'built']
        
        for post in posts:
            post_data = post.get('data', {})
            title = post_data.get('title', '')
            score = post_data.get('score', 0)
            url = post_data.get('url', '')
            permalink = "https://reddit.com" + post_data.get('permalink', '')
            
            lower_title = title.lower()
            if any(keyword in lower_title for keyword in keywords):
                count += 1
                print(f"[Aplicación/Herramienta {count}]")
                print(f"Título: {title}")
                print(f"Score Reddit: {score}")
                print(f"URL Herramienta: {url}")
                print(f"Hilo Reddit: {permalink}")
                print("-" * 50)
                
                if count >= 10:
                    break
                    
        if count == 0:
            print("[INFO] No se encontraron coincidencias explícitas en el top 100 de Reddit usando el script.")
            print("[ACCIÓN REQUERIDA] Agente, por favor usa la herramienta 'search_web' o 'read_url_content' directamente para buscar manualmente.")
            
    except urllib.error.HTTPError as e:
        print(f"Error HTTP al conectar con Reddit: {e.code} - {e.reason}")
        print("[ACCIÓN REQUERIDA] Reddit ha bloqueado la petición (probablemente 429 Too Many Requests). Agente, usa 'search_web' con la query 'site:reddit.com trending AI tools this month'.")
    except Exception as e:
        print(f"Error inesperado al conectar con Reddit: {e}")
        print("[ACCIÓN REQUERIDA] Usa 'search_web' para la búsqueda manual.")

if __name__ == "__main__":
    fetch_reddit()
