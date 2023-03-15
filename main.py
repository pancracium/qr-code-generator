#########################################
# QR CODE GENERATOR [v0.2 (15-03-2023)] #
#########################################

#Import necessary modules
import qrcode
import tkinter as tk
import tkinter.messagebox as msgbox
import tkinter.filedialog as fdialog
from PIL import ImageTk, Image

class QrCodeGeneratorApp:
    """Creates a class for better maintenance of the code."""
    def __init__(self, master=None):
        self.master = master
        self.photo_image = None
        self.font = ("TkFixedFont", 20, "normal")
        self.create_widgets()

    def create_widgets(self):
        """Creates the widgets."""
        #Creates a label for the input
        self.input_label = tk.Label(self.master, text="Enter text to encode:", font=self.font)
        self.input_label.place(x=285, y=10)
        #Creates an entry field for the input
        self.input_entry = tk.Entry(self.master, width=50, font=self.font)
        self.input_entry.place(x=20, y=50)
        #Creates a button which generates the QR code
        self.generate_button = tk.Button(self.master, text="Generate QR Code", relief="flat", background="grey75", 
                                         activebackground="grey60", width=30, height=2, highlightthickness=0,
                                         borderwidth=0, command=self.generate_qr)
        self.generate_button.place(x=175, y=100, width=200, height=50)
        #Creates a button which generates the QR code
        self.save_button = tk.Button(self.master, text="Save QR Code", relief="flat", background="grey75", 
                                     activebackground="grey60", width=30, height=2, highlightthickness=0,
                                     borderwidth=0, command=self.save_qr)
        self.save_button.place(x=425, y=100, width=200, height=50)
        #Creates a frame to show the image when it gets generated
        self.image_frame = tk.Frame(self.master, width=200, height=200)
        self.image_frame.pack()
        self.image_frame.place(anchor="center", relx=0.5, rely=0.6)

    def generate_qr(self):
        """Generates the QR code."""
        #Gets the text from the entry
        text = self.input_entry.get()
        if not text:
            msgbox.showerror(title="Error", message="Please insert text in the input box to generate a QR code.")
            return "NoText"
        #Generates the QR code
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        #Removes the previous label from the frame, if it exists
        if hasattr(self, "image_label"):
            self.image_label.destroy()
        #Displays the new QR code
        image = ImageTk.PhotoImage(img)
        self.image_label = tk.Label(self.image_frame, image=image)
        self.image_label.pack()
        self.photo_image = image

    def save_qr(self):
        """Saves the generated QR code image."""
        if self.photo_image is None:
            msgbox.showerror("Error", "No QR code image generated yet.")
            return "NoQRCode"
        self.name = self.input_entry.get().replace(".", "_").replace("://", "_").replace("/", "-").replace(":", "-") + ".png"
        #Prompt the user to choose a file location and name
        file_path = fdialog.asksaveasfilename(
            initialdir="~/Images",
            initialfile=self.name,
            filetypes=[("PNG", "*.png")]
        )
        #If the user selected a file location and name, save the image
        if file_path:
            self.photo_image._PhotoImage__photo.write(file_path, format='png')

#Sets up a window
WIDTH, HEIGHT = 800, 600
root = tk.Tk()
root.geometry(f"{WIDTH}x{HEIGHT}+{root.winfo_screenwidth() // 2 - WIDTH // 2}+{root.winfo_screenheight() // 2 - HEIGHT // 2}")
root.title("QR CODE GENERATOR")
root.iconbitmap("icon.ico")
app = QrCodeGeneratorApp(master=root)
root.mainloop()