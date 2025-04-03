# Gestión de las redes familiares

Esta aplicación gestiona la red de relaciones falimiares de los funcionarios públicos de Chile, permitiendo actualizarla con nueva información desde las fuentes oficiales y generar outputs útiles.

# Instalación

- Instale Rancher Desktop (recomendado) o Docker Desktop.
- Instale [uv](https://docs.astral.sh/uv/getting-started/installation/)


# Ejecución

Levante la base de datos con 
```bash
docker-compose up -d neo4j
```

Ahora puede ejecutar la aplicación con

```bash
uv run main.py --help
```