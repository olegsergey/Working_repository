from rest_framework import serializers

from schooldatas.models import Schooldata


class SchooldataSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schooldata
        fields = ('id', 'title') 
        # fields = ('id', 
        #           'school_id',
        #           'year',
        #           'week',
        #           'month',
        #           'elect_eur',
        #           'elect_kwh',
        #           'heating_eur',
        #           'heating_kwh',
        #           'water_eur',
        #           'water_litres',
        #         )
