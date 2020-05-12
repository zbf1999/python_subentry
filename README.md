# python_subentry
Beginner's exercise

## 一名大一新生，欢迎大家共享练习小项目

## A freshman, you are welcome to share the exercise program


## 推荐vscode  Anaconda
conda操作
    查看版本： conda --version
    更新： conda update conda
    创建环境： conda create -n <env_name> python=x.x 
    删除环境：conda remove -n <env_name> --all
    激活环境：activate <env_name>
    退出环境：deactivate
    pip install ipython

操作符
    什么是变量
        就像一个盒子
    运算操作符
        /   除
        //  整除
        %   取余
        **  指数
    
内置对象类型
    整数和浮点数
    字符和字符串
    列表[]
    元组（）    （2，）必须加，
    字典{}
    集合{}   无序且不重复
    
    #变量与对象
        a = 3
            a 是变量 ； 3是对象
        在python中不能单独定义变量
        变量引用了对象
        对调a和b
            a, b = b, a 
        变量的定义
            望文生义
    
    #整数和浮点数
        确定对象类型
            type(3)
        整数 int 
        浮点数 float
        定义整数类型
            int(345)
        id(3)
            获取3的内存地址
        5%2
            取余数
        divmod(5, 2)
            取余数
        更多内置函数见官方文档
        函数也是对象
        help(id)
            查看id的用法
        round()
            四舍五入
        math
            import math    #引进math模块
            dir(math)   #查看math中的函数
            math.pi     #使用math的pi
            help(math.pow)   #查看pow怎么用
                math.pow(2, 3)   #2**3;     2^3;     2x2x2
                math.sin(输入度数)

    #字符和字符串
        ORD('a') = 97
        bin(97) = '0b1100001'
        unicode 简写  utf   最常用 utf-8
        定义字符串
            a = "python"
            a = 'what\'s your name'      
        
        序列
        索引和切片
            第一个字符的编号是0 空格也是编号，右边开始时-1
                a = [1,2,3,4,5,6]
                a[-1] = 3
            倒序输出  r[::-1]
            a[:5:2] = 1, 3, 5    #步长为2，隔一个取一个
            
            input()
                用户输入
            print()打印
            
            a.splist(" ")
            "_".join(lst)
            "i like {0} and {1}".format("php","money")

    #列表
        lsp = []
        lsp()
        列表有循序，元素可重复
        dir(lst)查看列表方法
        append/insert/extend   插入
        pop/remove/clear 删除
        lst.sort()   排序  lst.sort(reverse=True)
        sorted() / list(reverse(lst2))只排序，不改变原序列
        将列表转换为字符串    "".join(lst)
    #元组
        元素不能修改
        t = (1,2)/tuple([1,23])
    #字典
        d = {}    映射   键值
        d['name']  查询字典name的值
        del d['city'] d.pop  d.popitem()  删除
        d.setdefault('name','zw')  d['b'] = 'hello'    d.uodate 插入
    集合
        s.add()    添加
        无序
        s.pop()   s.discard()  s.remove  删除
        f_set = frozenset('qiwsir')   创建不可变集合

方法
    "a".upper()     "A".louer()
    pow  round   ord

布尔类型
    bool:True  False
    A and B A为false返回A，否则返回B
    A or B  A为True返回A
    not A 

简单的语句
    import
        import math
        import math as ko
        from math import pi 
        from math import pi as si 
        from math import *
    赋值语句
    a,_,c = 1,2,3    //不用2了
    a, *b = 1,2,3    //不要2了
    a += 1    a = a+1

函数基础
    def function_name(x,y,z)
        def 定义函数的关键字

多线程与多进程
    计算机的CPU就像一个不断运行的工厂，提供算力
    进程就像一个车间
    线程就像车间内的工人

    使用多线程与多进程处理一个任务就相当于有多个人
    帮你处理同一件事情

    import time
    import threading

    def longtime():
        time.sleep(5)

    t = threading.Thread(target = longtime, name = 'longtime_thread')
    t.start()

    from multiprocessing import Process

    if __name__ == '__main__':
        p = Process(target=longtime)
        p.start()

嵌套函数
    def opt_seq(func, seq):
        r = [func(i) for i in seq]
        return r 
    
    opt_seq(abs, range(-5,5))

    def f3():
        global a   //调用函数外的变量
    
    def foo():
        a = 1
        def bar():
            nonloacl a    //可以调用foo里的a了
            a = a + 1
            print(a)
            bar()

装饰器
    @def
    装饰器是python中的一种函数，它可以让被它装饰器的函数在不修改任何代码的情况下添加额外的功能
    def log(func):
        def wrapper(*args, **kwargs):           #*args与**kwargs表示可以接收任何参数
            print('this is a log')
            return func(*args, **kwargs)
        return wrapper   #返回装饰后的函数
    @log
    def func():
        print('i am a function')

    func()
    装饰器的本质是调用函数

    类装饰器
        类装饰器使用 __call__方法
        
特殊函数
    lambda
        lam = lambda x: x + 3

    map
        m = map(lambda x: x + 3, range(10))

    filter
        过滤器
        f = filter(lambda x: x>0, n)

条件语句
    a = 3 if a >4 else 6

for
    d = {'name':'zw','age':20}
    dt = {}
    for k in d:
        print(k,d[k])
        dt[d[k]] = k
    
    几个常用函数
        range()
            range(4) -> 0,1,2,3
            range(i,j)->i,i+1....j-1

        zip()
            a = 'zw'
            b = 'cap'
            z = zip(a,b)
            把a,b配对
        enumerate()
        列表解析
            lst = []
            [i**2 for i in range(10)]
            [i for i in range(100) if i%3==0]

