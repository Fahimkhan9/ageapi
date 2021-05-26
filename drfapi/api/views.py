
from rest_framework.response import Response
import datetime
from .serializer import AgeSerializer
from rest_framework.decorators import api_view
# Create your views here.

@api_view(['GET'])
def home(request):
    routes = [
        'api/getage/<int:day>/<int:month>/<int:year>'
    ]
    return Response(routes)

@api_view(['GET'])
def getage(request,day,month,year):
    td=datetime.datetime.now().date()
    print(td)
    bd=datetime.date(year,month,day)
    age_years=int((td-bd).days /365.25)
    age= {
            "age":age_years
        }
    
    results =AgeSerializer(age,many=False)
    print((results))
    return Response(results.data)

