# Comandos utilizados

## Instalar [`customtkinter`](https://github.com/TomSchimansky/customtkinter)

```bash
# Con `pip` (manejador de paquetes por defecto)
pip install customtkinter

# Si llamar `pip` directamente no funciona, intenten:
py -m pip install customtkinter
```

-------------------------------------------------------

## Instalar [`uv`](https://github.com/astral-sh/uv)

`uv` es un manejador de proyectos moderno, que permite configurar ambientes e instalar dependencias.

#### Linux

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

#### Windows:
```powershell
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

### Comandos de uv:

```bash
# Crear nuevo proyecto
uv init <nombre-proyecto>

# Agregar dependencias a proyecto
uv add <nombre-paquete>

# Ver opciones y subcomandos
uv -h
uv <comando> -h
```

> #### [Documentación de `uv`](https://docs.astral.sh/uv/)
