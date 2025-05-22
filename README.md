# 🕵️ Enumerador de Usuarios - Fuerza Bruta con Python

Este script en Python permite enumerar usuarios válidos en un formulario de login web. Se basa en analizar la respuesta del servidor (código HTTP 301) para identificar nombres de usuario existentes.

### 🧠 ¿Cómo funciona?

1. **Enumeración inicial:**  
   Se prueba cada letra del abecedario como prefijo (`a*`, `b*`, etc.), observando si el servidor redirige (status `301`), lo cual indica un posible nombre de usuario válido.

2. **Expansión del nombre:**  
   Si una letra es válida, se itera carácter por carácter (`ab*`, `abc*`, ...) hasta que deja de redirigir. Esto permite descubrir nombres completos.

---

### 🚀 Uso

```bash
python3 user_enum.py

🔴 Asegurate de tener un servidor de pruebas corriendo en:
http://localhost:8888

Recuerda que podés modificar la variable url para apuntar a otra dirección local o de laboratorio.
