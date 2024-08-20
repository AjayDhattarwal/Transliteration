from indic_transliteration import sanscript
from enum import Enum
from typing import Literal, Union
from fastapi import Body, FastAPI , Query, Path
from pydantic import BaseModel, EmailStr, Field, HttpUrl
 


app = FastAPI()

class Language(str, Enum):
    hindi = "hi"
    punjabi = "pa"
    # Add other languages as needed

def transliterate_to_roman(text: str, source_Lang: Language) -> str:
    script_map = {
        Language.hindi: sanscript.DEVANAGARI,
        Language.punjabi: sanscript.GURMUKHI,
    }
    roman_text = sanscript.transliterate(text, script_map[source_script], sanscript.ITRANS)
    corrected_text = correct_transliteration(roman_text)
    return corrected_text

def correct_transliteration(text: str) -> str:
    corrected_text = text.replace('M', 'n').lower()
    return corrected_text

class TransliterationRequest(BaseModel):
    text: str = Field(..., example="नमस्ते")
    language: Language = Field(..., example="hi")

@app.post("/transliterate/")
async def transliterate(request: TransliterationRequest):
    transliterated_text = transliterate_to_roman(request.text, request.language)
    return {"transliterated_text": transliterated_text}


@app.get("/transliterate/")
async def transliterate_query(text: str = Query(..., example="ਨਮਸਤੇ"),
                              language: Language = Query(..., example="pa")):
    transliterated_text = transliterate_to_roman(text, language)
    return {"transliterated_text": transliterated_text}
