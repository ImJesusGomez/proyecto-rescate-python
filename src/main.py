# Importamos la libreria tabulate que no ayuda a darle una estructura y orden a nuestro tablero
from tablero import coordenadas_tablero
from tablero import logica_tablero
from tablero import preparacion_tablero
from tablero import imprimir_tablero
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
  print("|Pulsa start para comenzar|".center(65, '-'))
  comenzar = input("")


# Debido a la estructura de nuestro tablero, crear un dado de 6 y 8 caras no es una opción
# por lo que crearemos una función que simule el funcionamiento que tendria el lanzar los dados
def lanzar_dados():
  resultados_posibles = ['2.2', '2.3', '2.5', '2.7', '2.8', '2.10', '2.12', '2.14', '3.2', '3.3', '3.5', '3.7', '3.8', '3.10', '3.12',
                        '3.14', '5.2', '5.3', '5.5', '5.7', '5.8', '5.10', '5.12', '5.14', '6.2', '6.3', '6.5', '6.7', '6.8', '6.10', 
                        '6.12', '6.14', '8.2', '8.3', '8.5', '8.7', '8.8', '8.10', '8.12', '8.14', '9.2', '9.3', '9.5', '9.7', 
                        '9.8', '9.10', '9.12', '9.14']
  
  resultado = random.choice(resultados_posibles)
  partes = resultado.split('.')
  i = partes[0]
  i = int(i)
  j = partes[1]
  j = int(j)

  return resultado, i, j


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

def energia_gastar(con_persona):
  if(con_persona == False):
    energia = 1
  else:
    energia = 2
  
  return energia


