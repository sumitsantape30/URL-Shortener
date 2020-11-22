import tkinter
import pyshorteners
import clipboard

window= tkinter.Tk()

#Set default window size
window.geometry("400x200") # width X height

#make window not resizable
window.resizable(False,False) #not resizable in x and y



#app title
window.title("URL Shortner")

#url Entry
url_input= tkinter.Entry(window, font=("Helvetica","16"))
url_input.grid(row=1, column=2, pady=6)

#label shortened url
str_url = tkinter.StringVar(window)

shortened_url= tkinter.Label(window, textvariable= str_url, font=("Helvetica", "16"),fg= "#fff", bg="#1abc9c")
shortened_url.grid(row=3, column=2, pady= 6)

#copy short URL fuction
def copy_short_url():
    try:
        clipboard.copy(str_url.get())
        print("URL copied successfully!")
    except:
        str_url.set("Something went wrong, Please try again!")



#copy short url button
copy_btn= tkinter.Button(window, text="copy", bg="#34495e", fg= "#fff", font= ("Helvica","12"), command= copy_short_url)
copy_btn.grid(row=3, column=3, pady=6, padx=10)


#Short URL Fuctions
def short_url():
    try:
        s= pyshorteners.Shortner()
        url= url_input.get()
        final_result= s.tinyurl.short(url)
        str_url.set(final_result)
        url_input.delete(0, tkinter.END) #clear Input
    except:
        str_url.set("Enter URL Please!")

#click button to short url
btn= tkinter.Button(window, text="Short URL", padx=8, pady=4, bg= "#2ecc71", fg= "#fff", font=("Helvetica", "16"), activebackground= "#16a085", command= short_url)
btn.grid(row= 2, column= 2, pady=6)

window.mainloop()


