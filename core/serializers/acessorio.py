from rest_framework.serializers import ModelSerializer

from core.models import Acessorio

class AcessorioSerializer(ModelSerializer):
    class Meta:
        models = Acessorio
        fields = "__all__"