#!/usr/bin/python3
# @File: 学校信息管理系统.py
# --coding: utf-8--
# @Author: 孟德昊
# @Time: 2021年 11月 10日 16:21
'''说明:建立学校信息管理系统：
建立Person类，包括：姓名name、性别sex、年龄age这3个数据成员，一个构造函数、一个输出信息的printInfo函数。
建立Student类，该类继承自Person类，并且新增数据成员：班级class（用string类型）、学号studentID（用int类型）、成绩score（用字典类型，可以自己定义三门课程，比如语数外）、总人数count（用int类型，这是静态属性，即类属性），和一个构造函数、一个输出信息的printInfo函数。
建立Teacher类，该类也继承自Person类，并且新增：部门department（用string类型）、工号teacherID（用int类型）、讲授课程course（用列表类型）、薪水salary（用int类型，这是私有数据）这4个数据成员，和一个构造函数、一个输出信息的printInfo函数（这里不输出私有数据，但可以考虑一下如何提供私有数据的输出方法）。
然后创建2个学生对象和1个教师对象，然后分别调用这3个对象的printInfo函数输出各自的（非私有）数据信息。在学生的构造函数中让count自增，在析构函数中让count自减。
（说明：上面已经规定的内容在自己编程时也允许灵活调整，没有规定的更是可以自由发挥，主要是必须学会类的定义和使用）

'''
class Person:
    def __init__(self,name,sex,age):
        self.name = name
        self.sex = sex
        self.age = age
        # Person.pirntInfo(self)

    def pirntInfo(self):
        print("姓名：{},性别：{},年龄：{}".format(self.name,self.sex,self.age))

class Student(Person):
    count = 0
    def __init__(self,name,sex,age,classes,studentId,score):
        Person.__init__(self,name,sex,age)
        self.classes = classes
        self.studentId = studentId
        self.score = {"语文":score[0],"数学":score[1],"英语":score[2]}
        Student.count += 1
        # Student.pirntInfo(self)

    def __del__(self):
        Student.count -= 1
        print("{}已开除学籍".format(self.name))
        print(Student.count)

    def pirntInfo(self):
        print("姓名：{},性别：{},年龄：{},班级：{},学号：{},成绩：{}".format(self.name,self.sex,self.age,self.classes,self.studentId,self.score))
        print("学生人数:{}".format(Student.count))

class Teacher(Person):
    def __init__(self, name, sex, age, department, teacherId, course,salary):
        Person.__init__(self, name, sex, age)
        self.department = department
        self.teacherId = teacherId
        self.course = course
        self.__salary = salary
        # Teacher.pirntInfo(self)

    def pirntInfo(self):
        print("姓名：{},性别：{},年龄：{},部门：{},工号：{},讲授课程：{}".format(self.name, self.sex, self.age, self.department, self.teacherId,
                                                           self.course))

if __name__ == "__main__":
    a = Person("孟德昊","男",18)
    a.pirntInfo()
    b = Student("孟德昊","男",19,2102,3201303014,[98,91,33])
    b.pirntInfo()
    c = Student("小q","男",18,2102,3201303015,[98,91,77])
    c.pirntInfo()
    q = Student("杨y","女",21,1902,3190606066,[99,100,100])
    q.pirntInfo()
    d = Teacher("老q", "男", 40, "计算机学院", 123456789,"python及计算思维","100000")
    d.pirntInfo()
