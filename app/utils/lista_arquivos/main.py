import os

def lista_videos(pasta):
    resp = []
    caminho_origem = f'/static/{pasta}'
    for raiz, pasta, arquivos in os.walk(caminho_origem):
        
        for i in arquivos:
            nome, extensao = os.path.splitext(i)
            resp.append(nome)


    return resp

#lista_videos()