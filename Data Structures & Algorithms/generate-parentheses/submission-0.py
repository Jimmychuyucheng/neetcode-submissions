class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        '''
        '(':open ')':close
        when open added: when openN < n
        when close added: when closeN < openN 
        base case: if openN == closeN == n 

        ds:
        stack for backtracking
        list for res
        '''

        res = []
        stack = []

        def paren(openN, closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                paren(openN + 1, closeN)
                stack.pop()

            if closeN < openN:
                stack.append(")")
                paren(openN, closeN + 1)
                stack.pop()

        paren(0,0)
        return res
