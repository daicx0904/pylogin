from hashlib import sha256
from pprint import pprint
import csv
from os import system as cmd
import getpass
from random import randint
import smtplib
from email.mime.text import MIMEText


zt = False
user = None
'''Boolean zt为登录状态,未登录为False否则为True
String user为用户名称,zt为True的情况下会被赋值为当前用户名称,在当前用户使用logout()后会初始化为None,此时更多功能不可用
zt == False 可用功能为:login() reg()
'''
__all__ = ['login', 'logout', 'exit', 'reg', 'help', 'reset']

def fnd(name="name", pwd="sha256"):
    lst = [name, pwd]
    fl = 'data.csv'
    with open(fl) as f:
        c = csv.reader(f)
        c = list(c)
        try:
            c.index(lst)
            return True
        except ValueError as e:
            return False
        finally:
            return


def login():
    global zt, user
    userf = input("user name: ")
    pwd = str(sha256((getpass.getpass("password: ")).encode()).hexdigest())
    print(pwd)
    if not fnd(userf, pwd):
        print('您的账号或密码有误,请重试或使用 reset 指令来重置密码')
        return
    else:
        user = userf
        cmd("cls")
        zt = True
        print(f"用户 {userf},欢迎登录!")
        return

def logout():

    global zt, user
    print(zt)
    if zt:
        zt = False
        cmd("cls")
        print("已注销该用户的登录")
        return
    else:
        print("当前未有用户登录!!!")
        return


def reg():
    pass
#TODO


def help():
    """帮助"""
    pass
#TODO


def reset():
    """reset your password"""


if __name__ == '__main__':
    while True:
        ipt = input() or None
        if ipt in __all__:
            ipt = ipt+"()"
            exec(ipt)
            #TODO
        else:
            if ipt is None:
                print("输入内容不能为空!!!")
            else:
                print(f'未知的命令 "{ipt}"')

exit()
