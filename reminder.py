

# ---------------------------------------
input1 = input("Write UserName:")

input2 = input("Write Medical History:")

file = open("UserData.txt", "w")

file.write("Name : " + input1 + "\n" + "Medical History : " + input2 + "\n")

file.close()


# ---------------------------------------

import tkinter
import json




def writeToJSONFile(Udetails, filename):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join data with file_data inside emp_details
        file_data["medicine_details"].append(Udetails)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)



def save_info():

    fileName = 'Med_details.json'

    Udetails = {}
    Udetails['UserName'] = Uname.get()
    Udetails['UserHistory'] = Uhistory.get()
    Udetails['Medicines'] = data = {}

    

    data['Medicine_1'] = Medicine1.get()
    data['Med1_Daily'] = Day1.get()
    data['Med1_Weekly'] = Week1.get()
    data['Med1_Monthly'] = Month1.get()
    data['Medicine_2'] = Medicine2.get()
    data['Med2_Daily'] = Day2.get()
    data['Med2_Weekly'] = Week2.get()
    data['Med2_Monthly'] = Month2.get()
    data['Medicine_3'] = Medicine3.get()
    data['Med3_Daily'] = Day3.get()
    data['Med3_Weekly'] = Week3.get()
    data['Med3_Monthly'] = Month3.get()
    data['Medicine_4'] = Medicine4.get()
    data['Med4_Daily'] = Day4.get()
    data['Med4_Weekly'] = Week4.get()
    data['Med4_Monthly'] = Month4.get()
    data['Medicine_5'] = Medicine5.get()
    data['Med5_Daily'] = Day5.get()
    data['Med5_Weekly'] = Week5.get()
    data['Med5_Monthly'] = Month5.get()
    data['Medicine_6'] = Medicine6.get()
    data['Med6_Daily'] = Day6.get()
    data['Med6_Weekly'] = Week6.get()
    data['Med6_Monthly'] = Month6.get()

    writeToJSONFile(Udetails, fileName)

    Uname_entry.delete(0, tkinter.END)
    Uhistory_entry.delete(0, tkinter.END)
    Medicine1_entry.delete(0, tkinter.END)
    Day1_entry.delete(0, tkinter.END)
    Week1_entry.delete(0, tkinter.END)
    Month1_entry.delete(0, tkinter.END)
    Medicine2_entry.delete(0, tkinter.END)
    Day2_entry.delete(0, tkinter.END)
    Week2_entry.delete(0, tkinter.END)
    Month2_entry.delete(0, tkinter.END)
    Medicine3_entry.delete(0, tkinter.END)
    Day3_entry.delete(0, tkinter.END)
    Week3_entry.delete(0, tkinter.END)
    Month3_entry.delete(0, tkinter.END)
    Medicine4_entry.delete(0, tkinter.END)
    Day4_entry.delete(0, tkinter.END)
    Week4_entry.delete(0, tkinter.END)
    Month4_entry.delete(0, tkinter.END)
    Medicine1_entry.delete(0, tkinter.END)
    Day5_entry.delete(0, tkinter.END)
    Week5_entry.delete(0, tkinter.END)
    Month5_entry.delete(0, tkinter.END)
    Medicine6_entry.delete(0, tkinter.END)
    Day6_entry.delete(0, tkinter.END)
    Week6_entry.delete(0, tkinter.END)
    Month6_entry.delete(0, tkinter.END)




root = tkinter.Tk()
root.geometry("1920x1080")
root.title("Medicine Form")
heading = tkinter.Label(text="Form for Medicine", bg="grey", fg="black", width="500", height="3")
heading.pack()

