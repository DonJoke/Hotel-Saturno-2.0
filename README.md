Hotel Saturno 2.0 - Back-End API

API REST desarrollada con Python, Django y Django REST Framework para la gestión integral de clientes, habitaciones y reservas del Hotel Saturno.
Tecnologías Utilizadas
*Python 3.10+*
*Django* (Framework web principal)
*Django REST Framework (DRF)** (Construcción de API REST)
*SQLite3* (Base de datos relacional)
---
#Modelos y Lógica de Negocio

El sistema cuenta con la aplicación `gestion_hotel`, estructurada en tres entidades principales:

1. *Cliente (`cliente`)*
   *Campos:** `nombre`, `rut` (único), `telefono`, `correo` (único).
   *Validación:** Implementa validación matemática chilena (**Módulo 11**) mediante `validar_rut` para rechazar RUTs inválidos o mal formateados.

2. *Habitación (`habitacion`)**
   *Campos:** `numero_habitacion` (único), `piso`, `tipo_de_habitacion`, `precio_noche`.
   *Validación:** Restricción mediante `MinValueValidator(1)` que impide registrar precios menores o iguales a cero.

3. *Reserva (`reserva`)**
   *Campos:** `cliente` (`ForeignKey`), `habitacion` (`ForeignKey`), `fecha_inicio`, `fecha_fin`, `estado`.
   *Reglas de Negocio (`clean` y `save`):*
   * Verifica que la fecha de inicio sea estrictamente anterior a la fecha de término.
   *Anti-solapamiento:* Impide reservar una habitación en fechas que ya estén ocupadas, excluyendo del bloqueo aquellas reservas cuyo estado sea `'Cancelada'`.
---
#Instalación y Ejecución Local

1. *Clonar el repositorio:*
   `git clone <URl>`
   `cd Hotel-Saturno-2.0`

2. *Crear el entorno virtual(windows):*
   `python -m venv .venv`
   `.\.venv\Scripts\Activate.ps1`
    
3. *Para linux o mac:*
    `python3 -m venv .venv`
    `source .venv/bin/activate`

4.*Instalar dependencias:*
    `pip install -r requirements.txt`

5.*Aplicar migraciones:*
 `python manage.py makemigrations`
 `python manage.py migrate`

6.*Iniciar servidor de desarrollo:*
  `python manage.py runserver`
