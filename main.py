# author : aayush
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
            print(f"Average Code Quality Score: {average_score}")
        
        common_issues = code_investigator.get_most_common_issues(file_quest)
        if common_issues:
            print("Most Common Issues:")
            for issue in common_issues:
                print(f"- {issue['message']} ({issue['category']})")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    code_inspection_party()
