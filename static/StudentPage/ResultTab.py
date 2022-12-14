'''=====================================================================================================================================
------------------------------Some code For Showing Result in the Tab Yet to Be Perfected ----------------------------------------------
====================================================================================================================================='''
import customtkinter as ctk


class ShowResult :
    def __init__(self,master=None) -> None:
        ctk.CTkLabel(master=master,text="Feature Currently Not Available",
                        text_color=('black','white'),font=('Bookman Old Style',30,"bold")).pack(pady=100)
