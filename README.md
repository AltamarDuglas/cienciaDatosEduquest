# Proyecto de Inferencia Narrativa con IA

Este proyecto entrena un modelo para predecir el nivel de inferencia (literal, causal, crítica) de una historia narrativa, usando un dataset de ejemplos tipo Story Cloze Test.

## Estructura

- `/datos`: contiene el Excel con los datos de entrenamiento.
- `/modelo`: se guardan los modelos entrenados.
- `/api`: contiene un microservicio Flask para probar la inferencia.

## Uso

1. Entrena el modelo:
   ```
   python entrenar_modelo.py
   ```

2. Ejecuta la API:
   ```
   python api/microservicio_flask.py
   ```

3. Envía un texto como:
```json
{
  "texto": "Pedro se quedó callado durante la reunión... Estaba decepcionado con la decisión tomada."
}
```

Recibirás algo como:
```json
{ "nivel": 3 }
```
