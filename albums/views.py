# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework import filters


# Create your views here.


class MusicianListViewset(viewsets.ModelViewSet):
    queryset = Musician.objects.all()
    serializer_class = MusicianSerializer
    filter_backends =(DjangoFilterBackend,filters.OrderingFilter,filters.SearchFilter)
    filterset_fields=('is_active',)
    ordering_fields = ['first_name', ]
    ordering = ['first_name']
    search_fields = ['first_name', ]
    # def get_queryset(self):
    #     queryset=Musician.objects.all()
    #     active=self.request.query_params.get('is_active','')
    #     if active :
    #         if active=='False':
    #             active=False
    #         elif active=='True':
    #             active=True
    #         else:
    #             return queryset
    #         return queryset.filter(is_active=active)
    #     else:
    #         return queryset
            


# class MusicianView(generics.RetrieveUpdateDestroyAPIView):
#     serializer_class = MusicianSerializer
#     queryset = Musician.objects.all()


class AlbumListView(viewsets.ModelViewSet):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer


class AlbumView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = AlbumSerializer
    queryset = Album.objects.all()
    
from rest_framework.response import Response 
    
class UpdateMusicianView(generics.GenericAPIView):
    serializer_class=MusicianSerializer
    def put(self,pk,request):
        musican=Musician.objects.filter(id=pk)
        if musican:
            serializer = self.serializer_class(musican, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data,many=True)
        
        
        

# Create your views here.


class QuestionViewsets(viewsets.ModelViewSet):
    serializer_class=QuestionSerializers
    
    def get_queryset(self):
        queryset=Question.objects.all()
        return queryset
    
    # def get_serializer_class(self):
    #     if self.action == 'list':
            
    #        return QuestionListSerializer
    #     else:
    #         return QuestionSerializers
    
    
class ChoiceViewsets(viewsets.ModelViewSet):
    serializer_class=ChoiceSerializers
    
    # def get_queryset(self):
    #     queryset=Choice.objects.all()
    #     return queryset
    
    def get_queryset(self):
        queryset=Choice.objects.all()
        return queryset
    
    
    
    

class StudentsViewSet(viewsets.ModelViewSet):
    serializer_class = StudentsSerializer

    def get_queryset(self):
        student = Student.objects.all()
        return student

    def create(self, request, *args, **kwargs):
        data = request.data
        #print('status=',data.status)

        new_student = Student.objects.create(
            name=data["name"],  grade=data["grade"])

        new_student.save()
        moduledata=data['modules']
        print('modules=',moduledata)
        
        for module in moduledata:
            
               module_obj = Module.objects.get(module_name=module["module_name"])
               print('module_obj=',module_obj)
               new_student.modules.add(module_obj)
               serializer = StudentsSerializer(data=new_student)
               if serializer.is_valid():
                   serializer.save()
        return Response({'messgae':'Success'})
    
    
            
   
class ModulesViewSet(viewsets.ModelViewSet):
    serializer_class = ModulesSerializer

    def get_queryset(self):
        module = Module.objects.all()
        return module




        
# from dateutil.rrule import *
# from dateutil.parser import *
# from datetime import datetime        

# start_date = parse("20230209T000000 ")
# end_date=parse("20230430T235959")
# byday='+3MO,+3TU,+3WE,+3TH,+3FR,+3SA,+3SU'
# Mo=str('+3MO')
# TU=str('+3TU')

# # list(rrulestr("DTSTART;TZID=Asia/Kolkata:20230209T000000 RRULE:FREQ=YEARLY;BYSETPOS=3;BYDAY=+1MO;BYMONTH=1;COUNT=20"))
# list(rrulestr("""
# DTSTART:19970902T090000
# RRULE:FREQ=DAILY;INTERVAL=10;COUNT=5
# RRULE:FREQ=DAILY;INTERVAL=5;COUNT=3
# """))

# data=rrulestr("""
# DTSTART:19970902T090000
# RRULE:FREQ=DAILY;INTERVAL=10;COUNT=5
# RRULE:FREQ=DAILY;INTERVAL=5;COUNT=3
# """)

#list(rrule(freq=YEARLY, count=20, dtstart=start_date, byweekday=0,bysetpos=3, bymonth=1 ))
# set = rruleset()
# set.exrule(rrule(freq=YEARLY, byweekday=(rrule.MO,rrule.TU, rrule.WE,rrule.TH,rrule.FR,rrule.SA,rrule.SU),dtstart=start_date,bysetpos=3, bymonth=1),count=20)



# from dateutil.rrule import *
# my_rrule = rrule(DAILY, count=30)
# print(list(my_rrule))



# list(rrule(freq=YEARLY, count=20, byweekday=(rrule.MO,rrule.TU, rrule.WE,rrule.TH,rrule.FR,rrule.SA,rrule.SU) ,dtstart=start_date,bysetpos=3, bymonth=(1,) ))

        
    