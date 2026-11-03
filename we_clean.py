import pandas as pd
import math


# ============================================================
# 01. FUNÇÕES DE DIAGNÓSTICO
# ============================================================

def contar_nulos(df):
    """Conta todas as células com valores nulos."""
    total = df.isnull().sum().sum()
    return total


def contar_duplicatas(df):
    """Conta as linhas duplicadas do DataFrame."""
    total = df.duplicated().sum()
    return total

def encontrar_colunas_vazias(df):
    """Retorna uma lista com colunas totalmente vazias."""
    colunas_vazias = df.columns[df.isnull().all()].tolist()
    return colunas_vazias

def resumo_dataframe(df):
    """Retorna a quantidade de linhas e colunas."""
    linhas = df.shape[0]
    colunas = df.shape[1]
    return linhas, colunas


def gerar_relatorio(df):
    """Organiza os indicadores do DataFrame em um dicionário."""
    linhas, colunas = resumo_dataframe(df)

    relatorio = {
        "linhas": linhas,
        "colunas": colunas,
        "tipos_dados": df.dtypes.astype(str).to_dict(),
        "nulos": contar_nulos(df),
        "duplicatas": contar_duplicatas(df)
    }

    return relatorio


# ============================================================
# 02. FUNÇÕES DE LIMPEZA
# ============================================================

def remover_duplicatas(df):
    """Remove linhas duplicadas."""
    df_limpo = df.drop_duplicates()
    return df_limpo


def remover_nulos(df):
    """Remove linhas que contêm valores nulos."""
    df_limpo = df.dropna()
    return df_limpo


def substituir_nulos(df, valor):
    """Substitui valores nulos pelo valor informado."""
    df_limpo = df.fillna(valor)
    return df_limpo


def substituir_nulos_media(df):
    """Substitui nulos das colunas numéricas pela média."""
    df_limpo = df.copy()

    colunas_numericas = df_limpo.select_dtypes(
        include="number"
    ).columns

    for coluna in colunas_numericas:
        media = df_limpo[coluna].mean()
        df_limpo[coluna] = df_limpo[coluna].fillna(media)

    return df_limpo


def substituir_nulos_mediana(df):
    """Substitui nulos das colunas numéricas pela mediana."""
    df_limpo = df.copy()

    colunas_numericas = df_limpo.select_dtypes(
        include="number"
    ).columns

    for coluna in colunas_numericas:
        mediana = df_limpo[coluna].median()
        df_limpo[coluna] = df_limpo[coluna].fillna(mediana)

    return df_limpo


def substituir_nulos_moda(df):
    """Substitui nulos pela moda de cada coluna."""
    df_limpo = df.copy()

    for coluna in df_limpo.columns:

        if df_limpo[coluna].isnull().sum() > 0:
            moda = df_limpo[coluna].mode()

            if not moda.empty:
                df_limpo[coluna] = df_limpo[coluna].fillna(moda[0])

    return df_limpo


def remover_espacos_texto(df):
    """Remove espaços extras no início e no fim das colunas de texto."""
    df_limpo = df.copy()

    colunas_texto = df_limpo.select_dtypes(
        include="object"
    ).columns

    for coluna in colunas_texto:
        df_limpo[coluna] = df_limpo[coluna].apply(
            lambda valor: valor.strip()
            if isinstance(valor, str)
            else valor
        )

    return df_limpo


def texto_minusculo(df):
    """Converte colunas de texto para letras minúsculas."""
    df_limpo = df.copy()

    colunas_texto = df_limpo.select_dtypes(
        include="object"
    ).columns

    for coluna in colunas_texto:
        df_limpo[coluna] = df_limpo[coluna].apply(
            lambda valor: valor.lower()
            if isinstance(valor, str)
            else valor
        )

    return df_limpo


def texto_maiusculo(df):
    """Converte colunas de texto para letras maiúsculas."""
    df_limpo = df.copy()

    colunas_texto = df_limpo.select_dtypes(
        include="object"
    ).columns

    for coluna in colunas_texto:
        df_limpo[coluna] = df_limpo[coluna].apply(
            lambda valor: valor.upper()
            if isinstance(valor, str)
            else valor
        )

    return df_limpo


def remover_colunas_vazias(df):
    """Remove colunas totalmente vazias."""
    colunas_vazias = encontrar_colunas_vazias(df)
    df_limpo = df.drop(columns=colunas_vazias)
    return df_limpo


# ============================================================
# 03. FUNÇÕES DE VALIDAÇÃO
# ============================================================

def solicitar_numero():
    """Solicita um número válido ao usuário."""

    while True:
        try:
            valor = float(input("Digite um número: "))

            if not math.isfinite(valor):
                print("❌ ERRO: Digite um número finito.")
                continue

            return valor

        except ValueError:
            print("❌ ERRO: Digite um número válido!")


