from rest_framework import serializers
from duck_salle.models import Reservation
from duck_utils.models import Salle


class SalleSerializer(serializers.HyperlinkedModelSerializer):
    # pk = serializers.IntegerField(read_only=True)
    # label = serializers.CharField(max_length=120)
    #
    # def create(self, validated_data):
    #     return Salle.objects.create(**validated_data)
    #
    # def update(self, instance, validated_data):
    #     instance.label = validated_data.get('label', instance.title)
    class Meta:
        model = Salle
        fields = ('id', 'label', 'url')

class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    # salle = serializers.HyperlinkedRelatedField(view_name='duck_salle_salles',
    #                                             read_only=True)
    class Meta:
        model = Reservation


# class ReservationSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Reservation
#         depth = 1