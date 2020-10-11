# 定义一个存储人员信息的变量
info = []
# 增加人员信息功能


def add_person():
    """增加人员"""
    person_dict = {}
    new_name = input("请输入人员姓名：")

    # 要增加的人员姓名是否存在
    global info
    for i in info:
        # print(i)
        if i["name"] == new_name:
            print("该人员已存在")
            break
    else:
        new_age = input("请输入人员年龄：")
        new_tel = input("请输入人员电话：")
        person_dict["name"] = new_name
        person_dict["age"] = int(new_age)
        person_dict["tel"] = int(new_tel)
        info.append(person_dict)
        print(info)


def del_person():
    """删除人员"""
    del_name = input("请输入要删除人员的姓名：")
    global info
    for i in info:
        # print(i)
        if i["name"] == del_name:
            info.remove(i)
            print("删除成功")
            break
    else:
        print("要删除的人员不存在")


def mod_person():
    """修改人员信息"""
    mod_name = input("请输入要修改人员的姓名：")
    global info
    for i in info:
        if i["name"] == mod_name:
            print("要修改人员的信息如下：")
            print(i)
            new_tel = input("请输入要修改人员的手机号：")
            i["tel"] = new_tel
            print("修改成功")
            break
    else:
        print("要修改的人员不存在")


def query_person():
    """查询单个人员信息"""
    query_name = input("请输入要查询人员的姓名：")
    global info
    for i in info:
        if i["name"] == query_name:
            print(i)
            break
    else:
        print("查无此人")


def query_all():
    """查询全部人员信息"""
    global info
    for i in info:
        print(f"{i['name']}\t{i['age']}\t{i['tel']}")


# 显示功能界面
while True:
    print("========人事管理系统========")
    print("""
    1.增加人员
    2.删除人员
    3.修改人员
    4.查询人员信息
    5.显示全部人员信息
    6.退出
    """)
    num = input("请输入序号：")
    # 根据选择进入相应的功能
    if int(num) == 1:
        print("增加人员")
        add_person()
    elif int(num) == 2:
        print("删除人员")
        del_person()
    elif int(num) == 3:
        print("修改人员信息")
        mod_person()
    elif int(num) == 4:
        print("查询人员信息")
        query_person()
    elif int(num) == 5:
        print("显示全部人员信息")
        query_all()
    elif int(num) == 6:
        print("退出")
        break
    else:
        print("输入错误，请重新输入")
