import json
from .data_handling import data_extraction
from .plots import plot_graph, get_chart_as_image

from django.http import JsonResponse
from rest_framework.decorators import api_view
from django.http import HttpResponse


@api_view(['POST'])  #Post request to create the graphs
def plot(request):

    try:
        json_data = json.loads(request.body)
    except:
        return JsonResponse({'error': 'File is not valid JSON'}, status=422)

    ecg, ppg = data_extraction(json_data)
    plot = plot_graph(ecg, ppg)
    plot_image = get_chart_as_image(plot)
    return HttpResponse(plot_image, content_type='image/png')      # Return the graph as an image.

