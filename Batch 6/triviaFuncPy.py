#Jonathan M Lucius
#The purpose of this code is to act as a the function module for the Trivia game.
import triviaClassPy

def TriviaTime():
    
    Question_list = []
    
    Q1 = triviaClassPy.trivia()
    Q1.set_qna('What is pokemon no.296?', 'Makuhita', 'Bulbasaur', 'Darkrai', 'Lampent',1)
    Q2 = triviaClassPy.trivia()
    Q2.set_qna('Who invented the first electric light?', 'Thomas Edison', \
        'Humphry Davy', 'Nikola Tesla', 'Henry Ford', 2)
    Q3 = triviaClassPy.trivia()
    Q3.set_qna('What anime uses the song "ALL OFF - Refrain Boy"?', 'One Piece', \
        'Pokemon', 'Durarara!!', 'Mob Psycho 100', 4)
    Q4 = triviaClassPy.trivia()
    Q4.set_qna('When was Coca-Cola first made?', 1893, 1886, 1969, 2002, 2)
    Q5 = triviaClassPy.trivia()
    Q5.set_qna('Where is the Grand Canyon located?', 'Florida', 'New York', 'Arizona', 'Colorado', 3)
    Q6 = triviaClassPy.trivia()
    Q6.set_qna('How many sides does a stop sign have?', 5, 6, 8, 10, 3)
    Q7 = triviaClassPy.trivia()
    Q7.set_qna('Solve (x + 6) * 3 = 12?', -2, 0, 9, 2, 1)
    Q8 = triviaClassPy.trivia()
    Q8.set_qna('How many stars are in the solar system?', '12 Billion', '15 Billion', 'Infinite', 1, 4)
    Q9 = triviaClassPy.trivia()
    Q9.set_qna('Who is the grand regent of the Theta Tau fraternity?', 'Me', 'Barack Obama', \
        'Stuart Kardian', 'Tom Pennington', 3)
    Q10 = triviaClassPy.trivia()
    Q10.set_qna('Who won The Great Emu war?', 'Australia', 'Emu', 'Great Britain', \
        'Mother Nature', 2)

    Question_list.append(Q1)
    Question_list.append(Q2)
    Question_list.append(Q3)
    Question_list.append(Q4)
    Question_list.append(Q5)
    Question_list.append(Q6)
    Question_list.append(Q7)
    Question_list.append(Q8)
    Question_list.append(Q9)
    Question_list.append(Q10)
    
    #for x in Question_list:
    #    print(x,'\n')

    return Question_list