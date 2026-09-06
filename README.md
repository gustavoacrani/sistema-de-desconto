# 🛍️ Sistema de Desconto Progressivo

Uma aplicação em **Python** que calcula automaticamente o desconto de uma compra de acordo com o valor total, exibindo o desconto aplicado e o valor final a ser pago.

## 🎯 Objetivo

Este projeto foi desenvolvido como atividade de iniciação em tecnologia para ajudar usuários a calcular:

* 💰 Valor do desconto aplicado
* 🏷️ Percentual de desconto conforme a faixa da compra
* 💳 Valor final da compra após o desconto

## 🛠️ Tecnologias utilizadas

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)
![VS Code](https://img.shields.io/badge/VS_Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)

## 📐 Regras de desconto

O programa utiliza uma estrutura condicional para aplicar o desconto correto conforme o valor da compra.

| 💵 Valor da compra | 🎁 Desconto |
|--------------------|------------:|
| Menor que **R$ 200,00** | **5%** |
| Entre **R$ 200,00** e **R$ 299,99** | **10%** |
| A partir de **R$ 300,00** | **15%** |

Após definir a porcentagem, o programa calcula:

`Valor Final = Valor da Compra - Valor do Desconto`

## ▶️ Como executar

1. Clone este repositório:

```bash
git clone https://github.com/gustavoacrani/sistema-desconto.git
```

2. Entre na pasta do projeto:

```bash
cd sistema-desconto
```

3. Execute o programa:

```bash
python app.py
```

## 💻 Exemplo de uso

```text

Digite o valor total da compra (R$): 250

===== RESUMO DA COMPRA =====

💰 Valor da compra: R$ 250.00
🏷️ Desconto aplicado: R$ 25.00 (10%)
💳 Valor final a pagar: R$ 225.00
```

## 👨‍💻 Autor

Desenvolvido por **Gustavo Tisiani Acrani** como atividade prática do curso de **Desenvolvimento de Sistemas**.
