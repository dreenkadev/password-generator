#!/usr/bin/env python3
"""Password Generator - Entry point"""

import argparse

from src import (
    VERSION, Colors, PasswordGenerator,
    print_banner, print_password, print_multiple
)


def main():
    parser = argparse.ArgumentParser(
        description="Secure Password Generator"
    )
    parser.add_argument("-l", "--length", type=int, default=16, help="Password length")
    parser.add_argument("-c", "--count", type=int, default=1, help="Number of passwords")
    parser.add_argument("--no-lower", action="store_true", help="Exclude lowercase")
    parser.add_argument("--no-upper", action="store_true", help="Exclude uppercase")
    parser.add_argument("--no-digits", action="store_true", help="Exclude digits")
    parser.add_argument("--no-symbols", action="store_true", help="Exclude symbols")
    parser.add_argument("--no-ambiguous", action="store_true", help="Exclude ambiguous chars (l1IO0)")
    parser.add_argument("--passphrase", action="store_true", help="Generate passphrase")
    parser.add_argument("--words", type=int, default=4, help="Words in passphrase")
    parser.add_argument("--version", action="version", version=f"v{VERSION}")
    
    args = parser.parse_args()
    
    print_banner()
    
    generator = PasswordGenerator(
        length=args.length,
        use_lower=not args.no_lower,
        use_upper=not args.no_upper,
        use_digits=not args.no_digits,
        use_symbols=not args.no_symbols,
        exclude_ambiguous=args.no_ambiguous
    )
    
    if args.passphrase:
        passphrase = generator.generate_passphrase(words=args.words)
        print(f"\n{Colors.BOLD}Generated Passphrase:{Colors.RESET}")
        print(f"  {Colors.CYAN}{passphrase}{Colors.RESET}")
        return
    
    if args.count > 1:
        passwords = generator.generate_multiple(args.count)
        print_multiple(passwords)
    else:
        password = generator.generate()
        print_password(password)


if __name__ == "__main__":
    main()
