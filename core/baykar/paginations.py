from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from collections import OrderedDict
from rest_framework.response import Response
class SmallPagination(PageNumberPagination):
    page_size = 25

class SmallOffsetPaginations(LimitOffsetPagination):
    default_limit = 25
    limit_query_param = 'length'
    offset_query_param = 'start'

    def get_paginated_response(self, data):
        return Response(OrderedDict([

            ('recordsTotal', self.count),
            ('recordsFiltered', self.count),
            ('draw', int(self.request.query_params.get("draw", 1))+1),
            ('length', self.limit),
            ('next', self.get_next_link()),
            ('previous', self.get_previous_link()),
            ('data', data)
        ]))

class MediumPagination(PageNumberPagination):
    page_size = 50

class LargePagination(PageNumberPagination):
    page_size = 100
