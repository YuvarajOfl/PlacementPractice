class Solution(object):
    def decodeString(self, s):
        stack = []
        current_str = ""
        current_k = 0
        
        for char in s:
            if char.isdigit():
               
                current_k = current_k * 10 + int(char)
            elif char == "[":
               
                stack.append((current_str, current_k))
                current_str = ""
                current_k = 0
            elif char == "]":
                last_str, last_k = stack.pop()
                
                current_str = last_str + (last_k * current_str)
            else:
                current_str += char
                
        return current_str