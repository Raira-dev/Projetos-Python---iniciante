from fastapi import FastAPI, HTTPException
import string, random

app = FastAPI()

# "Banco de dados" em memória
urls = {}

# Função para gerar códigos curtos
def gerar_codigo(tamanho=6):
    caracteres = string.ascii_letters + string.digits
    return ''.join(random.choice(caracteres) for _ in range(tamanho))

@app.post("/encurtar")
def encurtar(url: str):
    codigo = gerar_codigo()
    urls[codigo] = url
    return {"url_curta": f"http://localhost:8000/{codigo}"}

@app.get("/{codigo}")
def redirecionar(codigo: str):
    if codigo not in urls:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    return {"redireciona_para": urls[codigo]}
