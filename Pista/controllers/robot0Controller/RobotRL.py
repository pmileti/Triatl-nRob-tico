"""Roboliga Robot class v1
   Written by Ricardo Moran and Gonzalo Zabala (CAETI - UAI)
   Modified by Pablo Mileti
"""

from controller import Robot
import colorsys

class RobotRL:

    #propiedades de clase
    __timeStep = 32
    __max_velocity = 30

    def __init__(self):
        #propiedades de objeto
        self.__robot = Robot()

        self.__ruedaIzquierda = self.__robot.getDevice("motorIzquierdo")
        self.__ruedaDerecha = self.__robot.getDevice("motorDerecho")

        self.__camaraPisoI=self.__robot.getDevice("colorPisoI")
        self.__camaraPisoI.enable(self.__timeStep)

        self.__camaraPisoD=self.__robot.getDevice("colorPisoD")
        self.__camaraPisoD.enable(self.__timeStep)

        self.__senDistI=self.__robot.getDevice("sensorDistanciaI")
        self.__senDistI.enable(self.__timeStep)

        self.__senDistD=self.__robot.getDevice("sensorDistanciaD")
        self.__senDistD.enable(self.__timeStep)

        self.__bumperI=self.__robot.getDevice("bumperIzquierdo")
        self.__bumperI.enable(self.__timeStep)

        self.__bumperD=self.__robot.getDevice("bumperDerecho")
        self.__bumperD.enable(self.__timeStep)

        self.__ruedaIzquierda.setPosition(float("inf"))
        self.__ruedaDerecha.setPosition(float("inf"))

        self.setVel(0, 0)

    #Velocidad de las ruedas
    def setVel(self, vi, vd):
        self.setVI(vi)
        self.setVD(vd)

    def setVI(self, vi):
        self.__vi=vi*self.__max_velocity/100
        self.__ruedaIzquierda.setVelocity(self.__vi)

    def setVD(self, vd):
        self.__vd=vd*self.__max_velocity/100
        self.__ruedaDerecha.setVelocity(self.__vd)

    def getVI(self):
        return self.__vi*100/self.__max_velocity

    def getVD(self):
        return self.__vd*100/self.__max_velocity

    #Espera
    def esperar(self, duracion):
        inicio = self.tiempoActual()
        while (self.tiempoActual() - inicio) < duracion:
            self.step()

    def tiempoActual(self):
        return self.__robot.getTime()

    #funciones útiles
    def __mapeo(self, val, min, max):
        return int((val - min) * 100 / (max - min))

    #sensores

    def getColorPisoI(self):
        bgra = self.__camaraPisoI.getImage()
        hsv = colorsys.rgb_to_hsv(bgra[2]/255, bgra[1]/255, bgra[0]/255)
        return hsv[2]*100

    def getColorPisoD(self):
        bgra = self.__camaraPisoD.getImage()
        hsv = colorsys.rgb_to_hsv(bgra[2]/255, bgra[1]/255, bgra[0]/255)
        return hsv[2]*100

    def getDI(self):
        return self.__senDistI.getValue()

    def getDD(self):
        return self.__senDistD.getValue()

    def getBI(self):
        return bool(self.__bumperI.getValue())

    def getBD(self):
        return bool(self.__bumperD.getValue())

    def step(self):
        return (self.__robot.step(self.__timeStep) != -1)
