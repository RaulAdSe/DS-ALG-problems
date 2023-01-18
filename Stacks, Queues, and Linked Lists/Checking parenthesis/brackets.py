from easyinput import read

def areBracketsBalanced(expr):
	stack = []

	# Traversing the Expression
	for char in expr:
		if char in ["(", "{", "["]:

			# Push the element in the stack
			stack.append(char)
		else:

			# IF current character is not opening
			# bracket, then it must be closing.
			# So stack cannot be empty at this point.
			if not stack:       # Check if stack is empty.
				return False
			current_char = stack.pop()
			if current_char == '(':
				if char != ")":
					return False
			if current_char == '{':
				if char != "}":
					return False
			if current_char == '[':
				if char != "]":
					return False

	# Check Empty Stack
	if stack:
		return False
	return True


# Driver Code
if __name__ == "__main__":
    
    expr = read(str)
    while expr is not None:

        # Function call
        if areBracketsBalanced(expr):
            print(expr + " is correct")
        else:
            print(expr + " is incorrect")
        expr = read(str)


# This code is contributed by AnkitRai01 and improved
# by Raju Pitta
