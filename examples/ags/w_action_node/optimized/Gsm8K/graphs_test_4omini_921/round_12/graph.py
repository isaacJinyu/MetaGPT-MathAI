from typing import Literal
import examples.ags.w_action_node.optimized.Gsm8K.graphs.template.operator as operator
import examples.ags.w_action_node.optimized.Gsm8K.graphs.round_12.prompt as prompt_custom
from metagpt.provider.llm_provider_registry import create_llm_instance
from metagpt.utils.cost_manager import CostManager

DatasetType = Literal["HumanEval", "MMBP", "Gsm8K", "MATH", "HotpotQa", "MMLU"]

class SolveGraph:
    def __init__(
        self,
        name: str,
        llm_config,
        dataset: DatasetType,
    ) -> None:
        self.name = name
        self.dataset = dataset
        self.llm = create_llm_instance(llm_config)
        self.llm.cost_manager = CostManager()
        self.custom = operator.Custom(self.llm)
        self.programmer = operator.Programmer(self.llm)
        self.sc_ensemble = operator.ScEnsemble(self.llm)

    async def __call__(self, problem: str):
        """
        Implementation of the graph
        """
        analysis = await self.custom(input=problem, instruction=prompt_custom.ANALYZE_PROMPT)
        code_result = await self.programmer(problem=problem, analysis=analysis['response'])
        
        solutions = []
        for _ in range(3):  # Generate 3 solutions
            solution = await self.custom(input=problem + f"\nAnalysis: {analysis['response']}\nCode output: {code_result['output']}", instruction=prompt_custom.SOLVE_PROMPT)
            solutions.append(solution['response'])
        
        ensemble_result = await self.sc_ensemble(solutions=solutions, problem=problem)
        verification = await self.custom(input=problem + f"\nInitial solution: {ensemble_result['response']}", instruction=prompt_custom.VERIFY_PROMPT)
        return verification['response'], self.llm.cost_manager.total_cost
                    