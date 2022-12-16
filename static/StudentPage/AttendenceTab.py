import customtkinter as ctk
from typing import Union , Optional , Tuple
from datetime import date

try : from Helpers.Calender import CTkDateEntry   
except : pass


class ShowAttendence():
    class EntryFrame(ctk.CTkFrame):
        def __init__(self, master: any,
                        width: int = 500, height: int = 200, 
                        corner_radius: Optional[Union[int, str]] = None, 
                        border_width: Optional[Union[int, str]] = None, 
                        bg_color: Union[str, Tuple[str, str]] = "transparent", 
                        fg_color: Optional[Union[str, Tuple[str, str]]] = None, 
                        border_color: Optional[Union[str, Tuple[str, str]]] = None, 
                        background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, 
                        overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
            super().__init__(master, 
                        width = width, height = height, 
                        corner_radius = corner_radius, 
                        border_width = border_width, 
                        bg_color = bg_color, 
                        fg_color = fg_color, 
                        border_color = border_color, 
                        background_corner_colors = background_corner_colors, 
                        overwrite_preferred_drawing_method = None, **kwargs)

        def Cell(self,Text = None,width: int = 200,justify = 'left',fg_color = None):
                return ctk.CTkEntry(  master=self,text_color="black",
                                textvariable=Text,
                                justify=justify,
                                font=("Roboto Medium", -16,'bold'),
                                bg_color="black",fg_color=fg_color,
                                border_color="black",
                                border_width=2,
                                corner_radius=0,
                                height=40,width=width,
                                state='disabled')
    def HeadRow(self,master= None, TextLabel = Tuple):
        self.Frame = self.EntryFrame(master=master)
        for col,text in enumerate(TextLabel):
            text=ctk.StringVar(value=text)
            if col == 0 : self.Frame.Cell(Text=text,width=60,justify='center',fg_color="#086DDE").grid(row=0,column=col)
            else : self.Frame.Cell(Text=text,fg_color="#086DDE").grid(row=0,column=col)
    
    def DataRows(self,master= None, TextLabel = Tuple,fg_color = None):
        self.Frame = self.EntryFrame(master=master)
        for col,text in enumerate(TextLabel):
            text=ctk.StringVar(value=text)
            if col == 0 : self.Frame.Cell(Text=text,width=60,justify='center',fg_color=fg_color).grid(row=0,column=col)
            else : self.Frame.Cell(Text=text,fg_color=fg_color).grid(row=0,column=col)
    def grid(self,row: int,column: int,padx: int = 0,pady: int = 0,columnspan: int = 1,sticky: str = 'n'):
        self.Frame.grid(row=row,column=column,padx=padx,pady=pady,columnspan=columnspan,sticky=sticky)

class AttendenceFrame(ctk.CTkFrame):
    def __init__(self, master: any, 
                width: int = 500, height: int = 200, 
                corner_radius: Optional[Union[int, str]] = None, 
                border_width: Optional[Union[int, str]] = None, 
                bg_color: Union[str, Tuple[str, str]] = "transparent", 
                fg_color: Optional[Union[str, Tuple[str, str]]] = None, 
                border_color: Optional[Union[str, Tuple[str, str]]] = None, 
                background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, 
                overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
       
        super().__init__(master, 
                        width = width, height = height, 
                        corner_radius = corner_radius, 
                        border_width = border_width, 
                        bg_color = bg_color, 
                        fg_color = fg_color, 
                        border_color = border_color, 
                        background_corner_colors = background_corner_colors, 
                        overwrite_preferred_drawing_method = None, **kwargs)

        self.columnconfigure((0,2,4), weight=1,minsize=30)
        self.grid_rowconfigure((0,2), minsize=30)     
        self.grid_rowconfigure(4, minsize=150) 

        self.SubjectEntry = ctk.CTkOptionMenu(master=self,width=310,fg_color=ctk.ThemeManager.theme['CTkComboBox']['fg_color'],
                                         button_color=ctk.ThemeManager.theme['CTkComboBox']['button_color'],
                                         text_color=ctk.ThemeManager.theme['CTkComboBox']['text_color'],
                                         values= ['Database Management System','Operating System',
                                         'Software Engeneering And Project Management','Theory Of Computation','Stress Management'])
        self.SubjectEntry.grid(row=1, column=1,pady=20, sticky="w")
        self.SubjectEntry.set('Enter Subject')

        self.SelectTorP = ctk.CTkOptionMenu(master=self,fg_color=ctk.ThemeManager.theme['CTkComboBox']['fg_color'],
                                         button_color=ctk.ThemeManager.theme['CTkComboBox']['button_color'],
                                         text_color=ctk.ThemeManager.theme['CTkComboBox']['text_color'],
                                         values=['Theory','Practicle'])
        self.SelectTorP.grid(row=1, column=3,pady=20, sticky="w")

        label = ctk.CTkLabel( master=self,text="From :",font=("Roboto Medium", -15))
        label.grid(row=2, column=1, sticky="w",padx=10)
        self.FromDate = CTkDateEntry(master=self,SetDate=f'1-{date.today().month-1}-{date.today().year}',width=22)
        self.FromDate.grid(row=3, column=1, sticky="w",padx=5)

        label = ctk.CTkLabel( master=self,text="To :",font=("Roboto Medium", -15))
        label.grid(row=2, column=2, sticky="w",padx=10)
        self.ToDate = CTkDateEntry(master=self,width=22)
        self.ToDate.grid(row=3, column=2, sticky="w",padx=4)

        self.ConfirmButton = ctk.CTkButton( master=self,border_width=3,text="Confirm",font=("Microsoft YaHei UI Light",13,"bold"))
        self.ConfirmButton.grid(row=3, column=4,padx=30)
    
        self.TableFrame=ctk.CTkFrame(master=self)
        self.TableFrame.grid(row=5,column=0,columnspan=5,pady=5)
        
        self.showClass = ShowAttendence()
        self.Head()

    def Head(self):
        self.TableFrame.destroy()
        self.TableFrame=ctk.CTkFrame(master=self)
        self.TableFrame.grid(row=5,column=0,columnspan=5,pady=5)

        self.showClass.HeadRow(master=self.TableFrame,TextLabel=['SrNo.','Date','Time','Lacture','Attend'])
        self.showClass.grid(row=0,column=0,pady=5)
        self.label = ctk.CTkLabel( master=self.TableFrame,text="---- No Data To Show ----",font=("Roboto Medium", -15))
        self.label.grid(row=1, column=0)

    def showData(self):   #change by backend database
        for i in range(100):
            fg_color = '#8CEBFC' if i%2==0 else '#49E2EC'
            self.showClass.DataRows(master=self.TableFrame,TextLabel=[i+1,'Date','Time','Lacture','Attend'],fg_color=fg_color)
            self.showClass.grid(row=i+1,column=0)

    def Progress(self):
        self.label.grid_forget()
        self.Bar=ctk.CTkProgressBar(master=self.TableFrame,mode='indeterminate')
        self.Bar.grid(row=1, column=0,sticky='we',padx=50)
        self.Bar.start()

    def Progress_Stop(self):
        self.Bar.grid_forget()
        self.showData()
    
    def Error_Message(self,text: str = '---- No Data Found -----'):
        self.label.configure(text=text)
    

if __name__=='__main__':
    r=ctk.CTk()
    #ctk.set_appearance_mode('light')
    r.columnconfigure((0,2), weight=1)
    r.columnconfigure(1, weight=2)
    # ============ create two frames ===
    a=AttendenceFrame(master=r)
    a.grid(row=0,column=0,padx=15)
    
    a.ConfirmButton.configure(command=a.showData)
    r.mainloop()