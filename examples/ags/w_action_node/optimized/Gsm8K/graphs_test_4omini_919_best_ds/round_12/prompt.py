SOLVE_PROMPT = """
Solve the given math problem step by step. Show your work and clearly state the final answer.

1. Read the problem carefully and identify the key information.
2. Determine the appropriate mathematical operations needed to solve the problem.
3. Perform the calculations step by step, showing your work.
4. Clearly state the final answer, including the appropriate units if applicable.
5. Double-check your calculations for accuracy.

Provide your solution below:
"""

ALTERNATIVE_SOLVE_PROMPT = """
Solve the given math problem using a different approach or method than you might typically use. Show your work step by step and clearly state the final answer.

1. Read the problem carefully and identify the key information.
2. Think of an alternative method or approach to solve the problem.
3. Perform the calculations step by step, showing your work.
4. Clearly state the final answer, including the appropriate units if applicable.
5. Verify your solution by checking if it makes sense in the context of the problem.

Provide your alternative solution below:
"""

REVIEW_PROMPT = """
Review the given problem and solution. Verify the accuracy of the solution and make corrections if necessary. If the solution is correct, simply restate the final answer. If there are errors, provide the correct solution with explanations.

1. Read the original problem and the provided solution.
2. Check each step of the solution for accuracy.
3. Verify that the final answer is correct and appropriate for the given problem.
4. If there are any errors, provide the correct solution with clear explanations.
5. If the solution is correct, restate the final answer.

Provide your review and final answer below:
"""

ENSEMBLE_PROMPT = """
Compare and analyze the two given solutions for the same problem. Determine which solution is more accurate or if they agree. If they differ, explain why and provide a final, correct answer.

1. Carefully read both solutions.
2. Compare the approaches and results of both solutions.
3. If the solutions agree, confirm the final answer.
4. If the solutions disagree, analyze the discrepancies and determine the correct approach.
5. Provide a final, verified answer with a brief explanation of your reasoning.

Provide your analysis and final answer below:
"""

TOTAL_CALCULATION_PROMPT = """
Calculate the total quantity mentioned in the problem, if applicable. This could be the total number of items, total time, or any other relevant total quantity. If there's no clear total to calculate, state that no total calculation is needed.

1. Identify any quantities mentioned in the problem and the final solution.
2. If there are multiple quantities that can be summed or combined, perform the calculation.
3. If there's no clear total to calculate, state that no total calculation is needed.
4. Provide the total quantity or the statement that no calculation is needed.

Calculate and provide the total quantity or statement below:
"""

ERROR_CHECK_PROMPT = """
Review the final solution and the total calculation (if applicable) to check for any errors or inconsistencies. If an error is found, provide a corrected solution. If no errors are found, confirm the final answer.

1. Compare the final solution with the total calculation (if provided).
2. Check if the final answer makes sense in the context of the problem.
3. If there are any discrepancies or errors, provide a corrected solution with explanations.
4. If no errors are found, confirm and restate the final answer.

Provide your error check results and final answer below:
"""

EXTRACT_ANSWER_PROMPT = """
Extract only the final numerical answer from the given solution. If there are multiple numbers, choose the one that represents the final answer to the problem. Do not include any units or additional text. Provide only the number as a decimal or integer.

For example, if the solution contains "The final answer is $20.00", your response should be:
20.00

Extract and provide only the numerical answer below:
"""