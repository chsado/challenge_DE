from typing import List, Tuple
from datetime import datetime
import json
from collections import defaultdict, Counter

def q1_time(file_path: str) -> List[Tuple[datetime.date, str]]:
    date_user_count = defaultdict(Counter)
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                tweet = json.loads(line)
                date = datetime.strptime(tweet['date'][:10], '%Y-%m-%d').date()
                user = tweet['user']['username']
                date_user_count[date][user] += 1
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON in line: {line}")
                print(e)
    top_dates = Counter({date: sum(users.values()) for date, users in date_user_count.items()}).most_common(10)
    result = [(date, date_user_count[date].most_common(1)[0][0]) for date, _ in top_dates]
    
    return result

