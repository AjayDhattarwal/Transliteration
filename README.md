# RomanTranslation 

Api For RomanTranslation (word to word)

access using query

https://romantranslation.onrender.com/transliterate/?language=pa&text=ਨਮਸਤੇ
  
response:  ->>>>   

{
  "transliterated_text": "namasate"
}


access using requestBody 

curl -X 'POST' \
  'https://romantranslation.onrender.com/transliterate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "नमस्ते",
  "language": "hi"
}'
