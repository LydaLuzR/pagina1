def palindromo(palabra):
    palabra= palabra.replace(" ", "")
    palabra=palabra.lower()
    palabra_in= palabra[::-1]
    if palabra==palabra_in:
        return True
    else:
        return False

def run():
    palabra=input("Escribe una palabra: ")
    es_palindromo= palindromo(palabra)
    if es_palindromo==True: 
        print("Es palindromo")
    else:
        print("No es palindormo")


if __name__ == '__main__': 
    run()