import django_filters
# from sohc_api.app.filters.list_filter import ListFilter
from be_test.app.models import Jobs


class JobsFilter(django_filters.FilterSet):
    # description = django_filters.Filter(field_name='description', lookup_expr='iexact')
    location = django_filters.CharFilter(field_name='location', lookup_expr='iexact')

    class Meta:
        model = Jobs
        fields = '__all__'
