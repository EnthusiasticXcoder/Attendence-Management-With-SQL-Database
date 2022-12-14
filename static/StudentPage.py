import customtkinter as ctk
from typing import Union , Optional , Tuple

from Pages.MainPage import MainFrame
import StudentPage.AttendenceTab as AttendenceTab , StudentPage.HelperMST as HelperMST , StudentPage.ResultTab as ResultTab
import Helpers.ScrollFrame as ScrollFrame

class Student(MainFrame):
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

        self.BottomFrame.columnconfigure(0, weight=1)
        self.BottomFrame.rowconfigure(0, weight=1)

        Tab = ctk.CTkTabview(master=self.BottomFrame)
        Tab.grid(row=0,column=0,sticky='nsew')

        Tab.add('MST')
        Tab.add('Attendence')
        Tab.add('Result')

        '''--------------- MST Block Marks Of MST Exams Of All Subjects of Current Session ------------------------
        ======================================================================================================='''
        HelperMST.ShowMST(master=Tab.tab('MST'))
        
        '''--------------- Result Block Result Of Current Semister Exams Of All Sessions -------------------------
        ======================================================================================================='''
        ResultTab.ShowResult(master=Tab.tab('Result'))

        '''--------------- Attendence Block Attendence of Current Session ----------------------------------------
        ======================================================================================================='''
        Tab.tab('Attendence').grid_columnconfigure((0,2),weight=1)
        Tab.tab('Attendence').grid_columnconfigure(1,weight=2)

        scroll=ScrollFrame.ScrollFrame(master=Tab.tab('Attendence'))
        scroll.grid(row=0,column=1,sticky='nsew')

        NameFrame=ctk.CTkFrame(master=scroll.Frame,fg_color='transparent')
        NameFrame.grid(row=0,column=0,sticky='w')
        ctk.CTkLabel(master=NameFrame,text='View Attendence',font=('times new roman',30,"bold"),text_color='red').pack(padx=10)

        self.ShowResult=AttendenceTab.AttendenceFrame(master=scroll.Frame)
        self.ShowResult.grid(row=1,column=0,sticky='nsew')
        
        


if __name__=='__main__':
    r=ctk.CTk()
    r.state('zoomed')
    r.rowconfigure(0,weight=1)
    r.columnconfigure(0,weight=1)

    def show():
        s.ShowResult.showData()
        #f.updateScrollBar()

    s=Student(master=r)
    s.grid(row=0,column=0,sticky='nsew')

    #f=ScrollFrame.ScrollFrame(master=s.tab('Attendence'),binding_root=r)
    #f.grid(row=1,column=0)
    #f.Frame.configure(fg_color='blue')
    #s.ShowResult.ConfirmButton.configure(command= show)

    '''scroll.yscrollbar.grid_configure(padx=2)
    scroll.updateScrollBar()'''
    r.mainloop()
