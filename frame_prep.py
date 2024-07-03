# python的列表
list = ['','','','','','','','','','','','','','','']
list_2 = ['']*15
list_3 = ['' for i in range(15)]
print(list)
print(list_2)
print(list_3)

# python的字符串
str = 'XXXXX'
print(str)

# python的循环
for i in range(10):
    print(i)

# python的函数
def foo(x,y):
    print('两数之和为{}'.format(x+y))

foo(10,11)

# 用列表推导式创建一个二维列表
board = [[' ']*15 for line in range(15)]

# 用join方法将列表转化为字符串
list_4 = ['X','X','O','O']
list_str = ''.join(list_4)
print(list_str)

# 用find方法在字符串中查找指定字符串
line = ['O','O','O','O','O']
line_2 = ['O','O','O','O','X']
print('line转化为字符串：',''.join(line))
print('line_2转化为字符串：',''.join(line_2))
print('查找line是否有5个O：',''.join(line).find('O'*5))
print('查找line_2是否有5个O：',''.join(line_2).find('O'*5))

# 创建了一个函数，对某个二维列表的某个元素进行检查，如果不是空格，则打印“该位置已有棋子”，并返回布尔值False
# 如果是空格，则进行赋值操作并返回布尔值True
def set_chess(x,y,color):
    if board[x][y] != ' ':
        print('该位置已有棋子')
        return False
    else:
        board[x][y] = color
        return True