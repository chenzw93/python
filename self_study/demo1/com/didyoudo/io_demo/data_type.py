"""
    Json

"""
import json

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str))

d = dict(name='Bob', age=20, score=88)
print(d)


class JsonDemo:
    def __init__(self, first, second):
        self.first = first
        self.second = second


json_demo_inst = JsonDemo("name", "age")
print(json.dumps(json_demo_inst, default=lambda obj: obj.__dict__))
