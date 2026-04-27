# Simulador de Autómatas Finitos (AFD y AFND)

## Descripción
Proyecto desarrollado para la práctica de **Autómatas Finitos Deterministas (AFD)** y **Autómatas Finitos No Deterministas (AFND)**, implementado en **Python con Flask** para el backend y **HTML, CSS y JavaScript** para el frontend.

El sistema permite simular, validar y visualizar distintos problemas modelados mediante autómatas, mostrando:

- Alfabeto válido
- Transiciones
- Diagramas de estados
- Ejecución de cadenas
- Aceptación o rechazo del lenguaje

---

# Objetivos

- Implementar autómatas finitos deterministas y no deterministas.
- Simular problemas reales mediante reconocimiento de patrones.
- Comparar el comportamiento de AFD y AFND.
- Desarrollar una interfaz interactiva para ejecutar los autómatas.

---

# Ejercicios Implementados

## AFD (Autómatas Deterministas)

### 1. Flujo de Transacciones Bancarias
Lenguaje:

```
L = {ACL}
```

Patrón:

```
Autorización → Captura → Liquidación
```

---

## 2. Protocolo Three-Way Handshake

```
L = {SYA}
```

Patrón:

```
SYN → SYN-ACK → ACK
```

---

## 3. Cerradura Inteligente

Modela intentos fallidos y bloqueo tras múltiples errores.

---

# AFND (Autómatas No Deterministas)

## 4. Reconocimiento de Secuencias Genéticas

```
KGX*F
```

---

## 5. Comportamiento de Usuario en E-commerce

```
HS+C
```

---

## 6. Validación de Telemetría IoT

```
H(T|U)*C
```

---

# Tecnologías Utilizadas

- Python 3
- Flask
- Flask-CORS
- HTML5
- CSS3
- JavaScript
- JFLAP
- Git / GitHub

---

# Instalación

## Clonar repositorio

```bash
git clone https://github.com/usuario/automatas.git
cd automatas
```

---

## Instalar dependencias

```bash
pip install flask
pip install flask-cors
```

---

## Ejecutar backend

```bash
cd backend
python app.py
```

Servidor:

```text
http://127.0.0.1:5000
```

---

## Ejecutar frontend

Abrir:

```text
frontend/index.html
```

en el navegador.

---

# Casos de prueba

## Aceptadas

```text
ACL
SYA
FFO
KGXXF
HSSC
HTUC
```

---

## Rechazadas

```text
ALC
SAY
FFF
KGX
HC
HT
```

---

# Metodología

Se siguió una metodología incremental:

1. Análisis del problema.
2. Diseño formal de autómatas.
3. Construcción de diagramas de transición.
4. Implementación en Python/Flask.
5. Desarrollo del frontend.
6. Validación mediante casos de prueba.

---

# Características del Simulador

- Validación de cadenas
- Visualización del alfabeto
- Diagramas de transición
- Simulación de ejecución
- Comparación entre AFD y AFND

---

# Uso de Inteligencia Artificial

Este proyecto empleó herramientas de Inteligencia Artificial como apoyo para:

- asistencia conceptual
- revisión de código
- apoyo en documentación
- generación de ideas

La implementación, validación y adaptación final fueron realizadas por el estudiante.

---

# Autores

Jose Fermín Encalada Leiva  
Anthony Gutierrez Tapia