#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author : 陈坤泽
# @Email  : 877362867@qq.com
# @Date   : 2020/11/26


"""
安装方法： python setup.py build_ext develop
"""

from setuptools import setup, find_packages, Extension
import io
import numpy as np
import sys

if sys.platform == 'win32':
    extra_compile_args = ['-std=c99']
elif sys.platform.startswith('linux'):  # python2 will be 'linux2'
    extra_compile_args = ['-Wno-cpp', '-Wno-unused-function', '-std=c99']
else:
    raise NotImplementedError

# To compile and install locally run "python setup.py build_ext --inplace"
# To install library to Python site-packages run "python setup.py build_ext install"

ext_modules = [
    Extension(
        'xlcocotools._mask',
        sources=['xlcocotools/common/maskApi.c', 'xlcocotools/_mask.pyx'],
        include_dirs=[np.get_include(), 'xlcocotools/common'],
        extra_compile_args=extra_compile_args
    )
]

setup(
    name='xlcocotools',  # pip 安装时用的名字
    version='0.0.3',  # 当前版本，每次更新上传到pypi都需要修改
    author='code4101',
    author_email='877362867@qq.com',
    url='https://github.com/code4101/xlcocotools',
    keywords='xlcocotools',
    description='pycocotools修改版本',
    long_description=io.open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=('tests', 'tests.*')),
    include_package_data=True,
    classifiers=[
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',  # 大部分功能都是跨平台的
    ],
    python_requires='>=3.6',  # 我的项目大量使用f字符串
    install_requires=open('requirements.txt').readlines(),
    ext_modules=ext_modules
)
