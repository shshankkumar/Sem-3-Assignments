def report_decorator(func):
    def wrapper(*args, **kwargs):
        print("Generating report...")
        result = func(*args, **kwargs)
        print("generated successfully.")
        return result
    return wrapper



class Report:
    
    
    template = "demo Report"
    
    def __init__(self, title, content):
        self.title = title
        self.content = content

    def add_content(self , text):
        self.content.append(text)
        
@classmethod
def change_template(cls, new_template):
        cls.template = new_template
        
        def __str__(self):
            return f"template: {self.template}\nContent: {self.content}\nTemplate: {self.title}"
        def __len__(self):
            return len(self.content)
        
@report_decorator
def display_report(self):
        print(self)
        print("\nReport Content:")
        for item in self.content:
            print("- " + item)
        print(f"\nTotal items in report: {len(self)}")
        
output:         
                    
        
