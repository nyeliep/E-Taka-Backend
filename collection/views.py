from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import EwasteRequest
from .serializer import EwasteRequestSerializer

class EwasteRequestViewSet(viewsets.ModelViewSet):
    queryset = EwasteRequest.objects.all()
    serializer_class = EwasteRequestSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(requester=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        new_status = request.data.get('status', instance.status)
        new_payment_status = request.data.get('payment_status', instance.payment_status)

        if new_status not in ['Pending', 'Processing', 'Completed']:
         return Response({'message': 'Invalid status value'}, status=status.HTTP_400_BAD_REQUEST)

        if new_status == 'Completed':
         new_payment_status = 'Paid'
        else:
         new_payment_status = 'Unpaid'


        instance.status = new_status
        instance.payment_status = new_payment_status
        instance.save()

        return Response(serializer.data)


    def delete(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.delete()
        return Response({"message": "EwasteRequest deleted successfully."},status=status.HTTP_204_NO_CONTENT)










