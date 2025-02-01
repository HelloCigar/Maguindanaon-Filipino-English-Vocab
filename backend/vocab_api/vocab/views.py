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
        #arrange words alphabetically by maguindanaon
        translation = sorted(translation, key=lambda x: x.maguindanaon)
        
        #filter by approved
        translation = list(filter(lambda x: x.approved, translation))

        return 200, translation
    except AttributeError:
        return 404, {"error": "Word not found"}
    
@api.post("/add_word", response={200: TranslationSchema, 400: Error})
def add_word(request, translation: TranslationSchema):
    try:
        new_translation = Translation(english=translation.english, filipino=translation.filipino, maguindanaon=translation.maguindanaon)        
        new_translation.save()
        return 200, new_translation
    except AttributeError:
        return 400, {"error": "Word already exists"}
