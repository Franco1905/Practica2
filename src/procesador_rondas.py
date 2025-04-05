def calcular_puntos(score):
    """
    Calcula los puntos de un jugador en una ronda.
    """
    puntos = score.get('kills') * 3 + score.get('assists')
    if score.get('deaths'):
        puntos -= 1
    return puntos


def mvp(puntosTotales, totalPartida):
    """
    Calcula el jugador con más puntos (MVP) en una ronda.
    """
    max = -1
    maxPlay = ''
    for player in puntosTotales:
        if puntosTotales[player] > max:
            max = puntosTotales[player]
            maxPlay = player
    totalPartida[maxPlay]['mvp'] += 1
    return maxPlay, max


def procesar_ronda(round_data, totalPartida, puntosTotales):
    """
    Procesa una ronda completa, actualiza los datos de totalRonda, totalPartida y calcula el MVP.
    """
    totalRonda = {player: {'kills': 0, 'assists': 0, 'deaths': False, 'puntos': 0} for player in round_data}

    for player, score in round_data.items():
        # Calculamos los puntos del jugador
        puntos = calcular_puntos(score)

        # Actualizamos los valores de totalRonda
        totalRonda[player]['kills'] = score.get('kills')
        totalRonda[player]['assists'] = score.get('assists')
        totalRonda[player]['deaths'] = score.get('deaths')
        totalRonda[player]['puntos'] = puntos

        # Actualizamos puntosTotales para calcular el MVP
        puntosTotales[player] = puntos

        # Actualizamos totalPartida
        totalPartida[player]['kills'] += score.get('kills')
        totalPartida[player]['assists'] += score.get('assists')
        totalPartida[player]['puntos'] += puntos
        if score.get('deaths'):
            totalPartida[player]['deaths'] += 1

    # Calculamos el MVP de la ronda
    maxPlay, maxPuntos = mvp(puntosTotales, totalPartida)

    return totalRonda, maxPlay, maxPuntos


def imprimir_resultados_ronda(round_number, totalRonda, maxPlay, maxPuntos):
    """
    Imprime los resultados de una ronda.
    """
    print('*' * 32)
    print(f'Round numero {round_number}')
    print('*' * 32)
    for player, stats in totalRonda.items():
        print(f"{player}: {stats}")
    print(f'MVP de la ronda: {maxPlay} con {maxPuntos} puntos')


def imprimir_resultados_totales(totalPartida):
    """
    Imprime los resultados totales de la partida.
    """
    print('*' * 32)
    print('PUNTUACION TOTAL')
    print('*' * 32)
    for player, stats in totalPartida.items():
        print(f"{player}: {stats}")

# hace todo
def code (rounds, totalPartida , puntosTotales):    
    for i, round_data in enumerate(rounds):
     totalRonda, maxPlay, maxPuntos = procesar_ronda(round_data, totalPartida, puntosTotales)
     imprimir_resultados_ronda(i + 1, totalRonda, maxPlay, maxPuntos)
     for player in puntosTotales:
         puntosTotales[player] = 0

# Imprimir los resultados totales
    return(totalPartida)
        