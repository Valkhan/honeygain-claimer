from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import sys

# Receber e-mail e senha dos argumentos
if len(sys.argv) < 3:
    print("Informe o e-mail e senha do Honeygain")
    exit()

email = sys.argv[1]
passwd = sys.argv[2]

# Configurar o WebDriver
chrome_options = Options()
chromedriver_path = os.path.join(
    os.getcwd(), "venv-honeygain", "Scripts", "chromedriver.exe")

chrome_options.add_argument("--headless")  
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--start-maximized")

service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 15)  # Aumentado para garantir carregamento total

try:
    print("Acessando o site do Honeygain...")
    driver.get("https://dashboard.honeygain.com/")
    time.sleep(2)

    # Verifica se estamos na tela de login
    if "login" in driver.current_url:
        print("Página de login detectada. Aguardando campos de entrada...")

        # Esperar que o campo de e-mail apareça antes de tentar interagir
        email_input = wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, "input#email")))
        email_input.send_keys(email)

        pwd_input = driver.find_element(By.CSS_SELECTOR, "input#password")
        pwd_input.send_keys(passwd)
        pwd_input.send_keys(Keys.RETURN)

        print("Credenciais inseridas. Aguardando redirecionamento...")

        # **Aguardar que a URL MUDE para garantir que o login foi feito**
        wait.until(lambda d: "login" not in d.current_url)

        if "login" in driver.current_url:
            print("Usuário ou senha inválidos!")
            driver.quit()
            exit()

    print("Login realizado com sucesso!")

    # **Esperar a página de dashboard carregar completamente**
    time.sleep(5)
    print("Dashboard carregado!")

    # **Aguardar até que o botão de recompensa apareça**
    try:
        print("Procurando botão de recompensa...")
        claim_button = driver.find_element(By.CSS_SELECTOR, "button.jdbHQP")
        claim_button.click()
        print("Botão de recompensa encontrado e clicado!")
    except:
        print("O botão de recompensa não foi encontrado ou já foi coletado.")
        driver.quit()
        exit()

    # **Aguardar e confirmar a recompensa no modal**
    try:
        print("Aguardando botão de recompensa aparecer...")
        time.sleep(5)  # Ajuste conforme necessário

        # Localiza o botão corretamente
        claim_button = wait.until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".Modal button"))
        )
        print("Botão de recompensa encontrado!")

        # Verifica se o botão está realmente visível antes de tentar clicar
        if claim_button.is_displayed():
            try:
                claim_button.click()
                print("Botão de recompensa clicado com sucesso!")
            except:
                print("Clique normal falhou, tentando via JavaScript...")
                driver.execute_script("arguments[0].click();", claim_button)
                print("Botão clicado via JavaScript!")
        else:
            print("O botão não está visível na tela!")

    except Exception as e:
        print(f"Erro ao clicar no botão: {e}")


    except Exception as e:
        print(f"Erro ao clicar no botão:")
        print(e)

    time.sleep(3) # Aguarda a solicitação ser processada
finally:
    print("Fechando o navegador...")
    driver.quit()
