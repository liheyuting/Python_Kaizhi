#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/8/14 下午9:41
# @Author  : Dora
# @File    : issue.py

## 问题描述：


```


def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words


```

## 曾尝试过以下几种方式：
words = stuff.split(' ')
words = stuff.split()
words = stuff.split(' , ')
words = stuff.split('/')
words = stuff.split('+')
等，均报错显示empty
separator

## 电脑版本：
Mac／python3
朋友用windows／python
2
运行正常

感谢大家为我解答疑惑，这个问题几乎已经折腾我两天的学习时间了。。谢谢了。

## 过程探索 ##
*预期它的输出是什么？
预计的输出是当我输入

```
>import ex25
>sentence = "All good things come to those who wait."
>words = ex25.break_words(sentence)
>words
```

输出为：
```
['All', 'good', 'things', 'come', 'to', 'those', 'who', 'wait.']
```

** 出现与预期不一致的输出后，你做了哪些尝试去解决它？ **

* 先仔细检查了代码与原文的区别
* 用Google了** empty separator ** 的报错原因
* Google了** empty separator ** 通常由什么引起的，并查看相关文档和回答以及论坛里的回答，试用了回答里的修改方式
* 以为可能是python 3 和 2 的区别，查看了官方文档，没找到
* Google 了 python 3 与 2 的区别，找了一些论坛看，还是没找到
* 上GitHub查询** learn python the hard way ** 的点赞量最高的文件，找到python 3 的版本里的对应ex25.py，仔细对照了一个一个的代码。
* 微信群里询问微友，微友给出了几个方案，试了一下，未果
* 接受建议，发issue在GitHub上。



** 代码全文如下： **
```

# !/usr/bin/env python3
def break_words(stuff):
    """This function will break up words for us"""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after poping it off"""
    word = words.pop(0)
    print(word)


def print_last_word(words):
    """Print the first word after poping it off."""
    word = words.pop(-1)
    print(word)


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_words(sentence)
    print_first_word(words)
    print_last_word(words)

‘’‘