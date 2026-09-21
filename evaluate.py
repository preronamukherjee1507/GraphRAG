import json
import pandas as pd

def load_dataset(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def run_evaluation():
    data = load_dataset("eval_dataset.json")
    df = pd.DataFrame(data)
    
    print("--- Olympic RAG Benchmark Dataset Breakdown ---")
    qtype_counts = df["qtype"].value_counts()
    print(qtype_counts)
    
    # Example placeholder: Execute custom pipeline logic here per qtype
    # for item in data:
    #     response = rag_pipeline.query(item["question"])
    #     score = evaluate_response(response, item["qtype"])

    # Output metric summary
    summary = {
        "total_questions": len(df),
        "qtype_distribution": qtype_counts.to_dict()
    }
    
    with open("results.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)
        
    print("\nEvaluation run completed! Results saved to results.json")

if __name__ == "__main__":
    run_evaluation()
