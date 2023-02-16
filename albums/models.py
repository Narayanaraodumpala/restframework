from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Musician(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    instrument = models.CharField(max_length=100)
    is_active=models.BooleanField(default=False,null=True)

    def __str__(self):
        return self.first_name


class Album(models.Model):
    artist = models.ForeignKey(Musician, on_delete=models.CASCADE, related_name='album_musician', null=True, blank=True)
    name = models.CharField(max_length=100)
    release_date = models.DateField()
    num_stars = models.IntegerField()
    date=models.DateTimeField(auto_now_add=True,null=True)
    
    def __str__(self):
        return self.name
    

    
    
    
from django.db import models

from django.contrib.auth.models import User


class ObjectTracking(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,null=True)
    updated_at = models.DateTimeField(auto_now=True,null=True)

    class Meta:
        abstract = True
        ordering = ('-created_at',)

# Create your models here.

# def validate_file_extension(value):
#     import os
#     from django.core.exceptions import ValidationError
#     ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
#     valid_extensions = [ '.jpg', '.png', ]
#     if not ext.lower() in valid_extensions:
#         raise ValidationError('Unsupported file extension.')



#to allow only pdf file type


import os
import magic
from django.core.exceptions import ValidationError

def validate_is_pdf(file):
    valid_mime_types = ['application/pdf',]
    file_mime_type = magic.from_buffer(file.read(1024), mime=True)
    print('file_mime_type=',file_mime_type)
    if file_mime_type not in valid_mime_types:
        raise ValidationError('Unsupported file type.')
    valid_file_extensions = ['.pdf',]
    ext = os.path.splitext(file.name)[1]
    if ext.lower() not in valid_file_extensions:
        raise ValidationError('Unacceptable file extension.')
    
#to allow only pdf,jpg,png, jpeg  file types     
def validate_extension(file):
    valid_mime_types = ["application/pdf", "image/jpeg", "image/png", "image/jpg"]
    file_mime_type = magic.from_buffer(file.read(2048), mime=True) #  Changed this to 1024 to 2048

    if file_mime_type not in valid_mime_types:
        raise ValidationError("Unsupported file type.")

    valid_file_extensions = [".pdf", ".jpeg", ".png", ".jpg"]
    ext = os.path.splitext(file.name)[1]

    if ext.lower() not in valid_file_extensions:
        raise ValidationError("Unacceptable file extension.")

class Question(ObjectTracking):
    title = models.TextField(null=False, blank=False)
    status = models.CharField(default='inactive', max_length=10)
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)

    start_date = models.DateTimeField(null=True, blank=True)
    end_date = models.DateTimeField(null=True, blank=True)
    

    #tags = models.ManyToManyField(Tag)

    # comments = GenericRelation(Comment, related_query_name="question")

    # objects = QuestionManager()


    def __str__(self):
        return self.title

    @property
    def choices(self):
        return self.choice_set.all()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE,related_name='choices',null=True)
    text = models.TextField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    file = models.FileField(upload_to="documents/%Y/%m/%d", validators=(validate_extension,),null=True)

    def __str__(self):
        return self.text

    @property
    def votes(self):
        return self.answer_set.count()
    
    

      
      
class Module(models.Model) :
    module_name=models.CharField(max_length=30)
    description=models.CharField(max_length=300)   
    module_duaration = models.IntegerField()
    class_room = models.IntegerField()
    
    def __str__(self) :
          return self.module_name
          
        

class Student(models.Model):
      name=models.CharField(max_length=30)
      #status=models.BooleanField(default=False)
       
      grade = models.IntegerField()
      modules=models.ManyToManyField(Module,related_name='student_module')
      
      def __str__(self) :
          return self.name