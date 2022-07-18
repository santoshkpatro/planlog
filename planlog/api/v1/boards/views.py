from django.db import transaction, IntegrityError
from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from planlog.models.board import Board
from planlog.models.member import Member
from .serializers import BoardListSerializer, BoardCreateSerializer


class BoardListCreateView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        boards = Board.objects.filter(user=request.user)
        board_serializer = BoardListSerializer(boards, many=True)
        return Response(data=board_serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = BoardCreateSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(data={'detail': 'Invalid board details'}, status=status.HTTP_400_BAD_REQUEST)
        try:
            with transaction.atomic():
                board = serializer.save(user=request.user)
                Member.objects.create(board=board, user=board.user)

            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response(data={'detail': 'Something went wrong while creating board'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        
