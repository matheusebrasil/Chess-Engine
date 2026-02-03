@echo off
:: ROBÔ DE SETUP PARA PROJETOS DE DADOS
echo [1/4] Criando a caixa blindada (VENV)...
python -m venv venv

echo [2/4] Ativando o ambiente...
call venv\Scripts\activate

echo [3/4] Instalando as ferramentas essenciais (Pandas, Excel, Notebook)...
python -m pip install --upgrade pip
pip install pandas openpyxl notebook ipykernel

echo [4/4] Gerando a receita do bolo (requirements.txt)...
pip freeze > requirements.txt

echo.
echo ==================================================
echo   SUCESSO! O AMBIENTE ESTA PRONTO PARA USO.
echo   Para entrar, digite no terminal: .\venv\Scripts\activate
echo ==================================================
pause