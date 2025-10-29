from rest_framework.views import Response, APIView, status

from .serializers import CakeSerializer, CakePreviewSerializer
from .models import Cake
from .error_messages import CAKE_NOT_FOUND_ERROR, CAKE_CREATE_SUCCESS_MESSAGE


class CakeAPIView(APIView):
    def get(self, request):
        queryset = Cake.objects.all()
        serializer = CakePreviewSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = CakeSerializer(data=data)

        if serializer.is_valid():
            cake = serializer.save()
            return Response({"message": CAKE_CREATE_SUCCESS_MESSAGE,
                             "cake_id": cake.id},
                             status=status.HTTP_201_CREATED)

        return Response({"errors": serializer.errors}, 
                         status=status.HTTP_400_BAD_REQUEST)


class CakeDetailsAPIView(APIView):
    def get(self, request, cake_id):
        cake = Cake.objects.filter(id=cake_id).first()
        if not cake:
            return Response({"message": CAKE_NOT_FOUND_ERROR},
                             status=status.HTTP_404_NOT_FOUND)

        serializer = CakeSerializer(cake)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # def patch(self, request, cake_id):
    #     return Response({"message": "Cake successfully updated!"})

    # def delete(self, request, cake_id):
    #     return Response({"message": "Cake successfully deleted!"})
