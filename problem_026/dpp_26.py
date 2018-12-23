class NODE:
    def __init__(self, value, next_node):
        self.val = value
        self.next = next_node

    def get_val(self):
        return self.val

    def set_val(self,value):
        self.val = value



class LINKED_LIST:
    def __init__(self):
        self.head = None

    def insert(self, value):
        current_node = self.head
        new_node = NODE(value, current_node)
        self.head = new_node

def drop_kth_last_element(linked_list, k):
    dist = 0
    current_node = linked_list.head
    trailing_node = None
    while current_node.next != None:
        current_node = current_node.next
        if dist < k-1:
            dist += 1
        elif trailing_node == None:
            trailing_node = linked_list.head
        else:
            trailing_node = trailing_node.next
    ## Set trialing node next to next next
    delete_node = trailing_node.next
    trailing_node.next = delete_node.next


def walk_list(linked_list):
    current_node = linked_list.head
    while current_node != None:
        print(current_node.get_val())
        current_node = current_node.next



data = [10,9,8,7,6,5,4,3,2,1]
mylist = LINKED_LIST()
for i in data:
    mylist.insert(i)

walk_list(mylist)
drop_kth_last_element(mylist,5)
print()
walk_list(mylist)
        
    

