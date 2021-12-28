from django.shortcuts import render, redirect
from TranslHero import settings
from hashlib import md5
import requests
import random
from Translation import models as trans_models


# Create your views here.

def make_md5(s, encoding='utf-8'):
    return md5(s.encode(encoding)).hexdigest()


def set_params(from_language, to_language, input_text):
    salt = random.randint(32768, 65536)
    sign = make_md5(settings.APPID + input_text +
                    str(salt) + settings.APPKEY)
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {'appid': settings.APPID, 'q': input_text, 'from': from_language,
               'to': to_language, 'salt': salt, 'sign': sign}

    return payload, headers


def get_translation(request, payload, headers):
    try:
        r = requests.post(settings.BAIDU_URL, params=payload, headers=headers)
        result = r.json()
    except:
        return render(request, 'Translation/Translation.html')

    try:
        trans = result["trans_result"][0]['dst']
    except:
        return render(request, 'Translation/Translation.html')

    return trans


def store_history(from_language, to_language, input_text, translation, request):
    new_history = trans_models.History.objects.create()
    new_history.userId = request.session['user_id']
    new_history.username = request.session['user_name']
    new_history.from_language = from_language
    new_history.to_language = to_language
    new_history.input_text = input_text
    new_history.translation = translation
    new_history.save()


def translation(request):
    if request.session.get('is_login', None):
        if request.method == "POST":
            from_language = request.POST.get('fromLanguage')
            to_language = request.POST.get('toLanguage')
            input_text = request.POST.get('inputBox')

            payload, headers = set_params(from_language, to_language, input_text)
            result = get_translation(request, payload, headers)

            store_history(from_language, to_language, input_text, result, request)

            return render(request, 'Translation/Translation.html', {"translatedText": result, "inputText": input_text})
    else:
        return redirect('/login')

    return render(request, 'Translation/Translation.html')
