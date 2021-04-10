import random

from django.shortcuts import render
from django.views import View

import datetime

import logging


class LoggerPageView(View):

    def get(self, request):
        return render(request, 'logger.html')

    def post(self, request):

        action = self.request.POST['action']

        if action == 'logger_one':
            now = datetime.datetime.now()
            formatedate = now.strftime("%Y-%m-%d %H:%M:%S")
            error_string = f'[{formatedate}] "ERROR" Status: 500 "Message from Logger:" Internal Server Error'
            logger = logging.getLogger(__name__)
            logger.error(error_string)
            return render(request, 'logger.html')

        if action == 'logger_two':
            number1 = random.randint(1000, 9999)
            number2 = random.randint(1000, 9999)
            now = datetime.datetime.now()
            formatedate = now.strftime("%Y-%m-%d %H:%M:%S")
            credit_card_string = f'[{formatedate}] "INFO" Status: 200 Customer Credit Card number 4321-4321-{number1}-{number2}'
            logger = logging.getLogger(__name__)
            logger.error(credit_card_string)
            return render(request, 'logger.html')
