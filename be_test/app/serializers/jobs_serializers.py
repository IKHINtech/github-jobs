from rest_framework import serializers
from be_test.app.models import Jobs
from be_test.app.services.backend_services import BackendService
from rest_framework.serializers import ValidationError


class JobsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Jobs
        fields = '__all__'

    def get_all(self):
        service = BackendService()
        service.get_all()
        return

    def retrieve(self, id):
        try:
            job = Jobs.objects.get(id=id)
        except Jobs.DoesNotExist:
            raise ValidationError({"data: not found"}, 404)
        return job
