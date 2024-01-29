import numpy as np
import csv

class Partida():

    def __init__(self, jugadores, modo=0, id=0):
        self.id=id
        self.jugadores = jugadores
        self.modo = modo
        self.puntuacion = []
        self.tirada = []
        self.jugada = []
        self.extra = []
        self.tirada = 0
        self.finalizada = 0
        self.inicializaMarcador()
        self.valorSuma=[]

        self.locPartida=[0,0,0]


    def actualizaMarcador(self, valor):
        for j in range(self.locPartida[0], 10):
            for i in range(0, len(self.puntuacion)):
                for k in range(0, len(self.puntuacion[i][j])):
                    if (self.puntuacion[i][j][k] == -1):
                        self.puntuacion[i][j][k] = valor
                        return
        self.locPartida[0]+=1

        for i in range(0, len(self.puntuacion)):
            if (self.puntuacion[i][9][0] == 'X' or self.puntuacion[i][9][1] == '/') and valor !=' ':
                for j in range(0, 2):
                    if (self.extra[i][j] == -1):
                        self.extra[i][j] = valor
                        return
                    elif self.extra[i][1] == -1:
                        self.extra[i][1] = valor
                        return
    


    def inicializaMarcador(self):
        self.puntuacion=(np.full((len(self.jugadores), 10, 2), -1)).tolist();
        for i in range(0, len(self.jugadores)):
            self.extra.append([-1,-1])

    def calculaSuma(self):
        arraySuma=[]
        for j in range(0, 10):
            for i in range(0, len(self.puntuacion)):
                suma=0
                if len(arraySuma) < len(self.puntuacion):
                    arraySuma.append([])
                for k in range(0, len(self.puntuacion[i][j])):
                    if (self.puntuacion[i][j][k] != -1):
                        if self.puntuacion[i][j][1]=='/':
                            suma=10
                        elif self.puntuacion[i][j][0]=='X':
                            suma=11
                        elif self.puntuacion[i][j][1]==' ':
                            suma+=0
                        elif k == 1:
                            suma=self.puntuacion[i][j][k]
                    else:
                        if len(arraySuma) == len(self.puntuacion) and len(arraySuma[i]) == len(self.puntuacion[i]):
                            return True
                        else:
                            self.valorSuma = arraySuma
                            return False
                arraySuma[i].append(suma)
        self.valorSuma = arraySuma

    def calculaArraySuma(self, rango=0, jugador=0):
        try:
            suma=0
            for i in range(0, rango+1):
                if self.valorSuma[jugador][i] == 11:
                    if self.puntuacion[jugador][i+1][0] == 'X' and self.puntuacion[jugador][i+1][0] !=-1:
                        suma += 10
                        if i == 8:
                            if self.extra[jugador][0] !=-1:
                                if self.extra[jugador][0] == 'X':
                                    suma += 20
                                else:
                                    suma += int(self.extra[jugador][0])+10
                            else: 
                                return -1
                        elif self.puntuacion[jugador][i+2][0] == 'X':
                            suma += 20
                        elif self.puntuacion[jugador][i+2][0] !=-1 and self.puntuacion[jugador][i+2][0] !='/' :
                            suma += int(self.puntuacion[jugador][i+2][0])+10
                        else:
                            return -1
                    elif self.puntuacion[jugador][i+1][0] !=-1:
                        suma += int(self.valorSuma[jugador][i+1])+10
                    else:
                        return -1
                elif self.valorSuma[jugador][i] == 10:
                    if self.puntuacion[jugador][i+1][0] == 'X':
                        suma += 20
                    elif self.puntuacion[jugador][i+1][0] !=-1:
                        suma += int(self.puntuacion[jugador][i+1][0])+10
                    else:
                        return -1
                else:
                    suma += int(self.valorSuma[jugador][i])
                if i >= 9:
                    if self.extra[jugador][0] !=-1 and self.extra[jugador][1] !=-1:

                        if self.extra[jugador][0] == 'X':
                            suma += 10
                            if self.extra[jugador][1] == 'X':
                                suma += 20
                            else:
                                suma += int(self.extra[jugador][1]) + 10

                        elif self.extra[jugador][1] == '/':
                            suma += 20
                        else:
                            suma += int(self.extra[jugador][1]) + 10
                    else:
                        return -1
        except Exception as error:
            print(error)
        print(suma)
        return suma


    def cambiaTirada(self):
        if self.tirada:
            self.tirada = 0
        else:
            self.tirada = 1

    def guardaCSV(self, info):
        with open(f'csv/partida{self.id}_file.csv', encoding='UTF-8', mode='a') as partidas_file:
            str = ''
            for i in range(0, len(info['jugadores'])):
                str += f"{info['jugadores'][i]},"f"{info['puntuacion'][i]},"
            #print(str)
            partidas_file.write(str)
            partidas_file.write('\n')

    def leerCSV(self):
        with open('cafe-data.csv', newline='') as csv_file:
            csv_data = csv.reader(csv_file, delimiter=',')
            list_of_rows = []
            for row in csv_data:
                list_of_rows.append(row)

class Bolera():

    def __init__(self):
        self.numeroPistas = 4
        self.conexionPistas = [False, False, False, False]
        self.PartidaPistas = ['','','','']

    def addPartida(self, partida):
        self.PartidaPistas.append(partida)

    def comprobarConexion(self, pista):
        return self.conexionPistas[pista]

    def guardarPartida(self):
        pass

    def terminarPartida(self):
        pass
