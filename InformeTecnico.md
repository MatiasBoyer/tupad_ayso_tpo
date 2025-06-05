# Informe Técnico

## <a name = "indice"></a>Índice
- [Informe Técnico](#informe-técnico)
  - [Índice](#índice)
  - [Introducción](#introducción)
  - [Marco Teórico](#marco-teórico)
      - [¿Qué es la virtualización?](#qué-es-la-virtualización)
      - [Beneficios de la virtualización](#beneficios-de-la-virtualización)
      - [Componentes principales de la virtualización](#componentes-principales-de-la-virtualización)
        - [Máquina física](#máquina-física)
        - [Máquina virtual](#máquina-virtual)
      - [Hipervisores](#hipervisores)
      - [Tipos de Hipervisores](#tipos-de-hipervisores)
  - [Caso Práctico](#caso-práctico)
  - [Metodología Utilizada](#metodología-utilizada)
  - [Resultados Obtenidos](#resultados-obtenidos)
  - [Conclusiones](#conclusiones)

## <a name = "introduccion"></a>Introducción
La virtualización hoy en día, es una tecnología clave en la informática moderna, ya que nos permite ejecutar múltiples sistemas operativos sobre una única computadora, optimizando recursos y facilitando la posibilidad de tener distintos entornos de prueba, desarrollo y producción.
Este tema es de suma importancia para la carrera, porque hoy en día la gran mayoría de desarrollos y puestas en producción se realiza utilizando máquinas virtuales, Docker, VPS, etc. 
El objetivo principal de este trabajo es aplicar todos los conocimientos adquiridos durante la materia, mediante la creación de un entorno virtual. Se busca demostrar la capacidad de poder configurar un SO dentro de VirtualBox, entender la relación entre esta VM y la máquina HOST, y poder configurarlo correctamente.

## <a name = "marcoteorico"></a>Marco Teórico
#### ¿Qué es la virtualización? 
La virtualización es una tecnología que permite la creación de entornos virtuales a partir de una única máquina física, permitiendo un uso más eficiente de los recursos al distribuirlos entre entornos informáticos.
Mediante software, la virtualización crea una capa de abstracción sobre el hardware informático, dividiendo los componentes de un sistema, como procesadores, memoria, redes y almacenamiento, en múltiples máquinas virtuales (VM). Cada VM ejecuta su propio sistema  operativo y se comporta como un ordenador físico independiente, a pesar de compartir el mismo hardware subyacente.
<br>
![](./imagenes/img1.png)
<br>
_Imagen de ejemplo de virtualización de sistemas_

#### Beneficios de la virtualización
1. Ahorro de costos: Menor necesidad de hardware físico: se pueden ejecutar múltiples sistemas operativos en una sola máquina física.
2. Eficiencia:
Maximiza los recursos disponibles reduciendo el desperdicio y mejorando el rendimiento.
3. Flexibilidad y escalabilidad:
Las máquinas virtuales pueden crearse, duplicarse o eliminarse fácilmente, adaptándose a las necesidades del momento. 
4. Aislamiento y seguridad:
Cada máquina virtual está aislada del sistema operativo anfitrión y de otras VMs. 
Si una VM es atacada o presenta un fallo, no afecta a las demás ni al equipo real.

#### Componentes principales de la virtualización
La virtualización se basa en varios componentes clave para crear y gestionar entornos virtuales. Cada uno de ellos desempeña un papel fundamental para garantizar la asignación eficaz de recursos, de modo que varias máquinas virtuales puedan ejecutarse simultáneamente sin interferencias. Los componentes principales son:
1. Maquina fisica
2. Maquina virtual
3. Hipervisores

##### Máquina física
La máquina física, también denominada “máquina host”, es el hardware que proporciona CPU, memoria, almacenamiento y recursos de red para las máquinas virtuales.

##### Máquina virtual
Una máquina virtual (VM) es un entorno virtual que simula un ordenador físico mediante software. Las VM suelen denominarse "invitadas", con una o más máquinas "invitadas" ejecutándose en un host.<br>
Según Microsoft:
> "Una máquina virtual es un archivo de software (normalmente llamado imagen) que actúa como una computadora real. Puede ejecutar un sistema operativo completo y comportarse como si fuera una PC independiente."
(Fuente: Microsoft Learn – Virtual Machines)

Las máquinas virtuales tienden de varios archivos, incluyendo la configuración, el almacenamiento del disco duro virtual y otras dependencias.
Sus principales componentes son:
- *CPU virtual*: Procesador simulado, compartido con la CPU física del HOST.
- *Memoria RAM virtual*: Se asigna desde la RAM física del sistema anfitrión.
- *Disco duro virtual*: Archivo que simula un disco (.vdi , .vmdk ).
- *Sistema Operativo*: SO invitado, LINUX, WINDOWS.  

#### Hipervisores
Hipervisores
Los hipervisores son fundamentales en el funcionamiento de las máquinas virtuales. 

Según Red Hat:
> “El hipervisor es el software que crea y ejecuta las máquinas virtuales. Se encarga de asignar los recursos físicos entre las VMs.”<br>(Fuente: Red Hat – Virtualization overview)

Un hipervisor es la capa de software que coordina las máquinas virtuales. Actúa como interfaz entre la máquina virtual y el hardware físico, garantizando que cada una tenga acceso a los recursos físicos necesarios para su ejecución. También garantiza que las máquinas virtuales no interfieran entre sí, vulnerando el espacio de memoria o los ciclos de cómputo de las demás.

Función del hipervisor:
- Actúa como una capa de intermediación entre el hardware físico y las máquinas virtuales.
- Controla qué recursos se asignan a cada VM.
- Asegura el aislamiento entre las VMs para que no interfieran entre sí.

#### Tipos de Hipervisores
Tipos de hipervisores

<ul>
<li>
Hipervisor tipo 1: El hipervisor tipo 1 se ejecuta directamente sobre el hardware físico del sistema anfitrión, sin requerir un sistema operativo intermedio. Administra el acceso al hardware por parte de las VMs de forma directa, lo cual ofrece mejor rendimiento, menor latencia y mayor seguridad.
<br><br>
Ventajas:
<ul>
<li>Mayor rendimiento: Al ejecutarse directamente sobre el hardware, no hay capa de sistema operativo que interfiera.</li>
<li>Eficiencia en la gestión de recursos: Accede directamente al hardware, evitando sobrecargas del sistema operativo host.</li>
</ul>
<br>
Desventajas:
<ul>
<li>Complejidad de instalación: Requiere conocimientos técnicos y configuración específica del hardware.</li>
<li>Requiere hardware dedicado: Está pensado para servidores, no para equipos personales.</li>
</ul>
</li>
<br>

<li>
Hipervisor tipo 2: Los hipervisores de tipo 2 se ejecutan como una aplicación en un sistema operativo existente. Se utilizan con mayor frecuencia en dispositivos endpoint para ejecutar sistemas operativos alternativos y conllevan una sobrecarga de rendimiento, ya que deben usar el sistema operativo host para acceder y coordinar los recursos de hardware subyacentes.
<br><br>
Características técnicas
<br>
<ul>
<li>Corre sobre sistemas operativos como Windows, macOS o Linux.</li>
<li>Más fácil de instalar y configurar.</li>
<li>Puede tener menor rendimiento debido a la doble capa de abstracción (VM → Hipervisor → Host OS → Hardware).</li>
<li>Adecuado para entornos de desarrollo, pruebas, educación y laboratorios virtuales.</li>
</ul>

<br>
Ventajas:
<ul>
<li>Fácil de instalar: Se instala como un programa cualquiera (como instalar Chrome o Word).</li>
<li>Permite ejecutar múltiples SO sin afectar el host: Se puede tener Windows, Linux y otros corriendo dentro de tu PC.</li>
</ul>
<br>
Desventajas:
<ul>
<li>Menor rendimiento: La VM depende del sistema operativo host para acceder al hardware.</li>
<li>Menor aislamiento: Si el host tiene un problema, afecta a todas las VMs.</li>
<li>Menor escalabilidad: No está optimizado para muchas VMs concurrentes</li>
</ul>
</li>
</ul>



## <a name = "casopractico"></a>Caso Práctico
Ingresamos al [sitio web](<https://www.virtualbox.org/wiki/Downloads>) y presionamos ‘Windows hosts’
<br>
![](./imagenes/firefox_eVA2T2NJfV.png)
<br>

Se nos abre la pantalla de instalación
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_9cx8wGoYV0.png)
<br>

Aceptamos los términos y condiciones
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_GxfETMiurJ.png)
<br>

Nos permite elegir las características con las que viene VBox, le damos a Next
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_iUoKDGQAkd.png)
<br>

Nos avisa que el programa de instalación va a instalar los drivers de internet, por lo que puede dejarnos momentáneamente sin conexión
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_ynsEyYla47.png)
<br>

Nos informa que nos falta unas dependencias, le damos a Yes para instalarlas
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_kUeuwb6hBH.png)
<br>

Nos pregunta qué accesos directos queremos
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_IXlAFSGKa6.png)
<br>

Presionamos INSTALL y comienza el proceso de instalación
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_2pSOGrfwkG.png)
![](./imagenes/VirtualBox-7.1.10-169112-Win_KhYO8XW7rQ.png)
<br>

Una vez terminado, podemos presionar Finish y se nos abrirá el programa
<br>
![](./imagenes/VirtualBox-7.1.10-169112-Win_vbzEVqbWIQ.png)
<br>


Descargamos la distro de Ubuntu, desde el [sitio web oficial](https://ubuntu.com/download/desktop)
<br>
![](./imagenes/firefox_4Vx7RG5VEf.png)
<br>
![](./imagenes/explorer_2jRK6b9tup.png)
<br>

Una vez descargada, abrimos el programa y presionamos '**Nueva**'
<br>
![](./imagenes/VirtualBox_h4spb5XFcf.png)
<br>

Indicamos los datos necesarios:
• Nombre
• Carpeta
• Imagen ISO (descargada previamente)
• Tipo
• Subtipo
• Versión
<br>
![](./imagenes/VirtualBox_t5eeNUbrGI.png)
<br>

Dentro de la sección de 'Instalación desatendida', ingresamos nombre de usuario y contraseña, para que VBox instale Ubuntu de forma automática
<br>
![](./imagenes/VirtualBox_Tub25Ohdff.png)
<br>

Indicamos RAM y Procesadores a utilizar
La página oficial de Ubuntu, recomienda 4 GB mínimos.
<br>
![](./imagenes/VirtualBox_6tXlkeniVO.png)
<br>

Indicamos el espacio máximo del disco duro, y si queremos reservarlo ahora o almacenar dinámicamente
<br>
![](./imagenes/VirtualBox_ftojgare1K.png)
<br>

Presionamos '**Terminar**' y se nos abrirá la VM
<br>
![](./imagenes/VirtualBox_WMWPePWjtZ.png)
<br>

VirtualBox inicia la instalación de Ubuntu de forma automática
<br>
![](./imagenes/VirtualBoxVM_EGajKrp2v4.png)
<br>

Una vez terminado, se reiniciará la máquina virtual y nos permitirá iniciar sesión
<br>
![](./imagenes/VirtualBoxVM_8fVetkh7xC.png)
<br>

Iniciamos sesión, y ya tenemos nuestra VM con Ubuntu lista para usar
<br>
![](./imagenes/VirtualBoxVM_opawkC3AAs.png)
<br>

Abrimos la terminal
<br>
![](./imagenes/VirtualBoxVM_PLIVllGpQ5.png)
<br>
![](./imagenes/VirtualBoxVM_oECnFkOQW0.png)
<br>

Verificamos si Python está instalado, en este caso lo está
<br>
![](./imagenes/VirtualBoxVM_0O5kUZYUya.png)
<br>

Si Python no está instalado, podemos utilizar *sudo apt install python3* para instalarlo
<br>
![](./imagenes/VirtualBoxVM_dhhsLJu00N.png)
<br>

Creamos un nuevo archivo utilizando *nano ./promedios.py*
<br>
![](./imagenes/VirtualBoxVM_XsydECM6vx.png)
<br>

Guardamos el archivo presionando la combinación 'CTRL + X'
<br>
![](./imagenes/VirtualBoxVM_svIfZOs0OP.png)
<br>
Presionamos 'Y' y luego ENTER, y el archivo estará creado
<br>
![](./imagenes/VirtualBoxVM_5iSeK6FaT5.png)
<br>

Damos permisos de ejecución utilizando *chmod +x ./promedios.py*
<br>
![](./imagenes/VirtualBoxVM_4zfbvkwh35.png)
<br>

Y ejecutamos el mismo utilizando *python3 ./promedios.py*
<br>
![](./imagenes/VirtualBoxVM_mflhhcAYs2.png)
<br>

## <a name = "metodologia_utilizada"></a>Metodología Utilizada
Nos dividimos la investigación teórica, y el caso práctico por separado. Nos pusimos de acuerdo en que lo mostrado estaba OK guardando la información en un documento de google, y procedimos a la creación del repositorio.

## <a name = "resultados_obtenidos"></a>Resultados Obtenidos
- Obtuvimos VirtualBox
- Obtuvimos una máquina virtual configurada, y lista para su uso
- Descargamos e instalamos python
- Aprendimos que python no es lo mismo que python3 dentro de Linux

## <a name = "conclusiones"></a>Conclusiones
- Aprendimos a configurar una máquina virtual utilizando VirtualBox
- Aprendimos sobre hardware y especificaciones mínimas, dandole los recursos apropiados a la máquina virtual para ejecutarse correctamente
- Nos familiarizamos con Linux y su terminal, utilizando comandos como ls, nano y chmod para poder crear un nuevo script en Python directo desde ella
- Hicimos uso de ‘apt’, uno de los gestores de paquete más utilizados
- Creamos un script en Python dentro de la máquina virtual, aprendiendo sobre entornos aislados