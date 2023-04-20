def create_stack():
    stack=[]
    return stack
   
def empty_stack(stack):
     return len(stack)==0
     
def push(stack,item):
    stack.append(item)
   
def pop(stack):
    if (empty_stack(stack)):
        return("stack is empty")
    stack.pop()
   
stack=create_stack()
push(stack,str(13))
push(stack,str(1))
push(stack,str(58))
push(stack,str(9))
pop(stack)
print("the stack is"+ str(stack))