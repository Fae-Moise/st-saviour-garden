

if __name__ == '__main__':

    # print without a line break using this function

    # i'm using 🌺 and 🌸

   print('solid')
   for i in range (11):
      for j in range(11): 
         print('🌺' , end = '')
         # print ('🌸' , end = '')
      print ('')

   print('horizontal')    
   for i in range (11):
      for j in range(11):
         if i % 2 == 0:
            print('🌺' , end ='')
         else:
            print('🌸' , end = '')
      print('')
                        
   print('vertical')
   for i in range(11):
      for j in range(11):
         if j % 2 == 0:
            print('🌸', end='')
         else:
            print('🌺', end='')
      print('')
   print('diagonal')
for i in range(11):
        for j in range(11):
            if j % 2 == 0 and i % 2 == 0:
                print('🌸', end='')
            elif j % 2 == 1 and i % 2 == 1:
                print('🌺', end='')
            else:
                print('🌸', end='')
        print('')
print('plaid')
for i in range(11):
        for j in range(11):
            if j % 2== 0 and i % 2== 0:
                print('🌸', end='')
            else:
                print('🌺', end='')
        print('')



