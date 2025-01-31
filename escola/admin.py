from django.contrib import admin
from escola.models import Estudante,Curso,Matricula

class Estudantes(admin.ModelAdmin):
    list_display = ('id','nome','email','data_nascimento','celular',)
    list_display_links = ('id','nome',)
    list_per_page = 10
    search_fields = ('nome',)
    
admin.site.register(Estudante, Estudantes)

class Cursos(admin.ModelAdmin):
    list_display = ('id','codigo','description',)
    list_display_links = ('id','codigo',)
    search_fields = ('codigo',)
    
admin.site.register(Curso,Cursos)

class Matriculas(admin.ModelAdmin):
    list_display = ('id','estudante','curso','periodo')
    list_display_links = ('id',)
    
admin.site.register(Matricula,Matriculas)