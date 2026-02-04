class ToolRegistry:
    def __init__(self):
        self.tools = [
            {
                "name": "VADER",
                "module": "tools.vader_tool",
                "accuracy": 0.75,
                "speed": 0.9,
                "resource": 0.95,
                "interpretability": 0.9,
                "offline": True,
                "best_for": "small_medium"
            },
            {
                "name": "HF_TRANSFORMER",
                "module": "tools.hf_transformer_tool",
                "accuracy": 0.9,
                "speed": 0.5,
                "resource": 0.4,
                "interpretability": 0.6,
                "offline": True,
                "best_for": "medium_large"
            },
            {
                "name": "RULE_BASED",
                "module": "tools.rule_based_tool",
                "accuracy": 0.55,
                "speed": 0.95,
                "resource": 0.98,
                "interpretability": 1.0,
                "offline": True,
                "best_for": "small"
            }
        ]

    def get_tools(self):
        return self.tools
