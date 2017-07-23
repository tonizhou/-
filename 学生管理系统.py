# -*- coding: utf-8 -*-
# @Author: ToniZhou
# @Date:   2017-07-24 00:19:36
# @Last Modified by:   TuoniZhou
# @Last Modified time: 2017-07-24 01:13:24

stuinfos = []

while True:
    # 1.打印功能提示
    print('=' * 30)
    print('       学生管理系统v1.0')
    print('1.添加学生信息')
    print('2.删除学生信息')
    print('3.修改学生信息')
    print('4.查询学生信息')
    print('5.显示所有学生信息')
    print('0.退出系统')
    print('=' * 30)

    # 2.获取功能的选择
    key = input('请输入对应功能的序号：')

    # 3.根据用户的选择进行相应的操作

    # 添加学生信息
    if key == '1':
        # 提示并获取学生的姓名
        newName = input('请输入学生的姓名：')
        # 提示并获取学生的性别
        newSex = input('请输入学生的性别(男/女)：')
        # 提示并获取学生的手机号码
        newPhone = input('请输入学生的手机号码：')

        # 新的学生的信息
        newinfo = {}
        newinfo['name'] = newName
        newinfo['sex'] = newSex
        newinfo['phone'] = newPhone

        stuinfos.append(newinfo)

    # 显示所有学生信息
    elif key == '5':
        print('=' * 30)
        print('学生信息如下：')
        print('=' * 30)
        print('序号  姓名    性别  手机号码')

        i = 1
        for tempinfo in stuinfos:
        	print('%d     %s     %s    %s' %(i, tempinfo['name'],tempinfo['sex'],tempinfo['phone']))
        	i += 1

    #修改学生信息
    if key == '3':
    	stuid = int(input('请输入要修改的学生的序号：'))

    	#重新输入学生的信息
    	newName = input('请输入新学生的姓名：')
    	newSex = input('请输入新学生的性别：')
    	newPhone = input('请输入新学生的手机号码：')

    	stuinfos[stuid-1]['name'] = newName
    	stuinfos[stuid-1]['sex'] = newSex
    	stuinfos[stuid-1]['phone'] = newPhone
