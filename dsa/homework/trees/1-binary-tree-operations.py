from typing import Any, Optional


class TreeNode:
    def __init__(self, data: Any, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.data = data
        self.left = left
        self.right = right


def get_sample_tree() -> TreeNode:
    """
    Sample tree:
                  16
          14              10
      8       7         9     3
    2   4   1
    """
    return TreeNode(
        16,
        left=TreeNode(
            14,
            left=TreeNode(
                8,
                left=TreeNode(2), right=TreeNode(4)
            ),
            right=TreeNode(
                7,
                left=TreeNode(1)
            )
        ),
        right=TreeNode(
            10,
            left=TreeNode(9),
            right=TreeNode(3)
        )
    )


def homework_search_tree(root: TreeNode, target: Any) -> Optional[TreeNode]:
    """
    Search for a node with value=target
    """
    if root is None:
        return None
    if root.data == target:
        return root
    return (
            homework_search_tree(root.left, target) or
            homework_search_tree(root.right, target)
    )


def homework_insert(root: TreeNode, key: Any, value: Any):
    """
    Insert a node with value=value as the child of the node with given key
    """
    target = homework_search_tree(root, key)
    if target is None:
        raise ValueError(f"No such node: {key}")
    if target.left is None:
        target.left = TreeNode(value)
    elif target.right is None:
        target.right = TreeNode(value)
    else:
        raise ValueError(f"Target has both the children. Can't insert")


def homework_delete_a_leaf(node: TreeNode, value: Any, parent: TreeNode = None):
    if not node:
        return
    if node.data == value:
        if not parent:
            return None
        if parent.left == node:
            parent.left = None
        elif parent.right == node:
            parent.right = None
    homework_delete_a_leaf(node.left, value, node)
    homework_delete_a_leaf(node.right, value, node)


def homework_postorder_recursive(root: TreeNode):
    if not root:
        return
    homework_postorder_recursive(root.left)
    homework_postorder_recursive(root.right)
    print(root.data, end=', ')


def homework_postorder_iterative(root: TreeNode):
    stack = [root]
    reverse_order = []
    while stack:
        curr = stack.pop()
        reverse_order.append(curr.data)
        if curr.left:
            stack.append(curr.left)
        if curr.right:
            stack.append(curr.right)
    for data in reverse_order[::-1]:
        print(data, end=', ')


if __name__ == '__main__':
    t = get_sample_tree()
    assert homework_search_tree(t, 10) is not None  # there must be a node with value 10

    # Attach node with value=11 to node with value 7
    homework_insert(t, 7, 11)
    assert t.left.right.right.data == 11

    # Delete the node
    homework_delete_a_leaf(t, 11)
    assert t.left.right.right is None

    homework_postorder_iterative(t) or print()
    homework_postorder_recursive(t) or print()
