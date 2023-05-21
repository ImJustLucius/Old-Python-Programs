#Jonathan M Lucius 
#The purpose of this program is to mimic a magic 8 ball and give random answers to questions.
import random

def Response(fate):
    ans_list = ['It is certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes - definitely.', 'You may rely on it.',
    'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 
    'Better not tell you now.', 'Cannot predict now.', 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 
    'My sources say no.', 'Outlook not so good.', 'Very doubtful.']

    answer = ans_list[fate]
    
    print(answer)

def main():
    loop = 'yes'

    while(loop!='no'):
        question = input('What is your question? ')

        luck = random.randint(0,19)
        Response(luck)
        
        loop = input('Would you like to ask another question? ')
        loop = loop.lower()
    
main()
