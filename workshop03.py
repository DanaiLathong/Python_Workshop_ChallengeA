print ("""
***********************************************
***************** AREA & CUBE *****************
***********************************************
        [1] พื้นที่สี่เหลี่ยม
        [2] พื้นที่วงกลม
        [3] ปริมาตรทรงสี่เหลี่ยม
        [4] ปริมาตรทรงกลม
        [0] ออกจากการทำงาน
***********************************************
""")
cal = int(input("เลือกการทำงาน : "))
print ("***********************************************")
print ("                                               ")

if cal == 1 :
    print ("***********************************************")
    print ("            คำนวณพื้นที่สี่เหลี่ยม ")
    print ("***********************************************")
    W = float(input("กรอกความกว้าง : "))
    L = float(input("กรอกความยาว : "))
    rectangular_area = W * L
    print (f"คำนวณพื้นที่สี่เหลี่ยม : {rectangular_area}")
elif cal == 2 :
    print ("***********************************************")
    print ("            คำนวณพื้นที่วงกลม ")
    print ("***********************************************")
    radius = float(input("กรอกรัศมี(ไม่ต้องยกกำลัง) : "))
    radius2 = radius * radius
    circle_area = (22/7) * radius2
    print (f"คำนวณพื้นที่วงกลม : {circle_area}")
elif cal == 3 :
    print ("***********************************************")
    print ("            คำนวณปริมาตรทรงสี่เหลี่ยม ")
    print ("***********************************************")
    W = float(input("กรอกความกว้าง : "))
    L = float(input("กรอกความยาว : "))
    H = float(input("กรอกความสูง : "))
    Square_volume = W * L * H
    print (f"คำนวณปริมาตรทรงสี่เหลี่ยม : {Square_volume}")
elif cal == 4 :
    print ("***********************************************")
    print ("            คำนวณปริมาตรทรงกลม ")
    print ("***********************************************")
    radius = float(input("กรอกรัศมี(ไม่ต้องยกกำลัง) : "))
    radius2 = radius * radius
    Spherical_volume = 4/3 * 22/7 * radius2
    print (f"คำนวณปริมาตรทรงกลม : {Spherical_volume}")
else :
    print ("    กรุณาเลือกการทำงาน 1 , 2 , 3 , 4 , 0 เท่านั้น ")
    print ("                                               ")
    print ("***********************************************")