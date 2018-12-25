# -*- coding: utf-8 -*-
def fact(n):
    
    # 保存最终结果
    result = 1
    
    # 进行循环控制
    for i in range(1, n + 1):
        result *= i
    
    # 打印输出
    print(result)


def main():
    fact(8)


if __name__ == '__main__':
    main()
