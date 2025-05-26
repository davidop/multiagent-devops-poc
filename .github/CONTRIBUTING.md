# Guía de Contribución

¡Gracias por tu interés en contribuir! Sigue estos pasos para enviar tu PR:

1. **Fork** y crea una rama `feature/<nombre>`.
2. Usa mensajes de commit estilo *Conventional Commits* (`feat:`, `fix:`…).
3. Asegúrate de que `make lint test` pasa antes de abrir PR.
4. Describe qué problema arreglas o funcionalidad añades.

## Entorno local rápido

```bash
git clone https://github.com/tu-usuario/multiagent-devops-poc
cd multiagent-devops-poc
make setup        # crea venv y deps
make start        # arranca funciones localmente
```

## Ejecución de pruebas

```bash
make test
```

## Estilo de código

- `black` para formateo
- `flake8` para lint
- `pytest` para tests + `pytest-cov` para cobertura
