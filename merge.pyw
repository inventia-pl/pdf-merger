import glob, os
from PyPDF2 import PdfMerger, PdfWriter, PdfReader

import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
import tkinter.messagebox 
#
#import ctypes
#import os
#import win32process
#
#hwnd = ctypes.windll.kernel32.GetConsoleWindow()      
#if hwnd != 0:      
#    ctypes.windll.user32.ShowWindow(hwnd, 0)      
#    ctypes.windll.kernel32.CloseHandle(hwnd)
#    _, pid = win32process.GetWindowThreadProcessId(hwnd)
#    os.system('taskkill /PID ' + str(pid) + ' /f')


def merge_option():
    btn_folder["state"] = "normal"
    btn_go_home["state"] = "normal"
    btn_edit["state"] = "disabled"
    return

def edit_option():
    btn_open["state"] = "normal"
    btn_go_home["state"] = "normal"
    btn_merge["state"] = "disabled"
    return

def go_home(info_grid):
    for widgets in info_grid.winfo_children():
        widgets.destroy()

    if btn_merge["state"] == "disabled" or btn_edit["state"] == "disabled":
        btn_folder["state"] = "disabled"
        btn_open["state"] = "disabled"
        btn_merge["state"] = "normal"
        btn_edit["state"] = "normal"

    btn_go_home["state"] = "disabled"    
    return

def ok_delete_few(entry_ref, filepath):
    entry_input = entry_ref.get()
    pages_to_delete = [int(i) for i in entry_input.split() if i.isdigit()]
    pages_to_delete = [x - 1 for x in pages_to_delete]
    
    infile = PdfReader(filepath, 'rb')
    output = PdfWriter()
    
    for i in range(len(infile.pages) ):
        if i not in pages_to_delete:
            p = infile._get_page(i)
            output.add_page(p)
    filepath = asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Pliki pdf", "*.pdf")],
    )
    if not filepath:
        return

    with open(filepath, 'wb') as f:
        output.write(f)
    
     
    return

def delete_few(filepath, set_state):
    set_state["state"] = "disabled"
    btn_open["state"] = "disabled"
    info_lable = tk.Label(info_grid, text="Wpisz numery stron pliku PDF do usunięcia po spacji")
    info_lable.grid(row=2,column=0)
    entry_few = tk.Entry(info_grid, width=50)
    entry_few.grid(row=3,column=0)
    btn_delete = tk.Button(info_grid, text ="ok")
    btn_delete["command"] = lambda entry_ref = entry_few : ok_delete_few(entry_ref, filepath)
    btn_delete.grid(row=4,column=0)
    return

def ok_delete_set(entry_ref_od, entry_ref_do, filepath):
    entry_input_od = entry_ref_od.get()
    entry_input_do = entry_ref_do.get()
    if not entry_input_do.isnumeric() or not entry_input_od.isnumeric():
        tkinter.messagebox.showerror("Zły input","Sprawdź wpisane wartości")
        return 
    
    pages_od = int(entry_input_od) - 1
    pages_do = int(entry_input_do) - 1
    
    if pages_od < pages_do:
        pages_to_delete = list(range(pages_od, pages_do))
    else:
        pages_to_delete = list(range(pages_do, pages_od))
    
        
    infile = PdfReader(filepath, 'rb')
    output = PdfWriter()
    
    for i in range(len(infile.pages) ):
        if i not in pages_to_delete:
            p = infile._get_page(i)
            output.add_page(p)
    filepath = asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("Pliki pdf", "*.pdf")],
    )
    if not filepath:
        return

    with open(filepath, 'wb') as f:
        output.write(f)

    return

