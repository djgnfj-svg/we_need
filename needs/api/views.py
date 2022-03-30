
from  rest_framework import viewsets
from needs.api.serializers import NeedsSerializer

from needs.models import Needs

class NeedsViewsSet(viewsets.ModelViewSet):
	queryset = Needs.objects.filter()
	serializer_class = NeedsSerializer