from rest_framework import serializers
from .models import Note,Writer

class NoteSummarySerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField()

    class Meta:
        model = Note
        fields = ['id', 'heading', 'created_at', 'writer']

class NoteDetailSerializer(serializers.ModelSerializer):
    writer = serializers.StringRelatedField()

    class Meta:
        model = Note
        fields = ['id', 'heading', 'description', 'created_at', 'writer']



class NoteCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['heading', 'description']

class WriterSerializer(serializers.ModelSerializer):
    user_id=serializers.IntegerField(read_only=True)
    class Meta:
        model =Writer 
        fields = ['id','user_id','phone','birth_date']