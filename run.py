import sys
from blockchain.chain import Blockchain

def main():
    if sys.platform == "linux" and "android" in sys.version.lower():
        print("🔋 Modo Android ativado (otimizações de bateria)")
        # Configurações especiais para Android
    else:
        print("⚡ Modo desktop ativado")

if __name__ == "__main__":
    main()
