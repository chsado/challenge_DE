from typing import List, Tuple
import json
import re
from collections import Counter

def q3_time(file_path: str) -> List[Tuple[str, int]]:
    mention_pattern = re.compile(r'@\w+')
    
    mentions = Counter()
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            mentions.update(mention[1:] for mention in mention_pattern.findall(tweet['content']))
    
    return mentions.most_common(10)

