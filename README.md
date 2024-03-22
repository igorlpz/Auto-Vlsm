# Auto-VLSM

*Este script ha sido creado para aprender y el codigo puede no ser el mejor, aceptamos mejoras en pull requests*

## Prerequisitos
 - Python3
 - Git

## Instalacion

### Windows
```cmd copy showLineNumbers
git clone https://github.com/igorlpz/Auto-Vlsm.git
cd Auto-Vlsm
python3 auto-vlsm.py
```

### Linux
```bash copy showLineNumbers
git clone https://github.com/igorlpz/Auto-Vlsm.git
cd Auto-Vlsm
python3 auto-vlsm.py
```

## Uso de la herramienta

Para el uso de esta herramienta la abriremos desde la terminal con el siguiente comando:

```bash copy 
python3 auto-vlsm.py
```

Una vez ejecutado, rellena la informacion solicitada.

### Ejemplo
```bash filename="auto-vlsm.py" copy
 [->] Introduce la IP de la red: 192.168.10.20
 [->] Introduce la mascara de la red: 16
 [->] Introduce la cantidad de clientes: 1500
 ---------------------------------------------------
 [+] La IP de red es: 192.168.0.0/16
 [+] El Broadcast es: 192.168.7.255/21
 ---------------------------------------------------
 [->] Desea continuar (s/n): s
 [->] Introduce la cantidad de clientes: 500
 ---------------------------------------------------
 [+] La IP de red es: 192.168.8.0/23
 [+] El Broadcast es: 192.168.9.255/23
 ---------------------------------------------------
 [->] Desea continuar (s/n): s
 [->] Introduce la cantidad de clientes: 200
 ---------------------------------------------------
 [+] La IP de red es: 192.168.10.0/24
 [+] El Broadcast es: 192.168.10.255/24
 ---------------------------------------------------
 [->] Desea continuar (s/n): n
 [+] Cerrando el programa...
```
