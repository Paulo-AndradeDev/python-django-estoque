from django.urls import path
from .views import index, contato, produto

urlpatterns = [
    path('', index,name='index'),
    path('contato', contato,name='contato'),
    path('produto/<int:pk>',produto, name='produto')
    #o param 'pk' deve ter o mesmo nome nos arquivos urls views e template. senão, dá erro.
]
