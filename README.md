
# Voice Bot 🤖

-------------

Voice Bot orientado a la venta de productos y servicios, desarrollado en  [ChatScript](https://github.com/ChatScript/ChatScript) .
## Instalación 🔧

Primero debemos clonar el repositorio de [ChatScript](https://github.com/ChatScript/ChatScript) en nuestro ordenador, este contiene las carpetas básicas para el funcionamiento del proyecto.
Una vez clonado el repositorio en nuestro ordenador introducimos el contenido de este repositorio en siguiente directorio
```bash
\ChatScript\RAWDATA
```
## Modo independiente: se ejecuta localmente en una consola (para desarrollo/prueba) 
Desde el directorio de inicio de ChatScript, ir al directorio BINARIES:
```bash
cd BINARIOS
```
Y ejecuta el motor de ChatScript
### Windows
```bash
ChatScript
```
### Linux
```bash
./LinuxChatScript64 local
```
NOTA - Para establecer el ejecutable en Linux:  `chmod a+x ./LinuxChatScript64`

### Mac OS
```bash
./MacChatScript local
```
Esto hará que ChatScript se cargue y te pida un nombre de usuario, puedes introducir el que desees.
Entonces estás hablando con el bot de demostración predeterminado `Harry`.
## Modo Servidor (para producción)
Desde el directorio de inicio de ChatScript, ir al directorio BINARIES directory and run the ChatScript engine as server
### Ejecutar servidor en Windows
```bash
ChatScript port=1024
```
### Ejecutar servidor en Linux
```bash
./LinuxChatScript64
```
### Ejecutar servidor en MacOS
```bash
./MacChatScript
```
Esto hará que ChatScript se cargue como servidor.
Pero también necesita un cliente (para probar la comunicación cliente-servidor).
Puede ejecutar una ventana de comando separada e ir al directorio BINARIES y escribir:
### Ejecutar un cliente (test) en Windows
```bash
ChatScript client=localhost:1024 
```

### Ejecutar un cliente (test) en Linux
```bash
./LinuxChatScript64 client=localhost:1024
```

### Ejecutar un cliente (test) en MacOS
```bash
./MacChatScript client=localhost:1024
```
Esto hará que ChatScript se cargue como cliente y podrá hablar con el servidor.
