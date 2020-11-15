import random
base_list=['周杰伦','林俊杰','王力宏','蔡依林','薛之谦','张学友']
card_list=[]
while 1:
    print('充值能让你变得更强！\n请选择指令：\n1、抽卡\n2、查看背包\n3、整理背包\n4、离开')
    number=int(input())
    if number == 1:
        a = 1
        card_number=int(input('请输入抽卡次数：'))
        while a <= card_number:
            star = random.choice(base_list)
            print(star)
            card_list.append(star)
            a = a + 1
        print('卡已存入背包')
    if number == 2:
        for i in card_list:
            print(i)
    if number == 3:
        card_list.sort()
    if number == 4:
        break

