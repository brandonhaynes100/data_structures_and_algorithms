class Node(object):
    def __init__(self, val, _next=None):
        self.val = val
        self._next = _next

    def __str__(self):
        return '{val}'.format(val=self.val)

    def __repr__(self):
        return '<Node | Val: {self.val} | Next: {next}>'.format(val=self.val, next=self._next)