#Labels
Uname_text = tkinter.Label(text="Name * ",)
Uhistory_text = tkinter.Label(text="Medicial history *",)
Medicine1_text = tkinter.Label(text="Med 1 * ", )
Day1_text = tkinter.Label(text="Day * ", )
Week1_text = tkinter.Label(text="Week * ", )
Month1_text = tkinter.Label(text="Month * ", )
Medicine2_text = tkinter.Label(text="Med 2 * ", )
Day2_text = tkinter.Label(text="Day * ", )
Week2_text = tkinter.Label(text="Week * ", )
Month2_text = tkinter.Label(text="Month * ", )
Medicine3_text = tkinter.Label(text="Med 3 * ", )
Day3_text = tkinter.Label(text="Day * ", )
Week3_text = tkinter.Label(text="Week * ", )
Month3_text = tkinter.Label(text="Month * ", )
Medicine4_text = tkinter.Label(text="Med 4 * ", )
Day4_text = tkinter.Label(text="Day * ", )
Week4_text = tkinter.Label(text="Week * ", )
Month4_text = tkinter.Label(text="Month * ", )
Medicine5_text = tkinter.Label(text="Med 5 * ", )
Day5_text = tkinter.Label(text="Day * ", )
Week5_text = tkinter.Label(text="Week * ", )
Month5_text = tkinter.Label(text="Month * ", )
Medicine6_text = tkinter.Label(text="Med 6 * ", )
Day6_text = tkinter.Label(text="Day * ", )
Week6_text = tkinter.Label(text="Week * ", )
Month6_text = tkinter.Label(text="Month * ", )


#Label places for medicines and for their repetiveness 

Uname_text.place(x=800, y= 120)
Uhistory_text.place(x=800, y= 220)

Medicine1_text.place(x=15, y=120)
Day1_text.place(x=250, y=120)
Week1_text.place(x=450, y=120)
Month1_text.place(x=650, y=120)
Medicine2_text.place(x=15, y=220)
Day2_text.place(x=250, y=220)
Week2_text.place(x=450, y=220)
Month2_text.place(x=650, y=220)
Medicine3_text.place(x=15, y=320)
Day3_text.place(x=250, y=320)
Week3_text.place(x=450, y=320)
Month3_text.place(x=650, y=320)
Medicine4_text.place(x=15, y=420)
Day4_text.place(x=250, y=420)
Week4_text.place(x=450, y=420)
Month4_text.place(x=650, y=420)
Medicine5_text.place(x=15, y=520)
Day5_text.place(x=250, y=520)
Week5_text.place(x=450, y=520)
Month5_text.place(x=650, y=520)
Medicine6_text.place(x=15, y=620)
Day6_text.place(x=250, y=620)
Week6_text.place(x=450, y=620)
Month6_text.place(x=650, y=620)





Uname = tkinter.StringVar()
Uhistory = tkinter.StringVar()
Medicine1 = tkinter.StringVar()
Day1 = tkinter.IntVar()
Week1 = tkinter.IntVar()
Month1 = tkinter.IntVar()
Medicine2 = tkinter.StringVar()
Day2 = tkinter.IntVar()
Week2 = tkinter.IntVar()
Month2 = tkinter.IntVar()
Medicine3 = tkinter.StringVar()
Day3 = tkinter.IntVar()
Week3 = tkinter.IntVar()
Month3 = tkinter.IntVar()
Medicine4 = tkinter.StringVar()
Day4 = tkinter.IntVar()
Week4 = tkinter.IntVar()
Month4 = tkinter.IntVar()
Medicine5 = tkinter.StringVar()
Day5 = tkinter.IntVar()
Week5 = tkinter.IntVar()
Month5 = tkinter.IntVar()
Medicine6 = tkinter.StringVar()
Day6 = tkinter.IntVar()
Week6 = tkinter.IntVar()
Month6 = tkinter.IntVar()


#Entry fields for medicines

