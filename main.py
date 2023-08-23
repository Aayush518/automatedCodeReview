import json
from analyzer import EnhancedCodeAnalyzer

def code_inspection_party():
    code_investigator = EnhancedCodeAnalyzer()
    file_quest = input("Greetings! Provide the path to your enchanted code scroll: ")

    try:
        inspection_results = code_investigator.scrutinize(file_quest)
        print("Results of the Enchanted Code Inspection:")
        print(json.dumps(inspection_results, indent=2))

        average_score = code_investigator.get_average_score(file_quest)
        if average_score is not None:
            print(f"Average Code Quality Score: {average_score:.2f}")

        common_issues = code_investigator.get_most_common_issues(file_quest)
        if common_issues:
            print("Most Common Issues:")
            for issue in common_issues:
                print(f"- {issue['message']} ({issue['category']})")

        if 'suggestions' in inspection_results:
            print("\nSuggestions for Improvement:")
            for suggestion in inspection_results['suggestions']:
                print(f"- {suggestion}")

        function_list = code_investigator.get_function_list(file_quest)
        if function_list:
            print("\nFunctions found in the code:")
            for function in function_list:
                print(f"- {function}")

        class_list = code_investigator.get_class_list(file_quest)
        if class_list:
            print("\nClasses found in the code:")
            for class_name in class_list:
                print(f"- {class_name}")

        complexity = code_investigator.get_code_complexity(file_quest)
        if complexity != -1:
            print(f"\nCode Complexity: {complexity}")

    except Exception as e:
        print(e)

if __name__ == "__main__":
    code_inspection_party()
