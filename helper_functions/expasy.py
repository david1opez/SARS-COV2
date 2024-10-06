import http.client  # Libreria para realizar solicitudes HTTP
import urllib.parse  # Libreria para codificar parametros de la URL
import re  # Libreria para trabajar con expresiones regulares

# Funcion que envia una secuencia de ADN a un servidor para traducirla a proteinas
def translate(dna_sequence):
    # Definimos la URL base y el camino del recurso en el servidor que hara la traduccion
    url = "web.expasy.org"
    path = "/cgi-bin/translate/dna2aa.cgi"

    # Codificamos los parametros que se enviaran en la solicitud POST
    # 'dna_sequence' es la secuencia de ADN
    # 'output_format' especifica el formato de salida
    params = urllib.parse.urlencode({
        'dna_sequence': dna_sequence,
        'output_format': 'fasta'
    })

    # Definimos los encabezados de la solicitud, 
    # Aqui indicamos que el contenido es de tipo 'formulario'
    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }

    # Establecemos una conexion HTTPS con el servidor especificado en la variable 'url'
    conn = http.client.HTTPSConnection(url)

    # Enviamos una solicitud POST al servidor con el camino, los parametros y encabezados definidos
    conn.request("POST", path, params, headers)

    # Obtenemos la respuesta del servidor
    response = conn.getresponse()
    # Leemos y decodificamos el contenido de la respuesta
    data = response.read().decode('utf-8')

    # Cerramos la conexion
    conn.close()

    # Eliminamos cualquier linea que comience con '>', que normalmente son cabeceras en formato FASTA
    filtered_data = re.sub(r'>.*\n?', '', data)

    # Eliminamos cualquier salto de linea que quede y unimos todo en una sola cadena
    single_string = ''.join(filtered_data.splitlines())

    # Devolvemos la secuencia de proteinas como una sola cadena
    return single_string
