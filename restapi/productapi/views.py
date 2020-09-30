#from django.utils import simplejson
from rest_framework.decorators import APIView
from rest_framework.response import Response
from .models import Member
from .models import Period
from .serializers import MemberSerializer
from .serializers import PeriodSerializer
from rest_framework import status
from drf_multiple_model.views import ObjectMultipleModelAPIView
#from drf_multiple_model.views import FlatMultipleModelAPIView



class TextAPIView(ObjectMultipleModelAPIView):
  querylist = [
    {'queryset':Member.objects.all(), 'serializer_class': MemberSerializer},
    {'queryset': Period.objects.all(), 'serializer_class': PeriodSerializer},

  ]
'''
class TextAPIView(FlatMultipleModelAPIView):
  querylist = [
    {'queryset': Period.objects.all(), 'serializer_class': PeriodSerializer},
  ]'''










'''

class MemberListView(APIView):
  def get(self, request):
    Members = Member.objects.all()
    serializer = MemberSerializer(Members, many=True)
    return Response(serializer.data)

  def post(self, request):
    serializer = MemberSerializer(data=request.data)
    if (serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PeriodListView(APIView):
  def get(self, request):
    Periods = Period.objects.all()
    serializer = PeriodSerializer(Periods, many=True)
    return Response(serializer.data)

    # Deserialization(JSON TO MODEL)
  def post(self, request):
    serializer = PeriodSerializer(data=request.data)
    if (serializer.is_valid()):
      serializer.save()
      return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''
