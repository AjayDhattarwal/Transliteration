# RomanTranslation 

Api For RomanTranslation (word to word)

access using query

https://romantranslation.onrender.com/transliterate/?text=ਨਮਸਤੇ
  
response:  ->>>>   

{
  "transliterated_text":"namaste",
  "detected_language":"pa"
}


access using requestBody 

curl -X 'POST' \
  'http://127.0.0.1:8000/transliterate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "नमस्ते"
}'
