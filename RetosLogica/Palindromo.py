"""
Verifica si una palabra o número es igual al revés.
"""

def palindromo(text):
    text = str(text)

    list_texto = list(text)
    list_texto_r = list_texto[::-1]

    return "Si es Palindromo" if list_texto == list_texto_r else "No es Palindromo"

print(palindromo("abcba"))