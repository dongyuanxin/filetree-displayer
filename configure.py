# 最大文档检索数
MAX_NUM = 20

# 最大查找深度
MAX_DEPTH = 5

# 忽略的文件，后缀名作为标识
__filter = []
FILTER = list(map(lambda x:x.lower(),__filter))

# 需要选择的文件，后缀名作为标识
__select = []
SELECT = list(map(lambda x:x.lower(),__select))

'''
E.g
__filter = ['.py','.mp3'] # 必须 .+后缀名
__select = ['.md'] # 必须有.+后缀名
'''