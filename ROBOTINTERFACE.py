import math
from Tkinter import *
import Tkinter as tk
import time

from mc.dsa import*


class MyRobo:
    global x_positions
    global y_positions
    global Z_positions
    global g_positions
    x_positions = []
    y_positions = []
    Z_positions = []
    g_positions = []

    def __init__(self, win):
        self.lbl1=Label(win, text='Joint1 angle', bg="#FFDAB9", fg="maroon")
        self.lbl1.place(x=200, y=100)
        self.b1=Button(win, text='+10', command=self.joint1anglep)
        self.b1.place(x=200, y=125)

        self.lbl2=Label(win, text='Joint1 angle',bg="#FFDAB9", fg="maroon")
        self.lbl2.place(x=200, y=100)
        self.b2=Button(win, text='-10', command=self.joint1anglem)
        self.b2.place(x=235, y=125)

        self.lbl3=Label(win, text='X', bg="#FFDAB9", fg="Purple")
        self.lbl3.place(x=100, y=100)
        self.b3=Button(win, text='X+', command=self.xplus)
        self.b3.place(x=80, y=125)

        self.lbl4=Label(win, text='X', bg="#FFDAB9", fg="Purple")
        self.lbl4.place(x=100, y=100)
        self.b4=Button(win, text='X-', command=self.xminus)
        self.b4.place(x=110, y=125)

        self.lbl5=Label(win, text='Y', bg="#FFDAB9", fg="Purple")
        self.lbl5.place(x=100, y=200)
        self.b5=Button(win, text='Y+', command=self.yplus)
        self.b5.place(x=80, y=225)

        self.lbl6=Label(win, text='Y', bg="#FFDAB9", fg="Purple")
        self.lbl6.place(x=100, y=200)
        self.b6=Button(win, text='Y-', command=self.yminus)
        self.b6.place(x=110, y=225)

        self.lbl7=Label(win, text='Joint2 angle', bg="#FFDAB9", fg="maroon")
        self.lbl7.place(x=200, y=200)
        self.b7=Button(win, text='+10', command=self.joint2anglep)
        self.b7.place(x=200, y=225)

        self.lbl8=Label(win, text='Joint2 angle', bg="#FFDAB9", fg="maroon")
        self.lbl8.place(x=200, y=200)
        self.b8=Button(win, text='-10', command=self.joint2anglem)
        self.b8.place(x=235, y=225)

        self.lbl9=Label(win, text='Reference', bg="#FFDAB9", fg="brown")
        self.lbl9.place(x=350, y=200)
        self.b9=Button(win, text='Press', command=self.reference)
        self.b9.place(x=360, y=225)

        self.lbl10=Label(win, text='Position', bg="#FFDAB9", fg="brown")
        self.lbl10.place(x=350, y=300)
        self.b10=Button(win, text='Check', command=self.position)
        self.b10.place(x=352, y=325)
        self.lbl11=Label(win, text='The position is:', bg="#FFB6C1")
        self.lbl11.place(x=225, y=40)

        self.lbl12=Label(win, text='Enter', bg="#FFDAB9", fg="Purple")
        self.t1=Entry(bd=1)
        self.t2=Entry()
        self.b12=Button(win,text='Enter', command=self.inxy)
        self.lbl22=Label(win, text='X=', bg="#FFDAB9", fg="brown")
        self.lbl22.place(x=475, y=100)
        self.lbl23=Label(win, text='Y=', bg="#FFDAB9", fg="brown")
        self.lbl23.place(x=475, y=150)
        self.b12.place(x=525, y=200)
        self.t1.place(x=500, y=100)
        self.t2.place(x=500, y=150)

        self.lbl13=Label(win, text='Z', bg="#FFDAB9", fg="Purple")
        self.lbl13.place(x=100, y=300)
        self.b13=Button(win, text='Z+', command=self.zplus)
        self.b13.place(x=80, y=325)

        self.lbl14=Label(win, text='Z', bg="#FFDAB9", fg="Purple")
        self.lbl14.place(x=100, y=300)
        self.b14=Button(win, text='Z-', command=self.zminus)
        self.b14.place(x=110, y=325)

        self.lbl15=Label(win, text='Gripper', bg="#FFDAB9", fg="Purple")
        self.lbl15.place(x=80, y=400)
        self.b15=Button(win, text='ON', command=self.gon)
        self.b15.place(x=70, y=425)

        self.lbl16=Label(win, text='Gripper', bg="#FFDAB9", fg="Purple")
        self.lbl16.place(x=80, y=400)
        self.b16=Button(win, text='OFF', command=self.goff)
        self.b16.place(x=110, y=425)

        self.lbl17=Label(win, text='Gripper', bg="#FFDAB9", fg="maroon")
        self.lbl17.place(x=200, y=300)
        self.b17=Button(win, text='G+', command=self.gplus)
        self.b17.place(x=200, y=325)

        self.lbl18=Label(win, text='Gripper', bg="#FFDAB9", fg="maroon")
        self.lbl18.place(x=200, y=300)
        self.b18=Button(win, text='G-', command=self.gminus)
        self.b18.place(x=235, y=325)

        self.b19=Button(win, text='STOP',bg='red', command=self.stop)
        self.b19.place(x=350, y=115)

        self.b20=Button(win, text='TEACH', bg="#FFDAB9", fg="brown", command=self.teach)
        self.b20.place(x=500, y=300)

        self.b21=Button(win, text='APPLICATION', bg="#FFDAB9", fg="brown", command=self.app)
        self.b21.place(x=500, y=400)

        self.b22=Button(win, text='CLEAR', bg="#FFDAB9", fg="brown", command=self.clear)
        self.b22.place(x=550, y=300)

        self.b22=Button(win, text='CLOSE', bg="#FFDAB9", fg="red", command=self.close)
        self.b22.place(x=600, y=40)






    def joint1anglep(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)
         p11 =int(d1.ActPos())
         T1g = 10
         Ink1 = p11 + (T1g*270)
         p21 = int(Ink1)

         d1.Enable()
         d1.ModePos()

         d1.VelAcc_dV(1000)
         d1.VelAcc_dT(5000)

         d1.VelDec_dV(1000)
         d1.VelDec_dT(5000)

         d1.Vel(2500)
         d1.Mova(p21)
         time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))
    def joint1anglem(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)
         p11 =int(d1.ActPos())
         T1g = 10
         Ink1 = p11 - (T1g*270)
         p21 = int(Ink1)

         d1.Enable()
         d1.ModePos()

         d1.VelAcc_dV(1000)
         d1.VelAcc_dT(5000)

         d1.VelDec_dV(1000)
         d1.VelDec_dT(5000)

         d1.Vel(2500)
         d1.Mova(p21)
         time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def joint2anglep(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)
         p12 =int(d2.ActPos())
         T2g = 10
         Ink2 = p12 - (T2g*275)
         p22 = int(Ink2)

         d2.Enable()
         d2.ModePos()

         d2.VelAcc_dV(5000)
         d2.VelAcc_dT(5000)

         d2.VelDec_dV(5000)
         d2.VelDec_dT(5000)

         d2.Vel(2500)
         d2.Mova(p22)
         time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))


    def joint2anglem(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)
         p12 =int(d2.ActPos())
         T2g = 10
         Ink2 = p12 + (T2g*275)
         p22 = int(Ink2)

         d2.Enable()
         d2.ModePos()

         d2.VelAcc_dV(5000)
         d2.VelAcc_dT(5000)

         d2.VelDec_dV(5000)
         d2.VelDec_dT(5000)

         d2.Vel(2500)
         d2.Mova(p22)
         time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def xplus(self):

         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)

         p21 = int(d1.ActPos())  
         p22 = int(d2.ActPos())  

         # SCARA robot parameters
         L1 = 186  
         L2 = 157

         #find the angles
         T11 = ((70000 - p21) / 270) - ((70000 / 270) - 224.0740)
         T22 = ((82000 - p22) / 275) - ((82000 / 275) - 130.909090)

         # Convert angles T1 and T2 to radians
         T1 = math.radians(T11)
         T2 = math.radians(360 - T22)

         # Calculate coordinates
         x = round(L1 * math.cos(T1) + L2 * math.cos(T1 + T2))
         y = round(L1 * math.sin(T1) + L2 * math.sin(T1 + T2))


         def inverse_kinematics(x, y, L1, L2):
            
             r = math.sqrt(x ** 2 + y ** 2)

             # Check if the position is out of reach
             if r > L1 + L2 or r < abs(141):
                 raise ValueError("Position out of reach for the robot arm")

             theta1 = math.acos((r ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * r)) + math.acos(x / r)

           
             theta2 = math.acos((math.cos(theta1) * x + math.sin(theta1) * y - L1) / L2)

             return math.degrees(theta1), math.degrees(theta2)

         Xlist = [x ,x+50]
         Ylist = [y,y ]

         Ink1list = []
         Ink2list = []
         t = 50  
         s = 1

         Xline = []  # Create a new list called Xline
         Yline = []  # Create a new list called Yline

         for j in range(s):
             dX = (abs(Xlist[j] - Xlist[j + 1])) / t  
             dY = (abs(Ylist[j] - Ylist[j + 1])) / t  

             for i in range(t):
                 if Xlist[j] < Xlist[j + 1]:
                     Xline.append(int(Xlist[j] + (i + 1) * dX))  
                 else:
                     Xline.append(int(Xlist[j] - (i + 1) * dX))

             for i in range(t):
                 if Ylist[j] < Ylist[j + 1]:
                     Yline.append(int(Ylist[j] + (i + 1) * dY))
                 else:
                     Yline.append(int(Ylist[j] - (i + 1) * dY))

             for i in range(t):
                 x = Xline[i + j * t]
                 y = Yline[i + j * t]

                 try:
                     T1g, T2g = inverse_kinematics(x, y, L1, L2)

                     if T1g < 0:
                         T1g = 0

                     if T2g < 0:
                         T2g = 0

                     Ink1 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
                     Ink2 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275



                     Ink1list.append(Ink1)
                     Ink2list.append(Ink2)

                 except ValueError:
                     
                     print("error")


             for i in range (t):
                p11 = int(Ink1list[i+j*t]) 
                p12 = int(Ink2list[i+j*t]) 


                d1 = Dsa(1)
                d1.Enable()
                d1.ModePos()

                d2 = Dsa(35)
                d2.Enable()
                d2.ModePos()

                d1.Mova(p11)
                d2.Mova(p12)

                time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def xminus(self):

         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)

         p21 = int(d1.ActPos())  
         p22 = int(d2.ActPos())  

         # SCARA robot parameters
         L1 = 186  
         L2 = 157

         #find the angles
         T11 = ((70000 - p21) / 270) - ((70000 / 270) - 224.0740)
         T22 = ((82000 - p22) / 275) - ((82000 / 275) - 130.909090)

         # Convert angles T1 and T2 to radians
         T1 = math.radians(T11)
         T2 = math.radians(360 - T22)

         # Calculate coordinates
         x = round(L1 * math.cos(T1) + L2 * math.cos(T1 + T2))
         y = round(L1 * math.sin(T1) + L2 * math.sin(T1 + T2))


         def inverse_kinematics(x, y, L1, L2):
            
             r = math.sqrt(x ** 2 + y ** 2)

             # Check if the position is out of reach
             if r > L1 + L2 or r < abs(141):
                 raise ValueError("Position out of reach for the robot arm")

             theta1 = math.acos((r ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * r)) + math.acos(x / r)

           
             theta2 = math.acos((math.cos(theta1) * x + math.sin(theta1) * y - L1) / L2)

             return math.degrees(theta1), math.degrees(theta2)

         Xlist = [x ,x-50]
         Ylist = [y,y ]

         Ink1list = []
         Ink2list = []
         t = 50  
         s = 1

         Xline = []  # Create a new list called Xline
         Yline = []  # Create a new list called Yline

         for j in range(s):
             dX = (abs(Xlist[j] - Xlist[j + 1])) / t  
             dY = (abs(Ylist[j] - Ylist[j + 1])) / t  

             for i in range(t):
                 if Xlist[j] < Xlist[j + 1]:
                     Xline.append(int(Xlist[j] + (i + 1) * dX))  
                 else:
                     Xline.append(int(Xlist[j] - (i + 1) * dX))

             for i in range(t):
                 if Ylist[j] < Ylist[j + 1]:
                     Yline.append(int(Ylist[j] + (i + 1) * dY))
                 else:
                     Yline.append(int(Ylist[j] - (i + 1) * dY))

             for i in range(t):
                 x = Xline[i + j * t]
                 y = Yline[i + j * t]

                 try:
                     T1g, T2g = inverse_kinematics(x, y, L1, L2)

                     if T1g < 0:
                         T1g = 0

                     if T2g < 0:
                         T2g = 0

                     Ink1 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
                     Ink2 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275



                     Ink1list.append(Ink1)
                     Ink2list.append(Ink2)

                 except ValueError:
                     
                     print("error")


             for i in range (t):
                p11 = int(Ink1list[i+j*t]) 
                p12 = int(Ink2list[i+j*t]) 


                d1 = Dsa(1)
                d1.Enable()
                d1.ModePos()

                d2 = Dsa(35)
                d2.Enable()
                d2.ModePos()

                d1.Mova(p11)
                d2.Mova(p12)

                time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def yplus(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)

         p21 = int(d1.ActPos())  
         p22 = int(d2.ActPos())  

         # SCARA robot parameters
         L1 = 186  
         L2 = 157

         #find the angles
         T11 = ((70000 - p21) / 270) - ((70000 / 270) - 224.0740)
         T22 = ((82000 - p22) / 275) - ((82000 / 275) - 130.909090)

         # Convert angles T1 and T2 to radians
         T1 = math.radians(T11)
         T2 = math.radians(360 - T22)

         # Calculate coordinates
         x = round(L1 * math.cos(T1) + L2 * math.cos(T1 + T2))
         y = round(L1 * math.sin(T1) + L2 * math.sin(T1 + T2))


         def inverse_kinematics(x, y, L1, L2):
            
             r = math.sqrt(x ** 2 + y ** 2)

             # Check if the position is out of reach
             if r > L1 + L2 or r < abs(141):
                 raise ValueError("Position out of reach for the robot arm")

             theta1 = math.acos((r ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * r)) + math.acos(x / r)

           
             theta2 = math.acos((math.cos(theta1) * x + math.sin(theta1) * y - L1) / L2)

             return math.degrees(theta1), math.degrees(theta2)

         Xlist = [x ,x]
         Ylist = [y,y+50 ]

         Ink1list = []
         Ink2list = []
         t = 50  
         s = 1

         Xline = []  # Create a new list called Xline
         Yline = []  # Create a new list called Yline

         for j in range(s):
             dX = (abs(Xlist[j] - Xlist[j + 1])) / t  
             dY = (abs(Ylist[j] - Ylist[j + 1])) / t  

             for i in range(t):
                 if Xlist[j] < Xlist[j + 1]:
                     Xline.append(int(Xlist[j] + (i + 1) * dX))  
                 else:
                     Xline.append(int(Xlist[j] - (i + 1) * dX))

             for i in range(t):
                 if Ylist[j] < Ylist[j + 1]:
                     Yline.append(int(Ylist[j] + (i + 1) * dY))
                 else:
                     Yline.append(int(Ylist[j] - (i + 1) * dY))

             for i in range(t):
                 x = Xline[i + j * t]
                 y = Yline[i + j * t]

                 try:
                     T1g, T2g = inverse_kinematics(x, y, L1, L2)

                     if T1g < 0:
                         T1g = 0

                     if T2g < 0:
                         T2g = 0

                     Ink1 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
                     Ink2 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275



                     Ink1list.append(Ink1)
                     Ink2list.append(Ink2)

                 except ValueError:
                     
                     print("error")


             for i in range (t):
                p11 = int(Ink1list[i+j*t]) 
                p12 = int(Ink2list[i+j*t]) 


                d1 = Dsa(1)
                d1.Enable()
                d1.ModePos()

                d2 = Dsa(35)
                d2.Enable()
                d2.ModePos()

                d1.Mova(p11)
                d2.Mova(p12)

                time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def yminus(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)

         p21 = int(d1.ActPos())  
         p22 = int(d2.ActPos())  

         # SCARA robot parameters
         L1 = 186  
         L2 = 157

         #find the angles
         T11 = ((70000 - p21) / 270) - ((70000 / 270) - 224.0740)
         T22 = ((82000 - p22) / 275) - ((82000 / 275) - 130.909090)

         # Convert angles T1 and T2 to radians
         T1 = math.radians(T11)
         T2 = math.radians(360 - T22)

         # Calculate coordinates
         x = round(L1 * math.cos(T1) + L2 * math.cos(T1 + T2))
         y = round(L1 * math.sin(T1) + L2 * math.sin(T1 + T2))


         def inverse_kinematics(x, y, L1, L2):
            
             r = math.sqrt(x ** 2 + y ** 2)

             # Check if the position is out of reach
             if r > L1 + L2 or r < abs(141):
                 raise ValueError("Position out of reach for the robot arm")

             theta1 = math.acos((r ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * r)) + math.acos(x / r)

           
             theta2 = math.acos((math.cos(theta1) * x + math.sin(theta1) * y - L1) / L2)

             return math.degrees(theta1), math.degrees(theta2)

         Xlist = [x ,x]
         Ylist = [y,y-50 ]

         Ink1list = []
         Ink2list = []
         t = 50  
         s = 1

         Xline = []  # Create a new list called Xline
         Yline = []  # Create a new list called Yline

         for j in range(s):
             dX = (abs(Xlist[j] - Xlist[j + 1])) / t  
             dY = (abs(Ylist[j] - Ylist[j + 1])) / t  

             for i in range(t):
                 if Xlist[j] < Xlist[j + 1]:
                     Xline.append(int(Xlist[j] + (i + 1) * dX))  
                 else:
                     Xline.append(int(Xlist[j] - (i + 1) * dX))

             for i in range(t):
                 if Ylist[j] < Ylist[j + 1]:
                     Yline.append(int(Ylist[j] + (i + 1) * dY))
                 else:
                     Yline.append(int(Ylist[j] - (i + 1) * dY))

             for i in range(t):
                 x = Xline[i + j * t]
                 y = Yline[i + j * t]

                 try:
                     T1g, T2g = inverse_kinematics(x, y, L1, L2)

                     if T1g < 0:
                         T1g = 0

                     if T2g < 0:
                         T2g = 0

                     Ink1 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
                     Ink2 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275



                     Ink1list.append(Ink1)
                     Ink2list.append(Ink2)

                 except ValueError:
                     
                     print("error")


             for i in range (t):
                p11 = int(Ink1list[i+j*t]) 
                p12 = int(Ink2list[i+j*t]) 


                d1 = Dsa(1)
                d1.Enable()
                d1.ModePos()

                d2 = Dsa(35)
                d2.Enable()
                d2.ModePos()

                d1.Mova(p11)
                d2.Mova(p12)

                time.sleep(0.02)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def reference(self):


         d1 = Dsa(1)                 
         d1.Enable()
         d1.ModePos()               
         d1.HomeCmd(1)

         d2 = Dsa(35)                
         d2.Enable()
         d2.ModePos()              
         d2.HomeCmd(1)

         d3 = Dsa(69)               
         d3.Enable()
         d3.ModePos()                
         d3.HomeCmd(1)

         d4 = Dsa(103)               
         d4.Enable()
         d4.ModePos()               
         d4.HomeCmd(1)


         time.sleep(5)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))
    def position(self):

           d1 = Dsa(1)
           d2 = Dsa(35)

           p11 =int(d1.ActPos())
           p12 =int(d2.ActPos())  


           # SCARA robot parameters
           a1 = 186  # Length of the first arm
           a2 = 157  # Length of the second arm

           # Convert Ink1 and Ink2 to angles T1 and T2
           T1g = ((70000 - p11) / 270) - ((70000 / 270) - 224.0740)
           T2g = ((82000 - p12) / 275) - ((82000 / 275) - 130.909090)

           # Convert angles T1 and T2 to radians
           T1 = math.radians(T1g)
           T2 = math.radians(360 - T2g)


           # Calculate coordinates
           x1 = round(a1 * math.cos(T1) + a2 * math.cos(T1 + T2))
           y1 = round(a1 * math.sin(T1) + a2 * math.sin(T1 + T2))
           self.lbl11.config(text="The position is: "+'(' + str(x1)+' ' +','+' '+ str(y1)+')')

    def inxy(self):

         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)

         p21 = int(d1.ActPos()) 
         p22 = int(d2.ActPos())  

         
         L1 = 186  
         L2 = 157

         # Convert Ink1 and Ink2 to angles T1 and T2
         T11 = ((70000 - p21) / 270) - ((70000 / 270) - 224.0740)
         T22 = ((82000 - p22) / 275) - ((82000 / 275) - 130.909090)

         # Convert angles T1 and T2 to radians
         T1 = math.radians(T11)
         T2 = math.radians(360 - T22)

         # Calculate coordinates
         x = round(L1 * math.cos(T1) + L2 * math.cos(T1 + T2))
         y = round(L1 * math.sin(T1) + L2 * math.sin(T1 + T2))


         def inverse_kinematics(x, y, L1, L2):
             # Calculate r
             r = math.sqrt(x ** 2 + y ** 2)

            
             if r > L1 + L2 or r < abs(141):
                 raise ValueError("Position out of reach for the robot arm")

             
             theta1 = math.acos((r ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * r)) + math.acos(x / r)

            
             theta2 = math.acos((math.cos(theta1) * x + math.sin(theta1) * y - L1) / L2)

             return math.degrees(theta1), math.degrees(theta2)


         x2=int(self.t1.get())
         y2=int(self.t2.get())
         Xlist = [x ,x2]
         Ylist = [y,y2 ]

         Ink1list = []
         Ink2list = []
         t = 2  
         s = 1

         Xline = []  
         Yline = []  

         for j in range(s):
             dX = (abs(Xlist[j] - Xlist[j + 1])) / t  
             dY = (abs(Ylist[j] - Ylist[j + 1])) / t  

             for i in range(t):
                 if Xlist[j] < Xlist[j + 1]:
                     Xline.append(int(Xlist[j] + (i + 1) * dX))  
                 else:
                     Xline.append(int(Xlist[j] - (i + 1) * dX))

             for i in range(t):
                 if Ylist[j] < Ylist[j + 1]:
                     Yline.append(int(Ylist[j] + (i + 1) * dY))
                 else:
                     Yline.append(int(Ylist[j] - (i + 1) * dY))

             for i in range(t):
                 x = Xline[i + j * t]
                 y = Yline[i + j * t]

                 try:
                     T1g, T2g = inverse_kinematics(x, y, L1, L2)

                     if T1g < 0:
                         T1g = 0

                     if T2g < 0:
                         T2g = 0

                     Ink1 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
                     Ink2 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275

                     if Ink1 > 70000:
                         Ink1 = 70000
                     if Ink1 < 0:
                         Ink1 = 0
                     if Ink2 > 82000:
                         Ink2 = 82000
                     if Ink2 < 0:
                         Ink2 = 0

                     Ink1list.append(Ink1)
                     Ink2list.append(Ink2)

                 except ValueError:
                     
                     print(5)


             for i in range (t):
                p11 = int(Ink1list[i+j*t])
                p12 = int(Ink2list[i+j*t]) 

                diff = 200           
                d1 = Dsa(1)             
                d1.Enable()
                d1.ModePos()            

                d2 = Dsa(35)            
                d2.Enable()
                d2.ModePos()           
 
                d1.Mova(p11)      

                d2.Mova(p12)     

                time.sleep(0)

         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))
    def zplus(self):

         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)


         p13 =int(d3.ActPos())
         p23 = p13 + 4000
         d3.Enable()
         d3.ModePos()

         d3.Mova(p23)
         time.sleep(1)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def zminus(self):

         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)

         p13 =int(d3.ActPos())
         p23 = p13 - 4000
         d3.Enable()
         d3.ModePos()

         d3.Mova(p23)
         time.sleep(1)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def gon(self):
         d1 = Dsa(1)
         d1.DoutP0(0)
         time.sleep(1)

    def goff(self):
         d1 = Dsa(1)
         d1.DoutP0(1)
         time.sleep(1)

    def gplus(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)
         p14 =int(d4.ActPos())
         p24 = p14 + 5333
         d4.Enable()
         d4.ModePos()
         d4.Mova(p24)
         time.sleep(1)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))

    def gminus(self):
         d1 = Dsa(1)
         d2 = Dsa(35)
         d3 = Dsa(69)
         d4 = Dsa(103)
         p14 =int(d4.ActPos())
         p24 = p14 - 5333
         d4.Enable()
         d4.ModePos()
         d4.Mova(p24)
         time.sleep(1)
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions.append(int(d1.ActPos()))
         y_positions.append(int(d2.ActPos()))
         Z_positions.append(int(d3.ActPos()))
         g_positions.append(int(d4.ActPos()))
    def stop(self):
         d1 = Dsa(1)
         d1.Disable()

         d2 = Dsa(35)
         d2.Disable()

         d3 = Dsa(69)
         d3.Disable()

         d4 = Dsa(103)
         d4.Disable()
         d4.ClrError()
    def teach(self):
         global x_positions
         global y_positions
         global Z_positions
         global g_positions


         p21 = x_positions
         p22 = y_positions
         p23 = Z_positions
         p24 = g_positions
         t = len(p21)
         for i in range (t):
             p11 = int(p21[i]) 
             p12 = int(p22[i])
             p13 = int(p23[i]) 
             p14 = int(p24[i]) 
             diff = 200             
             d1 = Dsa(1)             
             d1.Enable()
             d1.ModePos()            

             d2 = Dsa(35)            
             d2.Enable()
             d2.ModePos()

             d3 = Dsa(69)           
             d3.Enable()
             d3.ModePos()

             d4 = Dsa(103)           
             d4.Enable()
             d4.ModePos()          


             d1.VelAcc_dV(10000) 
             d1.VelAcc_dT(5000)

             d1.VelDec_dV(10000) 
             d1.VelDec_dT(5000)

             d1.Vel(2500)       
             d1.Mova(p11)        

            
             d2.VelAcc_dV(10000) 
             d2.VelAcc_dT(5000)

             d2.VelDec_dV(10000) 
             d2.VelDec_dT(5000)

             d2.Vel(2500)       
             d2.Mova(p12)
             time.sleep(1)
             d4.VelAcc_dV(10000) 
             d4.VelAcc_dT(500)

             d4.VelDec_dV(10000) 
             d4.VelDec_dT(500)

             d4.Vel(2500)
             d4.Mova(p14)     

             time.sleep(1)
             d3.VelAcc_dV(10000) 
             d3.VelAcc_dT(5000)

             d3.VelDec_dV(10000) 
             d3.VelDec_dT(5000)
             d3.Mova(p13)

             time.sleep(0.5)
    def save(self):
        global x_positions
        global y_positions
        global Z_positions
        global g_positions
        x_positions = []
        y_positions = []
        Z_positions = []
        g_positions = []

    def clear(self):
         global x_positions
         global y_positions
         global Z_positions
         global g_positions
         x_positions = []
         y_positions = []
         z_positions = []
         g_positions = []

    def close(self):
         window.destroy()

    def app(self):
         d1 = Dsa(1)
         d2 = Dsa(35)

         L1 = 186
         L2 = 157

         def inverse_kinematics(x, y, L1, L2):
             # Calculate r
             r = math.sqrt(x ** 2 + y ** 2)

             # Check if the position is out of reach
             if r > L1 + L2 or r < abs(141):
                 raise ValueError("Position out of reach for the robot arm")

             # Calculate theta1
             theta1 = math.acos((r ** 2 + L1 ** 2 - L2 ** 2) / (2 * L1 * r)) + math.acos(x / r)

             # Calculate theta2
             theta2 = math.acos((math.cos(theta1) * x + math.sin(theta1) * y - L1) / L2)

             return math.degrees(theta1), math.degrees(theta2)


         x = 0
         y = 300



         try:
            T1g, T2g = inverse_kinematics(x, y, L1, L2)

            if T1g < 0:
                T1g = 0

            if T2g < 0:
                T2g = 0

            Ink1 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
            Ink2 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275



         except ValueError:

            print(error)



         p11 = int(Ink1) 
         p12 = int(Ink2)
         p13 = 31000
         p23 = 9600
         diff = 200             
         d1 = Dsa(1)          
         d1.Enable()
         d1.ModePos()          

         d2 = Dsa(35)            
         d2.Enable()
         d2.ModePos()

         d3 = Dsa(69)
         d3.Enable()
         d3.ModePos()          

           

         if d1.ActPos() == p11 or p11 +diff or p11 -diff and d2.ActPos() == p12 or p12 +diff or p12 -diff and d3.ActPos() == p13 or p13 +diff or p13 -diff :


            d1.DoutP0(1)   
            d3.VelAcc_dV(500) 
            d3.VelAcc_dT(5000)

            d3.VelDec_dV(500) 
            d3.VelDec_dT(5000)

            d3.Vel(2500)      
            d3.Mova(p13)
            time.sleep(3)
                 
            d1.VelAcc_dV(10000) 
            d1.VelAcc_dT(5000)

            d1.VelDec_dV(10000) 
            d1.VelDec_dT(5000)

            d1.Vel(2500)       
            d1.Mova(p11)        

           
            d2.VelAcc_dV(10000) 
            d2.VelAcc_dT(5000)

            d2.VelDec_dV(10000) 
            d2.VelDec_dT(5000)

            d2.Vel(2500)       
            d2.Mova(p12)

            time.sleep(2)

            d3.Mova(p23)
            time.sleep(5)
            d1.DoutP0(0)
            time.sleep(1)
            d3.VelAcc_dV(10000)
            d3.VelAcc_dT(5000)

            d3.VelDec_dV(10000)
            d3.VelDec_dT(5000)

            d3.Mova(p13)
            time.sleep(2)

         x1 = -200
         y1 = 250



         try:
            T1g, T2g = inverse_kinematics(x1, y1, L1, L2)

            if T1g < 0:
                T1g = 0

            if T2g < 0:
                T2g = 0

            Ink21 = 70000 - ((T1g + ((70000 / 270) - 224.0740))) * 270
            Ink22 = 82000 - ((T2g + ((82000 / 275) - 130.909090))) * 275

            if Ink1 > 70000:
                Ink1 = 70000
            if Ink1 < 0:
                Ink1 = 0
            if Ink2 > 82000:
                Ink2 = 82000
            if Ink2 < 0:
                Ink2 = 0


         except ValueError:
            # Handle position out of reach error
            print(5)



         p21 = int(Ink21) 
         p22 = int(Ink22)
         p33 = 9200

         diff = 200             
         d1 = Dsa(1)             
         d1.Enable()
         d1.ModePos()           

         d2 = Dsa(35)            
         d2.Enable()
         d2.ModePos()

         d3 = Dsa(69)
         d3.Enable()
         d3.ModePos()           

          

         if d1.ActPos() == p21 or p21 +diff or p21 -diff and d2.ActPos() == p22 or p22 +diff or p22 -diff and d3.ActPos() == p13 or p13 +diff or p13 -diff :

                  
            d1.VelAcc_dV(10000)
            d1.VelAcc_dT(5000)

            d1.VelDec_dV(10000) 
            d1.VelDec_dT(5000)

            d1.Vel(2500)       
            d1.Mova(p21)       

           
            d2.VelAcc_dV(10000) 
            d2.VelAcc_dT(5000)

            d2.VelDec_dV(10000) 
            d2.VelDec_dT(5000)

            d2.Vel(2500)      
            d2.Mova(p22)

            time.sleep(2)

            
            d3.VelAcc_dV(10000) 
            d3.VelAcc_dT(5000)

            d3.VelDec_dV(10000) 
            d3.VelDec_dT(5000)

            d3.Vel(2500)       
            d3.Mova(p33)

            time.sleep(3)
            d1.DoutP0(1)
                     


            time.sleep(1)

            d3.Mova(p13)


window=Tk()
mywin=MyRobo(window)
window.title('Robot Interface')
window.geometry("700x500+10+10")
window.configure(bg="#3CBB75")
window.mainloop()
