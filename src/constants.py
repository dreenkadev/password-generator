"""Password Generator - Constants"""

VERSION = "1.0.0"

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    DIM = '\033[2m'
    RESET = '\033[0m'

# Character sets
CHARSETS = {
    'lowercase': 'abcdefghijklmnopqrstuvwxyz',
    'uppercase': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
    'digits': '0123456789',
    'symbols': '!@#$%^&*()_+-=[]{}|;:,.<>?',
    'special': '~`\'"\\/',
    'ambiguous': 'l1IO0'
}

# Password strength criteria
STRENGTH_CRITERIA = {
    'weak': {'min_length': 6, 'min_types': 1},
    'fair': {'min_length': 8, 'min_types': 2},
    'good': {'min_length': 10, 'min_types': 3},
    'strong': {'min_length': 12, 'min_types': 4},
    'very_strong': {'min_length': 16, 'min_types': 4}
}

# Common password patterns to avoid
WEAK_PATTERNS = [
    r'(.)\1{2,}',           # Repeated characters
    r'(012|123|234|345|456|567|678|789|890)',  # Sequential numbers
    r'(abc|bcd|cde|def|efg|fgh|ghi|hij|ijk|jkl|klm|lmn|mno|nop|opq|pqr|qrs|rst|stu|tuv|uvw|vwx|wxy|xyz)',
    r'^[a-z]+$',            # Only lowercase
    r'^[0-9]+$',            # Only numbers
]
