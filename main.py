# 1. Damos la bienvenida al usuario
def bienvenida_usuario():
  print("BIENVENIDO A...: \n")
  print("""
██╗██████╗░███████╗░██████╗░█████╗░░█████╗░████████╗███████╗██╗
██║██╔══██╗██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║
██║██████╔╝█████╗░░╚█████╗░██║░░╚═╝███████║░░░██║░░░█████╗░░██║
╚═╝██╔══██╗██╔══╝░░░╚═══██╗██║░░██╗██╔══██║░░░██║░░░██╔══╝░░╚═╝
██╗██║░░██║███████╗██████╔╝╚█████╔╝██║░░██║░░░██║░░░███████╗██╗
╚═╝╚═╝░░╚═╝╚══════╝╚═════╝░░╚════╝░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝╚═╝""")
  comenzar = input("\nPulsa 1 para comenzar: \n")

# Creamos el diseño del tablero
def creacion_tablero():
  tablero_juego = [  
  ['0.0', '  0.1', '0.2', '0.3', '  0.4', '0.5', '  0.6', ' 0.7', ' 0.8', '  0.9'],
  ['1.0', '  ___', '___', '___', '  ___', '___', '  ___', ' ___', ' ___', '  1.9'],
  ['2.0', '|', '2.2', '2.3', '2.4', '|', '2.6', '2.7', '|', '2.9', '2.10', '2.11', '|', '2.13'],
  ['3.0', '|', '3.2', '3.3', '3.4', '|', '3.6', '3.7', '|', '3.9', '3.10', '3.11', '|', '3.13'],
  ['4.0', '|', '4.2', '4.3', '___', '|', '___', '___', '|', ' ___', ' ___', '___', '|', '4.13'],
  ['5.0', '|', '5.2', '5.3', '|', '5.5', '5.6', '5.7', '5.8', '|', '5.10', '5.11', '|', '5.13'],
  ['6.0', '|', '6.2', '6.3', '|', '6.5', '6.6', '6.7', '6.8', '|', '6.10', '6.11', '|', '6.13'],
  ['7.0', '|', '___', '___', '|', '___', '___', '___', '___', '|', '___', ' ___', ' |', '7.13'],
  ['8.0', '|', '8.2', '8.3', '8.4', '8.5', '8.6', '|', '8.8', '8.9', '|', ' 8.11', '|', '8.13'],
  ['9.0', '|', '9.2', '9.3', '9.4', '9.5', '9.6', '|', '9.8', '9.9', '|', ' 9.11', '|', '9.13'],
  ['10.0', '|', '___', '___', '___', '___', '___', '|', '___', '___', '|', '___', ' |', '10.13'],
  ['11.0', ' 11.1', '11.2', '11.3', '11.4', '11.5', '11.6', '11.7', '11.8', '11.9'],
  ]

  return tablero_juego

def main():
  bienvenida_usuario()

