from tabulate import tabulate

items = [
    {"nombre": "Café", "precio": 1.50},
    {"nombre": "Pan", "precio": 0.90},
    {"nombre": "Transporte", "precio": 2.80},
]

def crear_gasto(nombre: str, precio: float) -> dict:
    if not nombre or precio < 0:
        raise ValueError("Datos no váñido para crear el gasto")
    return {"nombre": nombre, "precio": precio}

if __name__ == "__main__":
    print("Lista de gastos:")
    print(tabulate(items, headers="keys", tablefmt="grid"))
