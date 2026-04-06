class Solution(object):
    def evalRPN(self, tokens):
        self.stack = []

        for token in tokens:
            if token.isdigit() or len(token) > 1:
                self.stack.append(int(token))
            
            else:
                if token == "+":
                    self.stack[-2] += self.stack[-1]
                
                elif token == "-":
                    self.stack[-2] -= self.stack[-1]
                
                elif token == "*":
                    self.stack[-2] *= self.stack[-1]
                
                else:
                    self.stack[-2] = int(float(self.stack[-2]) / self.stack[-1])

                self.stack.pop()
                

        return self.stack[0]