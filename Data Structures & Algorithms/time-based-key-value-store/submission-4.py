class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hashmap:
            return ""
        pairs = self.hashmap[key]

        left = 0
        right = len(pairs) - 1
        most_recent = -1
        most_recent_value = "" 
        while left <= right:
            mid = (left + right) // 2
            pair = pairs[mid]
            value = pair[0]
            time = pair[1]
            if time > timestamp:
                right = mid - 1
            else:
                if time > most_recent:
                    most_recent = time
                    most_recent_value = value
                left = mid + 1
        if most_recent == -1:
            return ""
        
        return most_recent_value

        
