import tkinter as tk

class Student:
    def __init__(self, name, rollno, m1, m2):
        self.name = name
        self.rollno = rollno
        self.m1 = m1
        self.m2 = m2

    def accept(self, Name, Rollno, marks1, marks2):
        ob = Student(Name, Rollno, marks1, marks2)
        ls.append(ob)

    def display(self, ob):
        return f"Name : {ob.name}\nRollNo : {ob.rollno}\nMarks1 : {ob.m1}\nMarks2 : {ob.m2}\n"

    def search(self, rn):
        for i in range(len(ls)):
            if ls[i].rollno == rn:
                return i
        return -1

    def delete(self, rn):
        i = self.search(rn)
        if i != -1:
            del ls[i]

    def update(self, rn, No):
        i = self.search(rn)
        if i != -1:
            ls[i].rollno = No

ls = []
obj = Student('', 0, 0, 0)

def accept_student():
    name = name_entry.get()
    try:
        rollno = int(rollno_entry.get())
        marks1 = int(marks1_entry.get())
        marks2 = int(marks2_entry.get())
        obj.accept(name, rollno, marks1, marks2)
    except ValueError:
        print("Invalid input for roll number or marks.")

def display_students():
    result_text.config(state=tk.NORMAL)
    result_text.delete(1.0, tk.END)
    for i in range(len(ls)):
        result_text.insert(tk.END, obj.display(ls[i]) + "\n")
    result_text.config(state=tk.DISABLED)

def search_student():
    rollno = int(search_rollno_entry.get())
    s = obj.search(rollno)
    if s != -1:
        search_result_text.config(state=tk.NORMAL)
        search_result_text.delete(1.0, tk.END)
        search_result_text.insert(tk.END, obj.display(ls[s]) + "\n")
        search_result_text.config(state=tk.DISABLED)
    else:
        print("Student not found.")

def delete_student():
    rollno = int(delete_rollno_entry.get())
    obj.delete(rollno)
    display_students()

def update_student():
    old_rollno = int(update_old_rollno_entry.get())
    new_rollno = int(update_new_rollno_entry.get())
    obj.update(old_rollno, new_rollno)
    display_students()

# GUI
root = tk.Tk()
root.title("Student Management System")

name_label = tk.Label(root, text="Name:")
name_label.grid(row=0, column=0)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1)

rollno_label = tk.Label(root, text="Roll No:")
rollno_label.grid(row=1, column=0)
rollno_entry = tk.Entry(root)
rollno_entry.grid(row=1, column=1)

marks1_label = tk.Label(root, text="Marks 1:")
marks1_label.grid(row=2, column=0)
marks1_entry = tk.Entry(root)
marks1_entry.grid(row=2, column=1)

marks2_label = tk.Label(root, text="Marks 2:")
marks2_label.grid(row=3, column=0)
marks2_entry = tk.Entry(root)
marks2_entry.grid(row=3, column=1)

accept_button = tk.Button(root, text="Accept Student", command=accept_student)
accept_button.grid(row=4, column=0, columnspan=2)

display_button = tk.Button(root, text="Display Students", command=display_students)
display_button.grid(row=5, column=0, columnspan=2)

search_rollno_label = tk.Label(root, text="Search Roll No:")
search_rollno_label.grid(row=6, column=0)
search_rollno_entry = tk.Entry(root)
search_rollno_entry.grid(row=6, column=1)
search_button = tk.Button(root, text="Search Student", command=search_student)
search_button.grid(row=7, column=0, columnspan=2)

delete_rollno_label = tk.Label(root, text="Delete Roll No:")
delete_rollno_label.grid(row=8, column=0)
delete_rollno_entry = tk.Entry(root)
delete_rollno_entry.grid(row=8, column=1)
delete_button = tk.Button(root, text="Delete Student", command=delete_student)
delete_button.grid(row=9, column=0, columnspan=2)

update_old_rollno_label = tk.Label(root, text="Old Roll No:")
update_old_rollno_label.grid(row=10, column=0)
update_old_rollno_entry = tk.Entry(root)
update_old_rollno_entry.grid(row=10, column=1)

update_new_rollno_label = tk.Label(root, text="New Roll No:")
update_new_rollno_label.grid(row=11, column=0)
update_new_rollno_entry = tk.Entry(root)
update_new_rollno_entry.grid(row=11, column=1)
update_button = tk.Button(root, text="Update Student", command=update_student)
update_button.grid(row=12, column=0, columnspan=2)

result_text = tk.Text(root, height=10, width=50)
result_text.grid(row=13, column=0, columnspan=2)
result_text.config(state=tk.DISABLED)

search_result_text = tk.Text(root, height=4, width=50)
search_result_text.grid(row=14, column=0, columnspan=2)
search_result_text.config(state=tk.DISABLED)

root.mainloop()
