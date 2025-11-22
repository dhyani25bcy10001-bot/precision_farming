import mysql.connector as my
import sys
cn=my.connect(host='localhost',
              user='root',    
              password='root',
              database='SMART_FARMING')
cur=cn.cursor()

admin_name=None

def admin_insert_crop():
      global admin_name
      crop=input('Enter the crop you want to provide us : ')
      soil=input('Enter the soil required for the crop : ')
      weather=input('Enter the weather conditions required : ')
      sow_month=input('Enter the sowing month : ')
      harvest_month=input('Enter the harvesting month : ')
      rain=input('Enter the rainfal suitable for the crop : ')
      fertilizer=input('Enter the fertilizers required : ')
      yeild=int(input('Enter the yield of crop per acre : '))
            
      cur.execute('''insert into crop_details
      values('{}','{}','{}','{}','{}','{}','{}')'''.format(crop,soil,weather,sow_month,harvest_month,rain,fertilizer))
      cn.commit()

      cur.execute("insert into crop_yield values('{}',{})".format(crop,yeild))
      cn.commit()
      print('Your data of',crop,'is successfully stored!')
      print('Thank you',admin_name,'''\n Now you can search through the PRECISION FARMING program''')
      print('- '*55)
      print('LOADING the homepage...')
      admin_login()

def admin_delete_data():
      global admin_name
      d_data=input("Enter the farmer's name you want to delete from the data (full name) :")
      u_data=input("Enter the farmer's username you want to delete from the data :")
      cur.execute("delete from user_data where name='{}'".format(d_data))
      cur.execute("delete from users where username='{}'".format(u_data))
      
      print('\nThe data of',d_data,'is removed from the records\n')
      print('- '*55)
      print('LOADING the homepage...')
      admin_login()

      
def admin_view_records():
      global admin_name
      while True:
            print('Hey',admin_name,',What do you want to see the record of?')
            print('''
1. Users list
2. User details
3. Crop Details
4. EXIT
''')
            ch=int(input('Enter the choice : '))
            if ch==1:
                  cur.execute("Select * from users")
                  dt=list(cur.fetchall())
                  print(' USERNAME\t PASSWORD')
                  print('-'*30)
                  for i in dt:
                        x=list(i)
                        if len(x[0])<=5:
                            print('',x[0],'\t\t',x[1])
                        else:
                            print('',x[0],'\t',x[1])
                  print('- '*55)
                  yn=input('Do you want to search records further ? (y/n)')
                  if yn in 'Yy':
                        admin_view_records()
                  elif yn in 'Nn':
                        print('DONE ')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT\n')
                  break
            elif ch==2:
                  cur.execute("Select * from user_data")
                  dt=list(cur.fetchall())
                  print('NAME - AGE - CROP - STATE - CITY - AREA - INCOME')
                  print('- '*43)
                  for i in dt:
                       x=list(i)
                       print(x[0],' - ',x[1],' - ',x[2],' - ',x[3],' - ',x[4],' - ',x[5],' - ',x[6])
                  print('- '*55)
                  yn=input('Do you want to search records further ? (y/n)')
                  if yn in 'Yy':
                        admin_view_records()
                  elif yn in 'Nn':
                        print('DONE')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT\n')
                  break
            elif ch==3:
                  cur.execute("Select * from crop_details")
                  dt=list(cur.fetchall())
                  print('CROP - SOIL - WEATHER - SOWING_MONTH - HARVESTING_MONTH - RAINFALL - FERTILIZER')
                  print('- '*43)
                  for i in dt:
                       x=list(i)
                       print(x[0],' - ',x[1],' - ',x[2],' - ',x[3],' - ',x[4],' - ',x[5],' - ',x[6])
                  print('- '*55)
                  yn=input('Do you want to search records further ? (y/n)')
                  if yn in 'Yy':
                        admin_view_records()
                  elif yn in 'Nn':
                        print('DONE')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT\n')
                  break
            elif ch==4:
                  print('Done')
                  print('- '*55)
                  print('LOADING the homepage...')
                  break
            else:
                  print('INVALID INPUT')
      admin_login()          



def insert_admin_name_login():
      global admin_name
      l1=[]
      l2=[]
      admin_name=input('Enter the admin name : ')
      pass_word=input('Enter password : ')
      cur.execute("select password from admin where password='{}'".format(pass_word))
      pw=cur.fetchall()
      for i in pw:
            c=i[0]
            l1.append(c)
      cur.execute("select admin from admin where admin='{}'".format(admin_name))
      an=cur.fetchall()
      for i in an:
            a=i[0]
            l2.append(a)
     
      if pass_word in l1:
            if admin_name in l2:
                  print('PASSWORD valid')
                  print('- '*55)
                  admin_login()
            else:
                  print('Password is correct but INVALID Admin name\nPlease login again\n')
      else:
            print('PASSWORD invalid\nPlease login again\n')
            return
      
def admin_login():
      global admin_name          
      while True:
                  print('Hey',admin_name,', What would you like to do?')
                  print('''
1. Insert crop details
2. Delete the user data
3. View records/data
4. Exit
''')
                  ch=int(input('Enter your choice : '))
                  if ch==1:
                        admin_insert_crop()
                        
                  elif ch==2:
                        admin_delete_data()
                        
                  elif ch==3:
                        admin_view_records()
                        
                  elif ch==4:
                        print('- '*55,'\n\t\t\t\t\tT H A N K  Y O U\n \t\t\t\tfor using PRECISION FARMING program')
                        print('- '*55)
                        sys.exit()
                        break
                  else:
                        print('INVALID INPUT')
                  break