#识人术
name=input('请输入你的名字：')
handsome=input('请为你的颜值打分(0-100):')
game=input('请输入你最喜欢的游戏：')
x=int(handsome)
if x==100:
    print(name,'你是一个爱玩'+game+'的大帅哥')
elif x>=70:
    print(name,'你是一个爱玩'+game+'的有点小帅的人')
elif x>=50:
    print(name,'你是一个爱玩'+game+'的普通人')
elif x>=20:
    print(name,'你是一个爱玩'+game+'的不太帅的人')
elif x>=0:
    print('李孟你别乱用'+name+'的名字')
elif x<0:
    print('彩蛋')

input('请按回车键退出')
