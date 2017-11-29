import json
import requests

archivo = open("config.json")
config = json.load(archivo)
urlBase = config["url_base"]
headers = config["request_headers"]
row_format = config["row_format"]
id_empresa = config["id_empresa"]
archivo_salida = config["output_filename"]
data = json.dumps(config["request_body"])

for rut in config["ruts"]:
    url = urlBase.format(rut_empresa=rut)
    respuesta = requests.post(url, data=data, headers=headers)
    r = respuesta.json()

    with open(archivo_salida, "a") as csvfile:
        fila = row_format.format(id=id_empresa,
                                 r=r["RUT"],
                                 rs=r["RazonSocial"],
                                 g=r["Giro"],
                                 d=r["Direccion"],
                                 num_res=r["NumeroResolucion"],
                                 fec_res=r["FechaResolucion"])
        print(fila)
        csvfile.write(fila)

print("Proceso finalizado")
