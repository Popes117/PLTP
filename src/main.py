import sys 
import ply.lex as lex

from translator import Translator
import analisadorlexico as analisadorlexico
#import analisadorsintatico as analisadorsintatico
import sys


# Versão analisador lexico
def main(args):
    lexer = analisadorlexico.Lexer()
    translation = Translator()

    with open(args[1], 'r') as file:
        lines = file.readlines()
    for line in lines:
        data = line.strip()
        lexer.input(data)
        for i in lexer.lexer:
            if i.type == 'STRING':
                value = translation.forth_push(i.value)
                print(value)
            if i.type == 'NUMBER':
                value = translation.forth_push(i.value)
                print(value)
            elif i.type == 'MATH_OPERATOR':
                value = translation.forth_math(i.value)
                print(value)
            elif i.type == 'POP':
                value = translation.forth_pop()
                print(value)
            elif i.type == 'DOT':
                value = translation.forth_print()
                print(value)
            elif i.type == 'COLON':
                in_func = True
                print("A iniciar função")
            

        print(translation.code)
            


if __name__ == '__main__':
    main(args=sys.argv)