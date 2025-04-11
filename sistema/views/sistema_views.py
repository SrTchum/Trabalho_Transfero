from django.shortcuts import render

# Aqui irão ficar todas as views (controladores) ref ao app sistema.
# A função index informa o que vai acontecer quando ela for chamada.
def index (request):
    return render(
        request,
        'sistema/sistema.html'
    )

def apresentacao(request):
    return render(
        request,
        'sistema/apresentacao.html'
    )



# REQUEST
# RESPONSE