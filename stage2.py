#总体思路：逐个提取列表的内容，判断是否大于10，如果是则提取个位与十位新添加到一个列表，利用第一题去计算组合列表的内容。把计算到的组合列表和上一次重新组合新列表
from stage1 import *
def main():
    list_tmp = []  # 存放个位与十位
    list_res = []  # 存放返回的组合列表
    tmp=[]
    new_list = []
    flag = 1
    list_num = input("Please enter input your list for example：[1,2,3,4]\n ")
    try:
        list_num = eval(list_num)
    except Exception as e:
        flag = 0

    for i in list_num:
        if i >= 0 and i <= 99:
            if i>9 and i <=99:
                num_1 = i % 10   #个位
                list_tmp.append(int(num_1))
                num_2 =int(i / 10)    #十位
                list_tmp.append(num_2)
                list_res = merge(list_tmp)  #获取两位数以上的字符组合
                list_tmp = []
            else:
                list_tmp.append(i)
                list_res = merge(list(list_tmp))  # 获取1位数以内的字符组合
                list_tmp = []
        else:
            print("your list is not in [0,99]")
            exit(0)
        if len(tmp) == 0:  # 首次直接赋予tmp为0-9的内容
            tmp = list_res
        else:
            for t in tmp:
                for d in list_res:
                    new_list.append(t + d)
            tmp = new_list
            new_list = []
    print(tmp)

if __name__ == '__main__':
    main()