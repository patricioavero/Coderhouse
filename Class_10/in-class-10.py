def convertir_tiempo(*args):
    if len(args) == 1:
        # recibí segundos
        segundos = args[0]
        minutos = segundos // 60
        segundos_restantes = segundos % 60
        horas = minutos // 60
        minutos_restantes = minutos % 60

        return horas, minutos_restantes, segundos_restantes
    else:
        # recibí hs minutos y segundos
        horas = args[0]
        minutos = args[1]
        segundos = args[2]

        return horas * 60 * 60 + minutos * 60 + segundos
