# IoTEnvironmentalData
Repo for my Internet of Things Project where I obtained real environmental data and saved it in a database

### Colaborators
Sergio Lopez Urzaiz A00827462

Ricardo Rodriguez Rodriguez A01283165

Mizael Beltran Romero A01114973

Armando Montaño Gonzalez A00827377

Oscar Adrian Bastidas Garzon A01741581

### Instructions
MQTT_Json.py: Python file with which we send data to the topic "f1004b/e1". These
data will be sent through 2 functions. The first function will be the "send" which allows
to the user to send a data from a specific sensor. The other function will be the one of "processes", which
will send data every 5 seconds so that our database receives it. This would be like a
simulation of having sensors in real life.

Reto_Script_Mysql.txt: txt file containing the SQL query used to create our database

mqtt_esp8266_Base3.ino: Archivo utilizado para las placas de arduino; para que estas prendan los 
sensores y lean informacion del mundo real.
