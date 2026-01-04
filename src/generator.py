"""Password Generator - Core generator"""

import re
import secrets
import string
import math
from dataclasses import dataclass
from typing import List, Dict, Optional

from .constants import CHARSETS, STRENGTH_CRITERIA, WEAK_PATTERNS


@dataclass
class Password:
    value: str
    length: int
    entropy: float
    strength: str
    has_lower: bool
    has_upper: bool
    has_digit: bool
    has_symbol: bool


class PasswordGenerator:
    def __init__(
        self,
        length: int = 16,
        use_lower: bool = True,
        use_upper: bool = True,
        use_digits: bool = True,
        use_symbols: bool = True,
        exclude_ambiguous: bool = False,
        custom_chars: str = ""
    ):
        self.length = length
        self.use_lower = use_lower
        self.use_upper = use_upper
        self.use_digits = use_digits
        self.use_symbols = use_symbols
        self.exclude_ambiguous = exclude_ambiguous
        self.custom_chars = custom_chars
        self.charset = self._build_charset()
    
    def _build_charset(self) -> str:
        if self.custom_chars:
            return self.custom_chars
        
        charset = ""
        if self.use_lower:
            charset += CHARSETS['lowercase']
        if self.use_upper:
            charset += CHARSETS['uppercase']
        if self.use_digits:
            charset += CHARSETS['digits']
        if self.use_symbols:
            charset += CHARSETS['symbols']
        
        if self.exclude_ambiguous:
            for char in CHARSETS['ambiguous']:
                charset = charset.replace(char, '')
        
        return charset
    
    def generate(self) -> Password:
        if not self.charset:
            self.charset = CHARSETS['lowercase'] + CHARSETS['uppercase'] + CHARSETS['digits']
        
        password = ''.join(secrets.choice(self.charset) for _ in range(self.length))
        
        # Ensure at least one of each required type
        if self.use_lower and not any(c in CHARSETS['lowercase'] for c in password):
            idx = secrets.randbelow(self.length)
            password = password[:idx] + secrets.choice(CHARSETS['lowercase']) + password[idx+1:]
        if self.use_upper and not any(c in CHARSETS['uppercase'] for c in password):
            idx = secrets.randbelow(self.length)
            password = password[:idx] + secrets.choice(CHARSETS['uppercase']) + password[idx+1:]
        if self.use_digits and not any(c in CHARSETS['digits'] for c in password):
            idx = secrets.randbelow(self.length)
            password = password[:idx] + secrets.choice(CHARSETS['digits']) + password[idx+1:]
        if self.use_symbols and not any(c in CHARSETS['symbols'] for c in password):
            idx = secrets.randbelow(self.length)
            password = password[:idx] + secrets.choice(CHARSETS['symbols']) + password[idx+1:]
        
        return self._analyze(password)
    
    def generate_multiple(self, count: int) -> List[Password]:
        return [self.generate() for _ in range(count)]
    
    def _analyze(self, password: str) -> Password:
        has_lower = any(c in CHARSETS['lowercase'] for c in password)
        has_upper = any(c in CHARSETS['uppercase'] for c in password)
        has_digit = any(c in CHARSETS['digits'] for c in password)
        has_symbol = any(c in CHARSETS['symbols'] for c in password)
        
        char_types = sum([has_lower, has_upper, has_digit, has_symbol])
        entropy = len(password) * math.log2(len(self.charset)) if self.charset else 0
        
        # Determine strength
        if len(password) >= 16 and char_types >= 4:
            strength = 'very_strong'
        elif len(password) >= 12 and char_types >= 4:
            strength = 'strong'
        elif len(password) >= 10 and char_types >= 3:
            strength = 'good'
        elif len(password) >= 8 and char_types >= 2:
            strength = 'fair'
        else:
            strength = 'weak'
        
        return Password(
            value=password,
            length=len(password),
            entropy=round(entropy, 2),
            strength=strength,
            has_lower=has_lower,
            has_upper=has_upper,
            has_digit=has_digit,
            has_symbol=has_symbol
        )
    
    def generate_passphrase(self, words: int = 4, separator: str = "-") -> str:
        wordlist = [
            "correct", "horse", "battery", "staple", "cloud", "thunder",
            "rocket", "sunset", "garden", "crystal", "harbor", "falcon",
            "silver", "phoenix", "dragon", "castle", "wizard", "forest",
            "ocean", "thunder", "cosmic", "stellar", "quantum", "cipher"
        ]
        return separator.join(secrets.choice(wordlist) for _ in range(words))
