from .models import *
from rest_framework import serializers, fields



class AlbumSerializer(serializers.ModelSerializer):
    
    #artist=serializers.CharField( source='artist.first_name'  ,read_only=True)

    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_date', 'num_stars',)


class MusicianSerializer(serializers.ModelSerializer):
    album_musician = AlbumSerializer(read_only=True, many=True)
    
    
    

    class Meta:
        model = Musician
        fields = ('id', 'first_name', 'last_name', 'instrument','album_musician')
        
    
        def update(self,instance,**validated_data):
            instance=self.first_name(instance.first_name,validated_data)
            instance=self.last_name(instance.last_name,validated_data)
            instance=self.instrument(instance.instrument,validated_data)
            instance.save()
    
    

from .models import Question

class ChoiceSerializers(serializers.ModelSerializer):
    id=serializers.IntegerField(required=False)
    class Meta:
        model=Choice
        fields="__all__"
        read_only_fields=('question',)

class QuestionSerializers(serializers.ModelSerializer):
    choices = ChoiceSerializers( many=True)
    #question=serializers.SerializerMethodField('question')
    class Meta:
        model=Question
        fields=['id','title','status','created_by','start_date','end_date','choices']
        
    def create(self, validated_data):
        choices = validated_data.pop('choices')
        #tags = validated_data.pop('tags')
        question = Question.objects.create(**validated_data)
        for choice in choices:
            Choice.objects.create(**choice, question=question)
        #question.tags.set(tags)
        return question
    
    def update(self, instance, validated_data):
        choices = validated_data.pop('choices')
        instance.title = validated_data.get("title", instance.title)
        instance.save()
        keep_choices = []
        #existing_ids=[c.id for c in instance.choices]
        for choice in choices:
            if "id" in choice.keys():
                if Choice.objects.filter(id=choice["id"]).exists():
                    c = Choice.objects.get(id=choice["id"])
                    c.text = choice.get('text', c.text)
                    c.save()
                    keep_choices.append(c.id)
                else:
                    continue
            else:
                c = Choice.objects.create(**choice, question=instance)
                keep_choices.append(c.id)

        for choice in instance.choices.all():
            if choice.id not in keep_choices:
                choice.delete()
        return instance



class QuestionListSerializer(serializers.ModelSerializer):
      class Meta:
          model=Question
          fields="__all__"
        

        
        
        



class ModulesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'module_name', 'description','module_duaration', 'class_room']


class StudentsSerializer(serializers.ModelSerializer):
    #student_module=ModulesSerializer()
    
    class Meta:
        model = Student
        fields = ['id', 'name', 'grade', 'modules',]
        depth = 1  
        
   