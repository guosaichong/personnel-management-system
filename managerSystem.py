from person import *


class PersonManager(object):
    """人员管理类"""

    def __init__(self):
        # 存储数据所用的列表
        self.person_list = []
    # 程序入口函数

    def run(self):
        # 加载文件里面的人员数据
        self.load_person()

        while True:
            # 显示功能菜单
            self.show_menu()
            # 用户输入目标功能序号
            menu_num = int(input("请输入需要的功能序号："))
            # 根据用户输入的序号执行不同的功能
            if menu_num == 1:
                # 添加人员
                self.add_person()
            elif menu_num == 2:
                # 删除人员
                self.del_person()
            elif menu_num == 3:
                # 修改人员
                self.mod_person()
            elif menu_num == 4:
                # 查询人员
                self.search_person()
            elif menu_num == 5:
                # 显示所有人员信息
                self.show_person()
            elif menu_num == 6:
                # 保存人员信息
                self.save_person()
            elif menu_num == 7:
                # 退出系统
                break
    # 系统功能函数
    # 显示功能菜单  静态方法

    @staticmethod
    def show_menu():
        print("请选择如下功能：")
        print("1.添加人员")
        print("2.删除人员")
        print("3.修改人员信息")
        print("4.查询人员信息")
        print("5.显示所有人员信息")
        print("6.保存人员信息")
        print("7.退出系统")
    # 添加人员

    def add_person(self):
        """添加人员信息"""
        # 输入人员信息
        name = input("请输入姓名：")
        gender = input("请输入性别：")
        tel = input("请输入电话：")
        # 创建人员对象
        person = Person(name, gender, tel)
        # 添加到人员列表
        self.person_list.append(person)
        print(person)

    def del_person(self):
        """删除人员信息"""
        # 输入要删除的人员姓名
        name = input("请输入要删除的人员姓名：")
        # 遍历人员列表，如果存在则删除，如果不存在则报错
        for i in self.person_list:
            if i.name == name:
                self.person_list.remove(i)
                print("删除成功")
                break
        else:
            print("要删除的人员不存在")

    def mod_person(self):
        """修改人员信息"""
        # 输入要修改的人员姓名
        name=input("请输入要修改的人员姓名：")
        # 遍历列表，如果要修改的人员存在则修改，否则报错
        for i in self.person_list:
            if i.name == name:
                tel=input("请输入新手机号：")
                i.tel=tel
                print("修改成功")
                print(i)
                break
        else:
            print("要修改的人员不存在")
        

    def search_person(self):
        """查询人员信息"""
        # 请输入要查询的人员姓名
        name=input("请输入要查询的人员姓名：")
        # 遍历列表，如果要查询的人员存在则显示，否则报错
        for i in self.person_list:
            if i.name == name:
                print(i)
                break
        else:
            print("要查询的人员不存在")

    def show_person(self):
        """显示所有人员信息"""
        print("姓名\t性别\t手机号")
        for i in self.person_list:
            print(f"{i.name}\t{i.gender}\t{i.tel}")

    def save_person(self):
        """保存人员信息"""
        # 打开文件
        f=open("person.data","w")
        # 文件写入数据
        # 人员对象转换成字典
        new_list=[i.__dict__ for i in self.person_list]
        f.write(str(new_list))
        # 关闭文件
        f.close()
    def load_person(self):
        """加载人员信息"""
        # 尝试以“r”模式打开数据文件，如果文件不存在，则提示用户;文件存在则读取数据
        try:
            f=open("person.data","r")
        except:
            f=open("person.data","w")
        else:
            data=f.read()
            print(data)
            # 读取的文件是字符串，需要转换。【｛｝】转换【人员对象】
            new_list=eval(data)
            self.person_list=[Person(i["name"],i["gender"],i["tel"]) for i in new_list]
        finally:
            f.close()
