import colorama
import math

colorama.init(True)

def getNextIpAddr(ip): #Obtiene la siguiente ip
    return sumIntToIp(ip, 1) #Suma 1 a la IP

#Funcion para convertir un array con 4 numeros int a un array binario
def getBinArray(ipArray):
    for i in range(4):
        ipArray[i] = bin(int(ipArray[i]))
        ipArray[i] = ipArray[i][2:].zfill(8)
    return ipArray

#Funcion para convertir la IP string a un array
def getIpArray(ip):
    return ip.split(".")

def getMaskFromClientNum(clientNum, type = "red"): #Calcula la mascara de la red (por defecto) o la mascara de los clientes en base al numero de los clientes
    x = math.log(int(clientNum), 2) #Calcula el logaritmo del numero de clientes con base de 2, este nos dará el valor mas aproximado de la mascara
    xround = math.ceil(x) #Redondea el valor hacia arriba
    if (type == "red"): 
        return 32 - xround #Si se busca la mascara de la red, este se restara a 32, si no, este se devolvera como mascara de cliente
    if (type == "cliente"):
        return xround
    else:
        return 'Error al obtener la mascara'

def convertBinaryStringToDecIp(string):
    val = ".".join([string[i:i+8] for i in range(0, len(string), 8)]) #Separa el string en grupos de 8 bits, dividos en puntos
    binArray = val.split(".") #Separa los puntos en un array
    intList = [] #Crea un array vacio
    for i in range(4): #Recorre el array de grupos de 8 bits
        currBin = int(binArray[i], 2) #Convierte el grupo de 8 bits en decimal
        intList.append(currBin) #Guarda el decimal en el array
    return f'{intList[0]}.{intList[1]}.{intList[2]}.{intList[3]}' #Devuelve la IP en decimal

def getBinFromArray(binArray):
    return f'{binArray[0]}{binArray[1]}{binArray[2]}{binArray[3]}'

#Funcion para sacar la direccion de red de la IP
def getNet(ip, mask, maskType = "red", type = "red",):
    ipArray = getIpArray(ip) #Separa la ip en 4 partes
    binArray = getBinArray(ipArray) #Obtien el array en binario
    thebin = getBinFromArray(binArray) #Crea un string con el array binario
    netMask = 0
    if (maskType == "red"): #Si el tipo de mascara es red, se restara la mascara de la red
        netMask = int(mask)
    elif (maskType == "cliente"): #Si el tipo de mascara es cliente, se calculara la mascara de red 
        netMask = int(32 - mask)
    elif (maskType == "clientNum"): #Si el tipo de mascara es Numero de clientes, se calculara la mascara de red 
        netMask = int(getMaskFromClientNum(mask))
    else: return "Error en la mascara"
    if (type == "red"):
        netBin = f'{thebin[:netMask]}'.ljust(32, '0') #Rellena el binario de la mascara de cliente con 0
    elif (type == "broadcast"):
        netBin = f'{thebin[:netMask]}'.ljust(32, '1')
    else: return "Error en el tipo"
    return convertBinaryStringToDecIp(netBin)

def myInput(string):
    return input(f'{colorama.Fore.WHITE} [{colorama.Fore.YELLOW}->{colorama.Fore.WHITE}] {string}')

def separator():
    print(f'{colorama.Fore.LIGHTBLACK_EX} ---------------------------------------------------')
    return

#Funcion para estilos de print
def myPrint(string, TYPE):
    if (TYPE == "info"):
        print(f'{colorama.Fore.WHITE} [{colorama.Fore.LIGHTGREEN_EX}i{colorama.Fore.WHITE}] {string}')
    elif (TYPE == "success"):
        print(f'{colorama.Fore.WHITE} [{colorama.Fore.GREEN}+{colorama.Fore.WHITE}] {colorama.Fore.LIGHTCYAN_EX}{string}')
    return
def sumaBin(num1, num2):
    suma = int(num1, 2) + int(num2, 2) #convierte el string a decimal y lo suma
    binario = bin(suma)[2:] #guarda la variable sin contar los dos primeros caracteres "0b"
    return binario

def sumIntToIp(ip1, integro): #Suma un int a una IP
    ip1bin = getBinFromArray(getBinArray(getIpArray(ip1))) #convierte la IP en binario
    integro = str(integro).zfill(32)
    suma = sumaBin(ip1bin, integro).zfill(32) #suma el binario con el int
    return convertBinaryStringToDecIp(suma) #convierte el binario a decimal y rellena con 0 a la izquierda

def main():
    separator()
    myPrint("Creado por: Igor", "info") #
    myPrint("Github: https://github.com/igorlpz", "info")
    separator()
    laIp = myInput("Introduce la IP de la red: ")
    ipMask = myInput("Introduce la mascara de la red: ")
    while (int(ipMask) > 32 or int(ipMask) < 0):
        myPrint("La mascara tiene que ser de 0 a 32", "info")
        ipMask = myInput("Introduce la mascara de la red: ")
    ipClients = myInput("Introduce la cantidad de clientes: ")
    separator()
    laIp = getNet(laIp, ipMask) 
    myPrint(f"La IP de red es: {laIp}/{ipMask}", "success")
    lastBrd = getNet(getNet(laIp, ipMask), ipClients, "clientNum", "broadcast")
    myPrint(f'El Broadcast es: {lastBrd}/{getMaskFromClientNum(ipClients)}', "success")
    while (True):
        separator()
        cont = myInput("Desea continuar (s/n): ")
        if (cont == "n"):
            break
        lastBrd = getNet(laIp, ipClients, "clientNum", "broadcast")
        ipClients = myInput("Introduce la cantidad de clientes: ")
        laIp = getNextIpAddr(lastBrd)
        separator()
        myPrint(f"La IP de red es: {laIp}/{getMaskFromClientNum(ipClients)}", "success")
        lastBrd = getNet(laIp, ipClients, "clientNum", "broadcast")
        myPrint(f'El Broadcast es: {lastBrd}/{getMaskFromClientNum(ipClients)}', "success")
    myPrint(f'Cerrando el programa...', "success")
    return

main()
