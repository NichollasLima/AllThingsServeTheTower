import os
import json
from bs4 import BeautifulSoup

# Configurações
PAGES_DIR = "./pages"
OUTPUT_JSON = "./data/pages_data.json"
BASE_URL = "/AllThingsServeTheTower/pages"

def extrair_info_do_html(caminho_html):
    from bs4 import BeautifulSoup

    with open(caminho_html, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

        # 🔹 Título: tenta <title>, depois <h1>, depois nome do arquivo
        titulo = soup.title.string.strip() if soup.title and soup.title.string else None
        if not titulo:
            h1 = soup.find("h1")
            titulo = h1.text.strip() if h1 else os.path.basename(caminho_html).replace(".html", "")

        # 🔹 Meta description (se existir)
        meta = soup.find("meta", attrs={"name": "description"})
        meta_desc = meta["content"].strip() if meta and "content" in meta.attrs else ""

        # 🔹 Pega todos os <p>
        paragrafos = " ".join(p.text.strip() for p in soup.find_all("p"))

        # 🔹 Pega todos os <li>
        listas = " ".join(li.text.strip() for li in soup.find_all("li"))

        # 🔹 Pega todos os <h2>
        subtitulos = " ".join(h2.text.strip() for h2 in soup.find_all("h2"))

        # 🔹 Junta tudo
        texto_completo = " ".join([meta_desc, paragrafos, listas, subtitulos]).strip()

        # 🔹 Limita a 600 caracteres
        descricao = texto_completo[:600] + "..." if len(texto_completo) > 600 else texto_completo

        return titulo, descricao

def gerar_json():
    paginas = []

    for root, _, files in os.walk(PAGES_DIR):
        for file in files:
            if file.endswith(".html"):
                caminho_completo = os.path.join(root, file)

                # Gera caminho relativo para URL
                caminho_relativo = os.path.relpath(caminho_completo, PAGES_DIR)
                url = f"{BASE_URL}/{caminho_relativo}".replace(os.sep, "/")

                titulo, descricao = extrair_info_do_html(caminho_completo)

                paginas.append({
                    "title": titulo,
                    "description": descricao,
                    "url": url
                })

    os.makedirs(os.path.dirname(OUTPUT_JSON), exist_ok=True)

    with open(OUTPUT_JSON, "w", encoding="utf-8") as f:
        json.dump(paginas, f, indent=2, ensure_ascii=False)

    print(f"✅ JSON gerado com sucesso: {OUTPUT_JSON} ({len(paginas)} páginas encontradas)")

if __name__ == "__main__":
    gerar_json()
