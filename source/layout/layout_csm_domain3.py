
""" HERE IS THE LAYOUT OF EVERYTHING RELATED TO THE CYBERSECURITY MATURITY """

import tkinter as tk
import DATA
import layout.layout_home as home
import layout.layout_csm as csm

""" This file is responsible for the layout of the Cybersecurity Maturity's Domain 1 page and everything within it """

class CSM_Domain3_Page(tk.Frame):
    #region
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Maturity - Cybersecurity Controls")

        home_button = tk.Button(self, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        back_button = tk.Button(self, text="Back", command=lambda: master.switch_frame(csm.CSM_Page))
        home_button.grid(row=0, column=0)
        back_button.grid(row=0, column=1)

        preventive_controls_button = tk.Button(self, text="Preventive Controls", command=lambda: master.switch_frame(CSM_Domain3_PreventiveControls_Page))
        detective_controls_button = tk.Button(self, text="Detective Controls", command=lambda: master.switch_frame(CSM_Domain3_DetectiveControls_Page))
        corrective_controls_button = tk.Button(self, text="Corrective Controls", command=lambda: master.switch_frame(CSM_Domain3_CorrectiveControls_Page))
        
        preventive_controls_button.grid(row=1, column=2)
        detective_controls_button.grid(row=2, column=2)
        corrective_controls_button.grid(row=3, column=2)

        preventive_controls_label = tk.Label(self, text=str(csm.submit_pressed(CSM_Domain3_PreventiveControls_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain3_PreventiveControls[i]) for i in DATA.CSM_Domain3_PreventiveControls])))
        detective_controls_label = tk.Label(self, text=str(csm.submit_pressed(CSM_Domain3_DetectiveControls_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain3_DetectiveControls[i]) for i in DATA.CSM_Domain3_DetectiveControls])))
        corrective_controls_label = tk.Label(self, text=str(csm.submit_pressed(CSM_Domain3_CorrectiveControls_Page.values)[3]) + "/" + str(sum([len(DATA.CSM_Domain3_CorrectiveControls[i]) for i in DATA.CSM_Domain3_CorrectiveControls])))
        
        preventive_controls_label.grid(row=1, column=3)
        detective_controls_label.grid(row=2, column=3)
        corrective_controls_label.grid(row=3, column=3)  
    #endregion


class CSM_Domain3_PreventiveControls_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Controls - Preventive Controls")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain3_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain3_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain3_PreventiveControls.items():               
            for j in range(len(values)):
                question = tk.Label(middle_frame, text=values[j], wraplength=700, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion


class CSM_Domain3_DetectiveControls_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Controls - Detective Controls")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain3_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain3_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain3_DetectiveControls.items():               
            for j in range(len(values)):
                question = tk.Label(middle_frame, text=values[j], wraplength=700, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                    
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion


class CSM_Domain3_CorrectiveControls_Page(tk.Frame):
    #region
    values = []

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        master.title("Cybersecurity Controls - Corrective Controls")

        # Top frame contains navigation widgets and labels
        top_frame = tk.Frame(self, borderwidth=1, relief="raised")
        top_frame.pack(side=tk.TOP, fill=tk.X, anchor="w")
        home_button = tk.Button(top_frame, text="Home", command=lambda: master.switch_frame(home.Home_Page))
        home_button.pack(side=tk.LEFT, padx=20, pady=20)
        back_button = tk.Button(top_frame, text="Back", command=lambda: master.switch_frame(CSM_Domain3_Page))
        back_button.pack(side=tk.LEFT)

        # Bottom frame contains the submit and clear buttons
        bottom_frame = tk.Frame(self, borderwidth=1, relief="raised")
        bottom_frame.pack(side=tk.BOTTOM, fill=tk.X, anchor="e")
        submit_button = tk.Button(bottom_frame, text='Submit', command=lambda: master.switch_frame(CSM_Domain3_Page))
        submit_button.pack(side=tk.RIGHT, padx=20)
        clear_button = tk.Button(bottom_frame, text='Clear', command=lambda: csm.clear_pressed(self.values)) #############
        clear_button.pack(side=tk.RIGHT, padx=10, pady=20)

        # Middle frame with a scrollbar and the questions
        my_canvas = tk.Canvas(self)
        my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        my_scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=my_canvas.yview)
        my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        my_canvas.configure(yscrollcommand=my_scrollbar.set, width=master.winfo_width(), height=master.winfo_height())

        def _on_mouse_wheel(event):
            my_canvas.yview_scroll(-1 * int((event.delta / 120)), "units")

        my_canvas.bind_all("<MouseWheel>", _on_mouse_wheel)                                                     # Bind mouse wheel to scrollbar
        my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))      # Bind mouse event to scrollbar

        middle_frame = tk.Frame(my_canvas)
        my_canvas.create_window((0,0), window=middle_frame, anchor="n")

        # Get the questions from DATA and align them on screen
        i=0
        for key,values in DATA.CSM_Domain3_CorrectiveControls.items():               
            for j in range(len(values)):
                question = tk.Label(middle_frame, text=values[j], wraplength=700, justify=tk.LEFT)
                question.grid(row=i, column=0, padx=10, pady=10, sticky="w")
                    
                self.values.append(tk.IntVar())

                yes_answer = tk.Radiobutton(middle_frame, text="Y", variable=self.values[i], value=1)
                yes_c_answer = tk.Radiobutton(middle_frame, text="Y(C)", variable=self.values[i], value=2)
                no_answer = tk.Radiobutton(middle_frame, text="N", variable=self.values[i], value=3)
                yes_answer.grid(row=i, column=1)
                yes_c_answer.grid(row=i, column=2)
                no_answer.grid(row=i, column=3)

                i += 1
    #endregion
