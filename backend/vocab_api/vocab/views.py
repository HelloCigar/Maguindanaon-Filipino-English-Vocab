from typing import List
from django.shortcuts import render
from django.db.models import Q
from django.db.utils import IntegrityError

# Create your views here.

from ninja import NinjaAPI, Schema
from ninja.pagination import paginate, PageNumberPagination
from .models import Translation

api = NinjaAPI()

class TranslationSchema(Schema):
    english: str
    filipino: str
    maguindanaon: str

class Error(Schema):
    error: str

@api.get("/translate", response=List[TranslationSchema])
@paginate(PageNumberPagination, page_size=50)
def translate_word(request, word: str):
    try:
        # get all related translations
        translation = Translation.objects.filter(Q(english__icontains=word) | Q(filipino__icontains=word) | Q(maguindanaon__icontains=word))
        #arrange words alphabetically by maguindanaon
        translation = sorted(translation, key=lambda x: x.maguindanaon)
        
        #filter by approved
        translation = list(filter(lambda x: x.approved, translation))

        return translation
    except AttributeError:
        return 404, {"error": "Word not found"}
    
class SuccessSchema(Schema):
    success: bool
    message: str = None


@api.post("/add_word", response={200: SuccessSchema, 200: SuccessSchema})
def add_word(request, translation: TranslationSchema):
    try:
        new_translation = Translation(english=translation.english, filipino=translation.filipino, maguindanaon=translation.maguindanaon)        
        new_translation.save()
        return 200, {"success": True, "message": "Word submitted and will be evaluated. Thank you for your contribution!"} 
    except IntegrityError:
        return 200, {"success": False, "message": "Sorry, the word already exists"}
