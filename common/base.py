import sys
import os
# 这个文件作用是 将common添加到 Python 的模块搜索路径sys.path中
# 方便导入common模块
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.abspath(os.path.dirname(curPath) + os.path.sep + ".")
sys.path.append(rootPath)