from typing import List, Tuple
import json
import re


def q2_memory(file_path: str) -> List[Tuple[str, int]]:
    emoji_pattern = re.compile("[\U00010000-\U0010FFFF]", flags=re.UNICODE)
    emoji_count = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            for emoji in emoji_pattern.findall(tweet['content']):
                if emoji not in emoji_count:
                    emoji_count[emoji] = 0
                emoji_count[emoji] += 1
    
    return sorted(emoji_count.items(), key=lambda x: x[1], reverse=True)[:10]
