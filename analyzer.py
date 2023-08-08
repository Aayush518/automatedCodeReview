import subprocess
import json

class CodeAnalyzer:
    def analyze(self, file_path):
        cmd = ['pylint', '--output-format=json', '--reports=no', file_path]
        
        try:
            process_output = subprocess.check_output(cmd, stderr=subprocess.STDOUT).decode('utf-8')
            parsed_output = self.parse_output(process_output)
            return json.dumps(parsed_output, indent=2)
            
        except subprocess.CalledProcessError as e:
            print(f"An error occurred during static analysis: {e.output}")
    
    def parse_output(self, output):
        try:
            parsed_output = json.loads(output)
            return parsed_output
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            return {}
