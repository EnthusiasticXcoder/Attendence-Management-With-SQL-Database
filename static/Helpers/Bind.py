import customtkinter as ctk
from typing import Callable , Union


class Bind:
    def __init__(self,button,ToggelMenu) -> None:
        '''   Show Lables Of Image Buttons Bind Functions of Image Buttons --------------------------------
        -------------------------------------------------------------------------------------------------'''

        self.showlabel=ctk.CTkLabel(master=ToggelMenu,text="",fg_color="#2A2D2E",text_color='white',
                                anchor='center',height=18,width=70,font=("Helvetica", 12),
                                corner_radius=5,justify='center')

        text=button[1].replace(" ","\n")
        self.bind(button[0],'<Enter>',lambda e : self.Show(button[0],text,ToggelMenu))
        self.bind(button[0],'<Leave>',self.Hide)

    def Show(self,Button,Text,ToggelMenu):
        self.showlabel.configure(text=Text)
        self.showlabel.place(x=10,y=ToggelMenu.scale_place(Button.winfo_y())+40)

    def Hide(self,e):
        self.showlabel.place_forget()
                
    def bind(self, Button, sequence: str = None, command: Callable = None, add: Union[str, bool] = True):
        """ called on the tkinter.Canvas """
        if not (add == "+" or add is True):
            raise ValueError("'add' argument can only be '+' or True to preserve internal callbacks")
        try :
            Button._text_label.bind(sequence, command, add=True)
            Button._canvas.bind(sequence, command, add=True)
            Button._image_label.bind(sequence, command, add=True)
        except :
            #Button._canvas.bind(sequence, command, add=True)
            Button._image_label.bind(sequence, command, add=True)

    def unbind(self,Button, sequence: str = None, funcid: str = None):
        """ called on the tkinter.Label and tkinter.Canvas """
        if funcid is not None:
            raise ValueError("'funcid' argument can only be None, because there is a bug in" +
                                " tkinter and its not clear whether the internal callbacks will be unbinded or not")
        Button._canvas.unbind(sequence, None)
        Button._text_label.unbind(sequence, None)
        Button._image_label.unbind(sequence, add=True)
        Button._create_bindings(sequence=sequence)