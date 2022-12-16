import requests
from bs4 import BeautifulSoup as bs
import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.resizable(0,0)
root.title("Currency Converter")
root.geometry("400x200")

clicks = 0

def user_choice():
    global output_frame
    global output_label
    global clicks
    clicks = clicks + 1

    if clicks > 1 and output_frame.winfo_exists():
        output_frame.destroy()

    output_frame = customtkinter.CTkFrame(master=root, fg_color="#1a1b1b")
    output_frame.grid(row=3, column= 0, columnspan= 2, pady=(25,0))

    if amount_entry_field.get().isdigit():
        modified_url = f"https://www.x-rates.com/calculator/?from={from_entry_field.get().upper()}&to={to_entry_field.get().upper()}&amount={amount_entry_field.get()}"
        page = requests.get(modified_url)

        if page.status_code == 200:
            content_of_page = page.content
            soup = bs(content_of_page, 'html.parser')
            conversion = soup.find("span", class_="ccOutputRslt")
            conversion_value = float(conversion.text[:-4])
            output_label = customtkinter.CTkLabel(master=output_frame, text_font=("Roboto", 12),bg="black", text_color="white", text=f"{amount_entry_field.get()} {from_entry_field.get().upper()} = {conversion_value} {to_entry_field.get().upper()}")
            output_label.grid(row=2, column= 0)

    else:
        output_label = customtkinter.CTkLabel(master=output_frame, text_color="Red", text=f"KINDLY ENTER THE CORRECT DETAILS")
        output_label.grid(row=2, column= 1, columnspan=2)


from_entry_field = customtkinter.CTkEntry(master=root, width=150, placeholder_text="Current curreny code",) 
from_entry_field.grid(row=0, column=0, padx=(20,10), pady=(20,20), ipadx=10, ipady=5)

to_entry_field = customtkinter.CTkEntry(master=root, width=150, placeholder_text="Target currency code")
to_entry_field.grid(row=0, column=1,padx=(10,30), pady=(20,20), ipadx=10, ipady=5)

amount_entry_field = customtkinter.CTkEntry(master=root, width=150, placeholder_text="Enter the amount")
amount_entry_field.grid(row=1, column=0,padx=(20,10), ipadx=10, ipady=5)

btn = customtkinter.CTkButton(master=root, text="CONVERT", bg="black", text_color="white", command=user_choice)
btn.grid(row=1, column=1, padx=(10,30), ipadx=18, ipady=4)

master=root.mainloop()
