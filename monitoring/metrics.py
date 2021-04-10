from prometheus_client import Counter

counter_one = Counter('arbitrary_counter_one', 'number of times button clicked')
counter_two = Counter('arbitrary_counter_two', 'number of times button clicked time two')


def increment_counter_one():
    counter_one.inc()


def get_current_counter_one_value():
    return counter_one._value.get()


def increment_counter_two():
    counter_two.inc(2)


def get_current_counter_two_value():
    return counter_two._value.get()
