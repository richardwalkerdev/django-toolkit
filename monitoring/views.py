from django.shortcuts import render
from django.views import View

from .metrics import increment_counter_one
from .metrics import increment_counter_two
from .metrics import get_current_counter_one_value
from .metrics import get_current_counter_two_value


class MonitoringPageView(View):

    def get(self, request):

        current_value_counter_one = get_current_counter_one_value()
        current_value_counter_two = get_current_counter_two_value()

        return render(request, 'monitoring.html', {'counter_one': current_value_counter_one,
                                                   'counter_two': current_value_counter_two})

    def post(self, request):

        action = self.request.POST['action']

        current_value_counter_one = get_current_counter_one_value()
        current_value_counter_two = get_current_counter_two_value()

        if action == 'metric_one':
            increment_counter_one()
            current_value_counter_one = get_current_counter_one_value()

        elif action == 'metric_two':
            increment_counter_two()
            current_value_counter_two = get_current_counter_two_value()

        return render(request, 'monitoring.html', {'counter_one': current_value_counter_one,
                                                   'counter_two': current_value_counter_two})
