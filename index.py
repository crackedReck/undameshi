import random
import sys
c_count = 0
lnumber = random.randint(1,100)
rnumber = input('割る数')
ans = lnumber / int(rnumber)
c_count+=1
while ans < 1:
        print('数値が大きすぎるよ！')
        rnumber = input('割る数')
        ans = lnumber/int(rnumber)
        c_count+=1
        if c_count==3:
            print('GAMEOVER')
            sys.exit()
print(ans)
print('元の数値'+str(lnumber))