while
    a = 0
    while a<3:
        s = input('input your lang:')
        if s == "python":
            print("your lang is {0}".format(s))
            break
    
类
    描述所创建的对象共同的属性和方法
    面向对象的程序设计将计算机中的程序视为一组对象的集合，每个对象都可以接受其他对象传递额信息并进行处理


    class SuperMan（object):                 //python 3.6/3.7建议使用（object)
    
        def __init__(self,name):             //init前后两个下划线 ；魔术方法
            ''' 初始化方法 '''
            self.name = name
            self.gender = 1
            self.single = False
            self.illness = False

        def nine_negative_kungfu(self):
            return "Ya! You have to die."

        guojing = SuperMan('guojing')
        print(guojing.name)
        print(guojing.gender)
        kongfu = guojing.nine_negative_kungfu()
        print(kongfu)

    对象
    面向对象程序设计
    实例和属性
        f = Foo()      #创建实例
        Foo.group = 'a'
        
方法
    使用装饰器：@classmethod
    类方法第一个参数：cls,表示类本身

    使用@staticmethod
    静态方法不与实例绑定
    
继承
    class C(P):
        pass
    子类和父类的方法同名，会覆盖父类的方法
    class Student(Person):
        def __init__(self, school, name, age)
            self.school = school
            super().__init__(name, age)           //不覆盖父类
        def grade(self, n):
            print("hahaha")

多态和封装
    子类都有父类的方法，是父类的多态
    通过父类操作子类
    python 中通过私有化的方式实现封装

定制类
    #分数运算
        from fractions import Fraction
        m, n = Fraction(1, 6), Fraction(3, 6)
    
控制属性的访问
    1.优化内存：__slots__
        class bar:
            __slots__ = ('name', 'age')
            def __getattr__(self, name):
                print("you user getattr")
            def __setattr__(self, name, value)：
                print("you use setattr")
                self.__dict__[name] = value

    2。掌握与属性相关的特殊方法
        __getattr__
        __setattr

迭代器和生成器
     python中有多种生成表达式，其语法相近，但获得的结构却截然不同
        列表生成表达式：
            l = [i for i in range(10)]
        字典生成表达式：
            d = {i: i + 10 for i in range(10)}
            {0: 10, 1: 11, 2: 12, 3: 13, 4: 14, 5: 15, 6: 16, 7: 17, 8: 18, 9: 19}
     hasattr(list, "__iter__")    #具有__iter__方法的称为可迭代方法
     iter_lst = iter(lst)
     iter_lst.__next__()

     import itertools
     counter = itertools.count(start=7)
     
     生成器解析
     gt = (x**2 for x in range(10))

标准库和第三方安装包
    pip install 
    pypi镜像使用
        临时使用
            pip install -i https://pypi.tuna.tsinghua.edu.cn/simple some-package
        设为默认
            1.升级pip到最新版本
            2.pip install pip -u
            3.pip config set global.index-url https://pypi.tuna.tsinghua.edu.cn/simple
        升级pip到最新版本
            pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pip -u
    pip  list
    pip uninstall

编写和发布模块
    if __name__ == "__main__":
    .py文件

    包
        有一定层次的目录结构
         python -m pip install --user --upgrade setuptools wheel
         检查setuptools 和 wheel 是不是最新版本，如果不是就升级
         
         登陆test.pypi
         
         pip install twine
         安装发布工具

         python setup.py sdist bdist_wheel
         twine upload --repository-url https://test.pypi.org/legacy/ ./dist/*

文件读写
    import os
    os.getcwd()

    创建文件
        f = open("test.txt","w")    r  只读；a  增加 ；   
        f.write('my name is capzw')
        f.close()

        创建.csv文件
            import csv
            data = []
            with open('csvfile.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(data)

            f = open('csvfile.csv')
            reader = csv.reader(f)
            for row in reader:
                print(row)
            
        pip install openpyxl    使用excel
        
        from openpyxl import Workbook
        wb = Workbook()
        ws = wb.active
        ws.title
        ws.title = 'python'
        ws2 = wb.create_sheet('java)
        ws['E1'] = 111
        ws.cell(row=2, column=2, value=222)
        wb.save('example.xlsx')

异常处理
    如何捕捉错误
        人不是神，无法预计到所有的情况，人的思维总是存在漏洞的，所以人编写出的程序也常会存在漏洞
        当系统越大时，存在漏洞的可能性越大，这些漏洞最终的结果就是让程序报错
        BUG:
            很久以前一只虫子粘在了继电器上，导致计算机无法正常工作，把虫子弄走后计算机又好了，bug的意思就是虫子
        try方法
            import traceback
            while True:
            try:
                a = float(input('first number:'))
                b = float(input('second number:'))
                r = a /b
                print("{0} / {1} = {2}".format(a, b, r))
                break
            except (ZeroDivisionError, ValueError):
                print("hahahahaha")
            #except ValueError:
            #    print("lalalalala")
            except:
                break
            
            except:
                traceback.print_exc()
        错误类型
            BaseException    所有异常的基类
            SystemExit        解释器请求退出
            KeyboardInterrupt 用户中断执行
            Exception           常规错误的基类
            StopIteration       迭代器没有更多的值
            GeneratorExit       生成器发生异常来通知退出
            StandardError       所有额内建标准异常的基类

案例
    SDK 开发工具集合

    API  应用程序接口