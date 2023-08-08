from analyzer import CodeAnalyzer

def main():
    analyzer = CodeAnalyzer()
    file_path = input("Enter the path to the source code file: ")
    analysis_results = analyzer.analyze(file_path)
    print("Analysis Results:")
    print(analysis_results)

if __name__ == "__main__":
    main()
