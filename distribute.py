#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : 陈坤泽
# @Email  : 877362867@qq.com
# @Date   : 2020/11/29

"""
自动发布pyxlpr的脚本
"""

from pyxllib.xl import *

# 1 每次发布版本，只要在这个文件改一次就行，会自动修改其他有需要用到的两个版本号位置
VERSION = '0.0.2'


def update_version(f):
    f = File(f'{f}')
    s = f.read()
    s = re.sub(r"((?:version|VERSION)\s*=\s*').+?(')", rf'\g<1>{VERSION}\g<2>', s)
    f.write(s)


update_version('setup.py')

# 2 打包发布
subprocess.run('python setup.py sdist')
subprocess.run('twine upload dist/*')

# 3 删除发布文件
Dir('dist').delete()
Dir('xlcocotools.egg-info').delete()
Dir('build').delete()
