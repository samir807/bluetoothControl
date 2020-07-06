from os import system as sys
import sys as sy
print('BluetoothControl')
def xex():
	print("</Успешно>")

print("Разблокировка блютуз устройств... ")
sys("sudo rfkill unblock bluetooth")
xex()

while True:
	function = input("[1]Проверить наличие подключенных устройств \n[2]Включить устройство \n[3]Сканирование bluetooth устройств \n[4]Узнать подробную информацию об устройстве{Требуется mac адрес}\n[0] Выход\n")
	if function == "1":
		sys("sudo rfkill list")
		xex()
	elif function == "2":
		device = input("Введите название устройства. Например: [hci0]: ")
		sys("sudo hciconfig " + device + " up")
		xex()
	elif function == "3":
		sys("sudo hcitool scan")
		xex()
	elif function == "4":
		macaddr = input("Введите mac адрес сканирующего устройства: ")
		sys("sdptool browse " + macaddr)
		xex()
	elif function == "0":
		sy.exit()