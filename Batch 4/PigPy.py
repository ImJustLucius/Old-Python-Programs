#Jonathan M Lucius 
#The purpose of this program is to take text file inputs and convert them to pig latin

f = open("C:/Users/jonal/Documents/Coding/Python/Batch 4/surfacepressure.txt", "r")
file = f.readlines()

n = open("newpig.txt", "w")

def latinator(word):
    if(len(word)>1):
        ans = word[1:] + word[0] + 'ay'
    else:
        ans = word + 'ay'
    
    return ans

def Sentence_Scramble(line):    
    line_list = line.split(" ")
    ans = ''
    for x in line_list:
        fix = x.rstrip()
        ans += latinator(fix) + ' '
    ans += '\n'
    return ans

for x in file:
    #print(x)
    #print(Sentence_Scramble(x))
    n.write(Sentence_Scramble(x))

f.close
