import subprocess
import json

class EnhancedCodeAnalyzer:
    def __init__(self):
        self.analysis_cache = {}
    
    def scrutinize(self, file_path):
        if not self._is_valid_file(file_path):
            return "Oops! This doesn't look like a wizard's spell book (Python file)."
        
        if file_path in self.analysis_cache:
            return self.analysis_cache[file_path]
        
        commando = ['pylint', '--output-format=json', '--reports=no', file_path]
        
        try:
            process_output = subprocess.check_output(commando, stderr=subprocess.STDOUT).decode('utf-8')
            parsed_result = self._parse_output(process_output)
            self.analysis_cache[file_path] = parsed_result
            return parsed_result
            
        except subprocess.CalledProcessError as ex:
            error_msg = f"Magical mishap! An error occurred during analysis: {ex.output}"
            raise Exception(error_msg)
    
    def get_average_score(self, file_path):
        parsed_result = self.scrutinize(file_path)
        if 'global_note' in parsed_result:
            return parsed_result['global_note']
        return None
    
    def get_most_common_issues(self, file_path, num_issues=5):
        parsed_result = self.scrutinize(file_path)
        issues = parsed_result.get('messages', [])
        if issues:
            sorted_issues = sorted(issues, key=lambda x: x['message'], reverse=True)
            return sorted_issues[:num_issues]
        return []
    
    def _parse_output(self, output_data):
        try:
            parsed_result = json.loads(output_data)
            return parsed_result
        except json.JSONDecodeError as json_err:
            print(f"Oops! Error deciphering the mystical JSON: {json_err}")
            return {}
    
    def _is_valid_file(self, file_path):
        return file_path.endswith('.py')
