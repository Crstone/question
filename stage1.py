#总体思路：逐个遍历输入的列表，每次与上次组合结果生成新的组合列表
dic = {}
dic[0] = []
dic[1] = []
dic[2] = ["a","b","c"]
dic[3] = ["d","e","f"]
dic[4] = ["g","h","i"]
dic[5] = ["j","k","l"]
dic[6] = ["m","n","o"]
dic[7] = ["p","q","r","s"]
dic[8] = ["t","u","v"]
dic[9] = ["w","x","y","Z"]


def merge(list_num):
    tmp = []
    new_list = []
    for i in list_num:       #循环读取列表的内容
        if i >=0 and i<=9:
            if len(tmp) == 0 :     #首次直接赋予tmp为0-9的内容
                tmp = dic[i]
            else:           #非首次则与tmp列表组合新的列表
                for t in tmp:
                    if i == 0 or i == 1:      #如果为1和0则保持tmp不变
                        pass
                    else:
                        for d in dic[i]:
                            new_list.append(t + d)
                        tmp = new_list
                new_list = []
        else:
            print("your list is not in [0,9]")
            exit(0)
    return tmp


def main():
    flag = 1
    list_num = input("Please enter input your list for example：[1,2,3,4]\n ")
    try:
        list_num = eval(list_num)
    except Exception as e:
        flag = 0

    if flag == 1:
        tmp = merge(list_num)
        print(tmp)
    else:
        print("your list is not in [0-9]")

if __name__ == '__main__':
    main()

