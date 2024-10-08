from typing import Literal
import examples.ags.w_action_node.optimized.Gsm8K.graphs.template.operator as operator
import examples.ags.w_action_node.optimized.Gsm8K.graphs.round_9.prompt as prompt_custom
import examples.ags.w_action_node.optimized.Gsm8K.graphs.template.prompt_lib as prompt_lib
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
        self.generate = operator.Generate(self.llm)
        self.format = operator.Format(self.llm)
        self.sc_ensemble = operator.ScEnsemble(self.llm)
        self.rephrase = operator.Rephrase(self.llm)
        self.custom = operator.Custom(self.llm)

    async def __call__(self, problem: str):
        """
        Implementation of the graph
        """
        rephrased_problem = await self.rephrase(problem=problem)
        
        enhanced_problem = await self.custom(input=problem + f" Rephrased problem: {rephrased_problem['response']}", instruction=prompt_custom.ENHANCE_PROBLEM)
        
        solutions = []
        for _ in range(3):  # Generate 3 solutions
            solution = await self.generate(problem=enhanced_problem['response'])
            solutions.append(solution['response'])
        
        best_solution = await self.sc_ensemble(solutions=solutions, problem=enhanced_problem['response'])
        format_solution = await self.format(problem=problem, solution=best_solution['response'])
        return format_solution['response'], self.llm.cost_manager.total_cost
                    