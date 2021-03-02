import time
import json
import paho.mqtt.client as mqtt
import datetime
import pytz
import random
import mysql.connector

# Funcino para generar id
def uniqueid():
    seed = random.getrandbits(32)
    while True:
       yield seed
       seed += 1

# Callback Function on Connection with MQTT Server
def on_connect( client, userdata, flags, rc):
    print ("Connected with Code :" +str(rc))
    # Subscribe Topic from here
    client.subscribe("f1004b/e1")
    client.subscribe("tc1004b/profe/dispositivos")


# Callback Function on Receiving the Subscribed Topic/Message
def on_message( client, userdata, msg):
    # print the message received from the subscribed topic
    topicoLlegada = msg.topic
    mensajeLlegada = str(msg.payload.decode("utf-8","ignore"))
    m_in = json.loads(mensajeLlegada)
    print()
    print('Topico: ', topicoLlegada)
#    print(type(mensajeLlegada), ' ', mensajeLlegada)
#    print(type(m_in), ' ', m_in)
    print('Dispositivo: ', type(m_in['dispositivo']), ' ', m_in['dispositivo'])
    print('Tipo: ', type(m_in['tipo']), ' ', m_in['tipo'])
    print('Dato: ', type(m_in['dato']), ' ', m_in['dato'])
    tzyc = pytz.timezone('America/Monterrey')
    current_datetime = datetime.datetime.now(tzyc)
    database = mysql.connector.connect (
        host = '127.0.0.1',
        user = 'root',
        password = '',
        database = 'reto_iot'
    )
    cur = database.cursor()
    addLectura = 'INSERT INTO Lectura (lecturaID, dato, fecha, sensorID) VALUES (%s, %s, %s, %s)'
    unique_sequence = uniqueid()
    lecturaID = next(unique_sequence)
    data = (lecturaID, m_in['dato'], current_datetime, m_in['dispositivo'])
    cur.execute(addLectura, data)
    database.commit()

def envia_dispositivo():
    dispositivo = input('ID del dispositivo: ')
    tipo = input('Sensor del dispositivo: ')
    dato = int(input('Dato: '))
    dicSalida = {'dispositivo':dispositivo, 'tipo':tipo, 'dato':dato}
    salidaJson = json.dumps(dicSalida)
    client.publish("f1004b/e1", salidaJson)

def envia_dispositivoT():
    dispositivo = "ST001"
    tipo = "Temperatura"
    dato = random.randrange(20, 40, 1)
    dicSalida = {'dispositivo':dispositivo, 'tipo':tipo, 'dato':dato}
    salidaJson = json.dumps(dicSalida)
    client.publish("f1004b/e1", salidaJson)

def envia_dispositivoH():
    dispositivo = "SH001"
    tipo = "Humedad"
    dato = random.randrange(20, 100, 1)
    dicSalida = {'dispositivo':dispositivo, 'tipo':tipo, 'dato':dato}
    salidaJson = json.dumps(dicSalida)
    client.publish("f1004b/e1", salidaJson)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.mqtt-dashboard.com", port=1883)
#client.username_pw_set("setsmjwc", "apDnKqHRgAjA")


# client.loop_forever()
client.loop_start()
time.sleep(3)
opc = 'x'
while opc != 's':
    opc = input('e)Envia p)Procesa s)Salir ')
    if opc == 'e':
        envia_dispositivo()
    elif opc == 'p':
        doing = True
        while(doing):
            envia_dispositivoT()
            envia_dispositivoH()
            time.sleep(5)


client.loop_stop()
client.disconnect()
