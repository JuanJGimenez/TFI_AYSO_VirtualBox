# TFI AYSO — Virtualización con VirtualBox

**Trabajo Práctico Integrador**
**Materia:** Arquitectura y Sistemas Operativos
**Tecnicatura Universitaria en Programación a Distancia — UTN**

---

## Descripción

Este proyecto documenta la configuración de un entorno de desarrollo virtualizado sobre Windows mediante Oracle VM VirtualBox, con Ubuntu Server 26.04 LTS como sistema operativo invitado, y la ejecución de un programa Python que realiza conversiones de temperatura entre las escalas Celsius, Fahrenheit y Kelvin.

---

## Estructura del Repositorio

```
tp-virtualizacion/
├── README.md
├── TP_Virtualizacion_Informe.pdf
├── main.py
└── capturas/
    ├── asigno_especif.jpg
    ├── instalacion.jpg
    ├── 01_error_postinstall.png
    ├── 02_shell_emergencia_python.png
    ├── 03_ping_conectividad.png
    ├── 04_ubuntu_login.png
    ├── 05_error_cdrom.png
    ├── 06_apt_update_ok.png
    ├── 07_error_venv.png
    ├── 08_venv_instalado.png
    ├── 09_venv_activado.png
    ├── 10_ssh_habilitado.png
    ├── 11_reenvio_puertos.png
    ├── 12_vscode_ssh.png
    └── 13_ejecucion_programa.png
├── requirements.txt
```

---

## Requisitos

### Sistema anfitrión (host)
- Windows 10/11 de 64 bits
- Al menos 4 GB de RAM disponibles (2 GB se asignan a la VM)
- Al menos 25 GB de espacio libre en disco

### Software necesario
- [Oracle VM VirtualBox 7.x](https://www.virtualbox.org/wiki/Downloads)
- [Ubuntu Server 26.04 LTS ISO](https://ubuntu.com/download/server)
- [Visual Studio Code](https://code.visualstudio.com/) con extensión [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) _(opcional, para edición remota)_

---

## Instalación paso a paso

### 1. Crear la máquina virtual en VirtualBox

1. Abrir VirtualBox y hacer clic en **Nueva**.
2. Configurar los parámetros:
   - **Nombre:** TFI AYSO
   - **Tipo:** Linux / Ubuntu (64-bit)
   - **Memoria base:** 2056 MB
   - **Procesadores:** 2
   - **Disco virtual:** 20 GB (VDI, asignación dinámica)
3. Montar la ISO de Ubuntu Server 26.04 LTS en la unidad óptica virtual.
4. Completar la instalación desatendida con usuario `vboxuser`.

---

### 2. Errores conocidos y sus soluciones

#### ⚠️ Error 1: Fallo de postinstall durante la instalación desatendida

**Síntoma:**
```
apt-get update returned non-zero exit status 100
An error occurred. Press enter to start a shell
```

**Solución:** Presionar Enter para acceder al shell de emergencia. Verificar conectividad y que Python está disponible, luego continuar con la instalación. El sistema arranca correctamente al reiniciar.

```bash
python3 --version   # Python 3.12.3
ping -c 4 8.8.8.8   # verificar red
```

---

#### ⚠️ Error 2: Repositorio CDROM no encontrado al ejecutar `apt update`

**Síntoma:**
```
Err:2 file:/cdrom resolute Release
  File not found - /cdrom/dists/resolute/Release
Error: The repository 'file:/cdrom resolute Release' no longer has a Release file.
```

**Causa:** La instalación desatendida deja configurado un repositorio CDROM que ya no existe una vez finalizada la instalación.

**Solución:**
```bash
# Ver archivos de configuración apt
ls /etc/apt/sources.list.d/
# cdrom.sources  ubuntu.sources

# Eliminar el repositorio cdrom
sudo rm /etc/apt/sources.list.d/cdrom.sources

# Verificar que apt update funciona
sudo apt update
```

---

#### ⚠️ Error 3: `python3 -m venv` falla por falta de `ensurepip`

**Síntoma:**
```
The virtual environment was not created successfully
because ensurepip is not available.
apt install python3.14-venv
```

**Solución:**
```bash
sudo apt install python3.14-venv -y
```

---

#### ⚠️ Error 4: `nano` no disponible en la instalación mínima

**Síntoma:**
```
sudo: nano/etc/apt/...: command not found
```

**Solución:** Usar `sed -i` para editar archivos de configuración, o instalar nano:
```bash
sudo apt install nano -y
```

---

### 3. Preparar el entorno de trabajo

```bash
# Actualizar paquetes (luego de resolver el error de cdrom)
sudo apt update && sudo apt upgrade -y

# Crear directorio del proyecto
mkdir tfi_gimenez
cd tfi_gimenez

# Crear y activar entorno virtual Python
python3 -m venv env
source env/bin/activate
# El prompt cambia a: (env) vboxuser@TFI-AYSO:~/tfi_gimenez$
```

---

### 4. Configurar acceso SSH desde Windows (opcional)

Habilitar SSH en la VM:
```bash
sudo systemctl enable --now ssh
```

En VirtualBox, agregar una regla de reenvío de puertos:
- **Protocolo:** TCP
- **IP anfitrión:** 127.0.0.1
- **Puerto anfitrión:** 2222
- **Puerto invitado:** 22

Conectarse desde Windows:
```bash
ssh vboxuser@127.0.0.1 -p 2222
```

Para VS Code: instalar la extensión **Remote - SSH** y conectarse a `ssh://vboxuser@127.0.0.1:2222`.

---

### 5. Ejecutar el programa

```bash
# Activar el entorno virtual (si no está activo)
source env/bin/activate

# Ejecutar el conversor de temperaturas
python3 src/main.py
```

**Ejemplo de ejecución:**
```
===================================
   CONVERSOR DE TEMPERATURAS
===================================
Ingresa 3 valores en grados Celsius:
  Temperatura 1: 0
  Temperatura 2: 100
  Temperatura 3: -40

--- Resultados ---
-----------------------------------
  Celsius    : 0.00 C
  Fahrenheit : 32.00 F
  Kelvin     : 273.15 K
-----------------------------------
  Celsius    : 100.00 C
  Fahrenheit : 212.00 F
  Kelvin     : 373.15 K
-----------------------------------
  Celsius    : -40.00 C
  Fahrenheit : -40.00 F
  Kelvin     : 233.15 K
-----------------------------------

Promedio: 20.00 C
```

---

## Bibliografía

- Oracle. (2024). *Oracle VM VirtualBox User Manual* (v7.0). https://www.virtualbox.org/manual/
- Canonical Ltd. (2026). *Ubuntu Server 26.04 LTS Release Notes*. https://ubuntu.com/server/docs
- Python Software Foundation. (2024). *Python 3 Documentation*. https://docs.python.org/3/
- Silberschatz, A., Galvin, P. B., & Gagne, G. (2018). *Operating System Concepts* (10.ª ed.). John Wiley & Sons.
- Tanenbaum, A. S., & Bos, H. (2015). *Modern Operating Systems* (4.ª ed.). Pearson Education.

---

> **Materia:** Arquitectura y Sistemas Operativos — UTN TUPaD