def delete_set(filepath, few_state):
    few_state["state"] = "disabled"
    btn_open["state"] = "disabled"
    info_lable = tk.Label(info_grid, text="Wpisz zakres")
    info_lable.grid(row=3,column=0)
    info_lable_od = tk.Label(info_grid, text="od:")
    info_lable_od.grid(row=4,column=0)
    entry_od = tk.Entry(info_grid, width=10)
    entry_od.grid(row=4,column=1)
    info_lable_do = tk.Label(info_grid, text="do: ")
    info_lable_do.grid(row=5,column=0)
    entry_do = tk.Entry(info_grid, width=10)
    entry_do.grid(row=5,column=1)
    btn_delete = tk.Button(info_grid, text ="ok")
    btn_delete["command"] = lambda entry_ref_od = entry_od, entry_ref_do = entry_do : ok_delete_set(entry_ref_od, entry_ref_do, filepath)
    btn_delete.grid(row=6,column=0)

    return

def open_file():
    """Open a file for editing."""
    filepath = askopenfilename(
        filetypes=[("Pliki pdf", "*.pdf")]
    )
    if not filepath:
        tkinter.messagebox.showerror("Brak pliku","Plik ma złe rozszerzenie lub nieistnieje")
        return
    display_pdf = tk.Label(info_grid, text = "Wybrano " + filepath)
    display_pdf.grid(row=0,column=0)
    btn_delete_few = tk.Button(info_grid, text="Usuń wybrane strony")
    btn_delete_set = tk.Button(info_grid, text="Usuń zbiór")
    btn_delete_few["command"] = lambda set_state = btn_delete_set : delete_few(filepath, set_state)
    btn_delete_few.grid(row=1,column=0)
    btn_delete_set["command"] = lambda few_state = btn_delete_few : delete_set(filepath, few_state)
    btn_delete_set.grid(row=1,column=1)
    return

def merge_files(pdfs, pdf_directory, merge_btn):
    merger = PdfMerger()
    for pdf in pdfs:
        merger.append(pdf)

    merger.write("merged_file.pdf")
    merger.close()
    tkinter.messagebox.showinfo("Zapis", "Nowy plik zapisano w " + pdf_directory)
    merge_btn.destroy()
    return

def open_directory():
    pdf_directory = askdirectory()
    if not pdf_directory:
        return 
    os.chdir(pdf_directory)
    pdfs = []
    for file in glob.glob("*.pdf"):
        pdfs.append(file)
    if not pdfs:
        tkinter.messagebox.showwarning("Brak plików pdf","Nie znaleziono plików pdf w wybranym folderze")
        return
    element = 'Znalezione pliki pdf: \n'
    for i in range(len(pdfs)):
        element = element + pdfs[i] +'\n'
    display_pdf = tk.Label(info_grid, text = element)
    display_pdf.grid(row = 0, column = 0)
    btn_merge_files = tk.Button(info_grid, text="Połącz pliki")
    btn_merge_files["command"] = lambda merge_btn = btn_merge_files : merge_files(pdfs, pdf_directory, merge_btn)
    btn_merge_files.grid(row=1,column=0)
    return

    

window = tk.Tk()
window.title("PDF merger")
window.rowconfigure(0, minsize=400, weight=1)
window.columnconfigure(1, minsize=400, weight=1)

info_grid = tk.Frame(window)
frm_buttons = tk.Frame(window,relief=tk.RAISED, bd=2)

btn_merge = tk.Button(frm_buttons, text="Połącz pliki pdf", command=merge_option)
btn_edit = tk.Button(frm_buttons, text="Edytuj plik pdf", command=edit_option)
btn_folder = tk.Button(frm_buttons, text="Otwórz folder", command=open_directory, state = "disabled")
btn_open = tk.Button(frm_buttons, text="Otwórz plik", command=open_file, state = "disabled")
btn_go_home = tk.Button(frm_buttons, text="Wróć", command= lambda : go_home(info_grid), state = "disabled")

btn_merge.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_edit.grid(row=1, column=0, sticky="ew", padx=5, pady=5)
btn_folder.grid(row=2, column=0, sticky="ew", padx=5, pady=5)
btn_open.grid(row=3, column=0, sticky="ew", padx=5, pady=5)
btn_go_home.grid(row=4, column=0, sticky="ew", padx=5, pady=5)

frm_buttons.grid(row=0, column=0, sticky="ns")
info_grid.grid(row=0, column=1, sticky="nw")

window.mainloop()

