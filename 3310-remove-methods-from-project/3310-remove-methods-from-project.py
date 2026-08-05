class Solution(object):
    def remainingMethods(self, n, k, invocations):
        graph = [[] for _ in range(n)]

        for u, v in invocations:
            graph[u].append(v)

        suspicious = set()
        stack = [k]

        while stack:
            node = stack.pop()
            if node in suspicious:
                continue
            suspicious.add(node)
            stack.extend(graph[node])

        for u, v in invocations:
            if u not in suspicious and v in suspicious:
                return list(range(n))

        return [i for i in range(n) if i not in suspicious]