import requests as r
from django.http import HttpResponse
from celery import shared_task


# 79950071654
@shared_task()
def send_sms(request):
    send_data = {'api_id': 'A99AD5F9-80C1-62B5-36CB-A391552A6C0C',
                 'to': '79046664036', 'msg': 'Поступил заказ ', 'json': 1}
    result = r.post(url='https://sms.ru/sms/send', data=send_data)
    return HttpResponse('Sms was sended')
