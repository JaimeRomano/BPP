import csv
import matplotlib.pyplot as plt

# Verificar si el fichero existe y se puede abrir
try:
    with open('finanzas2020.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
except FileNotFoundError:
    print("El fichero no existe")
    # Manejar adecuadamente la excepción
except Exception as e:
    print("Error al abrir el fichero:", str(e))
    # Manejar adecuadamente la excepción

# Leer el contenido del fichero y verificar que tiene 12 columnas
try:
    with open('finanzas2020.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        headers = next(csv_reader)
        if len(headers) != 12:
            raise Exception("El fichero no tiene 12 columnas")
except Exception as e:
    print(str(e))
    # Manejar adecuadamente la excepción

# Verificar que cada mes tiene contenido
try:
    with open('finanzas2020.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # saltar la primera fila con los nombres de los meses
        for row in csv_reader:
            if len(row) != 12:
                raise Exception("El mes no tiene contenido")
except Exception as e:
    print(str(e))
    # Manejar adecuadamente la excepción

# Verificar que los datos son correctos
try:
    with open('finanzas2020.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        next(csv_reader)  # saltar la primera fila con los nombres de los meses
        for row in csv_reader:
            for value in row:
                try:
                    num = int(value)
                    if num < 0 and "Enero" in headers:  # para el caso de gastos, si hay una columna con el nombre "Enero"
                        continue
                    elif num < 0:
                        raise Exception("Valor negativo en columna de ingresos")
                except ValueError:
                    raise Exception("Valor no numérico en columna")
except Exception as e:
    print(str(e))
    # Manejar adecuadamente la excepción

# Cálculos y gráfica
    with open("finanzas2020.csv", "r") as f:
        reader = csv.reader(f)
        row1 = next(reader)
        gastos = []
        ingresos = []
        for i in range(12):
            gastos.append(0)
            ingresos.append(0)
        for row in reader:
            for i in range(12):
                val = float(row[i])
                if val < 0:
                    gastos[i] += val
                else:
                    ingresos[i] += val
        mes_gasto_max = row1[gastos.index(min(gastos))]
        mes_ahorro_max = row1[ingresos.index(max(ingresos))]
        media_gastos = sum(gastos) / 12
        gasto_total = sum(gastos)
        ingresos_total = sum(ingresos)
        plt.plot(row1[1:], ingresos[1:])
        plt.title("Evolución de ingresos en 2020")
        plt.xlabel("Mes")
        plt.ylabel("Ingresos")
        plt.show()
        print(f"Mes que se ha gastado más: {mes_gasto_max}")
        print(f"Mes que se ha ahorrado más: {mes_ahorro_max}")
        print(f"Media de gastos al año: {media_gastos:.2f}")
        print(f"Gasto total a lo largo del año: {gasto_total:.2f}")
        print(f"Ingresos totales a lo largo del año: {ingresos_total:.2f}")


