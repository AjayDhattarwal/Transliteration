
# Transliteration API

## Overview

The Transliteration API provides a service to convert text from one script to another while preserving its original pronunciation. This process is known as transliteration.

## Endpoints

### 1. Query Parameter Access

**GET** `https://romantranslation.onrender.com/transliterate/?text={ਨਮਸਤੇ}`

**Example Request:**


**Response:**

```json
{
  "transliterated_text": "namaste",
  "detected_language": "pa"
}

```


### 2. POST Request

`curl -X 'POST' \
  'https://romantranslation.onrender.com/transliterate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "नमस्ते"
}'`


**Response:**

```json
{
  "transliterated_text": "namaste",
  "detected_language": "hi"
}

```

## License

[MIT](https://github.com/AjayDhattarwal/Transliteration/blob/main/LICENSE)
