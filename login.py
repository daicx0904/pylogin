
((((((((()))))))))



from hashlib import sha256
from pprint import pprint
from os import system as cmd

global la
global user
import configparser

bl = False


cfg = configparser.ConfigParser()
path = r'.\data.ini'
cfg.read(path)  # configparser.DuplicateOptionError


class PasswordError(Exception):
    pass


la = cfg.items('data')


def login():  # XXX
    sa = str(sha256(input('请输入密码\n').encode()).hexdigest())
    name = cfg['data'][sa]
    print('密码正确！')
    print('欢迎{}'.format(name))
    return True


def reg(name, password='<unknow>'):
    global la
    global user
    global path
    try:
        cfg['data'][name]
        print('哎呀，这个名字已经有人用过了呢!')
    except KeyError:
        if "'" or '’' or '\\' or '^' or '*' or '/' not in password:
            if password != '<unknow>':
                cfg.set('data', sha256(password.encode()).hexdigest(), name)
                cfg.write(open(path, 'a'))
                """ """
            else:
                print('兄台您的密码呢？')
        else:
            print('兄台您的密码能不能正常一点啊喂!!!')
    return True



def logout():
    qt = input('确定要退出吗？\n确定请键入“Y”,否定请键入"n"').lower()
    if qt.lower() == 'y':
        exit()
    else:
        pass



if __name__ == '__main__':
    print('键入"/?"以获取帮助')
    while True:
        ipt = input('>>>')
        def exc(ipt1=ipt):
            exec(ipt1)

        try:
            si = ipt.split(' ')
            exec(str(si[0]) + '(' + '"' + str(si[1]) + '"' + ',' + '"' + str(si[2]) + '"' + ')')
        except IndexError: # IndexError: list index out of range
            try:
                exec(str(ipt) + '(' + ')')
            except IndexError:
                exc()
                if bl == True:
                    break
            except:
                if ipt == '/?':
                    print('''
注册：reg 昵称 密码
登录：login //键入login并回车后会提示输入密码
退出：logout

''')

                if ipt == '详细信息':
                    cmd('start https://gitee.com/dm-qaq/python/tree/master/%E5%9F%BA%E4%BA%8Ehashlib%E7%9A%84%E5%AF%86%E7%A0%81%E9%AA%8C%E8%AF%81%E4%BB%A3%E7%A0%81')


exit()
