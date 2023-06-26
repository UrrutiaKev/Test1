from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
import requests
 
from  models import Jurisprudencia

def buscar_jurisprudencias(request):
    try:
        # Obtener los datos de la petición POST
        id = request.POST.get('id')
        tipoCausa = request.POST.get('tipoCausa')
        rol = request.POST.get('rol')
        caratula = request.POST.get('caratula')
        nombreProyecto = request.POST.get('nombreProyecto')
        fechaSentencia = request.POST.get('fechaSentencia')
        descriptores = request.POST.get('descriptores')
        linkSentencia = request.POST.get('linkSentencia')
        urlSentencia = request.POST.get('urlSentencia')

        # Realizar la petición POST
        url = "https://www.buscadorambiental.cl/buscador-api/jurisprudencias/list"
        data = {
            "id": id,
            "tipoCausa": tipoCausa,
            "rol": rol,
            'caratula' : caratula,
            'nombreProyecto' : nombreProyecto,
            'fechaSentencia' : fechaSentencia,
            "descriptores": descriptores,
            "linkSentencia" : linkSentencia,
            "urlSentencia" : urlSentencia
        }
        headers = {
            "Content-Type": "application/json"
        }
        response = requests.post(url, json=data, headers=headers)
        print(response.content)

        # Verificar si la respuesta es válida
        if response.status_code != 200:
            raise Exception("La solicitud no se pudo completar correctamente")

        # Obtener la información de la respuesta
        informacion_respuesta = obtener_informacion_peticion(response)

        # Guardar la información en el modelo
        jurisprudencia = Jurisprudencia(
            id=informacion_respuesta['id'],
            tipoCausa=informacion_respuesta['tipoCausa'],
            rol=informacion_respuesta['rol'],
            caratula=informacion_respuesta['caratula'],
            nombreProyecto=informacion_respuesta['nombreProyecto'],
            fechaSentencia=informacion_respuesta['fechaSentencia'],
            descriptores=informacion_respuesta['descriptores'],
            linkSentencia=informacion_respuesta['linkSentencia'],
            urlSentencia=informacion_respuesta['urlSentencia']
        )
        jurisprudencia.save()

        # Obtener las jurisprudencias desde el modelo
        jurisprudencias = Jurisprudencia.objects.all()
        # Renderizar la plantilla y pasar los datos necesarios
        
        return render(request, 'buscar_jurisprudencias.html', {'resultados': jurisprudencias})


         
         

    except Exception as e:
        # Si ocurre un error, devolver un mensaje de error en formato JSON
        return JsonResponse({"error": str(e)})

def obtener_informacion_peticion(response):
    # Utilice el método "json()" del objeto de respuesta para convertir el cuerpo de la respuesta en formato JSON en un objeto de Python
    data = response.json()
    print(data)
    # Devuelva el objeto de Python que contiene la información extraída de la respuesta
    return data
