import os
from utils.lista_arquivos.main import lista_videos
from django.http import HttpResponse
from django.template import loader

def index(request):    
    vi = lista_videos('videos')
    
    print(f'teste vi {vi}')
    # Fetches all members from the database
    template = loader.get_template('index.html')
    
    context = {
        'vi': vi    }
    return HttpResponse(template.render(context, request))    


def exibir_video(request, nome):
    
    template = loader.get_template('exibir_video.html')
    context= {
        'nome':nome,
    }
    return HttpResponse(template.render(context))

def videos_novos(request):    
    
    vi = lista_videos('upload_videos_novos')
    if len(vi) > 0:
        #mnffmpeg.conversao()
        print(f'teste vi {vi}')
    else:
        print('não há videos novos por enquanto :D')
    # Fetches all members from the database
    template = loader.get_template('videos_novos.html')
    
    context = {
        'vi': vi    }
    return HttpResponse(template.render(context, request))    
