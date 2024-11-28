import tkinter as tk
from tkinter import ttk, messagebox
import subprocess
import os
import psutil  # Para verificar e gerenciar processos
import webbrowser  # Para abrir links no navegador

# Caminho para o ambiente virtual
venv_python = r"C:\\QAx\\ProtheusControlCenterDesktop\\venv\\Scripts\\python.exe"

# Variável global para rastrear o processo do programa
current_process = None

# Função para verificar se o processo está ativo
def is_process_active(proc):
    return proc and psutil.pid_exists(proc.pid)

# Função para abrir o instalador Protheus
def open_installer():
    global current_process
    if is_process_active(current_process):
        messagebox.showwarning("Aviso", "Já existe um programa aberto. Feche-o antes de abrir outro.")
        return
    try:
        current_process = subprocess.Popen(
            [venv_python, r"C:\\QAx\\ProtheusControlCenterDesktop\\instalador_protheus.py"],
            creationflags=subprocess.CREATE_NO_WINDOW  # Não abre terminal
        )
        root.wm_attributes("-topmost", False)  # Deixa a janela principal abaixo
        #messagebox.showinfo("Info", "Instalador Protheus iniciado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir o instalador Protheus: {e}")
        current_process = None

# Função para abrir o inicializador Protheus
def open_initializer():
    global current_process
    if is_process_active(current_process):
        messagebox.showwarning("Aviso", "Já existe um programa aberto. Feche-o antes de abrir outro.")
        return
    try:
        current_process = subprocess.Popen(
            [venv_python, r"C:\\QAx\\ProtheusControlCenterDesktop\\inicializador_protheus.py"],
            creationflags=subprocess.CREATE_NO_WINDOW  # Não abre terminal
        )
        root.wm_attributes("-topmost", False)  # Deixa a janela principal abaixo
        #messagebox.showinfo("Info", "Inicializador Protheus iniciado.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir o inicializador Protheus: {e}")
        current_process = None

# Função para abrir o appserver.ini
def open_conf_appserver():
    global current_process
    if is_process_active(current_process):
        messagebox.showwarning("Aviso", "Já existe um programa aberto. Feche-o antes de abrir outro.")
        return
    try:
        current_process = subprocess.Popen(
            [venv_python, r"C:\\QAx\\ProtheusControlCenterDesktop\\config_appserver.py"],
            creationflags=subprocess.CREATE_NO_WINDOW  # Não abre terminal
        )
        root.wm_attributes("-topmost", False)  # Deixa a janela principal abaixo
        #messagebox.showinfo("Info", "Configurador AppServer.ini")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao abrir o Configurador AppServer.ini: {e}")
        current_process = None

# Função para encerrar o programa aberto
def close_current_program():
    global current_process
    if is_process_active(current_process):
        current_process.terminate()
        current_process.wait()  # Aguarda o término completo do processo
        current_process = None
        messagebox.showinfo("Info", "Programa encerrado.")

# Função para sair do aplicativo
def quit_app():
    if messagebox.askokcancel("Sair", "Você tem certeza que deseja sair?"):
        close_current_program()  # Fecha qualquer programa ativo antes de sair
        root.quit()
        root.destroy()

# Função para abrir um link no navegador
def open_link(url):
    webbrowser.open(url)

# Inicialização da janela principal
root = tk.Tk()
root.title("Protheus Control Center")

# Verifique se o arquivo de ícone existe
icon_path = os.path.join(os.path.dirname(__file__), 'icon.ico')
if os.path.exists(icon_path):
    try:
        root.iconbitmap(icon_path)
    except Exception as e:
        print(f"Erro ao definir ícone: {e}")
else:
    print("Ícone não encontrado.")

root.geometry("700x600")
root.configure(bg='#333333')

# Estilo para tema dark e botões padronizados
style = ttk.Style()
style.theme_use('default')
style.configure('TButton', background='#666666', foreground='#8bb7f7', font=('Arial', 10), width=30)
style.map('TButton', background=[('active', '#555555')])

# Título principal
label = tk.Label(root, text="Protheus Control Center", bg='#333333', 
                 fg='#8bb7f7', font=('Arial', 20, 'bold'))
label.pack(pady=20)

# Texto de boas-vindas
welcome_label = tk.Label(
    root,
    text="Bem-vindo ao Protheus Control Center!\nEscolha uma das opções abaixo ou acesse a documentação para mais informações.",
    bg='#333333',
    fg='#ffffff',
    font=('Arial', 12),
    justify='center'
)
welcome_label.pack(pady=10)

# Links de documentação
frame_links = tk.Frame(root, bg='#333333')
frame_links.pack(pady=10)

link_installer = tk.Label(
    frame_links,
    text="Documentação: Instalador Protheus e Inicializador Protheus",
    bg='#333333',
    fg='#8bb7f7',
    font=('Arial', 10, 'underline'),
    cursor="hand2"
)
link_installer.pack(pady=5)
link_installer.bind(
    "<Button-1>",
    lambda e: open_link("https://github.com/GustavoDuranBR/Protheus-Control-Center_Desktop/blob/master/docs/CONFIGURACOES_DIRETORIOS.md")
)

# Frame central para os botões
frame_buttons = tk.Frame(root, bg='#333333')
frame_buttons.pack(pady=30)

# Botão para abrir o instalador Protheus
install_button = ttk.Button(frame_buttons, text="Instalador Protheus", command=open_installer)
install_button.pack(pady=10)

# Botão para abrir o inicializador Protheus
start_button = ttk.Button(frame_buttons, text="Inicializador Protheus", command=open_initializer)
start_button.pack(pady=10)

# Botão para abrir o configuração do Appserver.ini
start_button = ttk.Button(frame_buttons, text="Configurar AppServer.ini", command=open_conf_appserver)
start_button.pack(pady=10)

# Botão para sair
exit_button = ttk.Button(frame_buttons, text="Sair", command=quit_app)
exit_button.pack(pady=10)

# Informações do desenvolvedor e versão
dev_label = tk.Label(
    root,
    text="Desenvolvedor: Gustavo Duran\nVersão: 2.4",
    bg='#333333',
    fg='#8bb7f7',
    font=('Arial', 10, 'italic'),
    justify='center'
)
dev_label.pack(pady=10)

# Configuração de fechamento
root.protocol("WM_DELETE_WINDOW", quit_app)
root.mainloop()
