# Extração de valores numéricos (Janeiro)

Método pandas + regex para extrair valores numéricos de strings como
"Valor: R$ 1.234,56" -> 1234.56, tratando separador de milhar (.) e decimal (,)
no padrão brasileiro.

## Uso
```python
import pandas as pd
from extrair_valores_numericos import extrair_valores_numericos

df = pd.DataFrame({"texto": ["Valor: R$ 1.234,56", "Total: 89,90"]})
df = extrair_valores_numericos(df, "texto")
```
