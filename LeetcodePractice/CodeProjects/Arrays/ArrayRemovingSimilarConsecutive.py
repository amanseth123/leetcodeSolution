def find(arr):
    stack=[]
    prev=None
    for i in arr:
        while stack and stack[-1]==i:
            prev=stack.pop()
        stack.append(i)
        if stack[-1]==prev:
            stack.pop()
    return stack




    