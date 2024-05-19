# Importamos la libreria tabulate que no ayuda a darle una estructura y orden a nuestro tablero
from tablero import coordenadas_tablero
# Importamos las funciones de nuestro tablero
from tablero import logica_tablero
from tablero import preparacion_tablero
from tablero import imprimir_tablero

# Importamos el modulo random 
import random



# Creamos una función para dar la bienvenida al usuario
def bienvenida_usuario():
  print("|BIENVENIDO A...|".center(65,'-'))
  print("""\n
██╗██████╗░███████╗░██████╗░█████╗░░█████╗░████████╗███████╗██╗
██║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║██████╔╝█████╗░░╚█████╗░██║░░╚═╝███████║░░░██║░░░█████╗░░██║
╚═╝██╔══██╗██╔══╝░░░╚═══██╗██║░░██╗██╔══██║░░░██║░░░██╔══╝░░╚═╝
██╗██║░░██║███████╗██████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗██╗
╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝\n""")
  print("|Pulsa enter para comenzar|".center(65, '-'))
  comenzar = input("")


# Debido a la estructura de nuestro tablero, crear un dado de 6 y 8 caras no es una opción
# por lo que crearemos una función que simule el funcionamiento que tendria el lanzar los dados
def lanzar_dados():
  resultados_posibles = ['2.2', '2.3', '2.5', '2.7', '2.8', '2.10', '2.12', '2.14', '3.2', '3.3', '3.5', '3.7', '3.8', '3.10', '3.12',
                        '3.14', '5.2', '5.3', '5.5', '5.7', '5.8', '5.10', '5.12', '5.14', '6.2', '6.3', '6.5', '6.7', '6.8', '6.10', 
                        '6.12', '6.14', '8.2', '8.3', '8.5', '8.7', '8.8', '8.10', '8.12', '8.14', '9.2', '9.3', '9.5', '9.7', 
                        '9.8', '9.10', '9.12', '9.14']
  
  # Escoge un resultado aleatorio
  resultado = random.choice(resultados_posibles)

  # Lo dividimos en dos partes para obtener las coordenadas
  partes = resultado.split('.')
  i = partes[0]
  i = int(i)
  j = partes[1]
  j = int(j)

  return i, j


# Creamos una función para conocer la posicion actual del jugador y utilizarla en el juego 
def posicion_actual(tablero, jugador):
  # Recorremos las filas de la matriz
  for i, fila in enumerate(tablero):
    # Recorremos las columnas de la fila actual
    for j, valor in enumerate(fila):
      # Comparamos el valor actual con el elemento buscado
      if valor == jugador:
        # Si se encuentra el elemento, retornamos su ubicación
        return i, j
  
  return None



