# RomanTranslation 

Api For RomanTranslation (word to word)
note : For first response it may take upto 50sec 
access using query

https://romantranslation.onrender.com/transliterate/?text=ਨਮਸਤੇ
  
response:  ->>>>   

{
  "transliterated_text":"namaste",
  "detected_language":"pa"
}


access using requestBody 

curl -X 'POST' \
  'https://romantranslation.onrender.com/transliterate/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "text": "नमस्ते"
}'
