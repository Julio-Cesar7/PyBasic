import pandas as pd

list1 = ["Luis", "Melgarejo", 10, 20, 30, 40]
list2 = ["Manuel", "Esteban", 40, 30, 20, 10]

col1 = "Empleado 1"
col2 = "Empleado 2"

data = pd.DataFrame({col1: list1, col2: list2})
data.to_excel('usuarios.xlsx', index=False)
