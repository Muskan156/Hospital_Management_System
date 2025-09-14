from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
import random
import time
import datetime


class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        # ================= Variables =================
        self.Nameoftablets = StringVar()
        self.ref = StringVar()
        self.Dose = StringVar()
        self.Numberoftablets = StringVar()
        self.IssueDate = StringVar()
        self.ExpDate = StringVar()
        self.DailyDose = StringVar()
        self.sideEffect = StringVar()
        self.furtherInfo = StringVar()
        self.Medication = StringVar()
        self.PatientID = StringVar()
        self.nhsnumber = StringVar()
        self.PatientName = StringVar()
        self.DateOfBirth = StringVar()
        self.PatientAddress = StringVar()

        # ================= Title =================
        lbltitle = Label(self.root, bd=20, relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="green", bg="white",
                         font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ================= Data Frames =================
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("times new roman", 12, "bold"),
                                   text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)

        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10,font=("times new roman", 12, "bold"),
                                    text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ================= Buttons Frame =================
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ================= Details Frame =================
        Detailsframe = Frame(self.root, bd=20, relief=RIDGE)
        Detailsframe.place(x=0, y=600, width=1530, height=190)

        # ================= Dataframe Left (Input Fields) =================
        lblNameTablet = Label(DataframeLeft, text="Names of Tablet", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0, column=0)

        comboNametablet = ttk.Combobox(DataframeLeft, textvariable=self.Nameoftablets,
                                       font=("times new roman", 12, "bold"), width=33)
        comboNametablet["values"] = ("Nice", "Corona Vaccine", "Acetaminophen",
                                     "Adderall", "Amlodipine", "Ativan")
        comboNametablet.current(0)
        comboNametablet.grid(row=0, column=1)

        lblref = Label(DataframeLeft, text="Reference No. :", font=("times new roman", 12, "bold"),padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                       textvariable=self.ref, width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft, text="Dose :", font=("times new roman", 12, "bold"),padx=2,pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                        textvariable=self.Dose, width=35)
        txtDose.grid(row=2, column=1)

        lblNoOftablets = Label(DataframeLeft, text="No. Of Tablets :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblNoOftablets.grid(row=3, column=0, sticky=W)
        txtNoOftablets = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                               textvariable=self.Numberoftablets, width=35)
        txtNoOftablets.grid(row=3, column=1)


        lblIssueDate = Label(DataframeLeft, text="Issue Date :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblIssueDate.grid(row=5, column=0, sticky=W)
        txtIssueDate = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                             textvariable=self.IssueDate, width=35)
        txtIssueDate.grid(row=5, column=1)

        lblExpDate = Label(DataframeLeft, text="Exp Date :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblExpDate.grid(row=6, column=0, sticky=W)
        txtExpDate = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                           textvariable=self.ExpDate, width=35)
        txtExpDate.grid(row=6, column=1)

        lblDailyDose = Label(DataframeLeft, text="Daily Dose :", font=("times new roman", 12, "bold"),padx=2,pady=4)
        lblDailyDose.grid(row=7, column=0, sticky=W)
        txtDailyDose = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                             textvariable=self.DailyDose, width=35)
        txtDailyDose.grid(row=7, column=1)

        lblSideEffect = Label(DataframeLeft, text="Side Effect :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblSideEffect.grid(row=8, column=0, sticky=W)
        txtSideEffect = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                              textvariable=self.sideEffect, width=35)
        txtSideEffect.grid(row=8, column=1)

        lblFurtherInfo = Label(DataframeLeft, text="Further Information :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblFurtherInfo.grid(row=0, column=2, sticky=W)
        txtFurtherInfo = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                               textvariable=self.furtherInfo, width=35)
        txtFurtherInfo.grid(row=0, column=3)


        lblMedicine = Label(DataframeLeft, text="Medication :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblMedicine.grid(row=3, column=2, sticky=W)
        txtMedicine = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                            textvariable=self.Medication, width=35)
        txtMedicine.grid(row=3, column=3)

        lblPatientId = Label(DataframeLeft, text="Patient ID :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblPatientId.grid(row=4, column=2, sticky=W)
        txtPatientId = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                             textvariable=self.PatientID, width=35)
        txtPatientId.grid(row=4, column=3)

        lblNhsNumber = Label(DataframeLeft, text="NHS Number :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblNhsNumber.grid(row=5, column=2, sticky=W)
        txtNhsNumber = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                             textvariable=self.nhsnumber, width=35)
        txtNhsNumber.grid(row=5, column=3)

        lblPatientName = Label(DataframeLeft, text="Patient Name :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblPatientName.grid(row=6, column=2, sticky=W)
        txtPatientName = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                               textvariable=self.PatientName, width=35)
        txtPatientName.grid(row=6, column=3)

        lblDOB = Label(DataframeLeft, text="Date of Birth :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                       textvariable=self.DateOfBirth, width=35)
        txtDOB.grid(row=7, column=3)

        lblPatientAddress = Label(DataframeLeft, text="Patient Address :", font=("times new roman", 12, "bold"),padx=2,pady=6)
        lblPatientAddress.grid(row=8, column=2, sticky=W)
        txtPatientAddress = Entry(DataframeLeft, font=("times new roman", 12, "bold"),
                                  textvariable=self.PatientAddress, width=35)
        txtPatientAddress.grid(row=8, column=3)

        # ================= Dataframe Right =================
        self.txtPrescription = Text(DataframeRight, font=("times new roman", 12, "bold"),
                                    width=46, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ================= Buttons =================
        btnPrescription=Button(Buttonframe,text="Prescription",font=("times new roman",12,"bold"),bg="green",fg="white",width=23,height=2,padx=2,pady=2)
        btnPrescription.grid(row=0,column=0)

        btnPrescriptionData = Button(Buttonframe, text="Prescription Data",command=self.isPrescriptionData,font=("times new roman", 12, "bold"), bg="green", fg="white", width=23, height=2)
        btnPrescriptionData.grid(row=0, column=1)

        btnUpdate = Button(Buttonframe, text="Update", command=self.update_data,font=("times new roman", 12, "bold"),bg="green", fg="white", width=23, height=2)
        btnUpdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", command=self.delete_data,font=("times new roman", 12, "bold"),bg="green", fg="white", width=23, height=2)
        btnDelete.grid(row=0, column=3)

        btnClear = Button(Buttonframe, text="Clear", command=self.clear_data,font=("times new roman", 12, "bold"),bg="green", fg="white", width=23, height=2)
        btnClear.grid(row=0, column=4)

        btnExit = Button(Buttonframe, text="Exit", command=self.root.destroy,font=("times new roman", 12, "bold"),bg="green", fg="white", width=23, height=2)
        btnExit.grid(row=0, column=5)

        # ================= Table =================
        scroll_x = ttk.Scrollbar(Detailsframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Detailsframe, orient=VERTICAL)
        self.hospital_table = ttk.Treeview(Detailsframe,
                                           column=("nameoftablet", "ref", "dose", "nooftablets",
                                                   "issuedate", "expdate", "dailydose", 
                                                   "nhsnumber", "pname", "dob", "address"),
                                           xscrollcommand=scroll_x.set,
                                           yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablet", text="Name Of Tablet")
        self.hospital_table.heading("ref", text="Reference No.")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftablets", text="No. Of Tablets")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Expiry Date")
        self.hospital_table.heading("dailydose", text="Daily Dose")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")
        self.hospital_table["show"] = "headings"

        for col in ("nameoftablet", "ref", "dose", "nooftablets",
                    "issuedate", "expdate", "dailydose", 
                    "nhsnumber", "pname", "dob", "address"):
            self.hospital_table.column(col, width=100)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ================= Functions =================
    def isPrescriptionData(self):
        if self.Nameoftablets.get() == "" or self.ref.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="MS2815@Shaikh", database="hospital_db")
            my_cursor = conn.cursor()
            my_cursor.execute("insert into hospital values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                              (self.Nameoftablets.get(),
                               self.ref.get(),
                               self.Dose.get(),
                               self.Numberoftablets.get(),
                               self.IssueDate.get(),
                               self.ExpDate.get(),
                               self.DailyDose.get(),
                               self.nhsnumber.get(),
                               self.PatientName.get(),
                               self.DateOfBirth.get(),
                               self.PatientAddress.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Record has been inserted")

    def update_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="MS2815@Shaikh", database="hospital_db")
        my_cursor = conn.cursor()
        my_cursor.execute("update hospital set Name_Of_tablets=%s,Dose=%s,Number_Of_Tablets=%s,Issue_Date=%s,Expiry_Date=%s,Daily_Dose=%s,Patient_Name=%s,                        Date_Of_Birth=%s,Address=%s where Reference_No=%s",
                          (self.Nameoftablets.get(),
                           self.Dose.get(),
                           self.Numberoftablets.get(),
                           self.IssueDate.get(),
                           self.ExpDate.get(),
                           self.DailyDose.get(),
                           self.PatientName.get(),
                           self.DateOfBirth.get(),
                           self.PatientAddress.get(),
                           self.ref.get()))
        conn.commit()
        self.fetch_data()
        conn.close()
        messagebox.showinfo("Success", "Record Updated")

    def delete_data(self):
        if self.ref.get() == "":
            messagebox.showerror("Error", "Reference number is required")
        else:
            conn = mysql.connector.connect(host="localhost", username="root",
                                           password="MS2815@Shaikh", database="hospital_db")
            my_cursor = conn.cursor()
            my_cursor.execute("delete from hospital where Reference_No=%s", (self.ref.get(),))
            conn.commit()
            conn.close()
            self.fetch_data()
            messagebox.showinfo("Success", "Record Deleted")

    def clear_data(self):
        self.Nameoftablets.set("")
        self.ref.set("")
        self.Dose.set("")
        self.Numberoftablets.set("")
        self.IssueDate.set("")
        self.ExpDate.set("")
        self.DailyDose.set("")
        self.sideEffect.set("")
        self.furtherInfo.set("")
        self.Medication.set("")
        self.PatientID.set("")
        self.nhsnumber.set("")
        self.PatientName.set("")
        self.DateOfBirth.set("")
        self.PatientAddress.set("")
        self.txtPrescription.delete("1.0", END)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root",
                                       password="MS2815@Shaikh", database="hospital_db")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event):
        cursor_row = self.hospital_table.focus()
        content = self.hospital_table.item(cursor_row)
        row = content["values"]
        if row:
            self.Nameoftablets.set(row[0])
            self.ref.set(row[1])
            self.Dose.set(row[2])
            self.Numberoftablets.set(row[3])
            self.IssueDate.set(row[4])
            self.ExpDate.set(row[5])
            self.DailyDose.set(row[6])
            self.nhsnumber.set(row[7])
            self.PatientName.set(row[8])
            self.DateOfBirth.set(row[9])
            self.PatientAddress.set(row[10])


root = Tk()
ob = Hospital(root)
root.mainloop()
