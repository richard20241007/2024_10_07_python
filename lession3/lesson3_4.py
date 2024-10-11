import widget
from widget import get_person, get_student

print(widget.MON)
s1 = get_student(name="李啟民", age=26)
print(s1)
print(f'總共成績為{s1.total}')
print(f'平均成績為{s1.average()}')
