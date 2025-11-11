class Log:
    def __init__(self, max_size=100):
        self.operations = []
        self.max_size = max_size
    
    def add_operation(self, operation: str, a: float, b: float, result: float):
        if len(self.operations) >= self.max_size:
            self.operations.pop(0)
        
        self.operations.append({
            'operation': operation,
            'a': a,
            'b': b,
            'result': result
        })
    
    def get_last_operation(self):
        return self.operations[-1] if self.operations else None
    
    def get_all_operations(self):
        return self.operations.copy()
    
    def clear_history(self):
        self.operations.clear()