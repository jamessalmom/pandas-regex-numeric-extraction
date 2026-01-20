"""
Extração de valores numéricos de strings com regex.

Útil para limpar campos como "Valor: R$ 1.234,56" -> 1234.56,
tratando separador de milhar (.) e decimal (,) no padrão brasileiro.
"""
import pandas as pd

PADRAO_NUMERO = r'(\d{1,3}(?:\.\d{3})*(?:,\d+)?|\d+(?:\.\d+)?)'


def extrair_valores_numericos(df: pd.DataFrame, coluna: str, nova_coluna: str = None) -> pd.DataFrame:
    """
    Extrai o primeiro valor numérico encontrado em `coluna` e converte para float,
    tratando o formato brasileiro de milhar/decimal.

    Exemplo:
        df['valor_numerico'] = extrair_valores_numericos(df, 'texto')
    """
    nova_coluna = nova_coluna or f"{coluna}_numerico"

    extraido = df[coluna].astype(str).str.extract(PADRAO_NUMERO, expand=False)
    extraido = (
        extraido.str.replace('.', '', regex=False)
                .str.replace(',', '.', regex=False)
    )
    df[nova_coluna] = pd.to_numeric(extraido, errors='coerce')
    return df


if __name__ == "__main__":
    df = pd.DataFrame({"texto": ["Valor: R$ 1.234,56", "Total: 89,90", "sem número aqui"]})
    print(extrair_valores_numericos(df, "texto"))
