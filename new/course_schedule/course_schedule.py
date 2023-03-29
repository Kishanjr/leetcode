#tc -O(V + E)
#Sc -O(V + E)
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        # Create an empty adjacency list to store prerequisites for each course
        adj = {}
        for i in range(numCourses):
            adj[i] = []

        indegree = [0] * numCourses

        # Iterate over the prerequisites and update the adjacency list and indegree array
        for course, prereq in prerequisites:
            adj[prereq].append(course)
            indegree[course] += 1

        #  add all courses with indegree 0 to a queue
        q = deque()
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)

        # Iterate over the courses in the queue, decrement their dependent courses' indegrees,
        # and add any courses with indegree 0 to the queue
        while q:
            c = q.popleft()
            numCourses -= 1
            for dep in adj[c]:
                indegree[dep] -= 1
                if indegree[dep] == 0:
                    q.append(dep)

        # If all courses have been processed, return True; otherwise, return False
        return numCourses == 0
