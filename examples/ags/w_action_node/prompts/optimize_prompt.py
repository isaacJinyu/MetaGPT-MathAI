INITIALIZE_OPERATOR_PROMPT = """
您正在处理一个名为{dataset_name}的数据集。该数据集{dataset_description}。

输入特征包括:
{input_features}

输出特征为:
{output_features}

请根据以上信息,优化用途为{operator_name}的prompt以便更好地处理这个数据集:

{initial_prompt}

您的任务是:
1. 分析数据集的特点和结构
2. 考虑输入和输出特征之间的关系
3. 调整initial_prompt以更好地利用数据集信息
4. 提供一个经过优化的prompt版本

请提供您优化后的prompt,并简要解释您所做的更改及其原因。
"""

# TODO 这里也需要自适应的完成针对不同数据集的GRAPH OPTIMIZE PROMPT

GRAPH_OPTIMIZE_PROMPT = """You are building a Graph and corresponding Prompt to jointly solve {type} problems. 
Referring to the given graph and prompt, which forms a basic example of a {type} solution approach, 
please reconstruct and optimize them. You can add, modify, or delete nodes, parameters, or prompts. Include your 
single modification in XML tags in your reply. Ensure they are complete and correct to avoid runtime failures. When 
optimizing, you can incorporate critical thinking methods like Review, Revise, Ensemble, selfAsk, etc. Consider 
Python's loops (for, while, list comprehensions), conditional statements (if-elif-else, ternary operators), 
or machine learning techniques (e.g., linear regression, decision trees, neural networks, clustering). The graph 
complexity should not exceed 10. Use logical and control flow (IF-ELSE, loops) for a more enhanced graphical 
representation.You must include all the prompts related to the custom method. No other prompts are allowed."""

GRAPH_INPUT = """
Here is a Graph and corresponding Prompt(only relate to the Custom method) that performed excellently in a previous iteration (maximum score is 1):\n
<sample>
    <experience>{experience}</experience>
    <modification>None</modification>
    <score>{score}</score>
    <graph>{graph}</graph>
    <prompt>{prompt}</prompt>(Custom method)
    <operator_description>{operator_description}</operator_description>
</sample>
First provide optimization ideas. Only add/modify/delete one detail point, extensive modifications are prohibited.\n\n"
"""

GRAPH_TEMPLATE = """from typing import Literal
from examples.ags.w_action_node.optimized.Gsm8K.graphs.template.operator import *
from examples.ags.w_action_node.optimized.Gsm8K.graphs.round_{round}.prompt import *
from metagpt.provider.llm_provider_registry import create_llm_instance
from metagpt.utils.cost_manager import CostManager

DatasetType = Literal["HumanEval", "MMBP", "Gsm8K", "MATH", "HotpotQa", "MMLU"]

{graph}
                    """

OPERATOR_OPTIMIZE_PROMPT = """You are building a Operator and corresponding Prompt to jointly solve {type} problems.
Referring to the given combination of Operator and prompt, which forms a basic example of a {type} solution approach, please reconstruct and optimize the Prompt and Operator. You can add, modify, or delete nodes and parameters in the Operator, as well as modify, delete, or add new Prompts.
Put your modification (only make one point of change, i.e., one sentence), and the modified Prompt and Operator in XML tags in your reply. They will be used as new Prompt and Operator for calculation and iteration. Please ensure they are complete and correct, otherwise it may lead to runtime failures.
Only modify the parts in Prompt and Operator.

Don't be limited to the previous format.You can consider Python's built-in loops (like for, while, and list comprehensions) or conditional statements (such as if-elif-else and ternary operators), or even machine learning methods ranging from basic supervised learning techniques (e.g., linear regression, decision trees) to more advanced approaches like neural networks and clustering algorithms. However, you must ensure that each call to the Operator internally involves at most 10 interactions, i.e., the complexity of the Operator does not exceed 15."""


OPERATOR_INPUT = """
Here is a Operator and corresponding Prompt that performed excellently in a previous iteration (maximum score is 1), Graph calls the Operator:\n
<sample>
    <experience>{experience}</experience>
    <modification>None</modification>
    <score>{score}</score>
    <operator>{operator}</operator>
    <prompt>{prompt}</prompt>
    <graph>{graph}</graph>
</sample>
First provide optimization ideas. Note that ANSWER_FORMAT_PROMPT must exist and cannot be modified. Only add/modify/delete one detail point, extensive modifications are prohibited.\n\n"
"""


OPERATOR_TEMPLATE = """
import ast
import random
import sys
import traceback
from collections import Counter
from typing import Dict, List, Tuple

from tenacity import retry, stop_after_attempt
from examples.ags.w_action_node.optimized.gsm8k.operators.round_{round}.prompt import *
from examples.ags.w_action_node.operator_an import (
    GenerateOp,
)
from metagpt.actions.action_node import ActionNode
from metagpt.llm import LLM
from metagpt.logs import logger


class Operator:
    def __init__(self, name, llm: LLM):
        self.name = name
        self.llm = llm

    def __call__(self, *args, **kwargs):
        raise NotImplementedError
        
{operator}
                    """