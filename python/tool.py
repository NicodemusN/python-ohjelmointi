import re

with open("slides.md", "r", encoding="utf-8") as f:
    text = f.read()

emoji_pattern = re.compile(
    "[\U0001F600-\U0001F64F"  # emoticons
    "\U0001F300-\U0001F5FF"  # symbols & pictographs
    "\U0001F680-\U0001F6FF"  # transport & map symbols
    "\u2600-\u26FF"          # misc symbols
    "]+", flags=re.UNICODE)

cleaned_text = emoji_pattern.sub(r'', text)

with open("output.md", "w", encoding="utf-8") as f:
    f.write(cleaned_text)