import tkinter as tk
import customtkinter as ctk
from typing import Union , Optional , Tuple
from PIL import Image,ImageTk

try : import Helpers.Bind as Bind
except : import Bind


class ToggelMenu(ctk.CTkFrame):
    def __init__(self, master: any, 
                width: int = 500, height: int = 200, 
                corner_radius: Optional[Union[int, str]] = 0, 
                border_width: Optional[Union[int, str]] = None, 
                bg_color: Union[str, Tuple[str, str]] = "transparent", 
                fg_color: Optional[Union[str, Tuple[str, str]]] = 'sky blue3', 
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
        
        self.grid_rowconfigure(1, minsize=20)   # empty row with minsize as spacing
        self.grid_rowconfigure(12, weight=1)  # empty row as spacing
        self.grid_rowconfigure(14, minsize=15)    # empty row with minsize as spacing
        self.grid_rowconfigure(16, minsize=30)

        self.columnconfigure(2,minsize=15)
        
        self.imgmenu = ImageTk.PhotoImage(Image.open('images/menu.png').resize((35,35)))
        self.imgx = ImageTk.PhotoImage(Image.open('images/x.png').resize((35,35)))

        self.Buttonarray=[]  # Button array with [CTkButton class Object , Text , CTkImage class Object]

        self.HomeButton = ctk.CTkButton(master=self,text="",image=self.loadImage('Images/home.png',30),width=30,compound='right',fg_color='transparent')
        self.Buttonarray.append([self.HomeButton,"Home",self.loadImage('Images/home.png',30)])

        ModeChange = ctk.CTkOptionMenu(master=self,
                                            values=["Light", "Dark", "System"],
                                            command=ctk.set_appearance_mode)
        ModeChange.set('System')
        ModeSwitch = ctk.CTkSwitch(master=self,text="",command= lambda :self.change_mode(ModeSwitch),width=0)
        ModeSwitch.grid(row=15, column=0,sticky='e',columnspan=3,padx=20)
        
        def close(e):
            label.configure(image=self.imgmenu)
            for row,button in enumerate(self.Buttonarray) :
                button[0].configure(text="",image=button[2],width=30,fg_color='transparent')
                button[0].grid_configure(row=row+2,column=0,padx=20,pady=3)
            ModeChange.grid_forget()
            ModeSwitch.grid(row=15, column=0,sticky='e',columnspan=3,padx=20)
            label.bind("<Button-1>",open)

        def open(e):
            label.configure(image=self.imgx)
            for row,button in enumerate(self.Buttonarray) :
                button[0].configure(text=button[1],image=self.loadImage('Images/blank.png',1),width=130,fg_color=ctk.ThemeManager.theme['CTkButton']['fg_color'])
                button[0].grid_configure(row=row+2,column=1,padx=20,pady=6)
            ModeSwitch.grid_forget()
            ModeChange.grid(row=15, column=1,padx=20,sticky='ew',columnspan=3)
            label.bind("<Button-1>",close)
   
        label=tk.Label(self,image=self.imgmenu,text=None,bg=fg_color,cursor='hand2')
        label.grid(row=0,column=0,sticky='w',padx=20)
        label.bind("<Button-1>",open)
    
    
    def Update_Button(self):
        for row,button in enumerate(self.Buttonarray) :
            button[0].grid(row=row+2,column=0,padx=20,pady=3)
        self.BindConfigure()

    def loadImage(self,path,size):
        return ctk.CTkImage(light_image=Image.open(path),
                            dark_image=Image.open(path),
                            size=(size,size))
    
    def change_mode(self,ModeSwitch):
        if ModeSwitch.get() == 0:
            ctk.set_appearance_mode("dark")
        else:
            ctk.set_appearance_mode("light")

    def scale_place(self,coordinate):
        coordinate=(coordinate*1/self._get_widget_scaling())
        return coordinate
    
    def BindConfigure(self):
        for button in self.Buttonarray :
            Bind.Bind(button,self)



if __name__=='__main__':
    r=ctk.CTk()
    #ctk.set_appearance_mode('light')
    r.rowconfigure(0, weight=1)
    r.columnconfigure(1, weight=1)
    # ============ create two frames ===
    a=ToggelMenu(master=r)
    a.grid(row=0,column=0,sticky='nsew')
    a.Update_Button()
    ctk.CTkFrame(master=r,fg_color='blue').grid(row=0,column=1,sticky='nsew')
    
    r.mainloop()