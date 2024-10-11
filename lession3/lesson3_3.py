import tools
import os
os.system('cls')

print(tools.SUN)
p1 = tools.Person(name="Richard", age=20)
print(p1)

s1 = tools.Student(name="李啟民", age=28, chinese=88, english=95, math=90)
print(s1.name)
print(f'我的年紀是{s1.age}歲')
print(f'英文成績為{s1.english}')
print(f'數學成績為{s1.math}')
print(f'中文成績為{s1.chinese}')
print(f'總共成績為{s1.total}')
print(f'平均成績為{s1.average()}')

print("================")
p2 = tools.get_person("張三", 28)
print(p2)

print("================")
s2 = tools.get_student(name='李四', age=38)
print(s2)
print(s2.total)
print(s2.average())

