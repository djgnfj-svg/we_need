
from rest_framework import serializers

from needs.models import Needs

class NeedsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Needs
		fields = "__all__"