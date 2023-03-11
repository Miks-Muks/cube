import requests as r
from django.shortcuts import redirect
from random import choice


def send_sms(request):
    send_data = {'api_id': 'AF33C9EA-6B46-7961-7EA3-F062F1EE2503',
                 'to': '79950071654', 'msg': 'Поступил заказ', 'json': 1}
    result = r.post(url='https://sms.ru/sms/send', data=send_data)
    return redirect('home')


def create_random_user_name():
    '''create user name'''
    result = ''
    str_l = 'aaasfwegWRHSD'
    letters = [i for i in str_l]
    for i in range(4):
        result += choice(letters)
    return result