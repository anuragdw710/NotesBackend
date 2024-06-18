from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin,RetrieveModelMixin,DestroyModelMixin,UpdateModelMixin
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Note,Writer
from .serializers import NoteSummarySerializer, NoteDetailSerializer,WriterSerializer
from .permissions import IsAdminOrReadOnly

class NoteViewSet(ModelViewSet):
    permission_classes=[IsAuthenticated]

    def get_serializer_context(self):
        return {'user_id':self.request.user.id}

    def get_queryset(self):
        user=self.request.user
        if user.is_staff:
            return Note.objects.all()
        (writer_id,created)=Writer.objects.get_or_create(user_id=user.id)
        return Note.objects.filter(writer_id=writer_id.id)

    def get_serializer_class(self):
        if self.action == 'list':
            return NoteSummarySerializer
        return NoteDetailSerializer
        
class WriterViewSet(ModelViewSet):
    queryset = Writer.objects.all()
    serializer_class = WriterSerializer
    permission_classes=[IsAdminUser]


    @action(detail=False, methods=['GET','PUT'],permission_classes=[IsAuthenticated])
    def me(self,request):
        (writer,created)=Writer.objects.get_or_create(user_id=request.user.id)
        if request.method=='GET':
            serializer=WriterSerializer(writer)
            return Response(serializer.data)
        elif request.method=='PUT':
            serializer=WriterSerializer(writer,data=request.data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)