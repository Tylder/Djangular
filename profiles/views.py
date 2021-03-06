from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework import permissions

from rest_framework import generics, filters
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.generics import CreateAPIView, RetrieveUpdateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

from .serializers import TeacherSerializer, StudentSerializer, LessonCreatorSerializer
from .models import TeacherProfile, StudentProfile, LessonCreator


class TeacherViewSet(ModelViewSet):
    """
       Reads and updates UserModel fields
       Accepts GET, PUT, PATCH methods.

       Default accepted fields: username, first_name, last_name
       Default display fields: pk, username, email, first_name, last_name
       Read-only fields: pk, email

       Returns UserModel fields.
       """
    queryset = StudentProfile.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = (IsAuthenticated,)
    #
    # def get_object(self):
    #     queryset = self.get

    def get_queryset(self):

        user = self.request.user
        return TeacherProfile.objects.filter(user=user)


#
# class TeacherViewSet(ModelViewSet):
#     queryset = TeacherProfile.objects.all()
#     serializer_class = TeacherSerializer
#     permission_classes = (IsAuthenticated,)
#
#     # filter_backends = (filters.SearchFilter, filters.DjangoFilterBackend)
#     # search_fields = ('rank', 'base_salary', 'user__username')
#     # # filter_fields = ('rank', 'user__pk')
#
#     # def list(self, request):
#     #     user = request.user
#     #     queryset = TeacherProfile.objects.filter(user=user)
#     #     serializer = TeacherSerializer(queryset)
#     #     return Response(serializer.data)
#
#         # queryset = TeacherProfile.objects.all()
#         # req_rank = self.request.query_params.get('rank', None)
#         # if req_rank is not None:
#         #     queryset = queryset.filter(rank=req_rank)
#         #
#         # return queryset


class StudentViewSet(ModelViewSet):
    queryset = StudentProfile.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):

        user = self.request.user
        return StudentProfile.objects.filter(user=user)
    #
    # class TeacherByRank(generics.ListAPIView):
    #     serializer_class = TeacherSerializer
    #     permission_classes = (AllowAny,)
    #     model = TeacherProfile
    #
    #     def get_queryset(self):
    #
    #         queryset = TeacherProfile.objects.all()
    #
    #         print('sesdsdsdsd',self.request.query_params)
    #
    #         # req_rank = self.request.query_params.get('rank', None)
    #         req_rank = self.kwargs['rank']
    #         # if req_rank is not None:
    #         queryset = queryset.filter(rank=req_rank)
    #         return queryset
    #         user = self.request.user
    #         return TeacherProfile.objects.filter(user=user)
    #
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


class LessonCreatorViewSet(ModelViewSet):
    queryset = LessonCreator.objects.all()
    serializer_class = LessonCreatorSerializer
    permission_classes = (AllowAny,)
