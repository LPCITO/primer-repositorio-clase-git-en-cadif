import time

# Lista de tuplas: (línea de la canción, tiempo de espera en segundos)
letra_con_ritmo = [
    ("Dile al amor...", 1.0),
    ("que no toque mi puerta", 1.5),
    ("que yo no estoy en casa", 1.2),
    ("que no vuelva mañana", 2.0),
    ("a mi corazón ya le han fallado en ocasiones", 3.0),
    ("me fui de vacaciones, lejos de los amores", 2.5),
    ("Dile al amor...", 1.0),
    ("que no es grato en mi vida", 1.5),
    ("dale mi despedida", 1.2),
    ("cuéntale las razones", 2.0),
    ("Yes sir, le gusta mi bachata", 1.8),
    ("Amiguita", 1.0),
    ("No quiero fechas en mi calendario", 2.0),
    ("ni citas en mi horario", 2.0),
    ("si se trata de amor", 2.5)
]

# Recorre la lista de tuplas
for linea, tiempo_de_espera in letra_con_ritmo:
    # Imprime la línea
    print(linea)
    # Pausa por el tiempo especificado en la tupla
    time.sleep(tiempo_de_espera)