
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from profiles_api import serializer

class HelloApiView(APIView):
    """Test APIView"""
    serializer_class = serializer.HelloSerializer

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Lo primero',
            'lo segundo',
            'lo tercero',
            'y lo cuarto'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})

    def post(self, request):
        """Create a hello message with our name """    
        serializer = self.serializer_class(data=request.data)
       
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f'Hello {name}'
            return Response({'message':message})
        else:
            return Response(
                serializer.errors, 
                status= status.HTTP_400_BAD_REQUEST               
                )

    def put(self, request, pk=None):
        """Method PUT"""
        return Response({'message':'Put your ligths on'})

    def patch(self, request, pk=None):
        """Method PATCH"""
        return Response({'message':'Patch your ass on'})  

    def delete(self, request, pk=None):
        """Method DELETE"""
        return Response({'message':'Delete my number!!'})      


class OtraPrueba(APIView):
    """Una prueba"""

    def get(self, request, format=None):
        """Regresa otra mamada"""
        una_lista_x = [
            'esta es la lista',
            'de lo que se prueba',
            'en esta pagina'
        ]

        return Response({'message': 'Me cachis', 'una_lista_x': una_lista_x})