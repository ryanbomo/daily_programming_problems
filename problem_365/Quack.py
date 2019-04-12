import random

class Quack:
    stack_top = []
    stack_bottom = []
    stack_temp = []
    
    def push(self, item):
        self.stack_top.append(item)
        

    def pop(self):
        if len(self.stack_top)==0:
            print("Hit bottom of top")
            if not self.refill_stack(self.stack_top, self.stack_bottom):
                return "bottom, can't pop()"
        return self.stack_top.pop()

    def pull(self):
        if len(self.stack_bottom)==0:
            print("Hit bottom of bottom")
            if not self.refill_stack(self.stack_bottom, self.stack_top):
                return "bottom, can't pull()"
        return self.stack_bottom.pop()

    def refill_stack(self, stack_empty, stack_full):
        print("Refilling Stack")
        i = 0
        num_items = len(stack_full)/2
        if num_items < 1:
            return False
        while i<num_items:
            self.stack_temp.append(stack_full.pop())
            i+=1

        while len(stack_full)>0:
            stack_empty.append(stack_full.pop())

        while len(self.stack_temp)>0:
            stack_full.append(self.stack_temp.pop())
        return True


def test():
    quack = Quack()
    i = 0
    while i < 1000:
        quack.push(i)
        i+=1

    while i>0:
        if random.randint(1,2)%2 == 0:
            print(quack.pop())
        else:
            print(quack.pull())
        i-=1
        
        

