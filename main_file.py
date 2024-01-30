import tkinter as tk
import requests


def get_exchange_rates():
    api_key = open('api_key').readline().strip()
    base_currency = base_currency_entry.get().upper()
    target_currency = target_currency_entry.get().upper()

    url = f"https://open.er-api.com/v6/latest/{base_currency}?apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    if "error" in data:
        return f"Error: {data['error']}"
    else:
        rates = data["rates"]
        if target_currency in rates:
            return rates[target_currency]
        else:
            return f"Currency {target_currency} not found"


def calculate_sum():
    amount = float(amount_entry.get())
    exchange_rate = get_exchange_rates()
    if isinstance(exchange_rate, float):
        converted_amount = amount * exchange_rate
        result_label.config(
            text=f"{amount} {base_currency_entry.get()} = {converted_amount:.2f} {target_currency_entry.get()}")
    else:
        result_label.config(text=exchange_rate)


# Creating the main window
root = tk.Tk()
root.title("Currency Converter")

# Creating GUI elements
base_currency_label = tk.Label(root, text="Base Currency:")
base_currency_label.grid(row=0, column=0, padx=10, pady=5)

base_currency_entry = tk.Entry(root, width=10)
base_currency_entry.grid(row=0, column=1, padx=10, pady=5)

target_currency_label = tk.Label(root, text="Target Currency:")
target_currency_label.grid(row=1, column=0, padx=10, pady=5)

target_currency_entry = tk.Entry(root, width=10)
target_currency_entry.grid(row=1, column=1, padx=10, pady=5)

amount_label = tk.Label(root, text="Amount:")
amount_label.grid(row=2, column=0, padx=10, pady=5)

amount_entry = tk.Entry(root, width=10)
amount_entry.grid(row=2, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="Calculate", command=calculate_sum)
calculate_button.grid(row=3, columnspan=2, padx=10, pady=10)

result_label = tk.Label(root, text="", font=("Helvetica", 12))
result_label.grid(row=4, columnspan=2, padx=10, pady=5)

# Starting the main loop
root.mainloop()
