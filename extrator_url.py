import re


class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()

    def sanitiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url:
            raise ValueError("A URL está vazia")

        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(url)
        if not match:
            raise ValueError("A URL não é válida")

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametros(self):
        indice_interrogacao = self.url.find('?')
        url_parametros = self.url[indice_interrogacao + 1:]
        return url_parametros

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametros().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) + 1
        indice_e_comercial = self.get_url_parametros().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametros()[indice_valor:]
        else:
            valor = self.get_url_parametros()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + "\n" + "Parâmetros: " + self.get_url_parametros() + "\n" + "URL Base: " + self.get_url_base()

    def __eq__(self, other):
        return self.url == other.url

url = "bytebank.com/cambio?quantidade=100&moedaOrigem=dolar&moedaDestino=real"
extrator_url = ExtratorURL(url)
extrator_url_2 = ExtratorURL(url)
# print("O tamanho da URL: ", len(extrator_url))
# print(extrator_url)

# print(extrator_url == extrator_url_2)

valor_quantidade = extrator_url.get_valor_parametro("quantidade")
# print(valor_quantidade)


###DESAFIO###
# valor_dolar = 5.50  # 1 dólar = 5.50 reais
def conversao_dolar_real():
    moeda_origem = extrator_url.get_valor_parametro("moedaOrigem")
    moeda_destino = extrator_url.get_valor_parametro("moedaDestino")
    quantidade = extrator_url.get_valor_parametro("quantidade")

    valor_dolar = float(input("Digite o valor do dolar: "))

    if moeda_origem == 'dolar' and moeda_destino == 'real':
        valor_final = float(quantidade) / valor_dolar
    elif moeda_origem == 'real' and moeda_destino == 'dolar':
        valor_final = float(quantidade) * valor_dolar
    else:
        raise ValueError("A url não possui ambos parâmetros.")

    valor_final_formatado = f"{valor_final:.2f}"
    return  valor_final_formatado

print("O valor em real:",conversao_dolar_real())

###DESAFIO FEITO PELO PROFESSOR###
VALOR_DOLAR = 5.50  # 1 dólar = 5.50 reais
moeda_origem1 = extrator_url.get_valor_parametro("moedaOrigem1")
moeda_destino1 = extrator_url.get_valor_parametro("moedaDestino1")
quantidade1 = extrator_url.get_valor_parametro("quantidade1")

if moeda_origem1 == "real" and moeda_destino1 == "dolar":
    valor_conversao1 = int(quantidade1) / VALOR_DOLAR
    print("O valor de R$" + quantidade1 + " reais é igual a $" + str(valor_conversao1) + " dólares.")
elif moeda_origem1 == "dolar" and moeda_destino1 == "real":
    valor_conversao = int(quantidade1) * VALOR_DOLAR
    print("O valor de $" + quantidade1 + " dólares é igual a R$" + str(valor_conversao) + " reais.")
else:
    print(f"Câmbio de {moeda_origem1} para {moeda_destino1} não está disponível.")

