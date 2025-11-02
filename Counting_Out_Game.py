import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def remove(self, node):
        current = self.head
        if current == node:
            self.head = self.head.next
        else:
            while current.next != self.head:
                if current.next == node:
                    current.next = node.next
                    break
                current = current.next

def potato(n, k):
    linked_list = LinkedList()
    for i in range(n):
        linked_list.append(i)

    current = linked_list.head
    while current.next != current:
        for _ in range(k - 1):
            current = current.next
        linked_list.remove(current)
        current = current.next

    return linked_list.head.data

class CountingOutGameGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Counting-Out Game GUI")

        self.N = tk.IntVar()
        self.K = tk.IntVar()

        self.info_text = tk.Text(master, height=5, width=50)
        self.info_text.pack()

        tk.Label(master, text="Enter value of N:").pack()
        self.entry_N = tk.Entry(master, textvariable=self.N)
        self.entry_N.pack()

        tk.Label(master, text="Enter value of K:").pack()
        self.entry_K = tk.Entry(master, textvariable=self.K)
        self.entry_K.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_game)
        self.start_button.pack()

        self.eliminate_button = tk.Button(master, text="Eliminate", command=self.eliminate_player, state=tk.DISABLED)
        self.eliminate_button.pack()

        self.players_frame = tk.Frame(master)
        self.players_frame.pack()

    def start_game(self):
        N = self.N.get()
        K = self.K.get()

        if not (1 < N < 12) or K <= 1:
            messagebox.showinfo("Invalid Input", "Allowed values for N: 1 < N < 12 and K > 1")
            return

        self.players = [i for i in range(N)]
        self.update_players()

        self.current_player = potato(N, K)

        self.info_text.insert(tk.END, f"Game started. N={N} K={K}\n")

        self.start_button.config(state=tk.DISABLED)
        self.eliminate_button.config(state=tk.NORMAL)

    def update_players(self):
        for widget in self.players_frame.winfo_children():
            widget.destroy()
        for player in self.players:
            tk.Label(self.players_frame, text=f"Player {player}").pack()

    def eliminate_player(self):
        self.info_text.insert(tk.END, f"Eliminated player: {self.current_player}\n")
        self.players.remove(self.current_player)
        self.update_players()
        if len(self.players) == 1:
            self.info_text.insert(tk.END, f"Winner: {self.players[0]}\n")
            self.start_button.config(state=tk.NORMAL)
            self.eliminate_button.config(state=tk.DISABLED)
        else:
            self.current_player = potato(len(self.players), self.K.get())

def main():
    root = tk.Tk()
    app = CountingOutGameGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
