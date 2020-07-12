from rest_framework.serializers import (IntegerField,CharField,Serializer)
from notes.models import Note

class NoteSerializer(Serializer):
    id = IntegerField(read_only=True)
    title = CharField(required=True, max_length=250)
    text = CharField(required=False,allow_blank=True)

    def create(self, validate_data):
        return Note.objects.create(**validate_data)

    def update(self, instance, validate_data):
        print('instance', instance)
        print('validate_data', validate_data)        
        instance.title = validate_data.get('title',instance.title)
        instance.text = validate_data.get('text',instance.text)
        instance.save()
        return instance
