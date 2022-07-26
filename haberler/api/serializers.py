from rest_framework import serializers
from haberler.models import Makale, Gazeteci
from datetime import datetime, date
from django.utils.timesince import timesince


class MakaleSerializer(serializers.ModelSerializer):
        time_since_publication = serializers.SerializerMethodField()
        # yazar = serializers.StringRelatedField()
        # yazar = GazeteciSerializer()
        class Meta:
            model = Makale
            fields = "__all__"
  
        def get_time_since_publication(self, obj):
            now = datetime.now()
            pub_date = obj.yayımlanma_tarihi
            if obj.aktif == True:
                return timesince(pub_date, now)
            else:
                return "Makale yayımlanmamış"
        
        def validate_yayımlanma_tarihi(self, value):
            if value > date.today():
                raise serializers.ValidationError("Yayımlanma tarihi bugünden ileride olamaz")
            return value

class GazeteciSerializer(serializers.ModelSerializer):
    # makaleler = MakaleSerializer(many=True, read_only=True)
    makaleler = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name="makale-detail") 
    class Meta:
        model = Gazeteci
        fields = '__all__'



#############################################################################################
class MakaleDefaultSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    yazar = serializers.CharField()
    baslik = serializers.CharField()
    acıklama = serializers.CharField()
    metin = serializers.CharField()
    sehir = serializers.CharField()
    yayımlanma_tarihi = serializers.DateField()
    aktif = serializers.BooleanField()
    yaratilma_tarihi = serializers.DateTimeField(read_only=True)
    guncelleme_tarihi = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        return Makale.objects.create(**validated_data)


    def update(self, instance, validated_data):
        instance.yazar = validated_data.get('yazar', instance.yazar)
        instance.baslik = validated_data.get('baslik', instance.baslik)
        instance.acıklama = validated_data.get('acıklama', instance.acıklama)
        instance.metin = validated_data.get('metin', instance.metin)
        instance.sehir = validated_data.get('sehir', instance.sehir)
        instance.yayımlanma_tarihi = validated_data.get('yayımlanma_tarihi', instance.yayımlanma_tarihi)
        instance.aktif = validated_data.get('aktif', instance.aktif)
        instance.save()
        return instance

    def validate(self, data):
        if data['baslik'] == '':
            raise serializers.ValidationError("Başlık boş olamaz")
        return data
    
    def validate_yazar(self, value):
        if len(value) < 3:
            raise serializers.ValidationError("Yazar uzun olmalı")
        return value
        