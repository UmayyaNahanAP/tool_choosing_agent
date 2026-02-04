# from agent import ToolChoosingAgent
# from executor import Executor

# def load_data(path="data/reviews.txt"):
#     with open(path) as f:
#         return f.readlines()

# if __name__ == "__main__":
#     task = "Analyze sentiment from 5,000 user reviews"
#     data = load_data()
#     dataset_size = len(data)

#     agent = ToolChoosingAgent()
#     selected_tool = agent.analyze_task(task, dataset_size)

#     executor = Executor()
#     results = executor.execute(selected_tool, data)

#     print("Selected Tool:", selected_tool["name"])
#     print("Sample Output:", results[:10])
# import os

# def load_data(path="data/reviews.txt"):
#     os.makedirs("data", exist_ok=True)

#     if not os.path.exists(path):
#         sample_data = [
#             "This product is excellent and works great",
#             "Worst purchase ever",
#             "Average quality, okay for the price",
#             "I am very happy with this",
#             "Terrible experience, not recommended"
#         ]
#         with open(path, "w", encoding="utf-8") as f:
#             f.write("\n".join(sample_data))

#     with open(path, encoding="utf-8") as f:
#         lines = [line.strip() for line in f.readlines() if line.strip()]

#     # Failsafe
#     if len(lines) == 0:
#         lines = [
#             "Good product",
#             "Bad experience",
#             "Neutral feeling"
#         ]

#     return lines


from agent import ToolChoosingAgent
from executor import Executor
import os

def load_data(path="data/reviews.txt"):
    os.makedirs("data", exist_ok=True)

    # Create file if missing
    if not os.path.exists(path):
        sample_data = [
            "This product is excellent and works great",
            "Worst purchase ever",
            "Average quality, okay for the price",
            "I am very happy with this",
            "Terrible experience, not recommended"
        ]
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(sample_data))

    # Load + clean
    with open(path, encoding="utf-8") as f:
        data = [line.strip() for line in f if line.strip()]

    # Final failsafe
    if len(data) == 0:
        data = [
            "Good product",
            "Bad experience",
            "Neutral feeling"
        ]

    return data

if __name__ == "__main__":
    task = "Analyze sentiment from 5,000 user reviews"

    data = load_data()
    dataset_size = len(data)   # ✅ now correct

    agent = ToolChoosingAgent()
    selected_tool = agent.analyze_task(task, dataset_size)

    executor = Executor()
    results = executor.execute(selected_tool, data)

    print("\n=== AUTONOMOUS AGENT OUTPUT ===")
    print("Selected Tool:", selected_tool["name"])
    print("Dataset Size Used:", dataset_size)
    print("Sample Output:", results[:10])

