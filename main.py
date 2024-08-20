from fastapi import Body, FastAPI , Query, Path, Request
from pydantic import BaseModel, EmailStr, Field, HttpUrl
from indic_transliteration import sanscript
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from langdetect import detect, DetectorFactory


app = FastAPI()


class TransliterationRequest(BaseModel):
    text: str
    language: str = None  

def detect_language(text: str) -> str:
    try:
        lang = detect(text)
        if lang == 'hi':
            return 'hi'
        elif lang == 'pa':
            return 'pa'
        # Add more mappings as needed
        else:
            return 'hi'  # Default to Hindi if unsure
    except:
        return 'hi'  # Default to Hindi on detection failure

def transliterate_to_roman(text: str, source_language: str) -> str:
    language_map = {
        'hi': sanscript.DEVANAGARI,
        'pa': sanscript.GURMUKHI,
        # Add other languages as needed
    }
    roman_text = sanscript.transliterate(text, language_map.get(source_language, ""), sanscript.ITRANS)
    corrected_text = correct_transliteration(roman_text)
    return corrected_text

def correct_transliteration(text: str) -> str:
    corrected_text = text.replace('M', 'n').lower()
    return corrected_text

def preprocess_text(text: str) -> str:
    if text.startswith('"') and text.endswith('"'):
        text = text[1:-1]
    return text

@app.post("/transliterate/")
async def transliterate(request: TransliterationRequest):
    processed_text = preprocess_text(request.text)
    source_language = request.language or detect_language(processed_text)
    result = transliterate_to_roman(processed_text, source_language)
    return {"transliterated_text": result, "detected_language": source_language}

@app.get("/transliterate/")
async def transliterate_query(text: str = Query(..., example="ਨਮਸਤੇ"),
                              language: str = Query(None)):
    source_language = language or detect_language(text)
    transliterated_text = transliterate_to_roman(text, source_language)
    return {"transliterated_text": transliterated_text, "detected_language": source_language}

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    errors = exc.errors()
    error_details = []
    for error in errors:
        loc = error.get("loc", [])
        if loc:
            field = loc[-1]
            error_details.append(f"Input field '{field}' is missing.")
    return JSONResponse(
        status_code=400,
        content={"detail": error_details},
    )

