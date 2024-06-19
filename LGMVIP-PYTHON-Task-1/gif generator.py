import glob
import imageio.v2 as imageio 
from tkinter import *
from tkinter import messagebox, filedialog


def chooseFolder():
    folder_path = filedialog.askdirectory()
    if folder_path:
        direc.set(folder_path)


def convertToGIF():
    path = direc.get()  
    ext = extension.get()  
    
    if ext == 'both':
        path_in = path + '/*.{png,jpeg}'  
    else:
        path_in = path + f'/*.{ext}'  
    
    path_out = filedialog.asksaveasfilename(defaultextension='.gif',
                                            filetypes=[("GIF files", "*.gif")],
                                            initialfile='MyGif.gif',
                                            title="Save GIF As") 
    if not path_out:
        return  
    
    imgs = []  
    try:
        files = glob.glob(path_in, recursive=True)  
        for im in files:
            imgs.append(imageio.imread(im)) 

        imageio.mimsave(path_out, imgs)  
        
        messagebox.showinfo("DataFlair GIF Generator", "GIF is saved successfully!")

    except Exception as e:
        messagebox.showinfo("Error occurred!", f"Error: {e}\nPlease check the path of the folder or the extension of images.")

wn = Tk()
wn.title("Image to GIF Generator")  
wn.geometry('500x300')
wn.config(bg='#F0F0F0')  
extension = StringVar(wn)
direc = StringVar(wn)
Label(wn, text='Image to GIF Convertor', bg='#F0F0F0', fg='black', font=('Times', 20, 'bold')).place(x=60, y=10)
Label(wn, text='Please select the extension of the images', bg='#F0F0F0', anchor="e", justify=LEFT).place(x=20, y=70)
OptionMenu(wn, extension, 'png', 'jpeg', 'both').place(x=220, y=70)
Button(wn, text="Select Folder", bg='#5C85FB', fg='white', font=('calibre', 10, 'bold'), command=chooseFolder).place(x=20, y=100)
Label(wn, textvariable=direc, bg='#F0F0F0', font=('calibre', 10)).place(x=150, y=104)
Label(wn, text='Please click the button to get the GIF', bg='#F0F0F0', anchor="e", justify=LEFT).place(x=20, y=130)
Button(wn, text="Convert to GIF", bg='#4CAF50', fg='white', font=('calibre', 13, 'bold'), command=convertToGIF).place(x=230, y=160)
Label(wn, text="Made by: Harsh Bhardwaj", bg='#F0F0F0', fg='black', font=('Helvetica', 10, 'italic')).place(x=10, y=270)
wn.mainloop()
