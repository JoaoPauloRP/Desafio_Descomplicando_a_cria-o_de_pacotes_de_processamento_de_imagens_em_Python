from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="clear_dataframe",
    version="0.0.1",
    author="João Paulo",
    author_email="joaopauloresend@hotmail.com",
    description="pacote criado para realizar limpeza de dataframes",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/JoaoPauloRP/Desafio_Descomplicando_a_cria-o_de_pacotes_de_processamento_de_imagens_em_Python"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)