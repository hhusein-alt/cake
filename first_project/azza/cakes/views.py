from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from .serializers import CakeSerializer, CakePreviewSerializer
from .models import Cake
from .error_messages import CAKE_CREATE_SUCCESS_MESSAGE


class CakeAPIView(APIView):
    def get(self, request):
        queryset = Cake.objects.filter(is_active=True)
        serializer = CakePreviewSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = CakeSerializer(data=request.data)

        if serializer.is_valid():
            cake = serializer.save(user=request.user)

            return Response(
                {
                    "message": CAKE_CREATE_SUCCESS_MESSAGE,
                    "cake_id": cake.id
                },
                status=status.HTTP_201_CREATED
            )

        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )


class CakeDetailsAPIView(APIView):
    def get(self, request, cake_id):
        """Get detail info about Cake by its id."""
        cake = get_object_or_404(Cake, pk=cake_id)
        serializer = CakeSerializer(cake)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, cake_id):
        """Entirely updates the cake (all fields)."""
        cake = get_object_or_404(Cake, pk=cake_id)
        serializer = CakeSerializer(cake, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cake updated successfully"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def patch(self, request, cake_id):
        """Partially updates the cake (few fields)."""
        cake = get_object_or_404(Cake, pk=cake_id)
        serializer = CakeSerializer(cake, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Cake updated successfully"},
                status=status.HTTP_200_OK
            )

        return Response(
            {"errors": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, cake_id):
        """Delete cake by id."""
        data = request.data

        cake = get_object_or_404(Cake, pk=cake_id)

        return Response(
            {"message": "Yox qardaw bele gedesi deyil!"},
            status=status.HTTP_403_FORBIDDEN
        )
