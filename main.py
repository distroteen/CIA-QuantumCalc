import argparse
from cli.repl import start_repl
from api.server import run_api
from utils.logger import log

def main():
    parser = argparse.ArgumentParser(description="CIA QuantumCalc - Super Calculadora")
    parser.add_argument("--mode", choices=["cli", "api"], default="cli")
    args = parser.parse_args()

    if args.mode == "cli":
        start_repl()
    elif args.mode == "api":
        log("API iniciada em http://localhost:5000")
        run_api()

if __name__ == "__main__":
    main()