def solicitar_sim_nao(mensagem):
    """Solicita uma resposta válida entre S ou N."""

    while True:
        resposta = input(mensagem).strip().upper()

        if resposta == "S" or resposta == "N":
            return resposta

        print("❌ ERRO: Digite apenas S ou N.")


def solicitar_opcao(opcoes_validas):
    """Solicita uma opção até que seja válida."""

    while True:
        opcao = input("Digite a opção desejada: ").strip()

        if opcao in opcoes_validas:
            return opcao

        print("❌ ERRO: Opção inválida.")


# ============================================================
# 04. FUNÇÕES DE IMPORTAÇÃO
# ============================================================

def carregar_csv(caminho):
    """Carrega um CSV e trata erros de importação."""

    try:
        df = pd.read_csv(caminho)

        print("✓ Arquivo carregado com sucesso!")
        return df

    except FileNotFoundError:
        print("❌ ERRO: Arquivo CSV não encontrado!")
        return None

    except pd.errors.EmptyDataError:
        print("❌ ERRO: Arquivo CSV está vazio!")
        return None

    except (PermissionError, UnicodeError, OSError) as erro:
        print("❌ ERRO: Não foi possível ler o arquivo CSV.")
        print(f"Detalhes: {erro}")
        return None

# ============================================================
# 05. IMPORTAÇÃO DO ARQUIVO CSV
# ============================================================

print("\n===== IMPORTAÇÃO DO ARQUIVO =====")

caminho_arquivo = input(
    "Digite o caminho do arquivo CSV que deseja analisar: "
).strip()

df = carregar_csv(caminho_arquivo)

if df is None:
    raise SystemExit("⚠ Não foi possível iniciar o We Clean.")

acoes_realizadas = []

linhas_originais = df.shape[0]
nulos_originais = contar_nulos(df)
duplicatas_originais = contar_duplicatas(df)

print("\n===== PRÉVIA DO ARQUIVO =====")
print(df.head())


# ============================================================
# 06. DIAGNÓSTICO INICIAL
# ============================================================

print("\n===== DIAGNÓSTICO INICIAL =====")

linhas, colunas = resumo_dataframe(df)

print(f"Quantidade de linhas: {linhas}")
print(f"Quantidade de colunas: {colunas}")
print(f"Total de valores nulos: {nulos_originais}")
print(f"Total de linhas duplicadas: {duplicatas_originais}")

print("\nTipos de dados encontrados:")
print(df.dtypes)

nulos_por_coluna = df.isnull().sum()

colunas_com_nulos = nulos_por_coluna[
    nulos_por_coluna > 0
]

print("\nColunas com valores nulos:")

if colunas_com_nulos.empty:
    print("✓ Nenhuma coluna possui valores nulos.")
else:
    print(colunas_com_nulos)

linhas_duplicadas = df[df.duplicated()]

print("\nLinhas duplicadas:")

if linhas_duplicadas.empty:
    print("✓ Nenhuma linha duplicada encontrada.")
else:
    print(linhas_duplicadas)

if linhas_originais > 0:
    percentual_nulos = (
        nulos_por_coluna / linhas_originais
    ) * 100
else:
    percentual_nulos = nulos_por_coluna * 0

print("\nPercentual de nulos por coluna:")
print(percentual_nulos)

# ============================================================
# 07. VERIFICAÇÃO DE COLUNAS TOTALMENTE VAZIAS
# ============================================================

print("\n===== COLUNAS TOTALMENTE VAZIAS =====")

colunas_vazias = encontrar_colunas_vazias(df)

if len(colunas_vazias) > 0:
    print("⚠ Colunas totalmente vazias encontradas:")
    print(colunas_vazias)

    resposta_colunas = solicitar_sim_nao(
        "Deseja remover essas colunas? [S/N]: "
    )

    if resposta_colunas == "S":
        df = remover_colunas_vazias(df)

        acoes_realizadas.append(
            f"Colunas totalmente vazias removidas: {colunas_vazias}"
        )

        print("✓ Colunas totalmente vazias removidas!")

    else:
        print("Nenhuma coluna foi removida.")

else:
    print("✓ Nenhuma coluna totalmente vazia encontrada.")
# ============================================================
# 08. TRATAMENTO DE LINHAS DUPLICADAS
# ============================================================

print("\n===== TRATAMENTO DE DUPLICATAS =====")

duplicatas = contar_duplicatas(df)

print(f"Duplicatas encontradas: {duplicatas}")

resposta = solicitar_sim_nao(
    "Deseja remover as linhas duplicadas? [S/N]: "
)

