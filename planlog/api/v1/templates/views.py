from rest_framework import generics, permissions, pagination
from planlog.models.template import Template
from .serializers import TemplateListSerializer


class TemplateListPagination(pagination.PageNumberPagination):
    page_size = 20
    max_page_size = 30
    page_size_query_param = 'page_size'


class TemplateListView(generics.ListAPIView):
    serializer_class = TemplateListSerializer
    queryset = Template.objects.filter(is_active=True)
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = TemplateListPagination