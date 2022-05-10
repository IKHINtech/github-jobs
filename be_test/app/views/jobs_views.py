from rest_framework import filters, viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from be_test.app.filters.jobs_filtes import JobsFilter

from be_test.app.models import Jobs
from be_test.app.serializers.jobs_serializers import JobsSerializers


class JobsViewsSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    # filterset_fields = '__all__'
    filter_class = JobsFilter

    serializer_class = JobsSerializers
    http_method_names = ['get']
    queryset = Jobs.objects.all()
    search_fields = ['location', 'description', 'title', 'company']

    def get_queryset(self):
        serializer = self.get_serializer()
        serializer.get_all()
        queryset = Jobs.objects.all()
        fulltime = 'full_time' in self.request.query_params
        if fulltime:
            if self.request.query_params.get('full_time') == 'true':
                queryset = Jobs.objects.filter(type__iexact='Full Time')

        return queryset

    # def list(self, request, *args, **kwargs):
    #     self.filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    #     self.filter_class = JobsFilter
    #     serializer = self.get_serializer()
    #     queryset = serializer.get_all()
    #     page = self.paginate_queryset(queryset)
    #     if page is not None:
    #         serializer = self.get_serializer(page, many=True)
    #         return self.get_paginated_response(serializer.data)
    #     serializer = self.get_serializer(queryset, many=True)
    #     return Response(serializer.data)

    def retrieve(self, request, pk=None):
        serializer = self.get_serializer()
        queryset = serializer.retrieve(id=pk)
        serializer = self.get_serializer(queryset)
        return Response(serializer.data)
