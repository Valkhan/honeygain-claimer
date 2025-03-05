# Ativar o ambiente virtual
$env:Path = "D:\repos\private-study\python\honeygain\venv-honeygain\Scripts;" + $env:Path
$env:VIRTUAL_ENV = "D:\repos\private-study\python\honeygain\venv-honeygain"

# Definir diretório do script
Set-Location -Path "D:\repos\private-study\python\honeygain"

# Executar o script Python
python claim.py [email] [password]
