'''
需求：
使用标准库中的setuptools模块，打包发布一个之前写好的模块，并进行安装。需要给出安装结果截图和相关测试程序。
'''

from distutils.core import setup
setup(name='l2Setup',  #打包后的包文件名
      version='1.0',
      description='发布测试',
      author='Sunyue',
      author_email='18468152772@163.com',
      py_modules=['l2'],   #与前面的模块文件名一致
)