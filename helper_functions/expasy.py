import http.client
import urllib.parse
import re

def translate(dna_sequence):
    url = "web.expasy.org"
    path = "/cgi-bin/translate/dna2aa.cgi"

    params = urllib.parse.urlencode({
        'dna_sequence': dna_sequence,
        'output_format': 'fasta'
    })

    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }

    conn = http.client.HTTPSConnection(url)

    conn.request("POST", path, params, headers)

    response = conn.getresponse()
    data = response.read().decode('utf-8')

    conn.close()

    # Remove lines that start with '>'
    filtered_data = re.sub(r'>.*\n?', '', data)

    # Remove any remaining line breaks and join everything into a single string
    single_string = ''.join(filtered_data.splitlines())

    return single_string