# Empezamos con la funcion que se encargará de ejecutar nuestro juego
def main():
  # Empezamos la ejecución de nuestro código
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
  cubos_dmg = 0
  direccion = ''
  i = 0
  j = 0
  puntos_de_accion = [4, 4, 4, 4, 4, 4]
  puntos_de_interes = [True, True, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
  con_persona = False
  energia = energia_gastar(con_persona)
  # Variables que usamos para ciclos while
  perder = False
  casilla_valida = True
  direccion_valida = True

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
        Elección: """))
    

    # Mostramos las coordenadas del tablero
    if(opcion == 1):
      print("\nCoordenadas del Tablero: \n")
      imprimir_tablero(tablero_coordenadas)
    # Mostramos el estado base del tablero sin preparaciones
    elif(opcion == 2):
      print("\nEstado Base del Tablero: \n")
      imprimir_tablero(tablero_estado_base)
    # Mostramos la simbología de los elementos de nuestro tablero
    elif(opcion == 3):
      print("""\nSimbología: 
          # Pared vertical                 ||
          # Pared Vertical Medio Rota      |
          # Puerta Abierta                 ▯
          # Puerta Cerrada                 ▮
          # Jugador                        ♚ ♛ ♜ ♝ ♞ ♟
          # Casilla                        ⊡
          # Pared Horizontal               --
          # Pared Horizontal Medio Rota    ﹣
          # Fuego                          ✦
          # Humo                           ✧
          # Punto de interes               ✆\n""")
    # Empezamos con la primera configuración del juego, agregar los jugadores
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
        for jugador in range(jugadores):
          if(turno == 0): # Empezamos con el turno 0, en el cual el jugador deberá indicar donde posicionará su jugador
            while(casilla_valida): # Validamos que la casilla en la que inicio el jugador sea valida
              print("\nIndica las coordenadas de la casilla en la que deseas iniciar\nCasillas Disponibles:")
              # Imprimimos las casillas donde el usuario puede iniciar
              for casilla in casillas_iniciales:
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
              else:
                print("\nCasilla no válida")
                casilla = True
          else:
            while(puntos_de_accion[jugador] > 0):
              energia_gastar(con_persona)
              # Empezamos el juego oficialmente en el que el jugador deberá elegir que acción hacer
              print("\nTablero de Juego: \n")
              imprimir_tablero(tablero_de_juego)
              print("\nMenú de Acciones: ")
              accion = int(input("1. Moverse\n2. Apagar Fuego o Humo\n3. Abrir Puerta\nAcción: "))

              # Comenzamos con la ejecución para que el jugador pueda moverse
              if(accion == 1):
                i, j = posicion_actual(tablero_de_juego, jugadores_visual[jugador])

                while(direccion_valida):
                  print("Indica en qué direccion quieres moverte")
                  direccion = input("Posición: ")
                  # ! ARRIBA
                  if(direccion == "arriba"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i-1][j] == '--' or tablero_de_juego[i-1][j] == '- ' or tablero_de_juego[i-1][j] in jugadores_visual or tablero_de_juego[i-1][j] == '✦' or tablero_de_juego[i-1][j] == '✧':
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i-1][j] == ' ' or tablero_de_juego[i][j-1] == '▯':
                      tablero_de_juego[i-2][j] = jugadores_visual[jugador]
                      direccion_valida = False
                    # Si al momento de moverse hay una victíma
                    elif tablero_de_juego[i-1][j] == '✆':
                      pdi = random.choice[puntos_de_interes]
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!")
                        con_persona = True
                        energia_gastar(con_persona)
                        tablero_de_juego[i-1][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i-1][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                        direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i-1][j] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= energia
                      direccion_valida = False
                  # ! IZQUIERDA
                  elif(direccion == "izquierda"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i][j-1] == '||' or tablero_de_juego[i][j-1] == '| ' or tablero_de_juego[i][j-1] in jugadores_visual or tablero_de_juego[i][j-1] == '✦' or tablero_de_juego[i][j-1] == '✧': 
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i][j-1] == ' ' or tablero_de_juego[i][j-1] == '▯':
                      tablero_de_juego[i][j-2] = jugadores_visual[jugador]
                      direccion_valida = False
                    elif tablero_de_juego[i][j-1] == '✆':
                      pdi = random.choice[puntos_de_interes]
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!")
                        con_persona = True
                        tablero_de_juego[i][j-1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i][j-1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                        direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i][j-1] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= energia
                      direccion_valida = False
                  # ! DERECHA
                  elif(direccion == "derecha"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i][j+1] == '--' or tablero_de_juego[i][j+1] == '- ' or tablero_de_juego[i][j+1] in jugadores_visual or tablero_de_juego[i][j+1] == '✦' or tablero_de_juego[i][j+1] == '✧':
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta abierta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i][j+1] == ' ' or tablero_de_juego[i][j+1] == '▯':
                      tablero_de_juego[i][j+2] = jugadores_visual[jugador]
                      direccion_valida = False
                    # Si al momento de moverse hay una victíma
                    elif tablero_de_juego[i][j+1] == '✆':
                      pdi = random.choice[puntos_de_interes]
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!")
                        con_persona = True
                        energia_gastar(con_persona)
                        tablero_de_juego[i][j+1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i][j+1] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                      
                      direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i][j+1] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= energia
                      direccion_valida = False
                  # ! ABAJO
                  elif(direccion == "abajo"):
                    # Hacemos validaciones para que la direccion en que se quiere mover el jugador es valida
                    # Si el jugador se encuentra en una casilla en la que no se puede mover
                    if tablero_de_juego[i+1][j] == '--' or tablero_de_juego[i+1][j] == '- ' or tablero_de_juego[i+1][j] in jugadores_visual or tablero_de_juego[i+1][j] == '✦' or tablero_de_juego[i+1][j] == '✧':
                      print(f"No puedes moverte hacía {direccion}" )
                      direccion_valida = True
                    # Si el jugador se mueve a una casilla en blanco o a una puerta se moverá automaticamente una casilla más
                    elif tablero_de_juego[i+1][j] == ' ' or tablero_de_juego[i+1][j] == '▯':
                      tablero_de_juego[i+2][j] = jugadores_visual[jugador]
                      direccion_valida = False
                    # Si al momento de moverse hay una victíma
                    elif tablero_de_juego[i+1][j] == '✆':
                      pdi = random.choice[puntos_de_interes]
                      puntos_de_interes.pop(pdi)

                      # Si pdi es True entonces...
                      if(pdi):
                        print("Es una persona!!")
                        con_persona = True
                        energia_gastar(con_persona)
                        tablero_de_juego[i+1][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                      else:
                        print("Era una falsa alarma")
                        tablero_de_juego[i+1][j] = jugadores_visual[jugador]
                        puntos_de_accion[jugador] -= energia
                      
                      direccion_valida = False
                    # Si el jugador se puede mover sin problemas
                    else:
                      tablero_de_juego[i+1][j] = jugadores_visual[jugador]
                      puntos_de_accion[jugador] -= energia
                      direccion_valida = False
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