if resposta == "S":

    if duplicatas > 0:
        df = remover_duplicatas(df)

        acoes_realizadas.append(
            f"Duplicatas removidas: {duplicatas}"
        )

        print("✓ Linhas duplicadas removidas com sucesso!")

    else:
        print("✓ Nenhuma duplicata encontrada para remoção.")

else:
    print("Nenhuma linha duplicada foi removida.")

print(f"Total de linhas restantes: {df.shape[0]}")


# ============================================================
# 09. TRATAMENTO DE VALORES NULOS
# ============================================================

print("\n===== TRATAMENTO DE VALORES NULOS =====")

nulos = contar_nulos(df)

print(f"Total de valores nulos: {nulos}")

print("\nEscolha uma opção:")
print("1 - Remover linhas com valores nulos")
print("2 - Substituir nulos por um número informado")
print("3 - Substituir nulos pela média")
print("4 - Substituir nulos pela mediana")
print("5 - Substituir nulos pela moda")
print("6 - Manter os dados originais")

opcao = solicitar_opcao(
    ["1", "2", "3", "4", "5", "6"]
)

if opcao == "1":

    if nulos > 0:
        linhas_antes = df.shape[0]
        df = remover_nulos(df)
        linhas_removidas_nulos = linhas_antes - df.shape[0]

        acoes_realizadas.append(
            f"Linhas removidas por valores nulos: {linhas_removidas_nulos}"
        )

        print("✓ Linhas com valores nulos removidas!")
    else:
        print("⚠ Nenhum valor nulo encontrado.")


elif opcao == "2":

    if nulos > 0:

        valor = solicitar_numero()

        colunas_numericas = df.select_dtypes(
            include="number"
        ).columns

        nulos_numericos_antes = (
            df[colunas_numericas].isnull().sum().sum()
        )

        df[colunas_numericas] = substituir_nulos(
            df[colunas_numericas],
            valor
        )

        acoes_realizadas.append(
            f"{nulos_numericos_antes} nulos numéricos substituídos por {valor}."
        )

        print(
            f"✓ Nulos numéricos substituídos por {valor}!"
        )

        if contar_nulos(df) > 0:
            print(
                "⚠ Ainda existem valores nulos em outras colunas."
            )

    else:
        print("⚠ Nenhum valor nulo encontrado.")


elif opcao == "3":

    if nulos > 0:
        nulos_antes = contar_nulos(df)
        df = substituir_nulos_media(df)
        tratados = nulos_antes - contar_nulos(df)

        acoes_realizadas.append(
            f"{tratados} valores nulos substituídos pela média."
        )

        print(
            "✓ Valores nulos numéricos substituídos pela média!"
        )

        if contar_nulos(df) > 0:
            print(
                "⚠ Ainda existem valores nulos em outras colunas."
            )

    else:
        print("⚠ Nenhum valor nulo encontrado.")


elif opcao == "4":

    if nulos > 0:
        nulos_antes = contar_nulos(df)
        df = substituir_nulos_mediana(df)
        tratados = nulos_antes - contar_nulos(df)

        acoes_realizadas.append(
            f"{tratados} valores nulos substituídos pela mediana."
        )

        print(
            "✓ Valores nulos numéricos substituídos pela mediana!"
        )

        if contar_nulos(df) > 0:
            print(
                "⚠ Ainda existem valores nulos em outras colunas."
            )

    else:
        print("⚠ Nenhum valor nulo encontrado.")


elif opcao == "5":

    if nulos > 0:
        nulos_antes = contar_nulos(df)
        df = substituir_nulos_moda(df)
        tratados = nulos_antes - contar_nulos(df)

        acoes_realizadas.append(
            f"{tratados} valores nulos substituídos pela moda."
        )

        print("✓ Valores nulos substituídos pela moda!")

    else:
        print("⚠ Nenhum valor nulo encontrado.")


elif opcao == "6":
    print("Nenhuma alteração realizada.")


print(
    f"Valores nulos restantes: "
    f"{contar_nulos(df)}"
)


# ============================================================
# 10. TRATAMENTO DE COLUNAS DE TEXTO
# ============================================================

print("\n===== TRATAMENTO DE TEXTO =====")

colunas_texto = df.select_dtypes(
    include="object"
).columns

if len(colunas_texto) == 0:
    print("✓ Nenhuma coluna de texto encontrada.")

