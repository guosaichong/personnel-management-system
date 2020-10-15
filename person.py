class Person(object):
    """人员信息类"""

    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f"{self.name},{self.gender},{self.tel}"
