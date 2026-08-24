from django.http import HttpResponse

def test_view(request):
    return HttpResponse("Essa é a rota principal!")