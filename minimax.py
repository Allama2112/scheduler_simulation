import random

class Node:
    def __init__(self, value=None, children=None):
        self.value = value          # evaluation value (only for leaves)
        self.children = children or []  # list of child nodes

    def is_leaf(self):
        return len(self.children) == 0
    

def generate_tree(depth, branching_factor, value_range=(-10, 10)):
    """Generate a random minimax tree for testing."""
    if depth == 0:
        return Node(value=random.randint(*value_range))

    children = [
        generate_tree(depth - 1, branching_factor, value_range)
        for _ in range(branching_factor)
    ]
    return Node(children=children)


def alphabeta(node, depth, alpha, beta, maximizing):
    if depth == 0 or node.is_leaf():
        return node.value, [node]

    if maximizing:
        best_score = float('-inf')
        best_line = []

        for child in node.children:
            score, pv = alphabeta(child, depth - 1, alpha, beta, False)

            if score > best_score:
                best_score = score
                best_line = [node] + pv

            alpha = max(alpha, best_score)
            if beta <= alpha:
                break

        return best_score, best_line

    else:
        best_score = float('inf')
        best_line = []

        for child in node.children:
            score, pv = alphabeta(child, depth - 1, alpha, beta, True)

            if score < best_score:
                best_score = score
                best_line = [node] + pv

            beta = min(beta, best_score)
            if beta <= alpha:
                break

        return best_score, best_line


# Generate a test tree
root = generate_tree(depth=4, branching_factor=3)

# Run alpha-beta
score, pv = alphabeta(root, depth=4, alpha=float('-inf'), beta=float('inf'), maximizing=True)

print("Minimax Score:", score)
print("Principal Variation (leaf values):")
print([node.value for node in pv if node.is_leaf()])

