import datetime as dt

class A(object):
    def __init__(self):
        self.datetime = dt.datetime(2021, 5, 10, 22, 45)
        self.date = dt.date(2020, 10, 30)
        self.frozen = frozenset((1, 2))

def serialize(a: A):
    return f'''{{
    "datetime": {{
        "year": {a.datetime.year},
        "month": {a.datetime.month},
        "day": {a.datetime.day},
        "hour": {a.datetime.hour},
        "minute": {a.datetime.minute}
    }},
    "date": {{
        "year": {a.date.year},
        "month": {a.date.month},
        "day": {a.date.day}
    }},
    "frozen": {list(a.frozen)}
}}
'''

a = A()
print(serialize(a))