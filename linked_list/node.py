class Node(object):
    """
    Node class representing each of the linked nodes in the list.
    """

    def __init__(self, elem, next=None):
        self.elem = elem
        self.next = next

    def __str__(self):
        if self.next:
            _str = 'Node({}) > Node({})'.format(self.elem, self.next.elem)
        else:
            _str = 'Node({}) > /'.format(self.elem)
        return _str

    def __eq__(self, other):
        return (self.elem == other)

    def __repr__(self):
        return str(self)

