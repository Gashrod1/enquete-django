from django.contrib import admin

from .models import Question, Choice

# Register your models here.
from django.contrib import admin
from .models import Question, Choice


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    # Colonnes affichées dans la liste
    list_display = ("question_text", "pub_date")

    # Ajout d’un filtre temporel sur la date de publication
    list_filter = ("pub_date",)

    # Ajout d’une barre de recherche
    search_fields = ("question_text",)


@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    # Colonnes affichées
    list_display = ("choice_text", "votes", "question")

    # Filtrer par question liée
    list_filter = ("question",)

    # Recherche par texte de choix ou question associée
    search_fields = ("choice_text", "question__question_text")
