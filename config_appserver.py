import tkinter as tk
from tkinter import ttk, filedialog, messagebox

# Função para carregar o arquivo appserver.ini
def carregar_arquivo():
    caminho = filedialog.askopenfilename(
        title="Selecione o arquivo appserver.ini",
        filetypes=[("Arquivos INI", "*.ini"), ("Todos os Arquivos", "*.*")]
    )
    if caminho:
        try:
            with open(caminho, "r", encoding="utf-8") as f:
                conteudo = f.read()
            texto.delete("1.0", tk.END)
            texto.insert(tk.END, conteudo)
            caminho_arquivo.set(caminho)
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar o arquivo: {e}")

# Função para salvar o conteúdo no arquivo
def salvar_arquivo():
    caminho = caminho_arquivo.get()
    if not caminho:
        messagebox.showerror("Erro", "Nenhum arquivo carregado!")
        return
    try:
        conteudo = texto.get("1.0", tk.END).strip()
        with open(caminho, "w", encoding="utf-8") as f:
            f.write(conteudo)
        messagebox.showinfo("Sucesso", "Alterações salvas com sucesso!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar o arquivo: {e}")

# Função para aplicar o tema escuro
def aplicar_tema_dark():
    estilo = ttk.Style()
    estilo.theme_use("clam")
    estilo.configure('TFrame', background='#333333')
    estilo.configure('TLabel', background='#333333', foreground='#8bb7f7', font=('Arial', 10))
    estilo.configure('TButton', background='#666666', foreground='#8bb7f7', font=('Arial', 10), width=30, borderwidth=1)
    estilo.map('TButton', background=[('active', '#555555')])

    janela.configure(bg='#333333')
    texto.config(bg="#1e1e1e", fg="#ffffff", insertbackground="white", highlightbackground="#444444", highlightcolor="#565656")

# Interface Tkinter
janela = tk.Tk()
janela.title("Editor de Configuração - AppServer")
janela.geometry("700x500")

# Configurar o ícone da janela
janela.iconbitmap("icon.ico")  # Substitua "icon.ico" pelo caminho do seu arquivo .ico

# Variável para armazenar o caminho do arquivo
caminho_arquivo = tk.StringVar()

# Frame principal
frame_principal = ttk.Frame(janela)
frame_principal.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Botão para selecionar arquivo
btn_selecionar = ttk.Button(frame_principal, text="Selecionar Arquivo", command=carregar_arquivo)
btn_selecionar.pack(pady=5)

# Label para mostrar o caminho do arquivo selecionado
lbl_caminho = ttk.Label(frame_principal, textvariable=caminho_arquivo, anchor="center", wraplength=600)
lbl_caminho.pack(pady=5)

# Área de texto para exibir e editar o conteúdo do arquivo
texto = tk.Text(frame_principal, wrap=tk.NONE, height=20, font=("Consolas", 10))
texto.pack(pady=5, fill=tk.BOTH, expand=True)

# Barra de rolagem para o texto
scrollbar = ttk.Scrollbar(frame_principal, command=texto.yview)
texto.configure(yscrollcommand=scrollbar.set)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Botão para salvar alterações
btn_salvar = ttk.Button(frame_principal, text="Salvar Alterações", command=salvar_arquivo)
btn_salvar.pack(pady=10)

# Aplicar tema escuro depois de todos os widgets serem criados
aplicar_tema_dark()

# Iniciar o loop principal
janela.mainloop()
