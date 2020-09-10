from rest_framework import generics, viewsets, mixins
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions

from board.api.serializers import BoardSerializer
from board.api.permissions import IsOwnerOrReadOnly
from board.api.pagination import SmallSetPagination

from board.models import Board


class BoardViewSet(viewsets.ModelViewSet):
    queryset = Board.objects.all().order_by('-id')
    serializer_class = BoardSerializer
    pagination_class = SmallSetPagination
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

    def partial_update(self, request, obj):
        if obj.user == request.user.username:
            if obj.password == request.user.password:
                serializer_class.save(owner=self.request.user)

    def destroy(self, request, obj):
        if obj.user == request.user.username:
            if obj.password == request.user.password:
                serializer_class.delete(owner=self.request.user)
