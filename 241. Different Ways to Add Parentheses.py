class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # This method double counts inner parenthesis as two distict answers ((2*3)-(4*5))
        # Did not account for different ways the parenthesis not change the outcome
        # def add(a,b):
        #     return a+b

        # def sub(a,b):
        #     return a-b

        # def mult(a,b):
        #     return a*b

        # digits = ''
        # numbers = []
        # ops = []
        # for item in expression:
        #     if item.isdigit():
        #         digits+=item
        #     else:
        #         # print('digits now', digits)
        #         numbers.append(int(digits))
        #         ops.append(item)
        #         digits = ''
        # numbers.append(int(digits))

        # result = []

        # def recurse(numbers, ops):
        #     if ops==[]:
        #         print(f'adding valid', digits)
        #         result.append(numbers[0])
        #     for i in range(len(ops)):
        #         a,b = numbers[i:i+2]
        #         op = ops[i]
        #         if op=='+':
        #             calc_number = add(a,b)
        #         elif op == '-':
        #             calc_number = sub(a,b)
        #         elif op == '*':
        #             calc_number = mult(a,b)
        #         new_numbers = numbers[:i]+[calc_number]+numbers[i+2:]
        #         new_ops = ops[:i]+ops[i+1:]
        #         print('doing',op,'between',a,b,'results in', new_numbers, new_ops)

        #         recurse(new_numbers, new_ops)

        # recurse(numbers, ops)

        # return result




        # use divide-and-conquer (split calc at the operator)
        # use memoization to store precomputed results 
        # recording 'result' logic from https://leetcode.com/problems/different-ways-to-add-parentheses/solutions/5781291/beats-100-best-solution-easy-explaination/
        def calc(a,op,b):
            if op=='+':
                return a+b
            if op=='-':
                # print(f'subtracting {a} and {b} of type {type(a)}')
                return a-b
            if op=='*':
                # print(f'multiplying {a} and {b} of type {type(a)}')
                return a*b

        digits = ''
        # use tuple so it can serve as hash key during memoization
        num_ops = ()
        for item in expression:
            if item.isdigit():
                digits+=item
            else:
                # print('digits now', digits)
                num_ops += int(digits),
                num_ops += item,
                digits = ''
        num_ops += int(digits),

        memo = {}

        def recurse(num_ops):
            print('on', num_ops)

            # early stop
            if num_ops in memo:
                return memo[num_ops]

            # if len(num_ops)==1:
            #     res = [num_ops[0]]
            #     memo[num_ops]= res
            #     return res

            result = []

            # even elements are the ops
            for i in range(1,len(num_ops),2):
                # print(f'recurse left {num_ops[:i]}')
                left = recurse(num_ops[:i])
                # print(f'result from left is', left)
                op = num_ops[i]
                # print(f'recurse right {num_ops[i+1:]}')
                right = recurse(num_ops[i+1:])
                # print(f'result from right is {right} of type {type(right)}')
                
                # print(f'recurse left op right {left},{op},{right}')
                for l in left:
                    for r in right:
                        # print(f'l is {l}, op is {op}, r is {r}')
                        res = calc(l, op, r)
                        memo[num_ops] = res
                        result.append(res)

                # print(f'for index {i} result is', result)

            if not result:
                # when there's only one element left
                result.append(num_ops[0])

            memo[num_ops] = result
            
            return result

        return recurse(num_ops)

         