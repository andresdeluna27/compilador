import sys
tokens=open('tokens.txt','w+')
lexemas=open('lexemas.txt','w+')
erroresLexicos=open('erroresLexicos.txt','w+')
finCom=True
ln=1
col=2
b=0


def scanner(texto):
    i=0
    z=0
    reservadas=("main","if","then","else","end","do","while","repeat","until","cin","cout","real","int","boolean")
    simbolos=("+","-","*","/","%","(",")","{","}",",",";")
    lexema=""
    global finCom
    global b
    global ln
    global col
    while i<len(texto):
        if finCom==True:
            lexema=""
            c=0
            while i<len(texto):
                c=0
                if texto[i]==chr(32):# or texto[i]=="\t":
                    i+=1
                    col+=1
                elif texto[i]=="\t":
                    i+=1
                    col+=4
                elif texto[i]=="\n":
                    i+=1
                    ln+=1
                    col=1
                else:
                    if  texto[i]=="/" and texto[i+1]=="/":
                        lexema+=texto[i]+texto[i+1]
                        print("{simbolo especial,",lexema,"} ")
                        msj="{simbolo especial,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        #lexemas.write(lexema)
                        #lexemas.write('\n')
                        i+=2
                        col+=2
                        lexema=""
                        while i<len(texto) and texto[i]!="\n":
                            i+=1
                            #col+=1 #lo quito para ver si ya no se desfaza, igual despues de los comentarios es linea nueva
                    elif texto[i]=="/" and texto[i+1]=="*":
                        lexema+=texto[i]+texto[i+1]
                        print("{simbolo especial,",lexema,"} ")
                        msj="{simbolo especial,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        #lexemas.write(lexema)
                        #lexemas.write('\n')
                        lexema=""
                        i+=2
                        col+=2
                        if texto[i]=="\n":
                            i+=1
                            col=1
                            ln+=1
                            finCom=False
                            break
                        hecho=False
                        while hecho == False and i < len(texto):
                            while i<len(texto) and texto[i]!="*":
                                i+=1
                                col+=1
                            while i<len(texto) and texto[i]=="*":
                                i+=1
                                col+=1
                                if texto[i]=="/":
                                    lexema+=texto[i-1]+texto[i]
                                    print("{simbolo especial,",lexema,"} ")
                                    msj="{simbolo especial,",lexema,"}"
                                    tokens.write(str(msj))
                                    tokens.write('\n')
                                    #lexemas.write(lexema)
                                    #lexemas.write('\n')
                                    lexema=""
                                    i+=1
                                    if texto[i]=="\n":
                                        #ln+=1 #la agregue para ver desfasamiento 
                                        col=1
                                    col+=1
                                    hecho=True
                                    finCom=True
                        #while i<len(texto) and texto[i]!="*" and texto[i+1]!="/":
                            #i+=1
                        #lexema+=texto[i]+texto[i+1]
                        #print("{3,",lexema,"} ")
                        #msj="{3,",lexema,"}"
                        #tokens.write(str(msj))
                        #tokens.write('\n')
                        #lexema=""
                        #i+=2
                    elif texto[i]=="/":
                        lexema=texto[i]
                        print("{operador,",lexema,"} ")
                        msj="{operador,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        lexemas.write(lexema)
                        lexemas.write('\n')
                        i+=1
                        col+=1
                        lexema=""
                    elif texto[i].isalpha():
                        lexema+=texto[i]
                        i+=1
                        col+=1
                        while i<len(texto):
                            if texto[i].isalnum() or texto[i]=="_":
                                lexema+=texto[i]
                                i+=1
                                col+=1
                            else:
                                break
                        j=0
                        bandera=1
                        while j<len(reservadas):
                            if lexema==reservadas[j]:
                                print("{palabra reservada,",lexema,"} ")
                                msj="{palabra reservada,",lexema,"}"
                                tokens.write(str(msj))
                                tokens.write('\n')
                                lexemas.write(lexema)
                                lexemas.write('\n')
                                lexema=""
                                bandera=0
                                break
                            else:
                                j+=1
                        if bandera!=0:
                            print("{identificador,",lexema,"} ")
                            msj="{identificador,",lexema,"}"
                            tokens.write(str(msj))
                            tokens.write('\n')
                            lexemas.write(lexema)
                            lexemas.write('\n')
                            lexema=""
                    elif texto[i]=="+" and texto[i+1]=="+":
                         lexema+=texto[i]+texto[i+1]
                         print("{operador,",lexema,"} ")
                         msj="{operador,",lexema,"}"
                         tokens.write(str(msj))
                         tokens.write('\n')
                         lexemas.write(lexema)
                         lexemas.write('\n')
                         lexema=""
                         i+=2
                         col+=2
                   # elif texto[i]=="+" and texto[i+1].isdigit():
                    #    lexema=texto[i]+texto[i+1]
                     #   i+=2
                      #  col+=2
                       # while i<len(texto) and texto[i].isdigit():
                        #    lexema+=texto[i]
                         #   i+=1
                          #  col+=1
                        #if texto[i]==".":#if texto[i]=="." and texto[i+1].isdigit():
                         #   if texto[i+1].isdigit():
                          #      lexema+=texto[i]+texto[i+1]
                           #     i+=2
                            #    col+=2
                             #   while i<len(texto) and texto[i].isdigit():
                              #      lexema+=texto[i]
                                #    i+=1
                                 #   col+=1
                           # else:
                            #    c=1
                                #print("{constante numerica entera,",lexema,"} ")
                                #msj="{constante numerica entera,",lexema,"}"
                                #tokens.write(str(msj))
                                #tokens.write('\n')
                                #lexema=""
                             #   lexema+=texto[i]+texto[i+1]
                              #  print("error en ",lexema," en la linea ",ln," y columna ",col)
                               # msj="error en ",lexema," en linea ",ln," y columna ",col
                               # erroresLexicos.write(str(msj))
                               # erroresLexicos.write('\n')
                                #i+=2
                                #col+=2
                                #lexema=""
                       # if "." in lexema and lexema!=" ":
                        #    print("{constante numerica real,",lexema,"} ")
                         #   msj="{constante numerica real,",lexema,"}"
                          #  tokens.write(str(msj))
                           # tokens.write('\n')
                            #lexema=""
                        #else:
                         #   if c==0:
                          #      print("{constante numerica entera,",lexema,"} ")
                           #     msj="{constante numerica entera,",lexema,"}"
                            #    tokens.write(str(msj))
                             #   tokens.write('\n')
                              #  lexema=""
                    elif texto[i]=="+":
                        lexema+=texto[i]
                        i+=1
                        col+=1
                        print("{operador,",lexema,"} ")
                        msj="{operador,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        lexemas.write(lexema)
                        lexemas.write('\n')
                        lexema=""
                    elif texto[i]=="-" and texto[i+1]=="-":
                        lexema+=texto[i]+texto[i+1]
                        print("{operador,",lexema,"} ")
                        msj="{operador,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        lexemas.write(lexema)
                        lexemas.write('\n')
                        lexema=""
                        i+=2
                        col+=2
                   # elif texto[i]=="-" and texto[i+1].isdigit():
                    #    lexema=texto[i]+texto[i+1]
                     #   i+=2
                      #  col+=2
                       # while i<len(texto) and texto[i].isdigit():
                        #    lexema+=texto[i]
                         #   i+=1
                          #  col+=1
                        #if texto[i]==".":#if texto[i]=="." and texto[i+1].isdigit():
                         #   if texto[i+1].isdigit():
                          #      lexema+=texto[i]+texto[i+1]
                           #     i+=2
                            #    col+=2
                             #   while i<len(texto) and texto[i].isdigit():
                              #      lexema+=texto[i]
                               #     i+=1
                                #    col+=1
                           # else:
                            #    c=1
                                #print("{constante numerica entera,",lexema,"} ")
                                #msj="{constante numerica entera,",lexema,"}"
                                #tokens.write(str(msj))
                                #tokens.write('\n')
                                #lexema=""
                                #lexema=texto[i]
                               # lexema+=texto[i]+texto[i+1] 
                               # print("error en ",lexema, "en la linea ",ln," y columna",col-1)
                                #msj="error en ",lexema," en la linea ",ln," y columna ",col-1
                                #erroresLexicos.write(str(msj))
                                #erroresLexicos.write('\n')
                                #i+=2
                                #col+=2
                                #lexema=""
                        #if "." in lexema and lexema!=" ":
                         #   print("{constante numerica real,",lexema,"} ")
                          #  msj="{constante numerica real,",lexema,"}"
                           # tokens.write(str(msj))
                            #tokens.write('\n')
                            #lexema=""
                        #else:
                            #if c==0:
                                #print("{constante numerica entera,",lexema,"} ")
                                #msj="{constante numerica entera,",lexema,"}"
                                #tokens.write(str(msj))
                                #tokens.write('\n')
                                #lexema=""
                    elif texto[i]=="-":
                        lexema+=texto[i]
                        i+=1
                        col+=1
                        print("{operador,",lexema,"} ")
                        msj="{operador,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        lexemas.write(lexema)
                        lexemas.write('\n')
                        lexema=""
                    elif texto[i].isdigit():
                        lexema+=texto[i]
                        i+=1
                        col+=1
                        while i<len(texto) and texto[i].isdigit():
                            lexema+=texto[i]
                            i+=1
                            col+=1
                        if texto[i]==".":
                            if texto[i+1].isdigit():
                                lexema+=texto[i]+texto[i+1]
                                i+=2
                                col+=2
                                while i<len(texto) and texto[i].isdigit():
                                    lexema+=texto[i]
                                    i+=1
                                    col+=1
                            else:
                                c=1
                                #print("{constante numerica entera,",lexema,"} ")
                                #msj="{constante numerica entera,",lexema,"}"
                                #tokens.write(str(msj))
                                #tokens.write('\n')
                                #lexema=""
                                lexema+=texto[i]+texto[i+1]
                                print("error en ",lexema," en la linea ",ln," y columna ",col-1)
                                msj="error en ",lexema," en la linea",ln," y columna ",col-1
                                erroresLexicos.write(str(msj))
                                erroresLexicos.write('\n')
                                i+=2
                                col+=2
                                lexema=""
                        if "." in lexema and lexema!="":
                            print("{constante numerica real,",lexema,"} ")
                            msj="{constante numerica real,",lexema,"}"
                            tokens.write(str(msj))
                            tokens.write('\n')
                            lexemas.write(lexema)
                            lexemas.write('\n')
                            lexema=""
                        else:
                            if c==0:
                                print("{constante numerica entera,",lexema,"} ")
                                msj="{constante numerica entera,",lexema,"}"
                                tokens.write(str(msj))
                                tokens.write('\n')
                                lexemas.write(lexema)
                                lexemas.write('\n')
                                lexema=""
                    elif texto[i]=="<" or texto[i]==">" or texto[i]=="!" or texto[i]==":" or texto[i]=="=":
                        lexema+=texto[i]
                        i+=1
                        col+=1
                        if texto[i]=="=":
                            lexema+=texto[i]
                            i+=1
                            col+=1
                            print("{operador,",lexema,"} ")
                            msj="{operador,",lexema,"}"
                            tokens.write(str(msj))
                            tokens.write('\n')
                            lexemas.write(lexema)
                            lexemas.write('\n')
                            lexema=""
                        else:
                            if lexema==":":
                                print("error en ",lexema," en la linea ",ln," y columna ",col-2)
                                msj="error en ",lexema," en la linea ",ln," y columna ",col-2
                                erroresLexicos.write(str(msj))
                                erroresLexicos.write('\n')
                                lexema=""
                            if lexema=="=":
                                print("error en ",lexema," en la linea ",ln," y columna ",col-2)
                                msj="error en ",lexema," en la linea ",ln," y columna ",col-2
                                erroresLexicos.write(str(msj))
                                erroresLexicos.write('\n')
                                lexema=""
                            else:
                                print("{operador,",lexema,"} ")
                                msj="{operador,",lexema,"}"
                                tokens.write(str(msj))
                                tokens.write('\n')
                                lexemas.write(lexema)
                                lexemas.write('\n')
                                lexema=""
                    elif texto[i] in simbolos:
                        lexema+=texto[i]
                        i+=1
                        col+=1
                        print("{simbolo especial,",lexema,"} ")
                        msj="{simbolo especial,",lexema,"}"
                        tokens.write(str(msj))
                        tokens.write('\n')
                        lexemas.write(lexema)
                        lexemas.write('\n')
                        lexema=""
                    else:
                        print("error en ",texto[i]," en la linea ",ln," y columna ",col-1)
                        msj="error en ",texto[i]," en la linea ",ln," y columna ",col-1
                        erroresLexicos.write(str(msj))
                        erroresLexicos.write('\n')
                        i+=1
                        col+=1
                        lexema=""
        while i < len(texto) and finCom==False:
            while i<len(texto) and b==0 and texto[i]!="*":
                if texto[i]=="\n":
                    ln+=1
                    col=1
                    i+=1
                else:
                    i+=1
                    col+=1
            b=1
            if i<len(texto):
                i+=1
                col+=1
                if b==1 and texto[i]=="/":
                    lexema+=texto[i-1]+texto[i]
                    print("{simbolo especial,",lexema,"} ")
                    msj="{simbolo especial,",lexema,"}"
                    tokens.write(str(msj))
                    tokens.write('\n')
                    #lexemas.write(lexema)
                    #lexemas.write('\n')
                    i+=1
                    lexema=" "
                    finCom=True
                    break
                else:
                    if texto[i]=="\n":
                             ln+=1
                             col=1         
                    i+=1
                    col+=1
                    b=0
        
    


    
#cadena=" int vector, su&mas, res@tas,suma1,suma2,25ert;5 7 7.5 +5 -6 (){]\t"
archi=open(sys.argv[1],'r')
cadena=""
lineas=archi.readlines()
for li in lineas:
    cadena+=str(li)+" "    
scanner(cadena)  
archi.close()
tokens.close()
lexemas.close()
erroresLexicos.close()
