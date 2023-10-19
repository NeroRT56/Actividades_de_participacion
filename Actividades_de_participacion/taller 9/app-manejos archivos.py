class DatosMeteorologicos:
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo = nombre_archivo

    def procesar_datos(self) -> tuple[float, float, float, float, str]:
        temperaturas_leidas = []
        humedades_leidas = []
        presiones_leidas = []
        vientos_leidos = []

        with open("datos.txt", "r") as archivo:
            
            for linea in archivo:
                #temperatura
                if linea.startswith("Temperatura: "):
                    linea = float(linea[13:17])
                    temperaturas_leidas.append(linea)
                    suma = sum(temperaturas_leidas)
                    temperatura_promedio = suma/len(temperaturas_leidas)

                #humedad
                elif linea.startswith("Humedad: "):
                    linea = float(linea[9:13])
                    humedades_leidas.append(linea)
                    suma = sum(humedades_leidas)
                    humedad_promedio = suma/len(humedades_leidas)

                #presion
                elif linea.startswith("Presion: "):
                    linea = float(linea[8:15])
                    presiones_leidas.append(linea)
                    suma = sum(presiones_leidas)
                    presion_promedio = suma/len(presiones_leidas)
                
                #viento
                elif linea.startswith("Viento: "):
                    linea = linea.replace(",", " ")
                    linea = float(linea[8:12])
                    vientos_leidos.append(linea)
                    suma = sum(vientos_leidos)
                    viento_promedio = suma/len(vientos_leidos)

                elif linea.startswith("Viento: "):
                        puntos_cardinales = {
        'N': 0,
        'NNE': 22.5,
        'NE': 45,
        'ENE': 67.5,
        'E': 90,
        'ESE': 112.5,
        'SE': 135,
        'SSE': 157.5,
        'S': 180,
        'SSW': 202.5,
        'SW': 225,
        'WSW': 247.5,
        'W': 270,
        'WNW': 292.5,
        'NW': 315,
        'NNW': 337.5
    }

    

            print(f"La temperatura promedio es {temperatura_promedio}")
            print(f"La humedad promedio es de {humedad_promedio}")
            print(f"La presión promedio es de {presion_promedio}")
            print(f"El viento promedio es de {viento_promedio}")



DatosMeteorologicos.procesar_datos("datos.txt")