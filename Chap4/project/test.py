#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/9/16 下午8:55
# @Author  : Dora
# @File    : test.py


prev
创建数据库表

一个数据库可以存放多个数据表，一个数据表就是一个表格（比如 Excel 表格）。

在数据库中，表格每一列的名称和类型都需要明确定义后，才能开始使用。这个过程就是创建数据库表。

假设我们需要建立一个名为 users 的表，其中各列要求如下
id：整数型，记录当前记录号，不可重复
username：字符型，长度80，记录用户名，不可重复
email：字符型，长度120，记录邮件地址，不可重复
对应地，我们可以使用下面的语言来建立 users 表：

import sqlite3

conn = sqlite3.connect('user.db')
print("Opened database successfully.")
c = conn.cursor()
SQL = '''CREATE TABLE users (
        id INTEGER NOT NULL,
        username VARCHAR(80),
        email VARCHAR(120),
        PRIMARY KEY (id),
        UNIQUE (username),
        UNIQUE (email))'''
c.execute(SQL)
print("Table created successfully.")
conn.commit()
conn.close()