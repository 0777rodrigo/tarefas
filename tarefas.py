import customtkinter as ctk
from tkinter import *
from tkinter import messagebox


def adicionar_tarefa():
    tarefa = tarefa_entrada.get().capitalize()
    if tarefa:  
         lista_tarefas.insert(0,tarefa)
         tarefa_entrada.delete(0,END) 
         salve_tarefas()  
    else:
        messagebox.showerror('Error:','Digite uma tarefa')


def apagar_tarefas():
    selecionada = lista_tarefas.curselection()
    if selecionada:
        lista_tarefas.delete(selecionada(0))
        salve_tarefas()
    else:
        messagebox.showerror('Error:','Escolha uma tarefa para deletar')    
        
        
        
        

janela = ctk.CTk('#09112e')
janela.minsize(350,400)
janela.maxsize(350,450)
janela.title('Lista de tarefas V1.0 ')


font1 = ('Arial',30,'bold')
font2 = ('Arial',18,'bold')
font3 = ('Arial',10,'bold')


ctk.CTkLabel(janela,text='Lista de tarefas V1.0',font=font1,text_color='white').pack(padx=10,pady=10)


add_botao = ctk.CTkButton(janela,text='Adicionar tarefas',font=font1,text_color='white',fg_color='blue',cursor='hand2',corner_radius=5,width=10,command=adicionar_tarefa)
add_botao.place(x=30,y=80)


remove_botao = ctk.CTkButton(janela,text='Remover tarefas',font=font2,text_color='white',fg_color='red',cursor='hand2',corner_radius=5,width=80,command=remover_tarefa)
remove_botao.place(x=200,y=80)


tarefa_entrada = ctk.CTkEntry(janela,font=font2,text_color='black',fg_color='white',border_color='white',width=200,placeholder_text='Digite uma tarefa')
tarefa_entrada.place(x=100,y=120)


lista_tarefas = Listbox(janela,width=20,height=15,font=font3)
lista_tarefas.place(x=40,y=150)







janela.mainloop()