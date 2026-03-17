# factorial-using-function
ctorial Recursion Explanation (Points)
1️⃣ Function Definition

def factorial(n):

Creates a function named factorial

Takes one input n

2️⃣ Base Condition (Stopping Case)

if n == 0 or n == 1:

Stops recursion

Returns 1

Important to avoid infinite calls

3️⃣ Recursive Condition

return n * factorial(n-1)

Function calls itself

Reduces problem size (n → n-1)

4️⃣ Working Flow (Example n = 5)

factorial(5) → 5 × factorial(4)

factorial(4) → 4 × factorial(3)

factorial(3) → 3 × factorial(2)

factorial(2) → 2 × factorial(1)

factorial(1) → 1 (base case)

5️⃣ Backtracking (Returning Values)

factorial(1) = 1

factorial(2) = 2 × 1 = 2

factorial(3) = 3 × 2 = 6

factorial(4) = 4 × 6 = 24

factorial(5) = 5 × 24 = 120

6️⃣ Key Concepts

Recursion = function calling itself

Needs base case + recursive case

Works like a stack (LIFO)

7️⃣ Advantages

Code is short and clean

Useful for mathematical problems

Easy for divide & conquer problems

8️⃣ Disadvantages

Uses more memory (stack calls)

Slower than loops for large inputs

Can cause RecursionError

9️⃣ Final Output Example

Input: 5

Output: 120
