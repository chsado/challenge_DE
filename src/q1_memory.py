from typing import List, Tuple
from datetime import datetime
import json

def q1_memory(file_path: str) -> List[Tuple[datetime.date, str]]:
    user_count_per_date = {}
    
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            tweet = json.loads(line)
            date = datetime.strptime(tweet['date'][:10], '%Y-%m-%d').date()
            user = tweet['user']['username']
            
            if date not in user_count_per_date:
                user_count_per_date[date] = {}
            if user not in user_count_per_date[date]:
                user_count_per_date[date][user] = 0
            user_count_per_date[date][user] += 1
    
    top_dates = sorted(user_count_per_date.items(), key=lambda x: sum(x[1].values()), reverse=True)[:10]
    result = [(date, max(users.items(), key=lambda x: x[1])[0]) for date, users in top_dates]
    
    return result

