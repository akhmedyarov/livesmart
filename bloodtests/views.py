from rest_framework.response import Response
from rest_framework import status
from rest_framework import mixins
from rest_framework import generics

from .models import Test
from .serializers import TestSerializer


class TestDetails(mixins.RetrieveModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):

    lookup_field = 'code'
    queryset = Test.objects.all()
    serializer_class = TestSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create_or_update(request, *args, **kwargs)

    def create_or_update(self, request, *args, **kwargs):
        test = Test.objects.filter(code=request.data['code']).first()
        if not test:
            serializer = self.get_serializer(data=request.data)
        else:
            serializer = TestSerializer(test, data=request.data)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
