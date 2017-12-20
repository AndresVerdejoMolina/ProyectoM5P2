# encoding: utf -8
def morse(signo):
    if signo == 'a' or signo == 'A':
        traduccion = '.-'
    if signo == 'b' or signo == 'B':
        traduccion = '-...'
    if signo == 'c' or signo == 'C':
        traduccion = '-.-.'
    if signo == 'd' or signo == 'D':
        traduccion = '-..'
    if signo == 'e' or signo == 'E':
        traduccion = '.'
    if signo == 'f' or signo == 'F':
        traduccion = '..-.'
    if signo == 'g' or signo == 'G':
        traduccion = '--.'
    if signo == 'h' or signo == 'H':
        traduccion = '....'
    if signo == 'i' or signo == 'I':
        traduccion = '..'
    if signo == 'j' or signo == 'J':
        traduccion = '.---'
    if signo == 'k' or signo == 'K':
        traduccion = '-.-'
    if signo == 'l' or signo == 'L':
        traduccion = '.-..'
    if signo == 'm' or signo == 'M':
        traduccion = '--'
    if signo == 'n' or signo == 'N':
        traduccion = '-.'
    if signo == 'ñ' or signo == 'Ñ':
        traduccion = '--.--'
    if signo == 'o' or signo == 'O':
        traduccion = '---'
    if signo == 'p' or signo == 'P':
        traduccion = '.--.'
    if signo == 'q' or signo == 'Q':
        traduccion = '--.-'
    if signo == 'r' or signo == 'R':
        traduccion = '.-.'
    if signo == 's' or signo == 'S':
        traduccion = '...'
    if signo == 't' or signo == 'T':
        traduccion = '_'
    if signo == 'u' or signo == 'U':
        traduccion = '..-'
    if signo == 'v' or signo == 'V':
        traduccion = '...-'
    if signo == 'w' or signo == 'W':
        traduccion = '.--'
    if signo == 'x' or signo == 'X':
        traduccion = '-..-'
    if signo == 'y' or signo == 'Y':
        traduccion = '-.--'
    if signo == 'z' or signo == 'Z':
        traduccion = '--..'
    if signo == '0':
        traduccion = '-----'
    if signo == '1':
        traduccion = '.----'
    if signo == '2':
        traduccion = '..---'
    if signo == '3':
        traduccion = '...--'
    if signo == '4':
        traduccion = '....-'
    if signo == '5':
        traduccion = '.....'
    if signo == '6':
        traduccion = '-....'
    if signo == '7':
        traduccion = '--...'
    if signo == '8':
        traduccion = '---..'
    if signo == '9':
        traduccion = '----.'
    if signo == '.':
        traduccion = '.-.-.-'
    if signo == ',':
        traduccion = '--..--'
    if signo == '?':
        traduccion = '..--..'
    if signo == '!':
        traduccion = '-.-.--'
    if signo == ' ':
        traduccion = ' '
    return traduccion
 
print 'Introduce el texto, para traducir a morse:'
texto = raw_input('> ')
 
for letra in texto:
    print morse(letra)
 
raw_input()
