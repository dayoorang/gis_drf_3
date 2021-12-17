from rest_framework import serializers

from profileapp.models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    # owner = UserWithoutPasswordSerializer(read_only=True)

    class Meta:
        model = Profile
        fields = ['id','nickname','image','thumb','message','owner_id']