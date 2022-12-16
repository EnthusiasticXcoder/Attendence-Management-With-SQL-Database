import customtkinter as ctk
from typing import Union , Optional , Tuple
from PIL import Image


class MainFrame(ctk.CTkFrame):
    def __init__(self, master: any, 
                width: int = 200, height: int = 200, 
                corner_radius: Optional[Union[int, str]] = None, 
                border_width: Optional[Union[int, str]] = None, 
                bg_color: Union[str, Tuple[str, str]] = "transparent", 
                fg_color: Optional[Union[str, Tuple[str, str]]] = "sky blue3", 
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
        self.img= self.loadImage('Images/logoies.png',size=(600,130))
        self.imgProf= self.loadImage('Images/user.png',size=(30,30))

        UpperFrame = ctk.CTkFrame(master=self,fg_color=fg_color,corner_radius=0)
        UpperFrame.place(x=0,y=0,relheight=0.163,relwidth=1)
        
        UpperFrame.grid_columnconfigure(0, weight=0)
        UpperFrame.grid_columnconfigure(1, weight=10)
    
        label=ctk.CTkLabel(master=UpperFrame,text=None,image=self.img,fg_color=fg_color)
        label.grid(row=0,column=0,sticky='n')
        
        Frame=ctk.CTkFrame(master=UpperFrame,fg_color=fg_color)
        Frame.grid(row=0,column=1,sticky='nsew')
        
        NameFrame=ctk.CTkFrame(master=Frame,fg_color=fg_color)
        NameFrame.pack(side=ctk.RIGHT,padx=20,ipadx=50)
        NameLabel=ctk.CTkLabel(master=NameFrame,text="Login as : ",text_color='black',
                               font=('Goudy old style',18,"bold"),anchor='w')
        NameLabel.grid(row=0,column=1,sticky='w')
        NameLabel=ctk.CTkLabel(master=NameFrame,text='Anshul Verma',font=('Goudy old style',25,"bold"),text_color='red')
        NameLabel.grid(row=1,column=1)
        self.Profile=ctk.CTkButton(NameFrame,image=self.imgProf,fg_color='sky blue3',text="",width=30,cursor='hand2',command= lambda:self.ShowMenu(master=master))
        self.Profile.grid(row=1,column=0,sticky='e',rowspan=2,padx=4)
        NameLabel=ctk.CTkLabel(master=NameFrame,text='Student',font=('times new roman',15),text_color='black')
        NameLabel.grid(row=2,column=1,sticky='nw')

        self.BottomFrame=ctk.CTkFrame(master=self,fg_color=fg_color)
        self.BottomFrame.place(x=0,rely=0.163,relheight=0.840,relwidth=1)

        self.Menu()
        
    
    def Menu(self):
        self.menuFrame=ctk.CTkFrame(master=self,fg_color=('grey76','grey20'))

        self.ProfileButton=ctk.CTkButton(master=self.menuFrame ,image=self.loadImage('Images/user.png',size=(17,17)), text='Profile',fg_color='transparent',hover_color='grey30',corner_radius=0,text_color=('black','white'),anchor='w')
        self.ChangePassButton=ctk.CTkButton(master=self.menuFrame,text='Change Password',image=self.loadImage('Images\key.png',size=(17,17)),fg_color='transparent',hover_color='grey30',corner_radius=0,text_color=('black','white'),anchor='w')
        self.LogoutButton=ctk.CTkButton(master=self.menuFrame,text='Log Out',image=self.loadImage('Images/log-out.png',size=(17,17)),fg_color='transparent',hover_color='grey30',corner_radius=0,text_color=('black','white'),anchor='w')

        self.ProfileButton.grid(row=0,column=0,padx=5)
        self.ChangePassButton.grid(row=1,column=0,padx=5)
        self.LogoutButton.grid(row=2,column=0,padx=5)
    
    def ShowMenu(self,master) :
        self.menuFrame.place(x=(self.Profile.winfo_rootx()-self.winfo_rootx())/1.25-15,y=(self.Profile.winfo_rooty()-self.winfo_rooty())/1.25+50)
        master.bind('<Button-1>', lambda e :self.HideMenu(master=master))

    def HideMenu(self,master):
        self.menuFrame.place_forget()
        master.unbind('<Button-1>')
    
    def loadImage(self,path,size):
        return ctk.CTkImage(light_image=Image.open(path),
                            dark_image=Image.open(path),
                            size=size)




if __name__=='__main__':
    r=ctk.CTk()
    #ctk.set_appearance_mode('light')
    r.state('zoomed')
    r.grid_columnconfigure(0,weight=1)
    r.grid_rowconfigure(0,weight=1)
    MainFrame(master=r).grid(row=0,column=0,sticky='nsew')
    r.mainloop()
