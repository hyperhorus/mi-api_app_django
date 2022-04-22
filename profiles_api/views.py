from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    """Test APIView"""

    def get(self, request, format=None):
        """Return a list of APIView features"""
        an_apiview = [
            'Lo primero',
            'lo segundo',
            'lo tercero',
            'y lo cuarto'
        ]

        return Response({'message': 'Hello!', 'an_apiview': an_apiview})