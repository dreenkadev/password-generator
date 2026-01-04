"""Password Generator - Output formatting"""

from typing import List
from .constants import VERSION, Colors
from .generator import Password


def print_banner():
    print(f"""{Colors.CYAN}
  ____                                     _ 
 |  _ \\ __ _ ___ _____      _____  _ __ __| |
 | |_) / _` / __/ __\\ \\ /\\ / / _ \\| '__/ _` |
 |  __/ (_| \\__ \\__ \\\\ V  V / (_) | | | (_| |
 |_|   \\__,_|___/___/ \\_/\\_/ \\___/|_|  \\__,_|
   ____                           _             
  / ___| ___ _ __   ___ _ __ __ _| |_ ___  _ __ 
 | |  _ / _ \\ '_ \\ / _ \\ '__/ _` | __/ _ \\| '__|
 | |_| |  __/ | | |  __/ | | (_| | || (_) | |   
  \\____|\\___|_| |_|\\___|_|  \\__,_|\\__\\___/|_|   
{Colors.RESET}                                     v{VERSION}
""")


def print_password(password: Password, show_analysis: bool = True):
    strength_colors = {
        'weak': Colors.RED,
        'fair': Colors.YELLOW,
        'good': Colors.GREEN,
        'strong': Colors.GREEN,
        'very_strong': Colors.CYAN
    }
    
    color = strength_colors.get(password.strength, Colors.DIM)
    
    print(f"\n{Colors.BOLD}Generated Password:{Colors.RESET}")
    print(f"  {Colors.CYAN}{password.value}{Colors.RESET}")
    
    if show_analysis:
        print(f"\n{Colors.BOLD}Analysis:{Colors.RESET}")
        print(f"  Length: {password.length}")
        print(f"  Entropy: {password.entropy} bits")
        print(f"  Strength: {color}{password.strength.upper()}{Colors.RESET}")
        
        checks = []
        if password.has_lower:
            checks.append(f"{Colors.GREEN}lowercase{Colors.RESET}")
        if password.has_upper:
            checks.append(f"{Colors.GREEN}UPPERCASE{Colors.RESET}")
        if password.has_digit:
            checks.append(f"{Colors.GREEN}digits{Colors.RESET}")
        if password.has_symbol:
            checks.append(f"{Colors.GREEN}symbols{Colors.RESET}")
        
        print(f"  Contains: {', '.join(checks)}")


def print_multiple(passwords: List[Password]):
    print(f"\n{Colors.BOLD}Generated Passwords:{Colors.RESET}")
    print(f"{Colors.CYAN}{'─' * 50}{Colors.RESET}")
    
    for i, p in enumerate(passwords, 1):
        strength_colors = {
            'weak': Colors.RED,
            'fair': Colors.YELLOW,
            'good': Colors.GREEN,
            'strong': Colors.GREEN,
            'very_strong': Colors.CYAN
        }
        color = strength_colors.get(p.strength, Colors.DIM)
        print(f"  {i}. {p.value} {color}[{p.strength}]{Colors.RESET}")
