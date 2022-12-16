import customtkinter as ctk
from typing import Union , Optional , Tuple

from Helpers.Calender import CTkDateEntry

class EnterFrame(ctk.CTkFrame):
    def __init__(self, master: any, 
                width: int = 500, height: int = 200, 
                corner_radius: Optional[Union[int, str]] = 0, 
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
        self.grid_rowconfigure((0,2,4), minsize=30)    
        self.grid_rowconfigure(9, minsize=40)   
        self.grid_rowconfigure(11, minsize=40)

        self.WbEntry = ctk.CTkOptionMenu(master=self,values=['T1','T2','T3'])
        self.WbEntry.grid(row=1, column=1,pady=20, sticky="w")
        self.WbEntry.set('Select Class')

        self.SelectTorP = ctk.CTkOptionMenu(master=self,values=['Theory','Practicle'])
        self.SelectTorP.grid(row=1, column=3,pady=20, sticky="w")
        
        self.DateEntry = CTkDateEntry(master=self,width=15)
        self.DateEntry.grid(row=3, column=1,pady=20, sticky="w",padx=4)

        val=("9:45-10:35","10:35-11:25","11:30-12:20","12:20-1:10","1:40-2:30","2:30-3:20","3:20-4:05","4:05-4:50")
        self.TimeEntry = ctk.CTkComboBox(master=self,values=val)
        self.TimeEntry.grid(row=3, column=3,pady=20, sticky="w")
        self.TimeEntry.set('Time')

        label = ctk.CTkLabel( master=self,
                              text="Enter RollNo :",
                              font=("Roboto Medium", -16))
        label.grid(row=5, column=0, sticky="w",padx=20)

        self.RollList = ctk.CTkTextbox( self,width=700,
                                        font=("Roboto Medium", -30,'bold'),
                                        fg_color='white',
                                        text_color="black")
        self.RollList.grid(row=6, column=0,rowspan=3,columnspan=4,padx=30)

        self.ConfirmButton = ctk.CTkButton( master=self,text="Confirm" )
        self.ConfirmButton.grid(row=10, column=3)

if __name__=='__main__':
    from Calender import CTkDateEntry
    r=ctk.CTk()
    #ctk.set_appearance_mode('light')
    # ============ create two frames ===
    a=EnterFrame(master=r)
    a.grid(row=0,column=0)
    r.mainloop()