from rest_framework import serializers

from .models import Iha, Kiralama, Profil


class ProfilSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    foto = serializers.ImageField(read_only=True)

    class Meta:
        model = Profil
        fields = '__all__'


class ProfilFotoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profil
        fields = ['foto']


class IhaSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Iha
        fields = '__all__'

    def get_actions(self, instance):
        return ["Düzenle", "Sil", "Kirala"]


class KiralamaSerializer(serializers.ModelSerializer):
    actions = serializers.SerializerMethodField(read_only=True)
    uye_string = serializers.SerializerMethodField(read_only=True)
    iha_string = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Kiralama
        fields = '__all__'

    def get_actions(self, instance):
        return ["Düzenle", "Sil"]

    def get_uye_string(self, instance):
        return str(instance.uye)

    def get_iha_string(self, instance):
        return str(instance.iha)
