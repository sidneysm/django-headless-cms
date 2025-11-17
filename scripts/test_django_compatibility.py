#!/usr/bin/env python3
"""
Script para testar compatibilidade com diferentes versões do Django
"""
import subprocess
import sys
from pathlib import Path

DJANGO_VERSIONS = ["4.2", "5.0", "5.1", "5.2"]
PROJECT_ROOT = Path(__file__).parent.parent

def test_django_version(version):
    """Testa uma versão específica do Django"""
    print(f"\n🧪 Testando Django {version}...")

    try:
        # Instala a versão específica do Django
        subprocess.run([
            "uv", "add", f"Django~={version}.0"
        ], check=True, cwd=PROJECT_ROOT)

        # Executa os testes
        result = subprocess.run([
            "uv", "run", "--group", "test", "python", "-m", "pytest",
            "tests/", "-v", "--tb=short"
        ], cwd=PROJECT_ROOT, capture_output=True, text=True, check=False)

        if result.returncode == 0:
            print(f"✅ Django {version}: PASSOU")
            return True
        else:
            print(f"❌ Django {version}: FALHOU")
            print(f"Erro: {result.stderr}")
            return False

    except subprocess.CalledProcessError as e:
        print(f"❌ Django {version}: ERRO na instalação - {e}")
        return False

def main():
    """Função principal"""
    print("🚀 Testando compatibilidade com diferentes versões do Django")

    results = {}
    for version in DJANGO_VERSIONS:
        results[version] = test_django_version(version)

    print("\n📊 Resumo dos testes:")
    for version, passed in results.items():
        status = "✅ PASSOU" if passed else "❌ FALHOU"
        print(f"  Django {version}: {status}")

    failed_versions = [v for v, passed in results.items() if not passed]
    if failed_versions:
        print(f"\n⚠️  Versões com falha: {', '.join(failed_versions)}")
        sys.exit(1)
    else:
        print("\n🎉 Todas as versões passaram!")

if __name__ == "__main__":
    main()
