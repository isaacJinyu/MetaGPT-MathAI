THINK_PROMPT = """
Please reason step by step, think about what you know and what you need to solve.
"""

SELF_ASK_PROMPT = """
Based on your initial thoughts, ask yourself critical questions about the problem. What assumptions are you making? Are there any potential pitfalls or edge cases you should consider? What additional information might be helpful?
"""

REVIEW_PROMPT = """
Please review the solution to the given problem. Check for correctness, completeness, and clarity.
If the solution is correct and complete, return True. If not, return False and provide feedback on what needs to be improved.
"""

REVISE_PROMPT = """
Based on the given feedback, please revise the solution to address the issues mentioned.
Ensure that the revised solution is correct, complete, and clear.
"""

FU_ENSEMBLE_PROMPT = """
Critically evaluate the given solutions for the problem. Synthesize an enhanced integrated solution that combines the strengths of each approach while addressing any weaknesses or inconsistencies.
Ensure the final solution is correct, complete, and clear.
"""

REPHRASE_PROMPT = """
Please rephrase the given problem in a different way, maintaining its core meaning and requirements. This rephrasing should provide a fresh perspective on the problem.
"""