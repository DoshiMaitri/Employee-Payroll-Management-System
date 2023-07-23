from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import mysql.connector
import time

class employeeSystem:
    def __init__(self,root):

        self.root = root
        self.root.title('Employee Payrool Management System')
        self.root.geometry('1800x900')
        
        self.heading = Label(root,text='Employee Payroll Management System',bg= 'Black',fg='White',pady=10,padx=2, font=('Times New Roman', 30,'bold')).place(x = 0,y=0,relwidth=1)   
        
        # def check_connection():

        def employeeDetails():
            self.root2 = Toplevel(self.root)
            self.root2.title('Employee Payroll Management System')
            self.root2.geometry('900x600')
            self.root2.config(bg='white')
            self.heading = Label(self.root2,text='All Employee Details',bg= 'Black',fg='White',pady=10,padx=2, font=('Times New Roman', 30,'bold')).pack(fill=X,side=TOP)  
            self.root2.focus_force()

            self.scrollX= Scrollbar(self.root2,orient=HORIZONTAL)
            self.scrollY= Scrollbar(self.root2,orient=VERTICAL)
            self.scrollX.pack(fill=X,side=BOTTOM)
            self.scrollY.pack(fill=Y,side=RIGHT)

            self.employeeTree = ttk.Treeview(self.root2,yscrollcommand=self.scrollY.set,xscrollcommand=self.scrollX.set,columns=('code', 'designation', 'name', 'age', 'gender', 'email', 'department', 'dob', 'doj', 'experience', 'aadhar_no', 'contact_no', 'status', 'address', 'month', 'year', 'salary', 'total_days', 'medical', 'covenence', 'overtime', 'absent', 'pf', 'net_salary', 'latemark', 'after_net_salary'))
            
            self.employeeTree.heading('code',text='EID')
            self.employeeTree.heading('designation',text='Designation')
            self.employeeTree.heading('name',text='Name')
            self.employeeTree.heading('age',text='Age')
            self.employeeTree.heading('gender',text='Gender')
            self.employeeTree.heading('email',text='Email')
            self.employeeTree.heading('department',text='Department')
            self.employeeTree.heading('dob',text='DOB')
            self.employeeTree.heading('doj',text='DOJ')
            self.employeeTree.heading('experience',text='Experience')
            self.employeeTree.heading('aadhar_no',text='Aadhar no')
            self.employeeTree.heading('contact_no',text='Contact no')
            self.employeeTree.heading('status',text='Status')
            self.employeeTree.heading('address',text='Address')
            self.employeeTree.heading('month',text='Month')
            self.employeeTree.heading('year',text='Year')
            self.employeeTree.heading('salary',text='Salary')
            self.employeeTree.heading('total_days',text='Total Days')
            self.employeeTree.heading('medical',text='Medical')
            self.employeeTree.heading('covenence',text='Convenence')
            self.employeeTree.heading('overtime',text='Overtime')
            self.employeeTree.heading('absent',text='Absent')
            self.employeeTree.heading('pf',text='PF')
            self.employeeTree.heading('net_salary',text='Net_salary')
            self.employeeTree.heading('latemark',text='Latemark')
            self.employeeTree.heading('after_net_salary',text='Salary Receipt')
            self.employeeTree['show']=['headings']

            self.employeeTree.column('code',width=100)
            self.employeeTree.column('designation',width=150)
            self.employeeTree.column('name',width=100)
            self.employeeTree.column('age',width=100)
            self.employeeTree.column('gender',width=100)
            self.employeeTree.column('email',width=150)
            self.employeeTree.column('department',width=150)
            self.employeeTree.column('dob',width=100)
            self.employeeTree.column('doj',width=100)
            self.employeeTree.column('experience',width=100)
            self.employeeTree.column('aadhar_no',width=100)
            self.employeeTree.column('contact_no',width=100)
            self.employeeTree.column('status',width=100)
            self.employeeTree.column('address',width=200)
            self.employeeTree.column('month',width=100)
            self.employeeTree.column('year',width=100)
            self.employeeTree.column('salary',width=100)
            self.employeeTree.column('total_days',width=100)
            self.employeeTree.column('medical',width=100)
            self.employeeTree.column('covenence',width=100)
            self.employeeTree.column('overtime',width=100)
            self.employeeTree.column('absent',width=100)
            self.employeeTree.column('pf',width=100)
            self.employeeTree.column('net_salary',width=100)
            self.employeeTree.column('latemark',width=100)
            self.employeeTree.column('after_net_salary',width=200)
            self.scrollY.config(command=self.employeeTree.yview)
            self.scrollX.config(command=self.employeeTree.xview)
            
            self.employeeTree.pack(fill=BOTH,expand=1)

            try:
                mydb = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='employee'
                )
                mycursor = mydb.cursor()
                mycursor.execute('select * from salary')
                res = mycursor.fetchall()
                print(res)
                self.employeeTree.delete(*self.employeeTree.get_children())
                for row in res:
                    self.employeeTree.insert('',END,values=row)

            except Exception as ex:
                messagebox.showerror('ERROR',f'Error due to {str(ex)}')
        
            finally:
                if mycursor:
                    mycursor.close()
                if mydb.is_connected():
                    mydb.close()
            self.root2.mainloop()        
        
        
        self.btn_allEmp = Button(self.heading,text='All employees',command=employeeDetails,bg= '#838B83',fg='White', font=('Times New Roman', 18,'bold'))
        self.btn_allEmp.place(x = 1375,y= 27,width=150,height=32)

        # ====================EmpVariables======================

        self.var_code = StringVar()
        self.var_designation = StringVar()
        self.var_name = StringVar()
        self.var_age = StringVar()
        self.var_gender = StringVar()
        self.var_email= StringVar()
        self.var_department = StringVar()
        self.var_dob = StringVar()
        self.var_doj = StringVar()
        self.var_experience = StringVar()
        self.var_aadhar = StringVar()
        self.var_contact = StringVar()
        self.var_status = StringVar()
        # self.var_add = StringVar()
        
        #===================EmpSalVariables=======================

        self.var_month = StringVar()
        self.var_year = StringVar()
        self.var_salary = StringVar()
        self.var_total_days = StringVar()
        self.var_absent = StringVar()
        self.var_medical = StringVar()
        self.var_pf = StringVar()
        self.var_convence = StringVar()
        self.var_net_salary = StringVar()
        self.var_overtime = StringVar()
        self.var_late_mark = StringVar()

        def search():
            try:
                mydb = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='employee'
                )
                mycursor = mydb.cursor()
                id = list(self.var_code.get())
                mycursor.execute('select * from salary where code = %s',id)
                res = mycursor.fetchone()

                if res == None:
                    messagebox.showinfo('Invalid ID',"Invalid Employee Id, Please enter another employee id")
                else:
                    self.var_code.set(res[0]),      
                    self.var_designation.set(res[1]),
                    self.var_name.set(res[2]),
                    self.var_age.set(res[3]),
                    self.var_gender.set(res[4]),
                    self.var_email.set(res[5]),
                    self.var_department.set(res[6]),
                    self.var_dob.set(res[7]),
                    self.var_doj.set(res[8]),
                    self.var_experience.set(res[9]),
                    self.var_aadhar.set(res[10]),
                    self.var_contact.set(res[11]),
                    self.var_status.set(res[12]),
                    self.txt_eaddress.delete('1.0',END)
                    self.txt_eaddress.insert(END,res[13]),

                    self.var_month.set(res[14]),
                    self.var_year.set(res[15]),
                    self.var_salary.set(res[16]),
                    self.var_total_days.set(res[17]),
                    self.var_medical.set(res[18]),
                    self.var_convence.set(res[19]),
                    self.var_overtime.set(res[20]),
                    self.var_absent.set(res[21]),
                    self.var_pf.set(res[22]),
                    self.var_net_salary.set(res[23]),
                    self.var_late_mark.set(res[24]),
                    file_ = open("salaryReceipt/"+str(res[25]),'r')
                    self.dataText.delete('1.0',END)
                    for i in file_:
                        self.dataText.insert(END,i)
                    file_.close()

                    self.btn_save.config(state=DISABLED)
                    self.btn_delete.config(state = NORMAL)
                    self.btn_update.config(state=NORMAL)
                    self.txt_empcode.config(state = 'readonly')
                    # print(res)
                
            except Exception as ex:
                messagebox.showerror('ERROR',f'Error due to {str(ex)}')

        # <--------------------------------------Employee details---------------------------------------->

        self.frameEmp = Frame(root,bd = 3 , relief=RIDGE,bg='#F0FFF0')
        self.frameEmp.place(x = 6,y = 75,width=750,height=720)

        self.title2=Label(self.frameEmp,text='Employee Details',bg= '#838B83',fg='black', font=('Times New Roman', 20,'bold')).place(x = 0,y=0,relwidth=1)
        
        self.empcode=Label(self.frameEmp,text='Employee Code :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x=10,y=70)
        self.txt_empcode=Entry(self.frameEmp,textvariable=self.var_code,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'))
        self.txt_empcode.place(x =170,y=70,width=300)
        
        self.bttn_search=Button(self.frameEmp,text='Search',bg= '#838B83',fg='black', command=search,font=('Times New Roman', 15,'bold'))
        self.bttn_search.place(x =505,y=68,width=100,height=30)

        self.designation=Label(self.frameEmp,text='Designation :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x=10,y=130)   
        self.txt_designation=Entry(self.frameEmp,bg= '#E0EEE0',textvariable=self.var_designation,fg='black', font=('Times New Roman', 15,'bold'))
        self.txt_designation.place(x=130,y=130,width=200)
        
        self.ename=Label(self.frameEmp,text='Name :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =10,y=182)
        self.txt_ename=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_name)
        self.txt_ename.place(x=130,y=182,width=200)
        
        self.eage=Label(self.frameEmp,text='Age :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =10,y=233)  
        self.txt_eage=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_age)
        self.txt_eage.place(x=130,y=235,width=200)
        
        self.egender=Label(self.frameEmp,text='Gender :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =10,y=286)
        self.txt_egender=Entry(self.frameEmp,bg='#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_gender)
        self.txt_egender.place(x =130,y=286,width=200)
        
        self.eEmail=Label(self.frameEmp,text='Email :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =10,y=338) 
        self.txt_eEmail=Entry(self.frameEmp,bg='#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_email)
        self.txt_eEmail.place(x =130,y=338,width=200)
               
        self.edepart=Label(self.frameEmp,text='Department :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =10,y=390)
        self.txt_depart=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_department)
        self.txt_depart.place(x =130,y=390,width=200)
 
        self.eaddress=Label(self.frameEmp,text='Address :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =10,y=445)
        self.txt_eaddress=Text(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'))
        self.txt_eaddress.place(x =130,y=450,width=575,height=200)
        
        self.edob=Label(self.frameEmp,text='Date of birth :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =350,y=130)
        self.txt_edob=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_dob)
        self.txt_edob.place(x =500,y=130,width=210)
        
        self.edoj=Label(self.frameEmp,text='Date of joining :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =350,y=180)
        self.txt_edoj=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_doj)
        self.txt_edoj.place(x =500,y=180,width=210)
        
        self.eExp=Label(self.frameEmp,text='Experience :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =350,y=233)
        self.txt_eExp=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_experience)
        self.txt_eExp.place(x =500,y=235,width=210)
        
        self.eadh=Label(self.frameEmp,text='Aadhar No :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =350,y=286)
        self.txt_eadh=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_aadhar)
        self.txt_eadh.place(x =500,y=286,width=210)
        
        self.econ=Label(self.frameEmp,text='Contact No :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =350,y=338)
        self.txt_econ=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_contact)
        self.txt_econ.place(x =500,y=338,width=210)

        self.estat=Label(self.frameEmp,text='Status :',bg='#F0FFF0',fg='black', font=('Times New Roman', 15,'bold')).place(x =350,y=390)
        self.txt_estat=Entry(self.frameEmp,bg= '#E0EEE0',fg='black', font=('Times New Roman', 15,'bold'),textvariable=self.var_status)
        self.txt_estat.place(x =500,y=390,width=210)


        # <---------------------------------Salary details-------------------------------->
         
        self.frameSal = Frame(root,bd = 3 , relief=RIDGE,bg='#F0FFF0')
        self.frameSal.place(x = 765,y = 75,width=765,height=350)

        self.heading =Label(self.frameSal,text='Salary Details',bg= '#838B83',fg='black', font=('Times New Roman', 20,'bold')).place(x = 0,y=0,relwidth=1)

        def calculate():

            if self.var_month.get() == '' or self.var_year.get() == '' or self.var_salary.get() == '' or self.var_code.get() == '' or self.var_name.get() == '' or self.var_aadhar.get() == '' or self.var_status.get() == '' or self.var_total_days.get() == '' or self.var_absent.get()== '' :
                messagebox.showinfo("Error", "ALL FIELDS ARE REQUIRED!!")
            
            else:
                self.per_day_sal = int(self.var_salary.get()) / int(self.var_total_days.get())
                self.work_days = int(self.var_total_days.get())-int(self.var_absent.get())
                self.sal = int(self.per_day_sal) * self.work_days
                self.deduct = int(self.var_medical.get()) + int(self.var_pf.get()) + (int(self.var_late_mark.get())*200)
                self.addition = int(self.var_convence.get()) + (int(self.var_overtime.get())*200)
                self.net_sal = self.sal - self.deduct + self.addition
                
                self.var_net_salary.set(self.net_sal)

                #---------------------- Receipt----------------
                sample = f'''\tCompany name, XYZ\n\tAddress: Xyz, Floor4
--------------------------------------------------------
 Employee Id\t\t:  {self.var_code.get()}
 Salary of \t\t: {self.var_month.get()}-{self.var_year.get()}
 Generated On\t\t: {str(time.strftime("%d-%m-%Y"))}
--------------------------------------------------------
 Total Days\t\t:  {self.var_total_days.get()}
 Total Present\t\t:  {str(int((self.var_total_days.get()))-int((self.var_absent.get())))}
 Total Absent\t\t:  {self.var_absent.get()}
 Convence\t\t:  Rs.{self.var_convence.get()}
 Medical\t\t:  Rs.{self.var_medical.get()}
 pf\t\t:  Rs.{self.var_pf.get()}
 Gross Payment\t\t:  Rs.{self.var_salary.get()}
 Net Salary\t\t:  Rs.{self.var_net_salary.get()}
-------------------------------------------------------
This is a computer generated slip, not 
required any signature
'''
                
                self.dataText.delete('1.0',END)
                self.dataText.insert('end',sample)

        

        # check_connection(self)

        def save():
            if self.var_name.get()=='' or self.var_code.get()=='' or self.var_salary.get() == '':
                messagebox.showerror('Error','Employee details are required')
            else:    
                try:
                    mydb = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='employee'
                    )
                    mycursor = mydb.cursor()
                    id = list(self.var_code.get())
                    mycursor.execute('select * from salary where code = %s',id)
                    res = mycursor.fetchone()

                    if res != None:
                        messagebox.showinfo("Error","This ID already present.\n Try again with another ID.")
                    else:
                        mycursor.execute('insert into salary values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',
                    (
                        self.var_code.get(),      
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_department.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_experience.get(),
                        self.var_aadhar.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_eaddress.get('1.0', END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_total_days.get(),
                        self.var_medical.get(),
                        self.var_convence.get(),
                        self.var_overtime.get(),
                        self.var_absent.get(),
                        self.var_pf.get(),
                        self.var_net_salary.get(),
                        self.var_late_mark.get(),
                        self.var_code.get()+".txt"  
                    ))
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                        
                        file_ = open("salaryReceipt/"+str(self.var_code.get())+".txt",'w')
                        var = self.dataText.get('1.0',END)
                        file_.write(var)

                        # print()
                        messagebox.showinfo("Success","Record inserted successfully!!")

                except Exception as ex:
                    messagebox.showerror('ERROR',f'Error due to {str(ex)}')
        

        def update():
            if self.var_name.get()=='' or self.var_code.get()=='' or self.var_salary.get() == '':
                messagebox.showerror('Error','Employee details are required')
            else:    
                try:
                    mydb = mysql.connector.connect(
                        host='localhost',
                        user='root',
                        password='',
                        database='employee'
                    )
                    mycursor = mydb.cursor()
                    id = list(self.var_code.get())
                    mycursor.execute('select * from salary where code = %s',id)
                    res = mycursor.fetchone()

                    if res == None:
                        messagebox.showerror("Error","This ID is invalid.\n Try again with another ID.")
                    else:
                        mycursor.execute("UPDATE `salary` SET `designation`=%s,`name`=%s,`age`=%s,`gender`=%s,`email`=%s,`department`=%s,`dob`=%s,`doj`=%s,`experience`=%s,`aadhar_no`=%s,`contact_no`=%s,`status`=%s,`address`=%s,`month`=%s,`year`=%s,`salary`=%s,`total_days`=%s,`medical`=%s,`covenence`=%s,`overtime`=%s,`absent`=%s,`pf`=%s,`net_salary`=%s,`latemark`=%s,`after_net_salary`=%s WHERE `code`=%s",
                    (
                        self.var_designation.get(),
                        self.var_name.get(),
                        self.var_age.get(),
                        self.var_gender.get(),
                        self.var_email.get(),
                        self.var_department.get(),
                        self.var_dob.get(),
                        self.var_doj.get(),
                        self.var_experience.get(),
                        self.var_aadhar.get(),
                        self.var_contact.get(),
                        self.var_status.get(),
                        self.txt_eaddress.get('1.0', END),
                        self.var_month.get(),
                        self.var_year.get(),
                        self.var_salary.get(),
                        self.var_total_days.get(),
                        self.var_medical.get(),
                        self.var_convence.get(),
                        self.var_overtime.get(),
                        self.var_absent.get(),
                        self.var_pf.get(),
                        self.var_net_salary.get(),
                        self.var_late_mark.get(),
                        self.var_code.get()+".txt",  
                        self.var_code.get()      
                    ))
                    mydb.commit()
                    mycursor.close()
                    mydb.close()
                        
                    file_ = open("salaryReceipt/"+str(self.var_code.get())+".txt",'w')
                    var = self.dataText.get('1.0',END)
                    file_.write(var)
                    file_.close()
                    messagebox.showinfo("Success","Record Updated successfully!!")

                except Exception as ex:
                    messagebox.showerror('ERROR',f'Error due to {str(ex)}')

        def delete():
            try:
                if self.var_code.get()=='':
                    messagebox.showerror("Error","Please enter your employee id.")
                mydb = mysql.connector.connect(
                    host='localhost',
                    user='root',
                    password='',
                    database='employee'
                )
                mycursor = mydb.cursor()
                id = list(self.var_code.get())
                mycursor.execute('select * from salary where code = %s',id)
                res = mycursor.fetchone()

                if res == None:
                    messagebox.showinfo('Invalid ID',"Invalid Employee Id, Please enter another employee id")
                else:
                    delC = messagebox.askyesno("Confirm","Do you really want to delete?")
                    if delC==YES:
                        mycursor.execute('delete from salary where code = %s',id)
                        mydb.commit()
                        mycursor.close()
                        mydb.close()
                        messagebox.showinfo("Success","Successful! Data is deleted")
                        clear()
            except Exception as ex:
                messagebox.showerror('ERROR',f'Error due to {str(ex)}')
        
        def clear():
            self.btn_save.config(state=NORMAL)
            self.btn_delete.config(state = DISABLED)
            self.btn_update.config(state=DISABLED)    
            self.txt_empcode.config(state = NORMAL)


            self.txt_empcode.delete(0,'end')      
            self.txt_designation.delete(0,'end')
            self.txt_ename.delete(0,'end')
            self.txt_eage.delete(0,'end')
            self.txt_egender.delete(0,'end')
            self.txt_eEmail.delete(0,'end')
            self.txt_depart.delete(0,'end')
            self.txt_edob.delete(0,'end')
            self.txt_edoj.delete(0,'end')
            self.txt_eExp.delete(0,'end')
            self.txt_eadh.delete(0,'end')
            self.txt_econ.delete(0,'end')
            self.txt_estat.delete(0,'end')
            self.txt_eaddress.delete('1.0', END)
            self.txt_month.delete(0,'end')
            self.txt_year.delete(0,'end')
            self.txt_salary.delete(0,'end')
            self.txt_total_days.delete(0,'end')
            self.txt_medical.delete(0,'end')
            self.txt_convence.delete(0,'end')
            self.txt_overtime.delete(0,'end')
            self.txt_absent.delete(0,'end')
            self.txt_pf.delete(0,'end')
            self.txt_late_mark.delete(0,'end')
            self.txt_net_salary.delete(0,'end')
            self.dataText.delete(0,END)
        #--------------ROW1-----------------

        self.lbl_month = Label(self.frameSal,text='Month',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=20,y=65) 
        self.txt_month = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_month,font=('Times New Roman',15))
        self.txt_month.place(x=95,y=65,width=150)

        self.lbl_year = Label(self.frameSal,text='Year',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=273,y=65) 
        self.txt_year = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_year,font=('Times New Roman',15))
        self.txt_year.place(x=335,y=65,width=150)

        self.lbl_salary = Label(self.frameSal,text='Salary',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=515,y=65) 
        self.txt_salary = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_salary,font=('Times New Roman',15))
        self.txt_salary.place(x=585,y=65,width=150)

        # --------------ROW2-----------------

        self.lbl_total_days = Label(self.frameSal,text='Total Days',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=35,y=130) 
        self.txt_total_days = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_total_days,font=('Times New Roman',15))
        self.txt_total_days.place(x=170,y=130,width=150)

        self.lbl_absent = Label(self.frameSal,text='Absent',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=432,y=130) 
        self.txt_absent = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_absent,font=('Times New Roman',15))
        self.txt_absent.place(x=550,y=130,width=150)

        #--------------ROW3-----------------

        self.lbl_medical = Label(self.frameSal,text='Medical',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=35,y=167) 
        self.txt_medical = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_medical,font=('Times New Roman',15))
        self.txt_medical.place(x=170,y=167,width=150)

        self.lbl_pf = Label(self.frameSal,text='PF',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=432,y=167) 
        self.txt_pf = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_pf,font=('Times New Roman',15))
        self.txt_pf.place(x=550,y=167,width=150)

        #--------------ROW4-----------------

        self.lbl_convence = Label(self.frameSal,text='Convence',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=35,y=205) 
        self.txt_convence = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_convence,font=('Times New Roman',15))
        self.txt_convence.place(x=170,y=205,width=150)

        self.lbl_late_mark = Label(self.frameSal,text='Late Mark',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=432,y=205) 
        self.txt_late_mark = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_late_mark,font=('Times New Roman',15))
        self.txt_late_mark.place(x=550,y=205,width=150)

        # --------------ROW5-----------------

        self.lbl_overtime = Label(self.frameSal,text='Overtime',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=35,y=242) 
        self.txt_overtime = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_overtime,font=('Times New Roman',15))
        self.txt_overtime.place(x=170,y=242,width=150)

        self.lbl_net_salary = Label(self.frameSal,text='Net Salary',bg='#F0FFF0',fg='black',font=('Times New Roman',16)).place(x=432,y=242) 
        self.txt_net_salary = Entry(self.frameSal,bg='#E0EEE0',textvariable=self.var_net_salary,font=('Times New Roman',15))
        self.txt_net_salary.place(x=550,y=242,width=150)

        #--------------ROW6[BUTTONS]-----------------
        self.btn_update = Button(self.frameSal,text='Update',font=('Times New Roman',16),command=update,bg = 'Blue',fg='White')
        self.btn_update.place(x=100,y=288,width=100)
        self.btn_calc = Button(self.frameSal,text='Calculate',font=('Times New Roman',16),command=calculate,bg = '#ffc346',fg='Black')
        self.btn_calc.place(x=210,y=287,width=100)
        self.btn_save = Button(self.frameSal,text='Save',font=('Times New Roman',16),fg='White',command=save,bg='#438925')
        self.btn_save.place(x=320,y=287,width=100)
        self.btn_clear = Button(self.frameSal,text='Clear',font=('Times New Roman',16),command=clear,bg='Grey',fg='Black')
        self.btn_clear.place(x=430,y=287,width=100)
        self.btn_delete = Button(self.frameSal,text='Delete',font=('Times New Roman',16),command=delete,bg='Red',fg='White')
        self.btn_delete.place(x=540,y=287,width=100)

        # <--------------------------Calculator and receipt details------------------------>
        self.frameCR = Frame(root,bd = 3 , relief=RIDGE,bg='#F0FFF0')
        self.frameCR.place(x = 765,y = 430,width=765,height=363)

        # <------------------------------ Calculator Frame --------------------------------------> 
        self.frameC = Frame(self.frameCR,bd = 3 , relief=RIDGE, bg='#F0FFF0')
        self.frameC.place(x = 2,y = 3,width=385,height=352)

        self.entryVar = StringVar()
        self.operator = ''

        def buttonClick(num):
            self.operator = self.operator + str(num)
            self.entryVar.set(self.operator)
            # print(self.operator)

        def result():
            res = eval(self.operator)
            self.entryVar.set(res)
            self.operator = ''

        def delete_header():
            self.operator = ''
            self.entryVar.set('')

        self.header = Entry(self.frameC,font=('Times New Roman', 20,'bold'),justify=RIGHT,textvariable=self.entryVar).place(x = 3,y = 4,height=70,width=370)
        
        # Buttons 

        # Row 1
        self.button7 = Button(self.frameC,text='7',command = lambda:buttonClick(7) ,font=('Times New Roman', 18,'bold')).place(x = 2,y= 77,width=92,height=68)
        self.button8 = Button(self.frameC,text='8',command = lambda:buttonClick(8),font=('Times New Roman', 18,'bold')).place(x = 95,y= 77,width=93,height=68)
        self.button9 = Button(self.frameC,text='9',command = lambda:buttonClick(9),font=('Times New Roman', 18,'bold')).place(x = 190,y= 77,width=93,height=68)
        self.button_Slash = Button(self.frameC,command = lambda:buttonClick('/'),text='/',font=('Times New Roman', 18,'bold')).place(x = 285,y= 77,width=92,height=68)
        
        # Row 2
        self.button4 = Button(self.frameC,text='4',command = lambda:buttonClick(4),font=('Times New Roman', 18,'bold')).place(x = 2,y= 145,width=92,height=68)
        self.button5 = Button(self.frameC,text='5',command = lambda:buttonClick(5),font=('Times New Roman', 18,'bold')).place(x = 95,y= 145,width=93,height=68)
        self.button6 = Button(self.frameC,text='6',command = lambda:buttonClick(6),font=('Times New Roman', 18,'bold')).place(x =190,y= 145,width=93,height=68)
        self.button_astric = Button(self.frameC,text='*',command = lambda:buttonClick('*'),font=('Times New Roman', 18,'bold')).place(x = 285,y= 145,width=92,height=68)
        
        # Row 3
        self.button1 = Button(self.frameC,text='1',command = lambda:buttonClick(1),font=('Times New Roman', 18,'bold')).place(x = 2,y= 212,width=92,height=68)
        self.button2 = Button(self.frameC,text='2',command = lambda:buttonClick(2),font=('Times New Roman', 18,'bold')).place(x = 95,y= 212,width=93,height=68)
        self.button3 = Button(self.frameC,text='3',command = lambda:buttonClick(3),font=('Times New Roman', 18,'bold')).place(x =190,y= 212,width=93,height=68)
        self.button_minus = Button(self.frameC,text='-',command = lambda:buttonClick('-'),font=('Times New Roman', 18,'bold')).place(x = 285,y= 212,width=92,height=68)
        
        # Row 4
        self.button0 = Button(self.frameC,text='0',command = lambda:buttonClick(0),font=('Times New Roman', 18,'bold')).place(x = 2,y= 280,width=92,height=68)
        self.button_Clear = Button(self.frameC,text='C',command=lambda:delete_header(),font=('Times New Roman', 18,'bold')).place(x = 95,y= 280,width=93,height=68)
        self.button_plus = Button(self.frameC,text='+',command = lambda:buttonClick('+'),font=('Times New Roman', 18,'bold')).place(x = 190,y= 280,width=93,height=68)
        self.button_equal = Button(self.frameC,text='=',command=lambda:result(),font=('Times New Roman', 18,'bold')).place(x = 285,y= 280,width=92,height=68)

        #  <------------------------------Receipt Frame---------------------------------> 
        self.frameR = Frame(self.frameCR,bd = 3 , relief=RIDGE , bg='#F0FFF0')
        self.frameR.place(x = 388,y = 2,width=370,height=352)

        self.title3 = Label(self.frameR,text='Salary Receipt',bg= '#838B83',fg='black', font=('Times New Roman', 20,'bold')).place(x = 0,y=0,relwidth=1)

        # <------------------------TEXT Salary receipt Frame---------------------------->
        self.frameT = Frame(self.frameR,bd = 3 , relief=RIDGE )
        self.frameT.place(x = 0, y = 38, width = 364, height=307)

        self.scrollBar = Scrollbar(self.frameT, orient=VERTICAL)
        self.scrollBar.pack(side=RIGHT,fill=Y)
        self.dataText = Text(self.frameT,font=('Times New Roman', 13,'bold'),bg='#fadae8',yscrollcommand=self.scrollBar.set)
        self.dataText.pack(expand=1,fill=BOTH)   

        sample = f'''\tCompany name, XYZ\n\tAddress: Xyz, Floor4
--------------------------------------------------------
 Employee Id\t\t:  
 Salary of \t\t: Mon-Year
 Generated On\t\t: DD-MM-YYYY
--------------------------------------------------------
 Total Days\t\t:  DD
 Total Present\t\t:  DD
 Total Absent\t\t:  DD
 Convence\t\t:  Rs.----
 Medical\t\t:  Rs.----
 pf\t\t:  Rs.----
 Gross Payment\t\t:  Rs.----
 Net Salary\t\t:  Rs.----
-------------------------------------------------------
This is a computer generated slip, not 
required any signature
'''
                
        self.dataText.delete('1.0',END)
        self.dataText.insert('end',sample)


        self.scrollBar.config(command=self.dataText.yview)

root=Tk()
obj = employeeSystem(root)
root.mainloop()
