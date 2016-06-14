low = 0;
high =100;
isGuessed = False

print('Please think of a number between 0 and 100!');

#loop till guess is true.
while not isGuessed:
   #Checking your answer with Bisection Search Algorithm. It allows you to divide the search space in half at each step.
   ans = (low + high)/2;
   print('Is your secret number '+ str(ans) +'?');
   #explanation allows to user to write her/his own input
   explanation = raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ");
   #c represents correct answer. isGuessed will be true and game over.
   if(explanation == 'c'):
       isGuessed = True
   #h is used for that computer's guess is higher than user's secret answer. this means high should be limited by guess.
   elif(explanation == 'h'):
       high = ans
   #c is used for that computer's guess is lower than user's secret answer. this means low should be limited by guess.
   elif(explanation == 'l'):
        low = ans
   #this condition allows us to limit user's input by h, l, or c.
   else:
        print("Sorry, I did not understand your input.")

print('Game over. Your secret number was: ' + str(ans))
        
