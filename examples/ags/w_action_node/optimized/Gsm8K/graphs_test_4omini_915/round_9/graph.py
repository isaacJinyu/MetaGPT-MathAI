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
        self.review = operator.Review(self.llm)
        self.revise = operator.Revise(self.llm)
        self.custom = operator.Custom(self.llm)

    async def __call__(self, problem: str):
        """
        Implementation of the graph
        """
        solution = await self.generate(problem=problem)
        review_result = await self.review(problem=problem, solution=solution['response'])
        
        if not review_result['review_result']:
            context = await self.custom(input=problem + f" Original solution: {solution['response']}", instruction=prompt_custom.REVISION_CONTEXT)
            revised_solution = await self.revise(problem=problem, solution=solution['response'], feedback=review_result['feedback'] + f" Additional context: {context['response']}")
            solution = revised_solution
        
        format_solution = await self.format(problem=problem, solution=solution['response'])
        return format_solution['response'], self.llm.cost_manager.total_cost
                    