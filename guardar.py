import customtkinter
from customtkinter import *

'''- Criar janela x
- Mudar titulo x
- Criar uma Label de título : Protocolo de Insulina x
- Criar duas Entrys : 'Digite o horário:' e 'Digite a glicemia:' x
- Criar um botão : 'Enviar' x
- Label com os Resultados anteriores# - x
- Colocar um Frame de histórico x
- Atribuir comando ao botão de Enviar x
- Bindar o botão Enter ao botão x
- Apagar entrada de dados quando Enviar x
- Concatenar resultados x
- Alterar cores dos textos 
- Botão de correção
- Atribuir comando ao botão de correção
- 
-   
-
- 
- 
-
-
- Implementar backend ao projeto 
'''


def altera_vazao(glicemia):
    global vazao, vazao_inicial
    if vazao == 0:
        if int(glicemia) in range(100, 180):
            vazao += 1
        elif int(glicemia) in range(180, 251):
            vazao += 2
        elif int(glicemia) in range(251, 300):
            vazao += 3
        elif int(glicemia) > 299:
            vazao += 4
        return 'Vazão', 1
    else:
        if int(glicemia) > 141:
            lb_resultados_anteriores.configure(texto_concatenado)
            return f'Manter vazão em', 1

        if int(glicemia) in range(101, 141):
            lb_resultados_anteriores.configure(texto_concatenado)
            vazao /= 2
            return f'Alterar vazão para', 1

        if int(glicemia) in range(71, 101):
            lb_resultados_anteriores.configure(texto_concatenado)
            return f'Pare a Infusão e comunique o Médico Plantonista !!!', 0

        if int(glicemia) < 71:
            lb_resultados_anteriores.configure(texto_concatenado)
            return f'Pare a Infusão,\n comunique o \nMédico Plantonista e\n administre 40ml de G50% !!!', 0


def bind_enter(none):
    bt_click()


def bt_click():
    global vazao
    global texto_concatenado
    horario = ent_horario.get()
    glicemia = ent_glicemia.get()
    txt_vazao = altera_vazao(glicemia)
    objeto_criado = (f"Horario: {horario}h\n "
                     f"Glicemia: {glicemia}mg/dl\n "
                     f"{txt_vazao[0]}{txt_vazao[1] * (':' + str(vazao) + 'ml/h')}\n"
                     f"-----------------------------------------\n")
    texto_concatenado += objeto_criado
    ent_horario.delete(0, END)
    ent_glicemia.delete(0, END)
    lb_resultados_anteriores.configure(text=f'{texto_concatenado}')

vazao_inicial = 0
vazao = 0
texto_concatenado = ''

''' Janela propriamente dita '''
janela = CTk()
janela.title('Protocolo de Insulina')
janela.geometry('750x2000')
janela.configure(background='#dde')
set_appearance_mode('dark')

''' Frame '''
frame = CTkScrollableFrame(janela)

'''Label1 = Subtitulo (Protocolo de Insulina)'''
lb_subtitulo = CTkLabel(janela, text='Protocolo de Insulina')
lb_subtitulo.configure(janela, font=('Arial', 40))

'''Label2 = (Digite o Horário:) + Entry de Dados'''
lb_horario = CTkLabel(janela, text='Digite o horário: ')
lb_horario.configure(janela, font=('Arial', 25))

ent_horario = CTkEntry(janela, width=6)

'''Label3 = (Digite a glicemia:) + Entry de Dados'''
lb_glicemia = CTkLabel(janela, text='Digite a glicemia: ')
lb_glicemia.configure(janela, font=('Arial', 25))

ent_glicemia = CTkEntry(janela, width=6)

'''Botão (Enviar)'''
botao = CTkButton(janela, text='Enviar', corner_radius=32,
                  fg_color='#4158D0', border_color='#FFCC70', border_width=3, command=bt_click
                  )

'''Label3 = (Resultados anteriores)'''
lb_txt_resultados = CTkLabel(janela, text='Resultados Anteriores:', font=('Arial', 20))

'''Label4 = (Resultados anteriores)'''
lb_resultados_anteriores = CTkLabel(frame, text='')
lb_resultados_anteriores.configure(frame, font=('Arial', 11))

'''Bind Enter do Botão (Enviar)'''
janela.bind("<Return>", bind_enter)

''' Scrollbar '''

'''Todos os Packs em ordem'''
lb_subtitulo.pack(padx=10, pady=10)
lb_horario.place(x=280, y=100)
ent_horario.place(x=340, y=140)
ent_horario.configure(height=30, width=60)
lb_glicemia.place(x=280, y=180)
ent_glicemia.place(x=340, y=220)
ent_glicemia.configure(height=30, width=60)
botao.place(x=325, y=300)
botao.configure(width=100, height=50)
lb_txt_resultados.place(x=245, y=400)
lb_txt_resultados.configure(font=('Arial', 25))
lb_resultados_anteriores.pack(expand=True, padx=1, pady=1)
lb_resultados_anteriores.configure(font=('Arial', 20))
frame.place(x=190, y=490)  # Scrollbar
frame.configure(width=350, height=350, scrollbar_button_color='#CDCDCD')
janela.mainloop()

