class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        type_one = type_two  = 0

        for student in students:
            if student == 1:
                type_one += 1
            else:
                type_two += 1
        for i in range(len(sandwiches)):
            if sandwiches[i] == 1:
                if type_one == 0:
                    return len(sandwiches) - i
                type_one -= 1
            else:
                if type_two == 0:
                    return len(sandwiches) - i
                type_two -= 1
        return 0
                