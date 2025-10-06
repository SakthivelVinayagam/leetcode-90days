# Day 22: Valid Parentheses

**Problem**  
Link: https://leetcode.com/problems/valid-parentheses/  
Category: Stack / String  

---

## Approach
- Use a **stack** to keep track of opening brackets.  
- Iterate through each character:
  - If it’s an opening bracket `(`, `[`, or `{` → push it onto the stack.  
  - If it’s a closing bracket → check if the top of the stack matches its opening pair.  
    - If not matched or stack is empty → invalid.  
    - If matched → pop the top.  
- After processing all characters, if the stack is empty → valid string.

---

## Complexity
- **Time:** O(n) (each character processed once)  
- **Space:** O(n) (stack can hold all opening brackets in worst case)

---

## Patterns
- Stack-based validation  
- Related problems:
  - Min Remove to Make Valid Parentheses
  - Longest Valid Parentheses
  - Remove Invalid Parentheses

---

## Notes
- Always check stack before popping.  
- Return False early when encountering mismatches.  
- Works only for valid bracket characters — no letters or digits.  