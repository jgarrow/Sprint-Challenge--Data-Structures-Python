class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False

    def reverse_list(self, node, prev):
        # if there's nothing in the list
        if self.head is None:
            return None
        
        # if there's only 1 thing in the list
        elif self.head.next_node is None:
            return None
        
        # if there's 2+ things in the list
        elif self.head.next_node:
            # loop through nodes
            # for each node, set next_node.next_node to the previous node
            prev_node = None
            curr_node = self.head
            # next_node = self.head.next_node

            # while we're not at the end of the list/at the tail
            while curr_node is not None:
                # hold onto the next node
                new_next = curr_node.next_node

                # update the next node to be the current prev_node (flip next to point to the previous)
                curr_node.next_node = prev_node

                # update the prev node to be the current node
                prev_node = curr_node

                # update the current node to be the next node
                curr_node = new_next
            
            # curr_node will be None if we finished our loop 
            # prev_node will be the new head (the original tail)
            if curr_node is None:
                self.head = prev_node

