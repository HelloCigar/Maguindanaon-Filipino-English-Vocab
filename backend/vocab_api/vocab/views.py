from typing import List
from django.shortcuts import render
from django.db.models import Q

# Create your views here.

from ninja import NinjaAPI, Schema
from .models import Translation

api = NinjaAPI()

class TranslationSchema(Schema):
    english: str
    filipino: str
    maguindanaon: str

class Error(Schema):
    error: str


@api.get("/translate", response={200: List[TranslationSchema], 404: Error})
def translate_word(request, word: str):
    try:
        # get all related translations
        translation = Translation.objects.filter(Q(english__icontains=word) | Q(filipino__icontains=word) | Q(maguindanaon__icontains=word))
        return 200, translation
    except AttributeError:
        return 404, {"error": "Word not found"}
