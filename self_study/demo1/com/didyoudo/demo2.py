import os
import os
import json


def file_read(file):
    with open(file, mode="r", encoding="utf-8") as input:
        input
        input.writelines()


class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

    def student2dict(std):
        return {
            'name': std.name,
            'age': std.age,
            'score': std.score
        }


s = Student('Bob', 20, 88)
# json.dump()
json.dumps(s, default=Student.student2dict)
# json.dumps(s, default=student2dict())  # {"age": 20, "name": "Bob", "score": 88}
print(json.dumps(s, default=lambda obj: obj.__dict__))  # {"age": 20, "name": "Bob", "score": 88}

print(os.environ.get("JAVA_HOME"))
# for x in os.environ:
#     print(x)
