"""
Conjunto de estados = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17}
Estado inicial: 0
Estado de aceptación: {1,2,5,6,7,9,11,12,13,14,15,16,17}
Estado de terminación abrupta: {3}
"""
"Actividad 3.2: Programando un DFA"
"Jesus Alejandro - A01282990"
"Carlos Tadeo - A01197315"

"""
tokens = {
  "=":"Asignacion",
  "+":"Suma",
  "-":"Resta",
  "*":"Multiplicacion",
  "/":"Division",
  "^":"Potencia",
  "(":"Parentesis que abre",
  ")":"Parentesis que cierra",
  "//":"Comentario",
  ".":"Real",
  "int":"Entero",
  "var":"Variable"
}

caracteres = ["=", "+","-", "*", "/", "^", "(", ")"]

"def readLines(line):"

"""
import webbrowser
import re



def lexerAritmetico(file):
    
    regexAnd = re.compile(r'and')
    regexAs = re.compile(r'as')
    regexAssert = re.compile(r'assert')
    regexBreak = re.compile(r'break')
    regexContinue = re.compile(r'continue')
    regexDel = re.compile(r'del')
    regexElif = re.compile(r'elif')
    regexElse = re.compile(r'Else')
    regexExcept = re.compile(r'Except')
    regexFalse = re.compile(r'False')
    regexfinally = re.compile(r'finally')
    regexFor = re.compile(r'for')
    regexFrom = re.compile(r'from')
    regexGlobal = re.compile(r'global')
    regexIf = re.compile(r'if')
    regexImport = re.compile(r'import')
    regexIn = re.compile(r'in')
    regexIs = re.compile(r'is')
    regexLambda = re.compile(r'lambda')
    regexNone = re.compile(r'None')
    regexNonlocal = re.compile(r'nonlocal')
    regexNot = re.compile(r'not')
    regexOr = re.compile(r'or')
    regexPass = re.compile(r'pass')
    regexRaise = re.compile(r'raise')
    regexReturn = re.compile(r'return')
    regexTrue = re.compile(r'true')
    regexTry = re.compile(r'try')
    regexWhile = re.compile(r'while')
    regexWith = re.compile(r'with')
    regexYield = re.compile(r'yield')


    f=open("1.html","w")
    f.write('<body style="background-color:black; font-size:100">')

    
   
   

    archivo = open(file)
    a = archivo.read()
    lineas = a.split("\n")

    print("\nToken                Tipo\n")

    for linea in lineas:
        
        # linea = linea + "\n"
        linea = linea.replace("="," = ")
        linea = linea.replace("*"," * ")
        linea = linea.replace("("," ( ")
        linea = linea.replace(")"," ) ")
        tokens = linea.split(" ")
        contador = 0

        for token in tokens:
            message = ''
            contador+= 1
            estado = 0
            token_procesado = ""
            character = ""
            for character in token:
                token_procesado += character

            if re.search(regexAnd, token_procesado):
                print(token_procesado, "                Entero\n\n")
                message = "<span style=\"color:#b5cea8\">" + token_procesado + "<span>"
                f.write(message)
                
            if re.search(regexAnd, token_procesado):
                print(token_procesado, "                Entero\n\n")
                message = "<span style=\"color:#b5cea8\">" + token_procesado + "<span>"
                f.write(message)


                
                    
            elif estado == 5:
                print(token_procesado, "                Asignacion\n\n")
                message = "<span style=\"color:#d4d4d4\">" + token_procesado + "<span>"
                f.write(message)

                
            elif estado == 6:
                print(token_procesado, "                Flotante\n\n")
                message = "<span style=\"color:#b1c9a4\">" + token_procesado + "<span>"
                f.write(message)

                
            elif estado == 7:
                print(token_procesado, "                Variable\n\n")
                message = "<span style=\"color:#9cdcfb\">" + token_procesado + "<span>"
                f.write(message)

            elif estado == 11:
                

                rango = len(tokens) - contador
                comentario = ""
                for i in range (rango + 1):
                    comentario+=tokens[(contador - 1) + i] + " "
                print(comentario, "                Comentario\n\n")
                message = "<span style=\"color:#6a9955\">" + comentario + "<span>"
                f.write(message)
                break
                
            elif estado == 12:
                print(token_procesado, "                Flotante\n\n")
                message = "<span style=\"color:#b1c9a4\">" + token_procesado + "<span>"
                f.write(message)


            elif estado == 2:
                print(token_procesado, "                Parentesis que abre\n\n")
                message = "<span style=\"color:#fcd84a\">" + token_procesado + "<span>"
                f.write(message)

            
            elif estado == 13:
                print(token_procesado, "                Parentesis que cierra\n\n")
                message = "<span style=\"color:#fcd84a\">" + token_procesado + "<span>"
                f.write(message)

            
            elif estado == 9:
                print(token_procesado, "                Suma\n\n")
                message = "<span style=\"color:#d4d4d4\">" + token_procesado + "<span>"
                f.write(message)

                
            elif estado == 14:
                print(token_procesado, "               Resta\n\n")
                message = "<span style=\"color:#d4d4d4\">" + token_procesado + "<span>"
                f.write(message)

                
            elif estado == 15:
                print(token_procesado, "                Multiplicacion\n\n")
                message = "<span style=\"color:#d4d4d4\">" + token_procesado + "<span>"
                f.write(message)

            
            elif estado == 16:
                print(token_procesado, "                Division\n\n")
                message = "<span style=\"color:#d4d4d4\">" + token_procesado + "<span>"
                f.write(message)

                
            elif estado == 17:
                print(token_procesado, "                Potencia\n\n")
                message = "<span style=\"color:#d4d4d4\">" + token_procesado + "<span>"
                f.write(message)


            elif estado == 18:
                print(token_procesado, "                End of line\n\n")
                message = "<p></p>"
                f.write(message)

                

            # elif estado != 1 or estado != 5 or estado != 6 or estado != 7 or estado != 11 or estado != 12 or estado != 13 or estado != 9 or estado != 14 or estado != 15 or estado != 16 or estado != 17:
            #     print("el token:",token, "no es un token valido")
            
            
    f.close()
    webbrowser.open_new_tab("1.html")

    return

lexerAritmetico('casosDePrueba.txt')


