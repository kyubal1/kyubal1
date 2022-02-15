import tkinter as tk

class Application(tk.Frame):
    def __init__(self, master = None):
        super().__init__(master)

        self.master.title("照射ボタン")       # ウィンドウタイトル
        self.master.geometry("300x200") # ウィンドウサイズ(幅x高さ)

        # 照射ボタン
        btn_modeless = tk.Button(
            self.master,
            text = "画面を表示",   # ボタンの表示名
            command = self.create_modeless_dialog# クリックされたときに呼ばれるメソッド
            )
        btn_modeless.pack()



    def create_modeless_dialog(self):   #ボタンを押したら呼び出される関数
        '''モードレスダイアログボックスの作成'''
        dlg_modeless = tk.Toplevel(background='white')
        dlg_modeless.title("照射中")   #ウィンドウタイトル
        dlg_modeless.geometry("1400x1050")        # ウィンドウサイズ(幅x高さ)
        dlg_modeless.attributes('-fullscreen',True) #フルスクリーン
        dlg_modeless.after(2000,lambda: dlg_modeless.destroy()) #2000ms後に消える

if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master = root)
    app.mainloop()
