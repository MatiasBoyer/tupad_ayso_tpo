# Informe Técnico

## Caso Práctico
Ingresamos al [sitio web](<https://www.virtualbox.org/wiki/Downloads>) y presionamos ‘Windows hosts’
![](./imagenes/firefox_eVA2T2NJfV.png)
<br>

Se nos abre la pantalla de instalación
![](./imagenes/VirtualBox-7.1.10-169112-Win_9cx8wGoYV0.png)
<br>

Aceptamos los términos y condiciones
![](./imagenes/VirtualBox-7.1.10-169112-Win_GxfETMiurJ.png)
<br>

Nos permite elegir las características con las que viene VBox, le damos a Next
![](./imagenes/VirtualBox-7.1.10-169112-Win_iUoKDGQAkd.png)
<br>

Nos avisa que el programa de instalación va a instalar los drivers de internet, por lo que puede dejarnos momentáneamente sin conexión
![](./imagenes/VirtualBox-7.1.10-169112-Win_ynsEyYla47.png)
<br>

Nos informa que nos falta unas dependencias, le damos a Yes para instalarlas
![](./imagenes/VirtualBox-7.1.10-169112-Win_kUeuwb6hBH.png)
<br>

Nos pregunta qué accesos directos queremos
![](./imagenes/VirtualBox-7.1.10-169112-Win_IXlAFSGKa6.png)
<br>

Presionamos INSTALL y comienza el proceso de instalación
![](./imagenes/VirtualBox-7.1.10-169112-Win_2pSOGrfwkG.png)
![](./imagenes/VirtualBox-7.1.10-169112-Win_KhYO8XW7rQ.png)
<br>

Una vez terminado, podemos presionar Finish y se nos abrirá el programa
![](./imagenes/VirtualBox-7.1.10-169112-Win_vbzEVqbWIQ.png)
<br>


Descargamos la distro de Ubuntu, desde el [sitio web oficial](https://ubuntu.com/download/desktop)
![](./imagenes/firefox_4Vx7RG5VEf.png)
![](./imagenes/explorer_2jRK6b9tup.png)
<br>

Una vez descargada, abrimos el programa y presionamos '**Nueva**'
![](./imagenes/VirtualBox_h4spb5XFcf.png)
<br>

Indicamos los datos necesarios:
• Nombre
• Carpeta
• Imagen ISO (descargada previamente)
• Tipo
• Subtipo
• Versión
![](./imagenes/VirtualBox_t5eeNUbrGI.png)
<br>

Dentro de la sección de 'Instalación desatendida', ingresamos nombre de usuario y contraseña, para que VBox instale Ubuntu de forma automática
![](./imagenes/VirtualBox_Tub25Ohdff.png)
<br>

Indicamos RAM y Procesadores a utilizar
La página oficial de Ubuntu, recomienda 4 GB mínimos.
![](./imagenes/VirtualBox_6tXlkeniVO.png)
<br>

Indicamos el espacio máximo del disco duro, y si queremos reservarlo ahora o almacenar dinámicamente
![](./imagenes/VirtualBox_ftojgare1K.png)
<br>

Presionamos '**Terminar**' y se nos abrirá la VM
![](./imagenes/VirtualBox_WMWPePWjtZ.png)
<br>

VirtualBox inicia la instalación de Ubuntu de forma automática
![](./imagenes/VirtualBoxVM_EGajKrp2v4.png)
<br>

Una vez terminado, se reiniciará la máquina virtual y nos permitirá iniciar sesión
![](./imagenes/VirtualBoxVM_8fVetkh7xC.png)
<br>

Iniciamos sesión, y ya tenemos nuestra VM con Ubuntu lista para usar
![](./imagenes/VirtualBoxVM_opawkC3AAs.png)
<br>

Abrimos la terminal
![](./imagenes/VirtualBoxVM_PLIVllGpQ5.png)
![](./imagenes/VirtualBoxVM_oECnFkOQW0.png)
<br>

Verificamos si Python está instalado, en este caso lo está
![](./imagenes/VirtualBoxVM_0O5kUZYUya.png)
<br>

Si Python no está instalado, podemos utilizar *sudo apt install python3* para instalarlo
![](./imagenes/VirtualBoxVM_dhhsLJu00N.png)
<br>

Creamos un nuevo archivo utilizando *nano ./promedios.py*
![](./imagenes/VirtualBoxVM_XsydECM6vx.png)
<br>

Guardamos el archivo presionando la combinación 'CTRL + X'
![](./imagenes/VirtualBoxVM_svIfZOs0OP.png)
Presionamos 'Y' y luego ENTER, y el archivo estará creado
![](./imagenes/VirtualBoxVM_5iSeK6FaT5.png)
<br>

Damos permisos de ejecución utilizando *chmod +x ./promedios.py*
![](./imagenes/VirtualBoxVM_4zfbvkwh35.png)
<br>

Y ejecutamos el mismo utilizando *python3 ./promedios.py*
![](./imagenes/VirtualBoxVM_mflhhcAYs2.png)
<br>

