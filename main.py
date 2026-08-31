# ============================================
# BOT DE VENTAS - Script completo
# Guía 49: Cierre del Proyecto de Datos + Git
# ============================================

import glob

import matplotlib.pyplot as plt
import pandas as pd


# --------------------------------------------
# PARTE 1: Leer los archivos
# --------------------------------------------
archivos_csv = glob.glob("data/sucursal_*.csv")
archivos_xlsx = glob.glob("data/sucursal_*.xlsx")
lista_informes = []

for archivo in archivos_csv:
    df = pd.read_csv(archivo)
    lista_informes.append(df)

for archivo in archivos_xlsx:
    df = pd.read_excel(archivo, engine="openpyxl")
    lista_informes.append(df)

# PREGUNTA 1 (para su README): que hace glob.glob()?


# --------------------------------------------
# PARTE 2: Consolidar y renombrar columnas
# --------------------------------------------
if not lista_informes:
    raise FileNotFoundError(
        "No se encontraron archivos sucursal_*.csv o sucursal_*.xlsx dentro de data/."
    )

df_consolidado = pd.concat(lista_informes, ignore_index=True)

for i, df in enumerate(lista_informes):
    # enumerate da la posicion (i) y el contenido (df) a la vez
    if "Fecha_Venta" in df.columns:
        lista_informes[i] = df.rename(
            columns={
                "Fecha_Venta": "fecha",
                "Producto": "producto",
                "Categoria": "categoria",
                "Cant": "cantidad",
                "Valor_Unitario": "precio_unitario",
                "Vendedor": "vendedor",
                "Pago": "metodo_pago",
            }
        )

# Se vuelve a consolidar para incluir los DataFrames con las columnas renombradas.
df_consolidado = pd.concat(lista_informes, ignore_index=True)

# PREGUNTA 2: que hace pd.concat()? por que se ejecuta dos veces?
# PREGUNTA 3: que hace enumerate()? por que se necesita aqui (i)?


# --------------------------------------------
# PARTE 3: Limpieza
# --------------------------------------------
df_consolidado = df_consolidado.drop_duplicates()
df_consolidado["metodo_pago"] = df_consolidado["metodo_pago"].fillna("No especificado")
promedio_precio = df_consolidado["precio_unitario"].mean()
df_consolidado["precio_unitario"] = df_consolidado["precio_unitario"].fillna(
    promedio_precio
)

# PREGUNTA 4: que hace drop_duplicates()? que hace fillna()?

df_consolidado.to_excel("resultados/consolidado_limpio.xlsx", index=False)


# --------------------------------------------
# PARTE 4: Analisis y graficos
# --------------------------------------------
ventas_categoria = df_consolidado.groupby("categoria")["precio_unitario"].sum()
ventas_categoria.plot(kind="bar", title="Ventas por Categoria")
plt.tight_layout()
plt.savefig("resultados/grafico_categoria.png")
plt.show()
plt.close()

ventas_vendedor = df_consolidado.groupby("vendedor")["precio_unitario"].sum()
ventas_vendedor.plot(
    kind="pie", autopct="%1.1f%%", title="Participacion por Vendedor"
)
plt.tight_layout()
plt.savefig("resultados/grafico_vendedor.png")
plt.show()
plt.close()

# PREGUNTA 5: que hace groupby()? cual es la diferencia entre el
# grafico de barras y el de torta, cuando usar cada uno?

print("Proceso completo. Revisen la carpeta resultados/")
