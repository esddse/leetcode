"""
# Definition for a QuadTree node.
class Node(object):
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""
class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        
        if quadTree1.isLeaf and quadTree2.isLeaf:
            return Node(quadTree1.val or quadTree2.val, True, None, None, None, None)
        elif quadTree1.isLeaf and not quadTree2.isLeaf:
            dummy_node = Node(quadTree1.val, True, None, None, None, None)
            node = Node(True, False, None, None, None, None)
            node.topLeft     = self.intersect(dummy_node, quadTree2.topLeft)
            node.topRight    = self.intersect(dummy_node, quadTree2.topRight)
            node.bottomLeft  = self.intersect(dummy_node, quadTree2.bottomLeft)
            node.bottomRight = self.intersect(dummy_node, quadTree2.bottomRight)
        elif not quadTree1.isLeaf and quadTree2.isLeaf:
            dummy_node = Node(quadTree2.val, True, None, None, None, None)
            node = Node(True, False, None, None, None, None)
            node.topLeft     = self.intersect(dummy_node, quadTree1.topLeft)
            node.topRight    = self.intersect(dummy_node, quadTree1.topRight)
            node.bottomLeft  = self.intersect(dummy_node, quadTree1.bottomLeft)
            node.bottomRight = self.intersect(dummy_node, quadTree1.bottomRight)
        else:
            node = Node(True, False, None, None, None, None)
            node.topLeft     = self.intersect(quadTree2.topLeft, quadTree1.topLeft)
            node.topRight    = self.intersect(quadTree2.topRight, quadTree1.topRight)
            node.bottomLeft  = self.intersect(quadTree2.bottomLeft, quadTree1.bottomLeft)
            node.bottomRight = self.intersect(quadTree2.bottomRight, quadTree1.bottomRight)

        if node.topLeft.isLeaf and node.topRight.isLeaf and node.bottomLeft.isLeaf and node.bottomRight.isLeaf:
            val = node.topLeft.val
            if val == node.topRight.val and val == node.bottomLeft.val and val == node.bottomRight.val:
                node.val = val
                node.isLeaf = True
                node.topLeft = None
                node.topRight = None
                node.bottomLeft = None
                node.bottomLeft = None
        return node