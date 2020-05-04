
romanos = {'M': 1000,
           'D': 500,
           'C': 100,
           'L': 50,
           'X': 10,
           'V': 5,
           'I': 1,
           }

existen = ['IV', 'IX', 'XL', 'XC', 'CD', 'CM']


def romano_a_entero(numero_romano):

    if numero_romano == '':
        return 'Error en formato'
    if len(numero_romano) > 5:
        return 'Error en formato'

    entero = 0
    numRepes = 1
    letraAnt = ''
    contadorResta = 0

    for simbolo in numero_romano:

        if simbolo in romanos:
            if letraAnt == '' or romanos[letraAnt] >= romanos[simbolo]:
                entero += romanos[simbolo]
                contadorResta = 0
            else:
                if letraAnt + simbolo in existen and numRepes < 2 and contadorResta < 1:
                    entero = entero - romanos[letraAnt] * 2 + romanos[simbolo]
                    contadorResta += 1
                else:
                    return 'Error en formato'
        else:
            return 'Error en formato'

        if simbolo == letraAnt and numRepes == 3:
            return 'Error en formato'
        elif simbolo == letraAnt:
            numRepes += 1
        else:
            numRepes = 1

        letraAnt = simbolo
    return entero
