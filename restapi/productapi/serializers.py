    from rest_framework import serializers
    from .models import Member
    from .models import Period


    class MemberSerializer( serializers.ModelSerializer):
        tz = serializers.CharField()
        class Meta:
            model= Member
            fields = '__all__'

    class PeriodSerializer( serializers.ModelSerializer):
        class Meta:
            model= Period
            fields = ['start','end']
            depth =1