import time
#import RPi.GPIO as GPIO


#Los valores de 'leds' y 'boton' son los pines GPIO disponibles de la Rapsberry Pi 4.
numero = 0
leds = [27,22,5,6]
boton = 17 
chan_list= [leds]


#Devuelve el valor del parámetro en binario. Usamos el [2:] para que imprima apartir de la segunda posición (porque "bin" lo imprime como "0b'xxxx'")
def binario(numero):
    return bin(numero)[2:].zfill(4)


print("GPIO.setmode(GPIO.BCM)")
print("GPIO.setup(boton, GPIO.IN)")
print("GPIO.setup(chan_list, GPIO.OUT)")


while True:
    print("Timer 1 segundo") #Puede reemplazarse por un botón ("if GPIO.input(boton) == GPIO.HIGH")
    time.sleep(1)
    bnumero = binario(numero)
    if numero == 9:
        numero = 0
    else:
        numero = numero + 1
    for b in range(4):
        led = leds[b]
        valor = int(bnumero[b])
        print("GPIO.output", led, valor)

