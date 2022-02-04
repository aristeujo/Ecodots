from time import sleep
import sys
import dht11

EMULATE_HX711=False

referenceUnit = 1

if not EMULATE_HX711:
    import RPi.GPIO as GPIO
    from hx711 import HX711
else:
    from emulated_hx711 import HX711 


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)


def cleanAndExit():
    print("Cleaning...")

    if not EMULATE_HX711:
        GPIO.cleanup()
        
    print("Bye!")
    sys.exit()

def setupHX(pinoDT, pinoSCK):
    print("chegou aqui")
    global hx 
    hx = HX711(pinoDT, pinoSCK)

"""########################################################################################################################"""
#Metodo pra configurar o offset
def loadCell_Setup():
    hx.set_reference_unit(-11.55)
    hx.reset()
    hx.tare()
    print("Tare done! Add weight now...")

def loadCell_tare():
    hx.tare()
    print("Pronto para nova medicao...")

#metodo que retorna a leitura do peso em "Kg"
def loadCell_Read():
    try:
        val = hx.get_weight(5)*0.001
        #print("Massa (Kg): " + str(val))
        hx.power_down()
        hx.power_up()
        if(val < 0): val = 0.0
        sleep(0.1)

    except (KeyboardInterrupt, SystemExit):
        cleanAndExit()

    return val

"""########################################################################################################################"""
def setupDHT(pino):
    global instance
    instance = dht11.DHT11(pino)
"""########################################################################################################################"""

"""########################################################################################################################"""
valor = [0,0]
#faz a leitura da temperatura e umidade
def dht():
    result = instance.read()
    sleep(15)
    # if result.is_valid():
    temperatura = result.temperature
    umidade = result.humidity
        # print("Temperature: %-3.1f C" % temperatura)
        # print("Humidity: %-3.1f %%" % umidade)
    valor[0] = temperatura

    if(valor[0] > 0.5):
        valor[1] = valor[0]

    # else:
    #     print("Error: %d" % result.error_code)
        
    return valor[1]

"""########################################################################################################################"""
#retorna o estado de um sensor digital
def digital_state(pino):
    if GPIO.input(pino) == 1:
        estado = 1
        #print("Objeto Detectado!")
    else:
        estado = 0
        #print("Objeto Nao Detectado!")
    sleep(0.5)
    return estado

"""########################################################################################################################"""
#Configura o servo
def setupServo(pino): 
    global pwm
    GPIO.setup(pino, GPIO.OUT)
    pwm = GPIO.PWM(pino, 50)
    pwm.start(2)

"""########################################################################################################################"""
#movimento o servo para o angulo desejado de 0 a 180
def setAngle(angle): 
    duty = angle/18 + 2
    pwm.ChangeDutyCycle(duty)
    sleep(1)