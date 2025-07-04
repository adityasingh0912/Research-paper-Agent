from workflow.orchestrator import run_workflow

if __name__ == "__main__":
    query = input("Enter your research topic: ")
    report = run_workflow(query)
    print(report)
