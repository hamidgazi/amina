with open('Instagram_Chat_Analysis_Amina_Hamid.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
keywords = [
    'Baat Pakki', 'Engagement', 'Nikah', 'hand hold', 'First hug', 'First good kiss',
    'ticker-', 'photo1.jpg', 'polaroid', 'longest_break', '47.94', 'flight',
    'Pre-Nikah', 'sweet words', 'yaad', 'jaanu', 'Reaction Queen', 'trivia', 'Soulmate'
]

for kw in keywords:
    matches = list(re.finditer(re.escape(kw), text, re.I))
    print(f"{kw:20} -> {len(matches)} matches")
    if matches:
        first = matches[0].start()
        line_no = text[:first].count('\n') + 1
        print(f"   First at L{line_no}: {text[max(0, first-30):min(len(text), first+50)].strip()}")



