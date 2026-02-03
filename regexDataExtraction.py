import re

# These classes run the validation and data extraction
class BaseValidator:
    def __init__(self, name):
        self.name = name 
        self.regexpattern = None

    def extract(self, text):
        if len(text) > 10000: # Prevention of stupid large inputs (DoS Attack)
            return []
        
        matches = re.findall(self.regexpattern, text, re.IGNORECASE | re.DOTALL) # the last two things help with case sensitivity and overlooking data that's split by new line
        return [m[0] if isinstance(m,tuple) else m for m in matches]
        
    def validate(self, value):
        return bool(re.fullmatch(self.regexpattern, value, re.IGNORECASE))

class DataExtractor:
    def __init__(self):
        self.validators = [
            EmailValidator('Email'),
            UrlValidator('Url'),
            TimeValidator('Time'),
            CurrencyValidator('Currency'),
            HtmlTagsValidator('Html Tags'),
            HashtagsValidator('Hashtags'),
        ]
        
    def process(self, text):
        results = {}
        
        for validator in self.validators:
            raw = validator.extract(text)
            validated = [self.mask_sensitive(validator.name, item) for item in raw if validator.validate(item)]
            
            if validated:
                results[validator.name] = validated
        return results
    
    @staticmethod
    def mask_sensitive(name, value):
        if 'Email' in name:
            local, domain = value.split('@')
            return f"{local[0]}***@{domain}"
        return value

# Specific Validators for each RegexPattern
class EmailValidator(BaseValidator):
    def __init__(self, name):
        super().__init__(name)
        self.regexpattern = r'\b[a-zA-Z0-9._+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b'

class UrlValidator(BaseValidator):
    def __init__(self, name):
        super().__init__(name)
        self.regexpattern = r'https?:\/\/[a-zA-Z0-9._]+\.[a-zA-Z]{2,}(?:[\/\w /-]*)?'

class TimeValidator(BaseValidator):
    def __init__(self, name):
        super().__init__(name)
        self.regexpattern = r'\b((?:[01]?[0-9]|2[0-3]):[0-5][0-9](?:\s?(?:AM|PM))?)\b'

class CurrencyValidator(BaseValidator):
    def __init__(self, name):
        super().__init__(name)
        self.regexpattern = r'\$[0-9]{1,3}(?:,?[0-9]{3})*\.[0-9]{2}'

class HtmlTagsValidator(BaseValidator):
    def __init__(self, name):
        super().__init__(name)
        self.regexpattern = r'\</?[a-zA-Z0-9]+\>'
        
class HashtagsValidator(BaseValidator):
    def __init__(self, name):
        super().__init__(name)
        self.regexpattern = r'#[a-zA-Z0-9_]+'
        
# class CreditCardNumberValidator(BaseValidator):
#     def __init__(self, name):
#         super().__init__(name)
#         self.regexpattern = r'\b\d{4}[\s\-]?\d{4}[\s\-]?\d{4}[\s\-]?\d{4}\b'
        
# Reading Data from our sample text.
def read_input_file(filename="sample_input.txt"):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            text = f.read()
        if len(text) > 10000:
            print("Warning: Input truncated")
            text = text[:10000]
        return text
    except FileNotFoundError:
        print(f"{filename} not found.")
        return ""
    except Exception as e:
        print(f"File error: {e}")
        return ""

# Bring everything together
def main():
    print("=== Data Extraction ===")
    text = read_input_file()
    if not text:
        return
    
    extractor = DataExtractor()
    results = extractor.process(text)
    
    print("\nResults:")
    print("-" * 40)
    for data_type, values in results.items():
        print(f"\n{data_type}:")
        for i, value in enumerate(values, 1):
            print(f"  {i}. {value}")


if __name__ == '__main__':
    main()







