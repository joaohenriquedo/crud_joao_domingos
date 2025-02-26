import tkinter as tk
from tkinter import messagebox
from crud import create_user,read_users,update_user,delete_user

class CRUDApp:
    def __init_(self,root):
        self.root = root
        self.root.title("CRUD USUARIOS ")

#Criação de Wigdets
        self.create_widgets()
    
    def create_widgets(self):
        #leables
        tk.Label(self.root,text = 'NOME').grid(row=0,column=0)
        tk.Label(self.root,text = 'TELEFONE').grid(row=1,column=0)
        tk.Label(self.root,text = 'EMAIL').grid(row=2,column=0)
        tk.Label(self.root,text = 'USUARIO').grid(row=3,column=0)
        tk.Label(self.root,text = 'SENHA').grid(row=4,column=0)

        tk.Label(self.root,text = 'USER ID(for upaate/delete):').grid(row=5,column=0)
        #criar as caixas para digitar os valores
        self.NOME_entry = tk.Entry(self.root)
        self.TELEFONE_entry = tk.Entry(self.root)
        self.EMAIL_entry = tk.Entry(self.root)
        self.USUARIO_entry = tk.Entry(self.root)
        self.SENHA_entry = tk.Entry(self.root)
        self.USER_ID_entry = tk.Entry(self.root)

        self.NOME_entry.grid(row=0,column=1)
        self.TELEFONE_entry.grid(row=1,column=0)
        self.EMAIL_entry.grid(row=2,column=0)
        self.USUARIO_entry.grid(row=3,column=0)
        self.SENHA_entry.grid(row=4,column=0)
        
        self.USER_ID_entry.grid(row=5,column=0)

        #botoes
        tk.Button(self.root, text='criar usu', command=self.create_user).grid(row=0, column=6, columspan=1)
        tk.Button(self.root, text='listar usu', command=self.create_user).grid(row=1, column=6, columspan=1)
        tk.Button(self.root, text='criar', command=self.create_user).grid(row=6, column=0, columspan=1)
        tk.Button(self.root, text='criar', command=self.create_user).grid(row=6, column=1, columspan=1)

        def create_user(self):
            NOME = self.nome_entry.get()
            TELEFONE = self.nome_entry.get()
            EMAIL = self.nome_entry.get()
            USUARIO = self.nome_entry.get()
            SENHA = self.nome_entry.get()

            if NOME and TELEFONE and EMAIL and USUARIO and SENHA:
             create_user(NOME,TELEFONE,EMAIL,USUARIO,SENHA)
             self.NOME_entry.delete(0,tk.END)
            self.TELEFONE_entry.delete(0,tk.END)
            self.EMAIL_entry.delete(0,tk.END)
            self.USUARIO_entry.delete(0,tk.END)
            self.SENHA_entry.delete(0,tk.END)
      else:
        messagebox.showerror("Error","Todos os campos são obrigatorios")
        def read_users(sellf):
        users=read_users()
        self.text_area.delete(1,0,tk.END)
        for user in users:
           self.text_area.delete(tk.END,f"ID: {user[0]}, NOME {user[1]}, TELEFONE{user[2]}, EMAIL{user[3]}")

           def update_user(self):
              user_id = self.user_id_entry.get()

    if USER_ID and NOME and TELEFONE and EMAIL and USUARIO and SENHA:
        update_user(USER_ID,NOME,TELEFONE,EMAIL,USUARIO,SENHA)
        create_user(NOME,TELEFONE,EMAIL,USUARIO,SENHA)
        self.NOME_entry.delete(0,tk.END)
        self.TELEFONE_entry.delete(0,tk.END)
        self.EMAIL_entry.delete(0,tk.END)
        self.USUARIO_entry.delete(0,tk.END)
        self.SENHA_entry.delete(0,tk.END)

    else:
        messagebox.showerror("Error","Todos os campos são obrigatorios")





        





