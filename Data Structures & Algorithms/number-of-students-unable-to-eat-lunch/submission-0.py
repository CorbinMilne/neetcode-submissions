from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        count = 0

        while students:

            if count == len(students):
                return count

            if students[0] == sandwiches[0]:
                students.remove(students[0])
                sandwiches.remove(sandwiches[0])
                count = 0
            
            else:
                students.append(students[0])
                students.remove(students[0])
                count += 1
        
        return len(students)
            
        