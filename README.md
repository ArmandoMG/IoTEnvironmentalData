# IoTEnvironmentalData
Repo for my Internet of Things Project where I obtained real environmental data and saved it in a database for further data analysis

### Problem Explanation

Design and implement a prototype of a digital system capable of obtaining real physical data (Temperature in this case)through the use of sensors, processing it and depositing it as information on an internet platform, for its subsequent analysis and visualization.

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

mqtt_esp8266_Base3.ino: File used for arduino boards; so that these turn on the
sensors and read information from the real world.

### Dashboard
![image](https://user-images.githubusercontent.com/24629475/109723092-dda10800-7b6a-11eb-801e-1e38014c0825.png)

![image](https://user-images.githubusercontent.com/24629475/109723126-e8f43380-7b6a-11eb-884b-957f078e3659.png)

![image](https://user-images.githubusercontent.com/24629475/109723176-f7424f80-7b6a-11eb-86da-c9ecb2892165.png)

![image](https://user-images.githubusercontent.com/24629475/109723224-04f7d500-7b6b-11eb-8aae-b1c67630c7e7.png)

