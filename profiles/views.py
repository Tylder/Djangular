from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status

from .serializers import TeacherSerializer, StudentSerializer
from .models import TeacherProfile, StudentProfile

class TeacherViewSet(ModelViewSet):

    queryset = TeacherProfile.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (AllowAny,)

    filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
    search_fields = ('rank', 'base_salary', 'user__username')
    filter_fields = ('rank', 'user__username')
    #
    # def get_queryset(self):
    #
    #     queryset = TeacherProfile.objects.all()
    #     req_rank = self.request.query_params.get('rank', None)
    #     if req_rank is not None:
    #         queryset = queryset.filter(rank=req_rank)
    #
    #     return queryset

class StudentViewSet(ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
#
# class TeacherByRank(generics.ListAPIView):
#     serializer_class = TeacherSerializer
#     permission_classes = (AllowAny,)
#     model = TeacherProfile
# #     def get_queryset(self):
# #
# #         # queryset = TeacherProfile.objects.all()
# #         #
# #         # print('sesdsdsdsd',self.request.query_params)
# #         #
# #         # # req_rank = self.request.query_params.get('rank', None)
# #         # req_rank = self.kwargs['rank']
# #         # # if req_rank is not None:
# #         # queryset = queryset.filter(rank=req_rank)
# #         # return queryset
# #         user = self.request.user
#         return TeacherProfile.objects.filter(user=user)
# #
# @api_view(['POST'])
# def teachers_by_rank(request):
#
#     try:
#         teachers = TeacherProfile.objects.get(rank=request.data.get('rank'))
#     except:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     serializer = TeacherSerializer(data=request.data)
#     if serializer.is_valid():