import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime
import threading

from modules.scanner import scan_network
from modules.network import get_local_network
from modules.monitor import compare_devices
from modules.export import export_to_csv
from modules.topology import show_topology
from modules.portscanner import scan_ports
from modules.threat import calculate_risk
from modules.login import start_login


# ================= GLOBAL =================

all_devices = []
previous_devices = []

previous_devices = []

scan_running = False


# Variables (created later after root)

search_var = None

device_count = None
new_count = None
offline_count = None
last_scan = None
status_text = None

tree = None
root = None



# ================= CREATE SCANNER =================


def create_scanner():

    global root
    global search_var
    global device_count
    global new_count
    global offline_count
    global last_scan
    global status_text
    global tree


    root = tk.Tk()

    root.title(
        "Advanced Network Scanner | Cyber Security Tool"
    )

    root.geometry("1200x700")
    root.state("zoomed")
    root.configure(
        bg="#0b0b0b"
    )


    # VARIABLES

    search_var = tk.StringVar()

    device_count = tk.StringVar(
        value="0"
    )

    new_count = tk.StringVar(
        value="0"
    )

    offline_count = tk.StringVar(
        value="0"
    )

    last_scan = tk.StringVar(
        value="Never"
    )

    status_text = tk.StringVar(
        value="Ready"
    )



    # ================= DASHBOARD =================


    dashboard = tk.Frame(
        root,
        bg="#0b0b0b"
    )

    dashboard.pack(
        fill="x",
        pady=10
    )



    def create_card(parent,title,value):

        box = tk.Frame(
            parent,
            bg="#171717",
            width=220,
            height=90
        )

        box.pack(
            side="left",
            padx=10
        )


        tk.Label(
            box,
            text=title,
            bg="#171717",
            fg="cyan",
            font=("Arial",12)
        ).pack()


        tk.Label(
            box,
            textvariable=value,
            bg="#171717",
            fg="white",
            font=("Arial",22,"bold")
        ).pack()



    create_card(
        dashboard,
        "DEVICES",
        device_count
    )


    create_card(
        dashboard,
        "NEW",
        new_count
    )


    create_card(
        dashboard,
        "OFFLINE",
        offline_count
    )


    create_card(
        dashboard,
        "LAST SCAN",
        last_scan
    )
        # ================= SEARCH =================


    search_frame = tk.Frame(
        root,
        bg="#0b0b0b"
    )

    search_frame.pack(
        fill="x",
        padx=20
    )


    tk.Label(
        search_frame,
        text="Search Device:",
        fg="white",
        bg="#0b0b0b"
    ).pack(
        side="left"
    )


    search_box = tk.Entry(
        search_frame,
        textvariable=search_var,
        width=35
    )

    search_box.pack(
        side="left",
        padx=10
    )



    # ================= TABLE =================


    columns = (

        "IP",
        "MAC",
        "HOSTNAME",
        "VENDOR",
        "STATUS",
        "RISK"

    )


    tree = ttk.Treeview(

        root,

        columns=columns,

        show="headings"

    )


    for col in columns:

        tree.heading(
            col,
            text=col
        )

        tree.column(
            col,
            width=170
        )


    tree.pack(

        fill="both",

        expand=True,

        padx=20,

        pady=10

    )



    # ================= SEARCH FILTER =================


    def filter_devices(event=None):

        keyword = search_var.get().lower()


        tree.delete(
            *tree.get_children()
        )


        for device in all_devices:


            if keyword in str(device).lower():


                tree.insert(

                    "",

                    "end",

                    values=(

                        device.get("ip"),

                        device.get("mac"),

                        device.get("hostname"),

                        device.get("vendor"),

                        device.get("status"),

                        device.get("risk")

                    )

                )



    search_box.bind(
        "<KeyRelease>",
        filter_devices
    )



    # ================= UPDATE TABLE =================


    def update_table(devices):

        tree.delete(
            *tree.get_children()
        )


        for device in devices:


            try:

                risk, score = calculate_risk(
                    device
                )


                device["risk"] = (
                    f"{risk} ({score})"
                )


            except:

                device["risk"] = "Unknown"



            tree.insert(

                "",

                "end",

                values=(

                    device.get("ip"),

                    device.get("mac"),

                    device.get("hostname"),

                    device.get("vendor"),

                    device.get("status"),

                    device.get("risk")

                )

            )



    # ================= SCAN =================


    def start_scan():


        global all_devices
        global previous_devices
        global scan_running


        try:


            root.after(

                0,

                lambda:status_text.set(
                    "Scanning network..."
                )

            )


            network = get_local_network()


            devices = scan_network(
                network
            )


            previous_devices, new_devices, offline_devices = compare_devices(

                previous_devices,

                devices

            )


            all_devices = devices



            device_count.set(
                str(len(devices))
            )


            new_count.set(
                str(len(new_devices))
            )


            offline_count.set(
                str(len(offline_devices))
            )


            last_scan.set(

                datetime.now().strftime(
                    "%H:%M:%S"
                )

            )



            root.after(

                0,

                lambda:update_table(
                    devices
                )

            )



            root.after(

                0,

                lambda:status_text.set(
                    "Scan Completed"
                )

            )



        except Exception as e:


            root.after(

                0,

                lambda:messagebox.showerror(
                    "Scan Error",
                    str(e)
                )

            )


        finally:

            scan_running = False



    # ================= THREAD =================


    def scan_thread():

        global scan_running


        if scan_running:

            return


        scan_running = True


        threading.Thread(

            target=start_scan,

            daemon=True

        ).start()



    # ================= AUTO REFRESH =================


    def auto_refresh():


        if not scan_running:

            scan_thread()


        root.after(

            60000,

            auto_refresh

        )
            # ================= EXPORT =================


    def export_file():

        if not all_devices:

            messagebox.showwarning(

                "No Data",

                "Run scan first"

            )

            return


        file = export_to_csv(
            all_devices
        )


        messagebox.showinfo(

            "Export Complete",

            f"Saved:\n{file}"

        )



    # ================= PORT SCAN =================


    def run_port_scan():


        selected = tree.selection()


        if not selected:


            messagebox.showwarning(

                "Select Device",

                "Select a device first"

            )

            return



        values = tree.item(
            selected[0]
        )["values"]


        ip = values[0]



        try:


            ports = scan_ports(
                ip
            )


            messagebox.showinfo(

                "Port Scan Result",

                f"IP : {ip}\n\nOpen Ports:\n{ports}"

            )


        except Exception as e:


            messagebox.showerror(

                "Port Scan Error",

                str(e)

            )



    # ================= BUTTONS =================


    button_frame = tk.Frame(

        root,

        bg="#0b0b0b"

    )


    button_frame.pack(

        pady=10

    )



    tk.Button(

        button_frame,

        text="START SCAN",

        width=15,

        bg="green",

        fg="white",

        command=scan_thread

    ).pack(

        side="left",

        padx=5

    )



    tk.Button(

        button_frame,

        text="EXPORT CSV",

        width=15,

        bg="blue",

        fg="white",

        command=export_file

    ).pack(

        side="left",

        padx=5

    )



    tk.Button(

        button_frame,

        text="NETWORK TOPOLOGY",

        width=18,

        bg="purple",

        fg="white",

        command=lambda:show_topology(all_devices)

    ).pack(

        side="left",

        padx=5

    )



    tk.Button(

        button_frame,

        text="PORT SCANNER",

        width=15,

        bg="orange",

        fg="black",

        command=run_port_scan

    ).pack(

        side="left",

        padx=5

    )



    # ================= STATUS BAR =================


    status_bar = tk.Label(

        root,

        textvariable=status_text,

        bg="#151515",

        fg="cyan",

        anchor="w",

        font=("Arial",11)

    )


    status_bar.pack(

        fill="x",

        side="bottom"

    )



    # START AUTO SCAN

    root.after(

        3000,

        auto_refresh

    )


    root.mainloop()



# ================= LOGIN CONNECTION =================


def open_dashboard(login_window):

    login_window.destroy()

    create_scanner()



# ================= START PROGRAM =================


start_login(
    open_dashboard
)