from tkinter import *
from tkinter import messagebox
from web3 import Web3
import json
def send_transaction_to_contract():
    try:
        cost = int(ENTRY1.get())
    except ValueError:
        messagebox.showinfo("提示", "請輸入正確金額!!")
    else:
        transaction = contract.functions.AddBonus(cost).build_transaction({
            'from': server,
            'gas': 2000000,
            'gasPrice': web3.to_wei('40', 'gwei'),
            'nonce': web3.eth.get_transaction_count(server),
        })
        signed_transaction = web3.eth.account.sign_transaction(transaction, private_key)
        transaction_hash = web3.eth.send_raw_transaction(signed_transaction.rawTransaction)
        bonus = cost
    messagebox.showinfo("交易訊息", "Transaction hash: "+str(transaction_hash.hex())+"\n"+"Bonus:"+str(bonus))
def get_contract_data():
    total_rewards = contract.functions.TotalRewards().call()
    messagebox.showinfo("Total Rewards:", str(total_rewards))
if __name__ == '__main__':
    private_key = "7321ebce9684426955d43d22dfae6bb4e082778b10aad20dc04492b99de6f819"
    contract_address = "0xcc4769A4F0367d884177b041A7cd4E3bEF5Afa21"
    rpc_url = "https://rpc-mumbai.maticvigil.com"
    web3 = Web3(Web3.HTTPProvider(rpc_url))
    abi = json.loads('[{"inputs":[{"internalType":"address","name":"costomer","type":"address"}],"stateMutability":"nonpayable","type":"constructor"},{"inputs":[{"internalType":"uint256","name":"cost","type":"uint256"}],"name":"AddBonus","outputs":[],"stateMutability":"nonpayable","type":"function"},{"inputs":[],"name":"Bonus","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Costomer","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"Server","outputs":[{"internalType":"address","name":"","type":"address"}],"stateMutability":"view","type":"function"},{"inputs":[],"name":"TotalRewards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"stateMutability":"view","type":"function"}]')
    contract = web3.eth.contract(address=contract_address, abi=abi)
    server = contract.functions.Server().call()
    costomer = contract.functions.Costomer().call()
    TOP = Tk()
    TOP.bind("<Return>", send_transaction_to_contract)
    TOP.geometry("400x400")
    TOP.configure(background="#444444")
    TOP.title("Reward calculater")
    #TOP.resizable()
    LABLE = Label(TOP, bg="#444444", fg="#ffffff", text="紅利系統", font=("Helvetica", 15, "bold"), pady=10)
    LABLE.place(x=55, y=0)
    LABLE1 = Label(TOP, bg="#ffffff", text="輸入消費金額:", bd=6,font=("Helvetica", 10, "bold"), pady=5)
    LABLE1.place(x=55, y=60)
    ENTRY1 = Entry(TOP, bd=8, width=10, font="Roboto 11")
    ENTRY1.place(x=240, y=60)
    BUTTON = Button(bg="#000000", fg='#ffffff', bd=6, text="紅利", padx=10, pady=10, command=send_transaction_to_contract,font=("Helvetica", 20, "bold"))
    BUTTON.grid(row=5, column=0, sticky=W)
    BUTTON.place(x=75, y=250)
    BUTTON2 = Button(bg="#000000", fg='#ffffff', bd=6, text="紅利餘額", padx=10, pady=10, command=get_contract_data,font=("Helvetica", 20, "bold"))
    BUTTON2.grid(row=5, column=0, sticky=W)
    BUTTON2.place(x=225, y=250)
    
    TOP.mainloop()
 