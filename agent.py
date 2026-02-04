from tool_registry import ToolRegistry
from decision_engine import DecisionEngine
from logger import DecisionLogger

class ToolChoosingAgent:
    def __init__(self):
        self.registry = ToolRegistry()
        self.engine = DecisionEngine()
        self.logger = DecisionLogger()

    def analyze_task(self, task_description, dataset_size):
        tools = self.registry.get_tools()
        scored_tools = self.engine.choose_best_tool(tools, dataset_size)

        best_tool, best_score = scored_tools[0]

        justification = {
            "task": task_description,
            "dataset_size": dataset_size,
            "tool_scores": [
                {"tool": t["name"], "score": s}
                for t, s in scored_tools
            ],
            "selected_tool": best_tool["name"],
            "justification": (
                f"{best_tool['name']} selected due to optimal balance of "
                f"accuracy, speed, resource efficiency, and interpretability "
                f"for dataset size {dataset_size}."
            )
        }

        self.logger.log(justification)

        return best_tool
