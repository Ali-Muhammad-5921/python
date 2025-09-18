class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def is_empty(self):
        return len(self.items) == 0


def is_balanced(expression):
    stack = Stack()
    pairs = {')': '(', ']': '[', '}': '{'}  # matching pairs

    for char in expression:
        if char in "([{":   # opening
            stack.push(char)
        elif char in ")]}":  # closing
            if stack.is_empty():   # bug 1 fixed
                return False
            top = stack.pop()
            if pairs[char] != top:  # bug 2 fixed
                return False

    return stack.is_empty()  # bug 3 fixed


# Tests
print("Expression: {[()]}", "->", is_balanced("{[()]}"))   # ✅ True
print("Expression: {{()())}", "->", is_balanced("{{()())}"))  # ❌ False
print("Expression: (()}", "->", is_balanced("(()}"))  # ❌ False
