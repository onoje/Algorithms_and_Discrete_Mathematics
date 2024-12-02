from collections import deque

def decode_message(s):
    stack = []
    temp = []
    queue = deque()

    i = 0
    while i < len(s):
        if s[i] == '#':
            queue.append(s[i-1])
            stack.pop()
            while stack:
               temp.append(stack.pop())
            while queue:
               stack.append(queue.popleft())
            while temp:
               stack.append(temp.pop())
        elif s[i] == '@':
           i += 1
        else:
           stack.append(s[i])
        i += 1
    return ''.join(stack)

print(decode_message("ab#c@de#f#g"))