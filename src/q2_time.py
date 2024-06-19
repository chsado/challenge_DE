from typing import List, Tuple
import json
import re
from collections import Counter

def q2_time(file_path: str) -> List[Tuple[str, int]]:
    emoji_pattern = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)
    emojis = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                emojis.update(emoji for emoji in emoji_pattern.findall(tweet['content']))
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in line: {line}")
                print(e)
    
    return emojis.most_common(10)
