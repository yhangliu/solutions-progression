class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        q = deque()
        q.append(beginWord)
        transforms = 2
        seen = set()
        while q:
            for _ in range(len(q)):
                curr_word = q.popleft()
                if curr_word in seen:
                    continue
                seen.add(curr_word)

                for word in wordList:
                    if word == curr_word:
                        continue
                    diff = 0
                    for i in range(len(word)):
                        if curr_word[i] != word[i]:
                            diff += 1
                        if diff > 1:
                            break
                    if diff == 1:
                        if word == endWord:
                            return transforms
                        q.append(word)
            transforms += 1
        return 0

        