else:
    print("Colunas de texto encontradas:")
    print(list(colunas_texto))

    print("\nEscolha uma opção:")
    print("1 - Remover espaços no início e no fim")
    print("2 - Converter textos para minúsculas")
    print("3 - Converter textos para maiúsculas")
    print("4 - Manter os textos originais")

    opcao_texto = solicitar_opcao(
        ["1", "2", "3", "4"]
    )

    if opcao_texto == "1":
        df = remover_espacos_texto(df)

        acoes_realizadas.append(
            "Espaços no início e no fim dos textos foram removidos."
        )

        print("✓ Espaços extras removidos!")

    elif opcao_texto == "2":
        df = texto_minusculo(df)

        acoes_realizadas.append(
            "Textos convertidos para letras minúsculas."
        )

        print("✓ Textos convertidos para minúsculas!")

    elif opcao_texto == "3":
        df = texto_maiusculo(df)

        acoes_realizadas.append(
            "Textos convertidos para letras maiúsculas."
        )

        print("✓ Textos convertidos para maiúsculas!")

    elif opcao_texto == "4":
        print("Nenhuma alteração realizada.")


# ============================================================
# 11. NOVA VERIFICAÇÃO DE DUPLICATAS
# ============================================================

print("\n===== NOVA VERIFICAÇÃO DE DUPLICATAS =====")

duplicatas_pos_texto = contar_duplicatas(df)

print(
    f"Duplicatas encontradas após os tratamentos: "
    f"{duplicatas_pos_texto}"
)

if duplicatas_pos_texto > 0:

    resposta_final_duplicatas = solicitar_sim_nao(
        "Deseja remover essas duplicatas? [S/N]: "
    )

    if resposta_final_duplicatas == "S":
        df = remover_duplicatas(df)

        acoes_realizadas.append(
            f"Duplicatas adicionais removidas após os tratamentos: {duplicatas_pos_texto}"
        )

        print(
            "✓ Duplicatas adicionais removidas com sucesso!"
        )

    else:
        print(
            "Nenhuma duplicata adicional foi removida."
        )

else:
    print(
        "✓ Nenhuma nova duplicata encontrada."
    )


# ============================================================
# 12. RELATÓRIO COMPARATIVO
# ============================================================

print("\n===== RELATÓRIO WE CLEAN =====")

linhas_finais = df.shape[0]
nulos_finais = contar_nulos(df)
duplicatas_finais = contar_duplicatas(df)

linhas_removidas = (
    linhas_originais - linhas_finais
)

reducao_nulos = (
    nulos_originais - nulos_finais
)

reducao_duplicatas = (
    duplicatas_originais - duplicatas_finais
)

if linhas_originais > 0:
    percentual_removido = (
        linhas_removidas / linhas_originais
    ) * 100
else:
    percentual_removido = 0

print(f"Linhas originais: {linhas_originais}")
print(f"Linhas finais: {linhas_finais}")
print(f"Linhas removidas: {linhas_removidas}")

print(f"\nNulos originais: {nulos_originais}")
print(f"Nulos finais: {nulos_finais}")
print(f"Redução de nulos: {reducao_nulos}")

print(
    f"\nDuplicatas originais: "
    f"{duplicatas_originais}"
)

print(
    f"Duplicatas finais: "
    f"{duplicatas_finais}"
)

print(
    f"Redução de duplicatas: "
    f"{reducao_duplicatas}"
)

print(
    f"\nPercentual de linhas removidas: "
    f"{percentual_removido:.2f}%"
)


# ============================================================
# 13. RELATÓRIO ESTRUTURADO
# ============================================================

resultado = gerar_relatorio(df)

print("\n===== RESUMO DO DATAFRAME FINAL =====")

for chave, valor in resultado.items():
    print(f"{chave}: {valor}")


# ============================================================
# 14. RELATÓRIO DE AÇÕES REALIZADAS
# ============================================================

print("\n===== AÇÕES REALIZADAS =====")

if len(acoes_realizadas) == 0:
    print("Nenhuma alteração foi realizada no arquivo.")
else:
    for numero, acao in enumerate(acoes_realizadas, start=1):
        print(f"{numero}. {acao}")


# ============================================================
# 15. EXPORTAÇÃO DO ARQUIVO TRATADO
# ============================================================

print("\n===== EXPORTAÇÃO =====")

resposta2 = solicitar_sim_nao(
    "Deseja exportar o DataFrame tratado? [S/N]: "
)

if resposta2 == "S":

    nome_arquivo = input(
        "Digite o nome do arquivo (sem .csv): "
    ).strip()

    if nome_arquivo:

        try:
            df.to_csv(
                nome_arquivo + ".csv",
                index=False
            )

            print("✓ Arquivo exportado com sucesso!")

        except (OSError, UnicodeError) as erro:
            print(
                "❌ ERRO: Não foi possível exportar o CSV."
            )
            print(f"Detalhes: {erro}")

    else:
        print(
            "⚠ Nome vazio. Exportação cancelada."
        )

else:
    print("Exportação cancelada.")