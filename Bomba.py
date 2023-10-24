from time import sleep
for pojemnik in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, ]:
  print (pojemnik)
  sleep (1)
  if pojemnik == 10:
    print ('My Good this is the bomb!')
  if pojemnik == 8: 
    print ('How much time we have? Seven seconds!')
  if pojemnik == 5: 
    print ('I will try to disarm it, please leave the building! no way! ')
    sleep(1)
  if pojemnik == 4: 
   print('Are You sure how to do it? no, but I have no choice')
  sleep(1)
  if pojemnik <= 3:  
    sleep(1)
  if pojemnik == 1:  
   print ('red or green?')
   sleep(1)
   print ('red!')
   sleep(1)
   print ('Oh now!')
   sleep(1)
   print ('Run!')
   sleep(1)  
sleep(1)
print ('KAABBUM')
