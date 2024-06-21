from typing import List, Tuple
import json
import re

def q3_memory(file_path: str) -> List[Tuple[str, int]]:
    mention_pattern = re.compile(r'@\w+')
    mention_count = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                for mention in mention_pattern.findall(tweet['content']):
                    mention = mention[1:]
                    if mention not in mention_count:
                        mention_count[mention] = 0
                    mention_count[mention] += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in line: {line}")
                print(e)
                
    return sorted(mention_count.items(), key=lambda x: x[1], reverse=True)[:10]
