from typing import Dict, Union
def is_famous(stats: dict[str, Union[int, float]]) -> bool:
    views = stats.get('views', 0)
    likes = stats.get('likes', 0)
    shares = stats.get('shares', 0)
    favorites = stats.get('favorites', 0)
    
    return (views > 1000000 and likes > 60000) or (shares > 200000 and favorites > 40000)
stats = {
  'views': 1000000,
  'likes': 60000,
  'shares': 200000,
  'favorites': 40000
}

is_famous(stats)  # Returns True

