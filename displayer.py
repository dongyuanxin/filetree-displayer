import os
import sys
import time


try:
    from .configure import *
except:
    from configure import *

def check(func):
    def logger(*args,**kw):
        is_right =  (isinstance(MAX_NUM,int) and MAX_NUM>0 ) \
                    and (isinstance(MAX_DEPTH,int) and MAX_DEPTH>0) \
                    and isinstance(FILTER,list) \
                    and isinstance(SELECT,list)
        assert is_right,'配置文件错误，请仔细检查'
        return func(*args,**kw)
    return logger


class Load(object):
    __slots__ = ('max_num','max_depth','filter','select')
    @check
    def __init__(self):
        self.max_num = MAX_NUM
        self.max_depth = MAX_DEPTH
        self.filter = FILTER
        self.select = SELECT


class Filetree(Load):
    __slots__ = ('root')

    def __init__(self):
        super().__init__()
        self.root = None

    def __call__(self, *args, **kwargs):
        pass

    def __str__(self):
        return "A class to show file tree"

    def set_root(self,root):
        if os.path.isdir(root) and os.path.exists(root):
            self.root = root
        else:
            print("文件名不合法")

    def show(self):
        print()
        self.__show()
        print()

    def __show(self,path=None,times=1,tag="|   "):
        if times>self.max_depth: # 控制深度
            print(times * tag + '...')
            return
        if not path: # 刚开始的时候
            path = self.root
            if os.name=='nt':
                print(path+'\\')
            else:
                print(path+'/')
            if len(os.listdir(path))==0: # 考虑到子目录是空目录的情况
                print("debug")
                return

        if len(os.listdir(path))==0: # 当文件夹是空目录的时候
            return

        if len(os.listdir(path))>=self.max_num: # 如果当前目录下文档的数目多于设定的最大值
            print(times * tag + '...')
            return

        for file in os.listdir(path):
            real_path = os.path.join(path,file)
            if os.path.isdir(real_path):
                if os.name == 'nt':
                    name = real_path.split('\\')[-1]
                    print(times * tag + name + '\\')
                else:
                    name = real_path.split('/')[-1]
                    print(times * tag + name + '/')
                self.__show(path=real_path,times=times+1)
            else:
                name = os.path.split(real_path)[-1]
                type = os.path.splitext(real_path)[-1].lower()
                if type in FILTER: # 先过滤
                    continue
                if len(SELECT)==0: # 在考虑是否提供选择列表
                    print(times * tag + str(name))
                else:
                    if type in SELECT:
                        print(times * tag + str(name))


if __name__=='__main__':
    pass
