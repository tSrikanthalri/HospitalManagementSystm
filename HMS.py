from tkinter import * 
from tkinter import ttk 
import random 
import time     
import datetime 
from tkinter import messagebox
import mysql.connector



class Hospital:
    def __init__(self,root):
        self.root = root 
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        
        self.Nameoftablets=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.NumberofTablets=StringVar()
        self.Lot=StringVar()
        self.Issuedate=StringVar()
        self.ExpDate=StringVar()
        self.DailyDose=StringVar()
        self.SideEffect=StringVar()
        self.FurtherInformation=StringVar()
        self.StorageAdvice=StringVar()
        self.DrivingUsingMachine=StringVar()
        self.HowToUseMedication=StringVar()
        self.PatientId=StringVar()
        self.nhsNumber=StringVar()
        self.PatientName=StringVar()
        self.DateOfBirth=StringVar()
        self.PatientAddress=StringVar()
        
        lbltitle=Label(self.root,bd=20,relief=RIDGE,text="HOSPITAL MANAGEMENT SYSTEM",fg="red",bg="white",font=("times new roman",50,"bold"))
        lbltitle.pack(side=TOP,fill=X)
        
        # ================================Dataframe=======================================
        DataFrame=Frame(self.root,bd=20,relief=RIDGE)
        DataFrame.place(x=0,y=130,width=1530,height=400)
        
        DataframeLeft=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                            font=("arial",12,"bold"),text="Patient Information")
        DataframeLeft.place(x=0,y=5,width=980,height=350)
        
        dataframeRight=LabelFrame(DataFrame,bd=10,relief=RIDGE,padx=10,
                                             font=("arial",12,"bold"),text="Prescription")
        dataframeRight.place(x=990,y=5,width=460,height=350)
        
        #=================================Buttons frame=====================================
        
        Buttonframe=Frame(self.root,bd=20,relief=RIDGE)
        Buttonframe.place(x=0,y=530,width=1530,height=70)
         
        #================================Details frame=======================================
        
        Detailsframe=Frame(self.root,bd=20,relief=RIDGE)
        Detailsframe.place(x=0,y=600,width=1530,height=190)
        #=====================DataframeLeft=================================================
        lblNameTablet=Label(DataframeLeft,text="Names of Tablets:",font=("arial",12,"bold"),padx=2,pady=6)
        lblNameTablet.grid(row=0,column=0,sticky=W)
        
        comNametablet=ttk.Combobox(DataframeLeft,state="readonly",textvariable=self.Nameoftablets,
                                                                 font=("times new roman",12,"bold"), width=34)
                                                                                  
        comNametablet["value"]=("Nice","Corana Vacacine","Acetaminophen","Adderall","Amlodpine","Ativan")
        comNametablet.current(0)
        comNametablet.grid(row=0,column=1)
        
        lblref=Label(DataframeLeft,font=("arial",12,"bold"),text="Refence No:",padx=2)
        lblref.grid(row=1,column=0,sticky=W)
        txtref=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.ref,width=35)
        txtref.grid(row=1,column=1)
        
        lbldose=Label(DataframeLeft,font=("arial",12,"bold"),text="Dose:",padx=2,pady=4)
        lbldose.grid(row=2,column=0,sticky=W)
        txtdose=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.Dose,width=35)
        txtdose.grid(row=2,column=1)
        
        
        lblNoOftablets=Label(DataframeLeft,font=("arial",12,"bold"),text="No of Tablets::",padx=2,pady=6)
        lblNoOftablets.grid(row=3,column=0,sticky=W)
        txtNoOftablets=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.NumberofTablets,width=35)
        txtNoOftablets.grid(row=3,column=1)
        
        lblLot=Label(DataframeLeft,font=("arial",12,"bold"),text="Lot:",padx=2,pady=6)
        lblLot.grid(row=4,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.Lot,width=35)
        txtLot.grid(row=4,column=1)
        
        lblissueDate=Label(DataframeLeft,font=("arial",12,"bold"),text="issue Date:",padx=2,pady=6)
        lblissueDate.grid(row=5,column=0,sticky=W)
        txtLot=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.Issuedate,width=35)
        txtLot.grid(row=5,column=1)
        
        lblExpDate=Label(DataframeLeft,font=("arial",12,"bold"),text="Exp Date:",padx=2,pady=6)
        lblExpDate.grid(row=6,column=0,sticky=W)
        txtExpDate=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.ExpDate,width=35)
        txtExpDate.grid(row=6,column=1)
        
        lblDailyDose=Label(DataframeLeft,font=("arial",12,"bold"),text="Daily Dose:",padx=2,pady=6)
        lblDailyDose.grid(row=7,column=0,sticky=W)
        txtDailyDose=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.DailyDose,width=35)
        txtDailyDose.grid(row=7,column=1)
        
        lblSideEffect=Label(DataframeLeft,font=("arial",12,"bold"),text="Side Effect:",padx=2,pady=6)
        lblSideEffect.grid(row=8,column=0,sticky=W)
        txtSideEffect=Entry(DataframeLeft,font=('arial',13,"bold"),textvariable=self.SideEffect,width=35)
        txtSideEffect.grid(row=8,column=1)
        
        lblFurtherInformation=Label(DataframeLeft,font=("arial",12,"bold"),text="Further Information:",padx=2)
        lblFurtherInformation.grid(row=0,column=2,sticky=W)
        txtFurtherInformation=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.FurtherInformation,width=35)
        txtFurtherInformation.grid(row=0,column=3)
        
        lblBloodPressure=Label(DataframeLeft,font=("arial",12,"bold"),text="Blood Pressure:",padx=2,pady=6)
        lblBloodPressure.grid(row=1,column=2,sticky=W)
        txtBloodPressure=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DrivingUsingMachine,width=35)
        txtBloodPressure.grid(row=1,column=3)
        
        lblStorageAdvice=Label(DataframeLeft,font=("arial",12,"bold"),text="Storage Advice:",padx=2,pady=6)
        lblStorageAdvice.grid(row=2,column=2,sticky=W)
        txtStorageAdvice=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.StorageAdvice,width=35)
        txtStorageAdvice.grid(row=2,column=3)
        
        lblMedication=Label(DataframeLeft,font=("arial",12,"bold"),text="Medication:",padx=2,pady=6)
        lblMedication.grid(row=3,column=2,sticky=W)
        txtMedication=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.HowToUseMedication,width=35)
        txtMedication.grid(row=3,column=3)
        
        lblPatientId=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Id:",padx=2,pady=6)
        lblPatientId.grid(row=4,column=2,sticky=W)
        txtPatientId=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientId,width=35)
        txtPatientId.grid(row=4,column=3)
        
        lblNHSNumber=Label(DataframeLeft,font=("arial",12,"bold"),text="NHS Number",padx=2,pady=6)
        lblNHSNumber.grid(row=5,column=2,sticky=W)
        txtNHSNumber=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.nhsNumber,width=35)
        txtNHSNumber.grid(row=5,column=3)
        
        lblPatientName=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Name:",padx=2,pady=6)
        lblPatientName.grid(row=6,column=2,sticky=W)
        txtPatientName=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientName,width=35)
        txtPatientName.grid(row=6,column=3)
        
        lblDateOfBirth=Label(DataframeLeft,font=("arial",12,"bold"),text="Date of Birth:",padx=2,pady=6)
        lblDateOfBirth.grid(row=7,column=2,sticky=W)
        txtDateOfBirth=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.DateOfBirth,width=35)
        txtDateOfBirth.grid(row=7,column=3)
        
        lblPatientAddress=Label(DataframeLeft,font=("arial",12,"bold"),text="Patient Address:",padx=2,pady=6)
        lblPatientAddress.grid(row=8,column=2,sticky=W)
        txtPatientAddress=Entry(DataframeLeft,font=("arial",12,"bold"),textvariable=self.PatientAddress,width=35)
        txtPatientAddress.grid(row=8,column=3)
        
        # ===========================DataFrameRight========================================
        self.txtPrescription=Text(dataframeRight,font=("arial",12,"bold"),width=45,height=16,padx=2,pady=6)
        self.txtPrescription.grid(row=0,column=0)
        
        
        #=============================buttons============================================
        btnPrescription=Button(Buttonframe,text="Prescription",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescription.grid(row=0,column=0)
        
        btnPrescriptionData=Button(Buttonframe,command=self.iPrescriptionData,text="Prescription Data",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnPrescriptionData.grid(row=0,column=1)
        
        btnUpdate=Button(Buttonframe,text="Update",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnUpdate.grid(row=0,column=2)
        
        btnDelete=Button(Buttonframe,text="Delete",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnDelete.grid(row=0,column=3)
        
        btnExit=Button(Buttonframe,text="Exit",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnExit.grid(row=0,column=4)
        
        btnClear=Button(Buttonframe,text="Clear",bg="green",fg="white",font=("arial",12,"bold"),width=23,padx=2,pady=6)
        btnClear.grid(row=0,column=5)
        
        # ===============================================Table===============================
        # ============================================Scroll Bar ============================
        scroll_x=ttk.Scrollbar(Detailsframe,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Detailsframe,orient=VERTICAL)
        self.hospital_table=ttk.Treeview(Detailsframe,column=("nameoftable","ref","dose","nooftablets","lot","issuedate","expdate",
                            "dailydose","storage","nhsnumber","pname","dob","address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x=ttk.Scrollbar(command=self.hospital_table.xview)
        scroll_y=ttk.Scrollbar(command=self.hospital_table.yview)
        
        self.hospital_table.heading("nameoftable",text="Name of Table")
        self.hospital_table.heading("ref",text="Reference No.")
        self.hospital_table.heading("dose",text="Dose")
        self.hospital_table.heading("nooftablets",text="No Of Tablets")
        self.hospital_table.heading("lot",text="Lot")
        self.hospital_table.heading("issuedate",text="Issue Date")
        self.hospital_table.heading("expdate",text="Exp Date")
        self.hospital_table.heading("dailydose",text="Daily Date")
        self.hospital_table.heading("storage",text="Storage")
        self.hospital_table.heading("nhsnumber",text="NHS Number")
        self.hospital_table.heading("pname",text="Patient Name")
        self.hospital_table.heading("dob",text="DOB")
        self.hospital_table.heading("address",text="Address")
        
        self.hospital_table["show"]="headings"
        
       
        self.hospital_table.column("nameoftable",width=100)
        self.hospital_table.column("ref",width=100)
        self.hospital_table.column("dose",width=100)
        self.hospital_table.column("nooftablets",width=100)
        self.hospital_table.column("lot",width=100)
        self.hospital_table.column("issuedate",width=100)
        self.hospital_table.column("expdate",width=100)
        self.hospital_table.column("dailydose",width=100)
        self.hospital_table.column("storage",width=100)
        self.hospital_table.column("nhsnumber",width=100)
        self.hospital_table.column("pname",width=100)
        self.hospital_table.column("dob",width=100)
        self.hospital_table.column("address",width=100)
        
        self.hospital_table.pack(fill=BOTH,expand=1)
        
        # =======================functionality Declaration======================================
    def iPrescriptionData(self):
        print("iPrescriptionData called")  # Debug print
        if self.Nameoftablets.get()=="" or self.ref.get()=="":
            print("Validation failed: Required fields are empty")  # Debug print
            messagebox.showerror("Error","All fields are required")
        else:
            try:
                print("Attempting to connect to the database...")
                # Connect to the MySQL database with a timeout
                conn = mysql.connector.connect(
                    host="?",
                    user="?",  
                    password="?",
                    database="?",
                    connection_timeout=5
                )
                print("Connected to the database successfully")
                my_cursor = conn.cursor()
                my_cursor.execute(
                    "insert into hospitalhms values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                    (   
                     
                        print("inserting data into the database"),
                        self.Nameoftablets.get(),
                        self.ref.get(),
                        self.Dose.get(),
                        self.NumberofTablets.get(),
                        self.Lot.get(),
                        self.Issuedate.get(),
                        self.ExpDate.get(),
                        self.DailyDose.get(),
                        self.StorageAdvice.get(),
                        self.nhsNumber.get(),
                        self.PatientName.get(),
                        self.DateOfBirth.get(),
                        self.PatientAddress.get()
                    )
                )
                print("Data inserted successfully, committing...")
                conn.commit()
                conn.close()
                print("Connection closed, showing success message")
                messagebox.showinfo("Success", "Record inserted successfully")
            except Exception as e:
                print(f"Exception occurred: {str(e)}")  # Debug print
                messagebox.showerror("Database Error", f"Error: {str(e)}")
        
        
        
        
        
        
        
        
        
        
          
                 
          
          
root = Tk()
ob = Hospital(root)
root.mainloop()
