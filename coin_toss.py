# FILE NAME - coin_toss.py
# NAME: Mike Rahne
# DATE: 10/6/2025 
# BRIEF DESCRIPTION:  My coint_toss submission
# 1. Make sure you fill out the comments above
# 2. Write your code in the proper spot
# 3. Be sure to answer the Reflection Questions and Attestation below
# 4. The Sample Output has been included in this code for your convenience
########## ENTER YER CODE BELOW THIS LINE ##########


import random

def main():
    c_t_attempt()
def c_t_attempt():


                print ('===== Coin Flipper =====')

                random.seed()
                coin_flip = str(random.randint (1,2))
                

                if (coin_flip) == ('2'):
                    print('Tails')
                else:
                   print('Heads')

main()







########### END YER CODE ABOVE THIS LINE ###########


########################################
#          SAMPLE OUTPUT
########################################
'''
===== Coin Flipper =====
Heads
'''



'''
===== Coin Flipper =====
Tails
'''


########################################
#          REFLECTION QUESTIONS
########################################

'''

1. What was the hardest part of completing this lab? 
#I founf the most difficult par to be figuring out that I had to cast "coin_flip". I think I have a amental blobk on "str". I really need to get over that.






'''

########################################
#            ATTESTATION
########################################
'''
It is critical in this class that you understand the concepts as we explore them because
those concepts are required understanding for entry level programming. Reliance on resources
like AI and internet sites like Chegg, CourseHero, StackOverflow, and general Google results
may impede your understanding. Please rate how well you understand the concepts in this lab: 
[ ] I understand very little about this lab.
[ ] I am about 50/50 on this lab; I get parts of it but not the whole picture.
[ ] I pretty much get it.
[ ] I'm solid. Totally got it.
'''
