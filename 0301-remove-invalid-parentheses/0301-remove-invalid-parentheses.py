class Solution:
    def removeInvalidParentheses(self, s):
        def valid(x):
            count = 0

            for ch in x:
                if ch == '(':
                    count += 1
                elif ch == ')':
                    count -= 1

                    if count < 0:
                        return False

            return count == 0

        queue = [s]
        visited = set([s])
        answer = []

        while queue:
            found = False
            next_queue = []

            for x in queue:
                if valid(x):
                    answer.append(x)
                    found = True

            if found:
                return answer

            for x in queue:
                for i in range(len(x)):
                    if x[i] != '(' and x[i] != ')':
                        continue

                    new_string = x[:i] + x[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]