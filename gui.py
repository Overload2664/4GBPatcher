from tkinter import filedialog as fd
from tkinter import messagebox


from pe_patcher import enable_4GB, SUCCESS_MESSAGE

def run_gui() -> None:
    file_path = fd.askopenfilename()
    message = enable_4GB(file_path)
    if(message == SUCCESS_MESSAGE):
        messagebox.showinfo("4GB Patcher", message)
    else:
        messagebox.showerror("4GB Patcher", message)
