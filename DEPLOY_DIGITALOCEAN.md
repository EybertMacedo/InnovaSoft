# Guía de Despliegue en Digital Ocean 🌊

Esta guía te ayudará a desplegar el backend de InnovaSoft en Digital Ocean.

## Opción 1: App Platform (Recomendada 🌟)
La forma más fácil, similar a Vercel.

1.  Ve a [Digital Ocean Apps](https://cloud.digitalocean.com/apps).
2.  Click en **Create App**.
3.  Selecciona **GitHub** y conecta tu repositorio `InnovaSoft`.
4.  **Source Directory:** Selecciona la carpeta `backend`.
    *   Digital Ocean detectará automáticamente el `Dockerfile`.
5.  **Environment Variables:**
    *   Añade las variables de tu archivo `.env`:
        *   `GEMINI_API_KEY`
        *   `QDRANT_ENDPOINT`
        *   `QDRANT_API_KEY`
6.  **Instance Size:**
    *   Selecciona el plan **Basic** ($5/mo).
    *   Asegúrate de tener al menos **512MB** de RAM (1GB es mejor para estar seguros).
7.  Click **Next** y luego **Create Resources**.

¡Listo! Tu backend estará online en unos minutos.

---

## Opción 2: Droplet (VPS) 🖥️
Si prefieres tener tu propio servidor Linux (Ubuntu).

### 1. Crear el Droplet
*   Crea un Droplet en Digital Ocean.
*   Elige **Marketplace** -> **Docker** (viene con Docker pre-instalado).
*   Plan recomendado: **Basic ($6/mo) - 1GB RAM**. (512MB puede ser muy justo para Python + AI).

### 2. Conectar y Desplegar
Entra por SSH a tu servidor:
```bash
ssh root@tu-ip-del-droplet
```

Clona tu repositorio:
```bash
git clone https://github.com/EybertMacedo/InnovaSoft.git
cd InnovaSoft
```

Crea el archivo .env:
```bash
nano backend/.env
# Pega aquí tus variables de entorno (GEMINI_API_KEY, QDRANT..., etc)
# Guarda con Ctrl+O, Enter, Ctrl+X
```

Inicia el servicio:
```bash
docker compose up -d --build
```

### 3. Verificar
Tu backend estará corriendo en `http://tu-ip-del-droplet:8000`.

---

## Notas Importantes ⚠️
*   **Memoria:** Estamos usando `fastembed` que es ligero, pero Python siempre consume algo de RAM. El plan de 1GB es lo ideal para estabilidad.
*   **Frontend:** Tu frontend (Vue) puede seguir en Vercel. Solo necesitas actualizar la URL del backend en el frontend para que apunte a tu nueva IP o dominio de Digital Ocean.
