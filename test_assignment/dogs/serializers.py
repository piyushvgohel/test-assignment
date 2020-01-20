from rest_framework import serializers

from dogs.models import Breed, Dog

class BreedSerializer(serializers.ModelSerializer):

    def validate(self, data):
        """
        Check validattion.
        """
        if not(data['friendliness'] >=1 and data['friendliness']<=5):
            raise serializers.ValidationError("friendliness value shouls be between [1 - 5]")
        elif not(data['trainability'] >=1 and data['trainability']<=5):
            raise serializers.ValidationError("trainability value shouls be between [1 - 5]")
        elif not(data['shedding_amount'] >=1 and data['shedding_amount']<=5):
            raise serializers.ValidationError("shedding_amount value shouls be between [1 - 5]")
        elif not(data['exercise_needs'] >=1 and data['exercise_needs']<=5):
            raise serializers.ValidationError("exercise_needs value shouls be between [1 - 5]")
        return data


    class Meta:
        model = Breed
        fields = "__all__"


class DogSerializer(serializers.ModelSerializer):
    breed = serializers.SlugRelatedField(slug_field='uuid', 
                                        queryset=Breed.objects.all(), 
                                        allow_null=True)

    class Meta:
        model = Dog
        fields = "__all__"
