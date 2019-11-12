RockPaperScissors
1-rock
2-scissors
3-paper
'''

import random
x=random.randint(1, 3)
y=input('ваш выбор: ')
#win
if y=='1' and x==2:
    print('rock vs scissors','you win!')
elif y=='2' and x==3:
    print('scissors vs paper','you win!')
elif y=='3' and x==1:
    print('paper vs rock','you win!')
#lose
    
if y=='2' and x==1:
    print('scissors vs rock','you lose!')
elif y=='3' and x==2:
    print('paper vs scissors','you lose!')
elif y=='1' and x==3:
    print('rock vs paper','you lose!')
#ничья
if y=='1' and x==1:
    print('rock vs rock','ничья!')
elif y=='2' and x==2:
    print('scissors vs scissors','ничья!')
elif y=='3' and x==3:
    print('paper vs paper','ничья!')
    
else:
    print('')
