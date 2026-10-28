def is_valid_parentheses(s: str) -> bool:
    """Return True if parentheses and brackets are balanced."""
    stack = []
    matching = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for char in s:
        if char in '([{':
            stack.append(char)
        elif char in ')]}':
            if not stack:
                return False
            if stack.pop() != matching[char]:
                return False
    return len(stack) == 0