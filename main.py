from indic_transliteration import sanscript
from enum import Enum
from typing import Literal, Union
from fastapi import Body, FastAPI , Query, Path
from pydantic import BaseModel, EmailStr, Field, HttpUrl
 


app = FastAPI()


def transliterate_to_roman(text, source_script):
#     # Define script mappings
    script_map = {
        'devanagari': sanscript.DEVANAGARI,
        'bengali': sanscript.BENGALI,
        "punjabi": sanscript.GURMUKHI,
        # Add other scripts as needed
    }
    roman_text = sanscript.transliterate(text, sanscript.DEVANAGARI, sanscript.ITRANS)
    corrected_text = correct_transliteration(roman_text)
    return corrected_text


def correct_transliteration(text):
    # Replace 'M' with 'n' where appropriate
    corrected_text = text.replace('M', 'n').lower()
    return corrected_text
