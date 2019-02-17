'''
定义一个学生类，用来形容学生
'''

class Student():
    pass

# 定义一个对象
mingyue = Student()

# 再定义一个类，用来形容听python的学生
class PythonStudent():
    # 用None给不确定的变量赋值
    name = None
    age = 18
    course = "Python"

    # 需要注意
    # 1.def 的缩进层级
    # 系统默认一个self参数
    def dohomework(self):
        print("I 在做作业")

        # 推荐在函数末尾使用return语句
        return None


# 实例化一个月月学生，是一个具体的人
yueyue = PythonStudent()
print(yueyue.name)
print(yueyue.age)
# 注意成员函数的调用没有传入参数
yueyue.dohomework()