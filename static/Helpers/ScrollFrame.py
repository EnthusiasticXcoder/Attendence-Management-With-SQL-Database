import customtkinter as ctk
from typing import Union , Optional , Tuple

canvas=None
Axis='y'

class ScrollFrame(ctk.CTkFrame):
    def __init__(self, master: any,
                        width: int = 500, height: int = 200,PlaceScrollBar: str='y',
                        corner_radius: Optional[Union[int, str]] = None, 
                        border_width: Optional[Union[int, str]] = None, 
                        bg_color: Union[str, Tuple[str, str]] = "transparent", 
                        fg_color: Optional[Union[str, Tuple[str, str]]] = None, 
                        border_color: Optional[Union[str, Tuple[str, str]]] = None, 
                        background_corner_colors: Union[Tuple[Union[str, Tuple[str, str]]], None] = None, 
                        overwrite_preferred_drawing_method: Union[str, None] = None, **kwargs):
        global Axis
        Axis=PlaceScrollBar
        super().__init__(master, 
                        width = width, height = height, 
                        corner_radius = corner_radius, 
                        border_width = border_width, 
                        bg_color = bg_color, 
                        fg_color = fg_color, 
                        border_color = border_color, 
                        background_corner_colors = background_corner_colors, 
                        overwrite_preferred_drawing_method = None, **kwargs)

        master.rowconfigure(0, weight=1)
        master.columnconfigure(0, weight=1)

        self.grid_columnconfigure(0,weight=100)
        self.grid_columnconfigure(1,weight=1)
        self.grid_rowconfigure(0,weight=100)
        self.grid_rowconfigure(1,weight=1)

        frame= ctk.CTkFrame(master=self)
        frame.grid(row=0,column=0,sticky='nsew')
        global canvas
        canvasbg = ctk.ThemeManager.theme["CTkFrame"]["fg_color"] 
        canvas=ctk.CTkCanvas(frame)
        canvas.configure(bg=canvasbg[ctk.AppearanceModeTracker.appearance_mode])
        canvas.pack(side=ctk.LEFT, fill=ctk.BOTH, expand=1)

        if PlaceScrollBar!='x':
            self.yscrollbar = ctk.CTkScrollbar(master=self,command=canvas.yview)
            canvas.configure(yscrollcommand=self.yscrollbar.set)
        if PlaceScrollBar!="y":
            self.xscrollbar = ctk.CTkScrollbar(master=self,orientation=ctk.HORIZONTAL, command=canvas.xview)
            canvas.configure(xscrollcommand=self.xscrollbar.set)

        canvas.bind('<Configure>', lambda e: canvas.configure(scrollregion = canvas.bbox("all")))

        self.Frame= ctk.CTkFrame(master=canvas)
        canvas.create_window((0,0), window=self.Frame, anchor="nw")
    
    def Bind_Scroll(self,binding_root):
        def xscroll(e):
            canvas.xview_scroll(int(-1.1*(e.delta/120)),'units')
        def yscroll(e):
            canvas.yview_scroll(int(-1.1*(e.delta/120)),'units')
        def enter(e):
            if Axis!='x':
                binding_root.bind("<MouseWheel>",yscroll,add='+')
            if Axis!='y':
                binding_root.bind("<Shift-MouseWheel>",xscroll,add='+')
        def leave(e):
            binding_root.unbind("<MouseWheel>")
        
        canvas.bind("<Enter>",enter,add='+')
        canvas.bind("<Leave>",leave,add='+')
        canvas.yview_moveto(0)
        canvas.xview_moveto(0)

    def updateScrollBar(self):
        if Axis!='x':self.yscrollbar.grid(row=0, column=1,sticky='ns',padx=8)
        if Axis!='y':self.xscrollbar.grid(row=1, column=0,columnspan=1,sticky='ew',pady=10,padx=5)
    
    def resetScrollbar(self):
        if Axis!='x':self.yscrollbar.grid_forget()
        if Axis!='y':self.xscrollbar.grid_forget()
    


if __name__=="__main__":
    t=ctk.CTk()
    t.title("CustomTkinter complex_example.py")
    t.state('zoomed')

    def set_Scaling(self):
        factor=1.25 if self.winfo_height()> 1000 and self.winfo_width()>1900 else 1
        scal=ctk.ScalingTracker.get_window_scaling(self)
        if scal==factor:
            return
        else:
            scal=factor/scal
            ctk.set_widget_scaling(scal)
            ctk.set_window_scaling(scal)

    #set_Scaling(r)
    ctk.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
    ctk.set_default_color_theme("blue")
    r=ctk.CTkToplevel()
    r.rowconfigure(0, weight=1)
    r.columnconfigure(0, weight=1)
    # ============ create two frames ============
    f=ScrollFrame(master=r)
    f.grid(row=0,column=0,sticky='nsew')
    f.updateScrollBar()
    
    t.mainloop()
