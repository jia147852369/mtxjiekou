#!/anaconda3/envs/FEALPy/bin python3.7
# -*- coding: utf-8 -*-
# ---
# @File: readme.py
# @Author: Bull
# ---
# 1.在项目中，接口测试往往以一个接口为单位。进行编写、维护、组织
# 2.在这个过程中又需要一些辅助工具类（加解密、数据库操作等）
# 3.原生requests代码略显繁琐
# 接口框架思路：
# 1.api文件夹中，每一个.py文件。用来封装一个接口的各种调用。
# 2.封装的接口调用，对位提供方法和返回值
# 3.报告生成到独立文件夹
# 4.工具类统一写到tools