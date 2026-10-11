class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append((value,timestamp))
        

    def get(self, key: str, timestamp: int) -> str:
        pairs = self.hashmap[key]

        left = 0
        right = len(pairs) - 1
        most_recent = -1
        most_recent_time = 0
        while left <= right:
            mid = (left + right) // 2
            if pairs[mid][1] > timestamp:
                right = mid - 1
            else:
                if pairs[mid][1] > most_recent_time:
                    most_recent_time = pairs[mid][1]
                    most_recent = mid
                left = mid + 1
        if most_recent != -1:
            return pairs[most_recent][0]
        return ''
        
