#!/usr/bin/env python3
"""
Password Generator - Generate secure random passwords
"""

import argparse
import random
import string
import hashlib

VERSION = "1.0.0"

class Colors:
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BOLD = '\033[1m'
    RESET = '\033[0m'


def generate_password(length: int = 16, uppercase: bool = True, lowercase: bool = True,
                      digits: bool = True, special: bool = True, exclude: str = "") -> str:
    """Generate a random password"""
    chars = ""
    
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if digits:
        chars += string.digits
    if special:
        chars += "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Remove excluded characters
    for c in exclude:
        chars = chars.replace(c, "")
    
    if not chars:
        return ""
    
    # Ensure at least one of each required type
    password = []
    if uppercase and string.ascii_uppercase:
        password.append(random.choice([c for c in string.ascii_uppercase if c not in exclude]))
    if lowercase and string.ascii_lowercase:
        password.append(random.choice([c for c in string.ascii_lowercase if c not in exclude]))
    if digits:
        password.append(random.choice([c for c in string.digits if c not in exclude]))
    if special:
        special_chars = [c for c in "!@#$%^&*()_+-=[]{}|;:,.<>?" if c not in exclude]
        if special_chars:
            password.append(random.choice(special_chars))
    
    # Fill remaining
    while len(password) < length:
        password.append(random.choice(chars))
    
    # Shuffle
    random.shuffle(password)
    
    return ''.join(password[:length])


def check_strength(password: str) -> dict:
    """Check password strength"""
    score = 0
    feedback = []
    
    if len(password) >= 12:
        score += 25
    elif len(password) >= 8:
        score += 10
    else:
        feedback.append("Too short")
    
    if any(c.isupper() for c in password):
        score += 20
    else:
        feedback.append("Add uppercase")
    
    if any(c.islower() for c in password):
        score += 20
    else:
        feedback.append("Add lowercase")
    
    if any(c.isdigit() for c in password):
        score += 20
    else:
        feedback.append("Add digits")
    
    if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in password):
        score += 15
    else:
        feedback.append("Add special chars")
    
    if len(password) >= 16:
        score = min(100, score + 10)
    
    if score >= 80:
        strength = "Strong"
    elif score >= 50:
        strength = "Medium"
    else:
        strength = "Weak"
    
    return {'score': score, 'strength': strength, 'feedback': feedback}


def print_banner():
    print(f"""{Colors.CYAN}
  ____                                     _    ____            
 |  _ \ __ _ ___ _____      _____  _ __ __| |  / ___| ___ _ __  
 | |_) / _` / __/ __\ \ /\ / / _ \| '__/ _` | | |  _ / _ \ '_ \ 
 |  __/ (_| \__ \__ \\ V  V / (_) | | | (_| | | |_| |  __/ | | |
 |_|   \__,_|___/___/ \_/\_/ \___/|_|  \__,_|  \____|\___|_| |_|
{Colors.RESET}                                                   v{VERSION}
""")


def main():
    parser = argparse.ArgumentParser(description="Password Generator")
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length")
    parser.add_argument("-n", "--count", type=int, default=1, help="Number of passwords")
    parser.add_argument("--no-upper", action="store_true", help="No uppercase")
    parser.add_argument("--no-lower", action="store_true", help="No lowercase")
    parser.add_argument("--no-digits", action="store_true", help="No digits")
    parser.add_argument("--no-special", action="store_true", help="No special chars")
    parser.add_argument("-e", "--exclude", default="", help="Characters to exclude")
    parser.add_argument("-c", "--check", help="Check password strength")
    parser.add_argument("--demo", action="store_true", help="Run demo")
    
    args = parser.parse_args()
    print_banner()
    
    if args.demo:
        print(f"{Colors.CYAN}Generated Passwords:{Colors.RESET}")
        for i in range(5):
            pwd = generate_password(16)
            strength = check_strength(pwd)
            color = Colors.GREEN if strength['strength'] == 'Strong' else Colors.YELLOW
            print(f"  {pwd}  {color}[{strength['strength']}]{Colors.RESET}")
        return
    
    if args.check:
        result = check_strength(args.check)
        color = Colors.GREEN if result['score'] >= 80 else Colors.YELLOW if result['score'] >= 50 else Colors.RED
        print(f"{Colors.BOLD}Strength:{Colors.RESET} {color}{result['strength']} ({result['score']}/100){Colors.RESET}")
        if result['feedback']:
            print(f"{Colors.BOLD}Suggestions:{Colors.RESET} {', '.join(result['feedback'])}")
        return
    
    print(f"{Colors.BOLD}Generated Passwords:{Colors.RESET}\n")
    for i in range(args.count):
        pwd = generate_password(
            length=args.length,
            uppercase=not args.no_upper,
            lowercase=not args.no_lower,
            digits=not args.no_digits,
            special=not args.no_special,
            exclude=args.exclude
        )
        strength = check_strength(pwd)
        color = Colors.GREEN if strength['strength'] == 'Strong' else Colors.YELLOW
        print(f"  {pwd}  {color}[{strength['strength']}]{Colors.RESET}")


if __name__ == "__main__":
    main()