Uname_entry = tkinter.Entry(textvariable=Uname, width="50")
Uhistory_entry = tkinter.Entry(textvariable=Uhistory, width="50")
Medicine1_entry = tkinter.Entry(textvariable=Medicine1, width="30")
Day1_entry = tkinter.Entry(textvariable=Day1, width="10")
Week1_entry = tkinter.Entry(textvariable=Week1, width="10")
Month1_entry = tkinter.Entry(textvariable=Month1, width="10")
Medicine2_entry = tkinter.Entry(textvariable=Medicine2, width="30")
Day2_entry = tkinter.Entry(textvariable=Day2, width="10")
Week2_entry = tkinter.Entry(textvariable=Week2, width="10")
Month2_entry = tkinter.Entry(textvariable=Month2, width="10")
Medicine3_entry = tkinter.Entry(textvariable=Medicine3, width="30")
Day3_entry = tkinter.Entry(textvariable=Day3, width="10")
Week3_entry = tkinter.Entry(textvariable=Week3, width="10")
Month3_entry = tkinter.Entry(textvariable=Month3, width="10")
Medicine4_entry = tkinter.Entry(textvariable=Medicine4, width="30")
Day4_entry = tkinter.Entry(textvariable=Day4, width="10")
Week4_entry = tkinter.Entry(textvariable=Week4, width="10")
Month4_entry = tkinter.Entry(textvariable=Month4, width="10")
Medicine5_entry = tkinter.Entry(textvariable=Medicine5, width="30")
Day5_entry = tkinter.Entry(textvariable=Day5, width="10")
Week5_entry = tkinter.Entry(textvariable=Week5, width="10")
Month5_entry = tkinter.Entry(textvariable=Month5, width="10")
Medicine6_entry = tkinter.Entry(textvariable=Medicine6, width="30")
Day6_entry = tkinter.Entry(textvariable=Day6, width="10")
Week6_entry = tkinter.Entry(textvariable=Week6, width="10")
Month6_entry = tkinter.Entry(textvariable=Month6, width="10")



#inputbox places

Uname_entry.place(x = 800, y = 150)
Uhistory_entry.place(x = 800, y = 250)
Medicine1_entry.place(x=15, y=150)
Day1_entry.place(x=250, y=150)
Week1_entry.place(x=450, y=150)
Month1_entry.place(x=650, y=150)
Medicine2_entry.place(x=15, y=250)
Day2_entry.place(x=250, y=250)
Week2_entry.place(x=450, y=250)
Month2_entry.place(x=650, y=250)
Medicine3_entry.place(x=15, y=350)
Day3_entry.place(x=250, y=350)
Week3_entry.place(x=450, y=350)
Month3_entry.place(x=650, y=350)
Medicine4_entry.place(x=15, y=450)
Day4_entry.place(x=250, y=450)
Week4_entry.place(x=450, y=450)
Month4_entry.place(x=650, y=450)
Medicine5_entry.place(x=15, y=550)
Day5_entry.place(x=250, y=550)
Week5_entry.place(x=450, y=550)
Month5_entry.place(x=650, y=550)
Medicine6_entry.place(x=15, y=650)
Day6_entry.place(x=250, y=650)
Week6_entry.place(x=450, y=650)
Month6_entry.place(x=650, y=650)





register = tkinter.Button(root, text="Submit Form", width="30", height="2", command=save_info, bg="grey")
register.place(x=500, y=750)
root.mainloop()


#--------------------------------fdffdfdf----------------------------------#
#Code for Scheduling medicines on calender but not working

# from pprint import pprint
# from re import M
# from Google import Create_Service, convert_to_RFC_datetime

# CLIENT_SECRET_FILE = 'Med_details.json'
# API_NAME = 'calendar'
# API_VERSION = 'v3'
# SCOPES = ['https://www.googleapi.com/auth/calendar']

# service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
# calender_id = 'primary'


# Create event

# colors = service.colors().get().execute()
# pprint(colors)

# hour_adjustment = -5
# event_request_body = {
#     'start' : {
#         'dateTime' : convert_to_RFC_datetime(2021, 8, 15, 12 + hour_adjustment, 30),
#         'timeZone' : 'Asia/Kolkata'
#     },
#     'end' : {
#         'dateTime' : convert_to_RFC_datetime(2021, 8, 15, 14 + hour_adjustment, 30),
#         'timeZone' : 'Asia/Kolkata'
#     },
#     'summary' : 'Medicine Reminder',
#     'description' : 'Having medicines',
#     'colorId' : 5,
#     'status' : 'confirmed',
#     'transperancy' : 'opaque',
#     'visibility' : 'private',
#     'location' : 'New Delhi, india'
# }

# maxAttendees = 5
# sendNotification = True
# sendUpdate = 'none'
# supportsAttachments = 'True'

# response = service.events().insert(
#     calender_id = 'primary',
#     maxAttendees = maxAttendees,
#     sendNotification = sendNotification,
#     sendUpdate = sendUpdate,
#     supportsAttachments = supportsAttachments,
#     body = event_request_body
# ).execute()

# pprint(response)