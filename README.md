# Guía 49 — Cierre del Proyecto de Datos + Git

## Descripción

Este proyecto consolida los datos de ventas de cuatro sucursales, realiza una limpieza básica de los datos, genera un archivo Excel consolidado y crea gráficos de análisis por categoría y vendedor.

## Estructura del proyecto

```text
victor-github/
├── data/
│   ├── sucursal_medellin.csv
│   ├── sucursal_bogota.xlsx
│   ├── sucursal_cali.csv
│   └── sucursal_barranquilla.xlsx
├── resultados/
│   ├── consolidado_limpio.xlsx
│   ├── grafico_categoria.png
│   └── grafico_vendedor.png
├── main.py
├── README.md
└── .gitignore
```

## Requisitos

Instalar las librerías necesarias:

```bash
pip install pandas openpyxl matplotlib
```

## Ejecución

Desde la carpeta principal del proyecto:

```bash
python main.py
```

El programa lee los archivos de `data/`, consolida la información, limpia datos repetidos y valores faltantes, guarda el Excel en `resultados/` y genera los dos gráficos.

## Preguntas de comprensión

### 1. ¿Qué hace `glob.glob()`?

`glob.glob()` busca archivos que coincidan con un patrón determinado y devuelve una lista con las rutas encontradas. En este proyecto se usa `glob.glob("data/sucursal_*.csv")` y `glob.glob("data/sucursal_*.xlsx")` para encontrar automáticamente los archivos de las sucursales sin tener que escribir cada nombre manualmente.

### 2. ¿Qué hace `pd.concat()`? ¿Por qué se ejecuta dos veces?

`pd.concat()` une varios DataFrames en uno solo. En este código se ejecuta primero para hacer una consolidación inicial de los datos y después de renombrar las columnas se vuelve a ejecutar para construir nuevamente el DataFrame consolidado usando las versiones actualizadas de los DataFrames dentro de `lista_informes`.

### 3. ¿Qué hace `enumerate()`? ¿Por qué se necesita aquí `(i)`?

`enumerate()` permite recorrer una lista obteniendo al mismo tiempo la posición y el elemento. Aquí `i` representa la posición del DataFrame dentro de `lista_informes` y permite reemplazar directamente ese elemento con el DataFrame que tiene las columnas renombradas mediante `lista_informes[i] = ...`.

### 4. ¿Qué hace `drop_duplicates()`? ¿Qué hace `fillna()`?

`drop_duplicates()` elimina filas que están repetidas en el DataFrame. `fillna()` reemplaza los valores faltantes (`NaN`) por el valor indicado. En este proyecto se usa para colocar `"No especificado"` cuando falta el método de pago y para reemplazar precios faltantes por el promedio de los precios disponibles.

### 5. ¿Qué hace `groupby()`? ¿Cuál es la diferencia entre el gráfico de barras y el de torta, cuándo usar cada uno?

`groupby()` agrupa los datos según una columna y permite realizar operaciones sobre cada grupo. En este proyecto se usa para agrupar las ventas por categoría y por vendedor.

El gráfico de barras sirve para comparar cantidades o valores entre diferentes categorías y facilita ver qué grupo tiene un valor mayor o menor. El gráfico de torta representa partes de un total y es útil para mostrar porcentajes o participación. Por eso las barras son apropiadas para comparar categorías, mientras que la torta es útil para visualizar la participación de cada vendedor en el total.

## Git

Configuración inicial sugerida:

```bash
git config user.name "Tu Nombre"
git config user.email "tu-correo"
```

Comandos indicados en la guía:

```bash
git status
git init
git add .
git commit -m "primer commit - proyecto completo"
git remote add origin [URL]
git branch -M main
git push -u origin main
```

## Entrega

La guía solicita:

- Pantallazo de los gráficos generados.
- Pantallazo de `git log --oneline`.
- Link del repositorio de GitHub.
