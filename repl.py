import code
from utils.logger import log

def start_repl():
    log("Iniciando CIA QuantumCalc REPL... (digite Ctrl+D para sair)")
    code.interact(local=dict(globals(), **locals()))