# Empezamos con la funcion que se encargará de ejecutar nuestro juego
def main():
  # Empezamos la ejecución de nuestro código dando la bienvenida
  bienvenida_usuario()

  # Creamos las variables que usaremos a lo largo del proyecto
  tablero_coordenadas = coordenadas_tablero()
  tablero_de_juego = preparacion_tablero()
  tablero_estado_base = logica_tablero()
  jugadores_visual = ['♚','♛', '♜', '♝', '♞', '♟']
  jugadores = 0
  turno = 0
  coordenada = ''
  casillas_iniciales = ['0.2', '0.3', '0.5', '0.7', '0.8', '0.10', '0.12', '0.14', '2.0', '3.0', '5.0', '6.0', '8.0', '9.0', '11.2', '11.3', '11.5', '11.7', '11.8', '11.8', '11.10', '11.12', '11.14', '2.16', '3.16', '5.16', '6.16', '8.16', '9.16']
  casillas_iniciales_superiores = ['0.2', '0.3', '0.5', '0.7', '0.8', '0.10', '0.12', '0.14']
  casillas_iniciales_izquierda = ['2.0', '3.0', '5.0', '6.0', '8.0', '9.0']
  casillas_iniciales_inferiores = ['11.2', '11.3', '11.5', '11.7', '11.8', '11.8', '11.10', '11.12', '11.14']
  casillas_iniciales_derecha = ['2.16', '3.16', '5.16', '6.16', '8.16', '9.16']
  cubos_dmg = 0
  pdi_en_tablero = 3
  direccion = ''
  i = 0
  j = 0
  puntos_de_accion = [4, 4, 4, 4, 4, 4]
  puntos_de_interes = [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
  con_persona = [False, False, False, False, False, False]
  victimas_salvadas = 0
  victimas_perdidas = 0
  # Variables que usamos para ciclos while
  perder = False
  casilla_valida = True
  direccion_valida = True
  apagar_fuego = True
  lanzamiento_valido = True

  print("-".center(65, "-"))
  print("\nComencemos a jugar...\n\n")

  while(not perder):
    opcion = int(input("""\n\nMenú de Opciones: 
        1. Ver Coordenadas del Tablero
        2. Ver Estado Base del Tablero
        3. Simbología del Tablero
        4. Agregar jugadores
        5. Jugar a Rescate!
        6. Ver Estado Actual del Tablero
        7. Rendirse
        8. Ver estadísticas
        Elección: """))
    

    # ! ------------ Mostramos las coordenadas del tablero ------------
    if(opcion == 1):
      print("\nCoordenadas del Tablero: \n")
      imprimir_tablero(tablero_coordenadas)
    # !  ------------ Mostramos el estado base del tablero sin preparaciones ------------
    elif(opcion == 2):
      print("\nEstado Base del Tablero: \n")
      imprimir_tablero(tablero_estado_base)
    # !  ------------ Mostramos la simbología de los elementos de nuestro tablero ------------
    elif(opcion == 3):
      print("""\nSimbología: 
          # Pared vertical                 ||
          # Pared Vertical Medio Rota      |
          # Puerta Abierta                 ▯
          # Puerta Cerrada                 ▮
          # Jugador                        ♚ ♛ ♜ ♝ ♞ ♟
          # Casilla                        ▣
          # Pared Horizontal               --
          # Pared Horizontal Medio Rota    ﹣
          # Fuego                          ✦
          # Humo                           ✧
          # Punto de interes               ✆\n""")
    # !  ------------ Empezamos con la primera configuración del juego, agregar los jugadores ------------
    elif(opcion == 4):
      continuar = True
      while(continuar):
          # Validamos que los jugadores ingresados sean válidos
          if(jugadores == 0):
            jugadores = int(input("\n¿Cuántos jugadores van a jugar?\n"))
            if(jugadores <= 0 or jugadores > 6):
              print("\nNúmero de jugadores no soportado. Mínimo 1 - Máximo 6\n")
              continuar = True
              jugadores = 0
            else:
              print("Jugadores Registrados...")
              continuar = False
          elif(jugadores >= 1 or jugadores <= 6):
            print("\nYa no puede agregar más jugadores una vez la partida ha iniciado!!!\n")
            continuar = False
    #Comenzamos con la ejecución principal de nuestro juego
    elif(opcion == 5):
      if(jugadores == 0): # Usamos un if para validar que el usuario ha ingresado anteriormente la cantidad de jugadores
        print("\n\nPara jugar debes primero indicar cuántos jugadores van a jugar!!!")
      else: 
        if(turno == 0):
          for jugador in range(jugadores):
            casilla_valida = True
            while(casilla_valida): # Validamos que la casilla en la que inicio el jugador sea valida
              print("\nIndica las coordenadas de la casilla en la que deseas iniciar\nCasillas Disponibles:")
              # Imprimimos las casillas donde el usuario puede iniciar
              print("Casillas Superiores: ") 
              for casilla in casillas_iniciales_superiores:
                print(casilla, end = ' ')
              print("\nCasillas Inferiores: ")
              for casilla in casillas_iniciales_inferiores:
                print(casilla, end = ' ')
              print("\nCasillas Derecha: ") 
              for casilla in casillas_iniciales_derecha:
                print(casilla, end = ' ')
              print("\nCasillas Izquierda: ")
              for casilla in casillas_iniciales_izquierda:
                print(casilla, end = ' ')
              # Le pedimos al usuario que ingrese la casilla
              coordenada = input("\nCoordenada: ")
              partes_coordenada = coordenada.split('.')
              if coordenada in casillas_iniciales:
                i = int(partes_coordenada[0])
                j = int(partes_coordenada[1])
                tablero_de_juego[i][j] = jugadores_visual[jugador]
                print('\nTablero de Juego: ')
                imprimir_tablero(tablero_de_juego)
                casilla_valida = False
              elif tablero_de_juego[i][j] in jugadores_visual:
                print("\nCasilla no válida")
                casilla_valida = True
              else:
                print("\nCasilla no válida")
                casilla_valida = True
        else: 
          print(f"Turno {turno}")
          for jugador in range(jugadores):
            print("-".center(50,"-"))
            print(f"Turno de {jugadores_visual[jugador]}")
            puntos_de_accion = [4, 4, 4, 4, 4, 4]
            while(puntos_de_accion[jugador] >= 1):
              # Empezamos el juego oficialmente en el que el jugador deberá elegir que acción hacer
              print("\nTablero de Juego: \n")
              imprimir_tablero(tablero_de_juego)
              print("\nMenú de Acciones: ")
              accion = int(input("1. Moverse\n2. Apagar Fuego\n3. Apagar Humo\n4. Abrir Puerta\n5. Cerrar Puerta\n\nAcción: "))
              i, j = posicion_actual(tablero_de_juego, jugadores_visual[jugador]) # Obtenemos la posicion actual del jugador para poder realizar las acciones
              # Comenzamos con la ejecución para que el jugador pueda moverse
              if(accion == 1):
                tablero_de_juego[i][j] = '▣'
                direccion_valida = True

                while(direccion_valida):
                  direccion_valida = True
                  print("Indica en qué direccion quieres moverte")
                  direccion = input("Posición: ")
                  # ! ARRIBA
                  if(direccion == "arriba"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i-1][j] in ['--', '- ','✦','✧'] + jugadores_visual:
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta se moverá automaticamente una casilla más o no
                    elif tablero_de_juego[i-1][j] == ' ' or tablero_de_juego[i-1][j] == '▯':
                      if tablero_de_juego[i-2][j] in ['--', '- ','✦','✧', ' '] + jugadores_visual:
                        print(f"No puedes moverte hacía {direccion}" )
                        direccion_valida = True
                      else:
                        tablero_de_juego[i-2][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    # Si al momento de moverse hay una victíma
                    elif tablero_de_juego[i-1][j] == '✆':
                      pdi = random.choice(puntos_de_interes)
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!. El equipo de rescate ha llegado y la ha salvado.")
                        victimas_salvadas += 1
                        tablero_de_juego[i-1][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                      else:
                        print("Era una falsa alarma!!")
                        tablero_de_juego[i-1][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i-1][j] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= 1
                      direccion_valida = False
                  # ! IZQUIERDA
                  elif(direccion == "izquierda"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i][j-1] in ['||', '| ', '✦', '✧'] + jugadores_visual: 
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i][j-1] == ' ' or tablero_de_juego[i][j-1] == '▯':
                      if  tablero_de_juego[i][j-2] in ['||', '| ', '✦', '✧', ' '] + jugadores_visual:
                        print(f"No puedes moverte hacía {direccion}" )
                        direccion_valida = True
                      else:
                        tablero_de_juego[i][j-2] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    elif tablero_de_juego[i][j-1] == '✆':
                      pdi = random.choice(puntos_de_interes)
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!. El equipo de rescate ha llegado y la ha salvado.")
                        tablero_de_juego[i][j-1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i][j-1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i][j-1] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= 1
                      direccion_valida = False
                  # ! DERECHA
                  elif(direccion == "derecha"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i][j+1] in ['--', '- ', '✦', '✧'] + jugadores_visual:
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta abierta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i][j+1] == ' ' or tablero_de_juego[i][j+1] == '▯':
                      if tablero_de_juego[i][j+2] in ['--', '- ', '✦', '✧'] + jugadores_visual:
                        print(f"No puedes moverte hacía {direccion}" )
                        direccion_valida = True
                      else:
                        tablero_de_juego[i][j+2] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    # Si al momento de moverse hay una victíma
                    elif tablero_de_juego[i][j+1] == '✆':
                      pdi = random.choice(puntos_de_interes)
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!. El equipo de rescate ha llegado y la ha salvado.")
                        tablero_de_juego[i][j+1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i][j+1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                      
                      direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i][j+1] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= 1
                      direccion_valida = False
                  # ! ABAJO
                  elif(direccion == "abajo"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i+1][j] in ['--', '- ', '✦', '✧'] + jugadores_visual:
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i+1][j] == ' ' or tablero_de_juego[i+1][j] == '▯':
                      if tablero_de_juego[i+2][j] in ['--', '- ', '✦', '✧'] + jugadores_visual:
                        print(f"No puedes moverte hacía {direccion}" )
                        direccion_valida = True
                      else:
                        tablero_de_juego[i+2][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    # Si al momento de moverse hay una victíma
                    elif tablero_de_juego[i+1][j] == '✆':
                      pdi = random.choice(puntos_de_interes)
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!. El equipo de rescate ha llegado y la ha salvado.")
                        tablero_de_juego[i+1][j] = jugadores_visual[jugador]
                        tablero_de_juego[i][j] = '▣'
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i+1][j] = jugadores_visual[jugador]
                        tablero_de_juego[i][j] = '▣'
                        puntos_de_accion[jugador] -= 1
                        direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i+1][j] = jugadores_visual[jugador]
                      tablero_de_juego[i][j] = '▣'
                      puntos_de_accion[jugador] -= 1
                      direccion_valida = False
                  else:
                    direccion_valida = True
              # Comenzamos con la ejecución para apagar fuego
              elif(accion == 2):
                apagar_fuego = True
                while(apagar_fuego):
                # Comprobamos si hay un fuego que apagar alrededor del jugador
                  if(tablero_de_juego[i-1][j] == '✦' or tablero_de_juego[i+1][j] == '✦' or tablero_de_juego[i][j-1] == '✦' or tablero_de_juego[i][j+1] == '✦'):
                    direccion_fuego = input("Indica en qué dirección quieres apagar el fuego (arriba - abajo - derecha - izquierda)\nDirección: ")
                    
                    # En la direccion en la que ingreso el usuario apagamos el fuego
                    if(direccion_fuego == "arriba"):
                      tablero_de_juego[i-1][j] = '✧' 
                      puntos_de_accion[jugador] -= 1
                      apagar_fuego = False
                    elif(direccion_fuego == "abajo"):
                      tablero_de_juego[i+1][j] = '✧' 
                      puntos_de_accion[jugador] -= 1
                      apagar_fuego = False
                    elif(direccion_fuego == "derecha"):
                      tablero_de_juego[i][j+1] = '✧' 
                      puntos_de_accion[jugador] -= 1
                      apagar_fuego = False
                    elif(direccion_fuego == "izquierda"):
                      tablero_de_juego[i][j-1] = '✧' 
                      puntos_de_accion[jugador] -= 1
                      apagar_fuego = False
                    else:
                      print("\nDirección Inválida")
                      apagar_fuego = True
                  # En caso de que no se encuentre ningun fuego alrededor vuelve al menú de acciones
                  else:
                    print("\nNo hay ningún fuego alrededor!!!")
                    apagar_fuego = False
              # Comenzamos con la logica para apagar el humo
              elif(accion == 3):
                
                apagar_humo = True
                while(apagar_humo):
                # Comprobamos si hay un humo que apagar alrededor del jugador
                  if(tablero_de_juego[i-1][j] == '✧' or tablero_de_juego[i+1][j] == '✧' or tablero_de_juego[i][j-1] == '✧' or tablero_de_juego[i][j+1] == '✧'):
                    direccion_humo = input("Indica en qué dirección quieres apagar el humo (arriba - abajo - derecha - izquierda)\nDirección: ")

                    # En la direccion en la que ingreso el usuario apagamos el humo
                    if(direccion_humo == "arriba"):
                      tablero_de_juego[i-1][j] = '▣' 
                      puntos_de_accion[jugador] -= 1
                      apagar_humo = False
                    elif(direccion_humo == "abajo"):
                      tablero_de_juego[i+1][j] = '▣' 
                      puntos_de_accion[jugador] -= 1
                      apagar_humo = False
                    elif(direccion_humo == "derecha"):
                      tablero_de_juego[i][j+1] = '▣' 
                      puntos_de_accion[jugador] -= 1
                      apagar_humo = False
                    elif(direccion_humo == "izquierda"):
                      tablero_de_juego[i][j-1] = '▣' 
                      puntos_de_accion[jugador] -= 1
                      apagar_humo = False
                    else:
                      print("\nDirección Inválida")
                      apagar_humo = True
                  # En caso de que no se encuentre ningun fuego alrededor vuelve al menú de acciones
                  else:
                    print("\nNo hay ningún humo alrededor!!!")
                    apagar_humo = False
              # Comenzamos con la ejecucion para Abrir Puerta
              elif(accion == 4):
                # Comprobamos si hay una puerta alrededor de nosotros
                if(tablero_de_juego[i-1][j] == '▮' or tablero_de_juego[i+1][j] == '▮' or tablero_de_juego[i][j-1] == '▮' or tablero_de_juego[i][j+1] == '▮'):
                  # En este caso no hay necesidad de preguntarle al usuario en que direccion quiere abrir la puerta
                  
                  # Puerta en la dirrección de arriba
                  if(tablero_de_juego[i-1][j] == '▮'):
                    tablero_de_juego[i-1][j] = '▯'
                    puntos_de_accion[jugador] -= 1
                  # Puerta en la dirección de abajo
                  elif(tablero_de_juego[i+1][j] == '▮'):
                    tablero_de_juego[i+1][j] = '▯'
                    puntos_de_accion[jugador] -= 1
                  # Puerta en la dirección de izquierda
                  elif(tablero_de_juego[i][j-1] == '▮'):
                    tablero_de_juego[i][j-1] = '▯'
                    puntos_de_accion[jugador] -= 1
                  # Puerta en la dirección de derecha
                  elif(tablero_de_juego[i][j+1] == '▮'):
                    tablero_de_juego[i][j+1] = '▯'
                    puntos_de_accion[jugador] -= 1
                else:
                  print("\nNo hay ninguna puerta cerrada alrededor!!")
              # Comenzamos con la ejecucion para Cerrar Puerta
              elif(accion == 5):
                # Comprobamos si hay una puerta alrededor de nosotros
                if(tablero_de_juego[i-1][j] == '▯' or tablero_de_juego[i+1][j] == '▯' or tablero_de_juego[i][j-1] == '▯' or tablero_de_juego[i][j+1] == '▯'):
                  # En este caso no hay necesidad de preguntarle al usuario en que direccion quiere abrir la puerta
                  
                  # Puerta en la dirrección de arriba
                  if(tablero_de_juego[i-1][j] == '▯'):
                    tablero_de_juego[i-1][j] = '▮'
                    puntos_de_accion[jugador] -= 1
                  # Puerta en la dirección de abajo
                  elif(tablero_de_juego[i+1][j] == '▯'):
                    tablero_de_juego[i+1][j] = '▮'
                    puntos_de_accion[jugador] -= 1
                  # Puerta en la dirección de izquierda
                  elif(tablero_de_juego[i][j-1] == '▯'):
                    tablero_de_juego[i][j-1] = '▮'
                    puntos_de_accion[jugador] -= 1
                  # Puerta en la dirección de derecha
                  elif(tablero_de_juego[i][j+1] == '▯'):
                    tablero_de_juego[i][j+1] = '▮'
                    puntos_de_accion[jugador] -= 1
                else:
                  print("\nNo hay ninguna puerta abierta alrededor!!")
              else:
                print("\nAcción Inválida")
        
        if(turno > 0):
          # Una vez se ha terminado el turno de todos los jugadores, tenemos que preparar el tablero para el siguiente turno
          # 1. Primero verificamos que en el tablero haya tres puntos de interes
            pdi_en_tablero = 0 # Inicializamos en cero para saber cuantos pdi hay 

            for fila in tablero_de_juego: # Usamos un ciclo for para recorrer toda la matriz y buscar los pdi
              for valor in fila:
                if valor == '✆':
                  pdi_en_tablero += 1
          
          # En caso de que los pdi no hayan sido tres, usamos un ciclo while para colocar en nuestro tablero los pdi que faltan
            while(pdi_en_tablero != 3): 
              # Validamos que la posicion en donde se colocará el pdi sea válida
              while(lanzamiento_valido):
                i, j = lanzar_dados()
                # En caso de que la posicion este ocupada por un valor en el que no puede estar
                if(tablero_de_juego[i][j] in ['--', '- ', '||', '| ', '✆', ' ']):
                  lanzamiento_valido = True
                # En caso de que la posicion este ocupada por un jugador se desvelará automaticamente
                elif(tablero_de_juego[i][j] in jugadores_visual):
                  pdi = random.choice(puntos_de_interes)
                  puntos_de_interes.pop(pdi)

                  # Si pdi es True entonces...
                  if(pdi):
                    print("\nHaz encontrado una víctima escodida. El equipo de rescate la ha salvado.")
                    victimas_salvadas += 1
                    lanzamiento_valido = False
                    pdi_en_tablero += 1
                  else:
                    print("Era una falsa alarma")
                    lanzamiento_valido = False
                    pdi_en_tablero += 1
                else:
                  tablero_de_juego[i][j] = '✆'
                  lanzamiento_valido = False
                  pdi_en_tablero += 1
          
          # 2. Comenzamos con las explosiones 
            colocar_humo = 0 
            while(colocar_humo != 3):
              i, j = lanzar_dados()

              if(tablero_de_juego[i-1][j] == '✦' or tablero_de_juego[i+1][j] == '✦' or tablero_de_juego[i][j-1] == '✦' or tablero_de_juego[i][j+1] == '✦'): # Si en alguna casilla adyacente hay fuego, entonces se convierte automaticamente en fuego
                tablero_de_juego[i][j] = '✦'
                colocar_humo += 1
              elif(tablero_de_juego[i][j] == '▣'): # Si cae en una casilla vacia esta tendrá humo
                tablero_de_juego[i][j] = '✧'
                colocar_humo += 1
              elif(tablero_de_juego[i][j] in jugadores_visual): # Si en la casilla hay algun jugador, este regresará al inicio
                # Obtener el índice del jugador en la lista
                jugador_encontrado = jugadores_visual.index(tablero_de_juego[i][j])
                posicion = random.choice(casillas_iniciales)
                partes = posicion.split('.')
                i = int(partes[0])
                j = int(partes[1])
                tablero_de_juego[i][j] = jugadores_visual[jugador_encontrado]
                colocar_humo += 1
              elif(tablero_de_juego[i][j] == '✦'):
                colocar_humo += 1
                for direccion in ["arriba", "derecha", "abajo", "izquierda"]:
                  n = 0
                  explosion_fin = True
                  while(explosion_fin):
                    # ! ---------------- EXPLOSION ARRIBA ----------------
                    if(direccion == "arriba"):
                      n += -1
                      if(tablero_de_juego[i + n][j] == '▣'):
                        tablero_de_juego[i + n][j] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] == '--'):
                        tablero_de_juego[i + n][j] = '- '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i + n][j] == '- '):
                        tablero_de_juego[i + n][j] = ' '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i + n][j] == '✆'):
                        tablero_de_juego[i + n][j] = '✦'
                        pdi = random.choice(puntos_de_interes)
                        puntos_de_interes.pop(pdi)
                        # Si pdi es True entonces...
                        if(pdi): victimas_perdidas += 1 
                        else: pass
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] == '✧'):
                        tablero_de_juego[i + n][j] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] in jugadores_visual):
                        posicion = random.choice(casillas_iniciales)
                        partes = posicion.split('.')
                        i = int(partes[0])
                        j = int(partes[1])
                        tablero_de_juego[i][j] = jugadores_visual[jugador_encontrado]
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] == '▮'):
                        tablero_de_juego[i + n][j] = '▯'
                      elif(tablero_de_juego[i + n][j] == ' '):
                        tablero_de_juego[i + (n + 1)][j] = '✦'
                        explosion_fin = False
                    # ! ---------------- EXPLOSION DERECHA ----------------
                    elif(direccion == "derecha"):
                      n += 1
                      if(tablero_de_juego[i][j + n] == '▣'):
                        tablero_de_juego[i][j + n] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] == '||'):
                        tablero_de_juego[i][j + n] = '| '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i][j + n] == '| '):
                        tablero_de_juego[i][j + n] = ' '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i][j + n] == '✆'):
                        tablero_de_juego[i][j + n] = '✦'
                        pdi = random.choice(puntos_de_interes)
                        puntos_de_interes.pop(pdi)
                        # Si pdi es True entonces...
                        if(pdi): victimas_perdidas += 1 
                        else: pass
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] == '✧'):
                        tablero_de_juego[i][j + n] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] in jugadores_visual):
                        posicion = random.choice(casillas_iniciales)
                        partes = posicion.split('.')
                        i = int(partes[0])
                        j = int(partes[1])
                        tablero_de_juego[i][j] = jugadores_visual[jugador_encontrado]
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] == '▮'):
                        tablero_de_juego[i][j + n] = '▯'
                      elif(tablero_de_juego[i][j + n] == ' '):
                        tablero_de_juego[i][j + (n + 1)] = '✦'
                        explosion_fin = True
                    # ! ---------------- EXPLOSION ABAJO ----------------
                    elif(direccion == "abajo"):
                      n += 1
                      if(tablero_de_juego[i + n][j] == '▣'):
                        tablero_de_juego[i + n][j] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] == '--'):
                        tablero_de_juego[i + n][j] = '- '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i + n][j] == '- '):
                        tablero_de_juego[i + n][j] = ' '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i + n][j] == '✆'):
                        tablero_de_juego[i + n][j] = '✦'
                        pdi = random.choice(puntos_de_interes)
                        puntos_de_interes.pop(pdi)
                        # Si pdi es True entonces...
                        if(pdi): victimas_perdidas += 1 
                        else: pass
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] == '✧'):
                        tablero_de_juego[i + n][j] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] in jugadores_visual):
                        posicion = random.choice(casillas_iniciales)
                        partes = posicion.split('.')
                        i = int(partes[0])
                        j = int(partes[1])
                        tablero_de_juego[i][j] = jugadores_visual[jugador_encontrado]
                        explosion_fin = True
                      elif(tablero_de_juego[i + n][j] == '▮'):
                        tablero_de_juego[i + n][j] = '▯'
                      elif(tablero_de_juego[i + n][j] == ' '):
                        tablero_de_juego[i + (n + 1)][j] = '✦'
                        explosion_fin = False
                    # ! ---------------- EXPLOSION IZQUIERDA ----------------
                    elif(direccion == "izquierda"):
                      n += -1
                      if(tablero_de_juego[i][j + n] == '▣'):
                        tablero_de_juego[i][j + n] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] == '||'):
                        tablero_de_juego[i][j + n] = '| '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i][j + n] == '| '):
                        tablero_de_juego[i][j + n] = ' '
                        cubos_dmg += 1
                        explosion_fin = False
                      elif(tablero_de_juego[i][j + n] == '✆'):
                        tablero_de_juego[i][j + n] = '✦'
                        pdi = random.choice(puntos_de_interes)
                        puntos_de_interes.pop(pdi)
                        # Si pdi es True entonces...
                        if(pdi): victimas_perdidas += 1 
                        else: pass
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] == '✧'):
                        tablero_de_juego[i][j + n] =  '✦'
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] in jugadores_visual):
                        posicion = random.choice(casillas_iniciales)
                        partes = posicion.split('.')
                        i = int(partes[0])
                        j = int(partes[1])
                        tablero_de_juego[i][j] = jugadores_visual[jugador_encontrado]
                        explosion_fin = True
                      elif(tablero_de_juego[i][j + n] == '▮'):
                        tablero_de_juego[i][j + n] = '▯'
                      elif(tablero_de_juego[i + n][j] == ' '):
                        tablero_de_juego[i][j + (n + 1)] = '✦'
                        explosion_fin = True
        print("-".center(75, "-"))
        imprimir_tablero(tablero_de_juego)
        turno += 1
    # Mostramos el estado actual del tablero de juego
    elif(opcion == 6):
        print('\nTablero de Juego: ')
        imprimir_tablero(tablero_de_juego)
    elif(opcion == 7):
      print("\nSer bombero no es trabajo para todos. Hasta la próxima!!! ")
      break
  


if __name__ == '__main__':
  main()


