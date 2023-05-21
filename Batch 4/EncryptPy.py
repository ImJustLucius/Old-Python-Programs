#Jonathan M Lucius
#The purpose of this program is to encrypt the text in a file and print it into a new one

Encrypt_Code = {'A':')','a':'0','B':'(','b':'9','C':'*','c':'8',
    'D':'&','d':'7','E':'^','e':'6','F':'%','f':'5',
    'G':'$','g':'4','H':'#','h':'3','I':'@','i':'2', 
    'J':'!','j':'1','K':'Z','k':'z','L':'Y','l':'y', 
    'M':'X','m':'x','N':'W','n':'w','O':'V','o':'v', 
    'P':'U','p':'u','Q':'T','q':'t','R':'S','r':'s', 
    'S':'R','s':'r','T':'Q','t':'q','U':'P','u':'p', 
    'V':'O','v':'o','W':'N','w':'n','X':'M','x':'m', 
    'Y':'L','y':'l','Z':'K','z':'k','!':'J','1':'j', 
    '@':'I','2':'i','#':'H','3':'h','$':'G','4':'g', 
    '%':'F','5':'f','^':'E','6':'e','&':'D','7':'d', 
    '*':'C','8':'c','(':'B','9':'b',')':'A','0':'a', 
    ':':',',',':':','?':'.','.':'?','<':'>','>':'<', 
    "'":'"','"':"'",'+':'-','-':'+','=':';',';':'=', 
    '{':'[','[':'{','}':']',']':'}'}

def Encrypter(inpfile):

    Output = str(input('Please enter the name of the output file: '))
    f = open(Output+".txt", "w")
    
    for line in inpfile:
        for letter in line:
            ans = Encrypt_Code.get(letter, letter)
            f.write(ans)
    
    f.close
  
Input = input('Please enter the name of the input file: ')
r = open(Input+".txt", "r")

read = r.readlines()
Encrypter(read)