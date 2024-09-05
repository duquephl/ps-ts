#5) Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;

def reverte_string(string):
    string_revertida = ""
    for char in string:
        string_revertida = char + string_revertida
    return string_revertida

print(reverte_string("Hello, World!"))
