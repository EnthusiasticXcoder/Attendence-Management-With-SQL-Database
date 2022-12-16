import customtkinter as ctk
from typing import Union , Optional , Tuple
from PIL import Image

from Pages.MainPage import MainFrame
from Helpers import ScrollFrame , ToggelFrame
from AdminPage import EnterAttendence
import StudentPage.AttendenceTab as AttendenceTab , StudentPage.HelperMST as HelperMST , StudentPage.ResultTab as ResultTab

class StudentAdmin(MainFrame):
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

        self.BottomFrame.columnconfigure(1, weight=1)
        self.BottomFrame.rowconfigure(0, weight=1)

        ToggelMenu=ToggelFrame.ToggelMenu(master=self.BottomFrame)
        ToggelMenu.grid(row=0,column=0,sticky='nsew')
        
        '''--------------- Configuring Toggel Menu For Function Buttons  -----------------------------------------
        ======================================================================================================='''
        self.MainFrame=ctk.CTkFrame(master=self.BottomFrame)
        self.MainFrame.grid(row=0,column=1,sticky='nsew')
        
        self.EnterExcelButton = ctk.CTkButton(master=ToggelMenu,text="",image=ToggelMenu.loadImage('Images/edit.png',30),width=30,compound='right',fg_color='transparent')
        ToggelMenu.Buttonarray.append([self.EnterExcelButton,'Enter Attendence',ToggelMenu.loadImage('Images/edit.png',30)])

        self.DownloadExcelButton = ctk.CTkButton(master=ToggelMenu,text="",image=ToggelMenu.loadImage('Images/download-cloud.png',30),width=30,compound='right',fg_color='transparent')
        ToggelMenu.Buttonarray.append([self.DownloadExcelButton,'Download Excel',ToggelMenu.loadImage('Images/download-cloud.png',30)])
        
        self.ViewAttendenceButton = ctk.CTkButton(master=ToggelMenu,text="",image=ToggelMenu.loadImage('Images/file-text.png',30),width=30,compound='right',fg_color='transparent')
        ToggelMenu.Buttonarray.append([self.ViewAttendenceButton,'View Attendence',ToggelMenu.loadImage('Images/file-text.png',30)])

        self.ResultButton = ctk.CTkButton(master=ToggelMenu,text="",image=ToggelMenu.loadImage('Images/table.png',30),width=30,compound='right',fg_color='transparent')
        ToggelMenu.Buttonarray.append([self.ResultButton,'Result',ToggelMenu.loadImage('Images/table.png',30)])

        self.MSTButton = ctk.CTkButton(master=ToggelMenu,text="",image=ToggelMenu.loadImage('Images/clipboard.png',30),width=30,compound='right',fg_color='transparent')
        ToggelMenu.Buttonarray.append([self.MSTButton,'MST Marks',ToggelMenu.loadImage('Images/clipboard.png',30)])

        ToggelMenu.Update_Button()
        self.DownloadMenu()
        FuncArr=[self.Home,self.EnterExcelFrame,self.ShowDownload,self.ViewAttendenceFrame,self.ResultFrame,self.MSTFrame]
        for button,function in zip(ToggelMenu.Buttonarray,FuncArr):
            button[0].configure(command=function)

    def Home(self):
        self.MainFrame.destroy()
        self.MainFrame = ctk.CTkFrame(master=self.BottomFrame)
        self.MainFrame.grid(row=0, column=1, sticky="nswe")

    def DownloadMenu(self):
        self.pointerimg=ctk.CTkLabel(self,text="",image=ctk.CTkImage(light_image=Image.open("images/right.png"),
                                    dark_image=Image.open("images/right.png"),size=(30,30)),fg_color='transparent')
        self.downloadmenu=ctk.CTkFrame(master=self,fg_color=('#C0C2C5','#343638'))
        self.downloadmenu.grid_rowconfigure(0,minsize=10)
        sheets=['T1','T2','T3','CSE1']
        if sheets==[]:
            ctk.CTkLabel(master=self.downloadmenu,text=" --- NO FILE TO DOWNLOAD ---").grid(row=0,column=0)
            return
        for i,wb in enumerate(sheets):
            path='workbooks/{0}/{1}'.format('Anshul',wb)
            StudentAdmin.DownloadFrame(master=self.downloadmenu,Path=path,row=i+1)
        self.downloadmenu.grid_rowconfigure(i+2,minsize=10)
    
    
    def ShowDownload(self):
        self.master.bind('<Button-1>',self.HideDownload)
        self.update()

        y= self.scale_place(self.DownloadExcelButton.winfo_rooty()-self.winfo_rooty()) if self.DownloadExcelButton._text_label==None else self.scale_place(self.DownloadExcelButton.winfo_rooty()-self.winfo_rooty())-4
        x=self.scale_place(self.DownloadExcelButton.winfo_x())+50 if self.DownloadExcelButton._text_label==None else self.scale_place(self.DownloadExcelButton.winfo_x())+130

        self.pointerimg.place(x=x,y=y+4)
        self.downloadmenu.place(x=x+24,y=y)
    
    def HideDownload(self,e=None):
        self.pointerimg.place_forget()
        self.downloadmenu.place_forget()
        self.master.unbind('<Button-1>')

    def MSTFrame(self):
        '''--------------- MST Block Marks Of MST Exams Of All Subjects of Current Session ------------------------
        ======================================================================================================='''
        self.Home()
        HelperMST.ShowMST(master=self.MainFrame)
    def ResultFrame(self):
        '''--------------- Result Block Result Of Current Semister Exams Of All Sessions -------------------------
        ======================================================================================================='''
        self.Home()
        ResultTab.ShowResult(master=self.MainFrame)
    
    def ViewAttendenceFrame(self):
        '''--------------- Attendence Block Attendence of Current Session ----------------------------------------
        ======================================================================================================='''
        self.Home()
        self.MainFrame.grid_columnconfigure((0,2),weight=1)
        self.MainFrame.grid_columnconfigure(1,minsize=1110)
        self.MainFrame.grid_rowconfigure(0,weight=1)
        self.MainFrame.grid_rowconfigure(1,minsize=850)

        scroll=ScrollFrame.ScrollFrame(master=self.MainFrame)
        scroll.grid(row=1,column=1,sticky='nsew')

        NameFrame=ctk.CTkFrame(master=scroll.Frame,fg_color='transparent')
        NameFrame.grid(row=0,column=0,sticky='ew')
        ctk.CTkLabel(master=NameFrame,text='View Attendence',font=('times new roman',30,"bold"),text_color='red').pack(side=ctk.LEFT)

        self.ShowResult=AttendenceTab.AttendenceFrame(master=scroll.Frame)
        self.ShowResult.grid(row=1,column=0,sticky='nsew')

    def EnterExcelFrame(self):
        '''---------------Enter Attendence Block For Entering Attendence in The Block ----------------------------
        ======================================================================================================='''  
        self.Home()  
        self.MainFrame.grid_columnconfigure((0,2),weight=1)
        self.MainFrame.grid_columnconfigure(1,minsize=1000)
        self.MainFrame.grid_rowconfigure(0,weight=1)
        self.MainFrame.grid_rowconfigure(1,minsize=800)

        scroll=ScrollFrame.ScrollFrame(master=self.MainFrame)
        scroll.grid(row=1,column=1,sticky='nsew')

        self.EnterAttend= EnterAttendence.EnterFrame(master=scroll.Frame)
        self.EnterAttend.grid(row=0,column=0,sticky='nsew')
    
    def scale_place(self,coordinate):
        coordinate=(coordinate*1/self._get_widget_scaling())
        return coordinate

    class DownloadFrame:
        def __init__(self,master: any,Path: str = None , row: int = 0) -> None:
            Frame=ctk.CTkFrame(master=master)
            Frame.grid(row=row,column=0,sticky='ew')          
            Frame.columnconfigure(0,weight=1)
            self.green = self.loadPhoto("images/green.png",20)
            self.red= self.loadPhoto("images/x red.png",20)
            wb=Path.split("/")[-1]

            ctk.CTkFrame(Frame,height=2,width=0,fg_color="black",corner_radius=0).grid(row=0,column=0,sticky='ew')
            ctk.CTkLabel(master=Frame,text=wb,font=("times new roman",15)).grid(row=1,column=0,padx=25)
            ctk.CTkFrame(Frame,height=2,width=0,fg_color="black",corner_radius=0).grid(row=0,column=0,sticky='ew')

            ctk.CTkButton(master=master,text="",
                            fg_color=('#C0C2C5','#343638'),
                            image=self.green,width=20,border_width=2,
                            command=lambda: print(wb)).grid(row=row,column=1,padx=3)
            ctk.CTkButton(master=master,text="",
                            fg_color=('#C0C2C5','#343638'),
                            image=self.red,width=20,border_width=2).grid(row=row,column=2)

        def loadPhoto(self,path,size):
            return ctk.CTkImage(light_image=Image.open(path),
                                dark_image=Image.open(path),
                                size=(size,size))

if __name__=='__main__':
    r=ctk.CTk()
    r.state('zoomed')
    r.rowconfigure(0,weight=1)
    r.columnconfigure(0,weight=1)

    s=StudentAdmin(master=r)
    s.grid(row=0,column=0,sticky='nsew')
    


    #f=ScrollFrame.ScrollFrame(master=s.tab('Attendence'),binding_root=r)
    #f.grid(row=1,column=0)
    #f.Frame.configure(fg_color='blue')
    #s.ShowResult.ConfirmButton.configure(command= show)

    #scroll.yscrollbar.grid_configure(padx=2)
    #scroll.updateScrollBar()
    r.mainloop()

