class Node:
    def __init__(self, val):
        self.left_child = None
        self.right_child = None
        self.value = val
        self.locked = False

    def has_left(self):
        if self.left_child != None:
            return True
        return False

    def has_right(self):
        if self.rigth_child != None:
            return True
        return False

    def is_locked(self):
        return self.locked

    def lock(self):
        can_change = self.check_children_unlocked()
        if can_change:
            self.locked = True
            return True
        return False

    def unlock(self):
        can_change = self.check_children_unlocked()
        if can_change:
            self.locked = False
            return True
        return False

    def check_children_unlocked(self):

        ## If no children, both checks should be true
        right_check = True
        left_check = True

        ## Check down left
        if self.has_left():
            if self.left_child.is_locked():
                return False
            left_check = self.left_child.check_children_unlocked()

        ## Check down right
        if self.has_right():
            if self.right_child.is_locked():
                return False
            right_check = self.right_child.check_children_unlocked()

        ## Check to see if both left check down and right check down are good
        if right_check and left_check:
            return True
        return False
        
