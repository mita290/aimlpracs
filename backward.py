def backward_chaining(knowledge_base, goal, inferred=None):
    if inferred is None:
        inferred = set()

    if goal in inferred:
        return True

    if goal not in knowledge_base:
        return False

    for statement in knowledge_base[goal]:
        if backward_chaining(knowledge_base, statement, inferred):
            inferred.add(goal)
            return True

    return False

# Example knowledge base
kb_backward = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

goal_backward = 'A'

if not (backward_chaining(kb_backward, goal_backward)):
    print(f"Goal '{goal_backward}' can be inferred from the knowledge base.")
else:
    print(f"Goal '{goal_backward}' cannot be inferred from the knowledge base.")
