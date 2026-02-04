import yaml

class DecisionEngine:
    def __init__(self, config_path="config.yaml"):
        with open(config_path) as f:
            self.config = yaml.safe_load(f)

    def score_tool(self, tool, dataset_size):
        weights = self.config["weights"]

        score = (
            tool["accuracy"] * weights["accuracy"] +
            tool["speed"] * weights["speed"] +
            tool["resource"] * weights["resource"] +
            tool["interpretability"] * weights["interpretability"]
        )

        if dataset_size > self.config["dataset_size_threshold"]["medium"]:
            if tool["best_for"] == "small":
                score -= 0.2

        return round(score, 3)

    def choose_best_tool(self, tools, dataset_size):
        scored = []
        for tool in tools:
            tool_score = self.score_tool(tool, dataset_size)
            scored.append((tool, tool_score))

        scored.sort(key=lambda x: x[1], reverse=True)
        return scored
