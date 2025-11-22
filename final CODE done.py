# PRECISION FARMING FINAL CODE

import mysql.connector as my
import sys

cn=my.connect(host='localhost',
              user='root',    
              password='root',
              database='SMART_FARMING')
cur=cn.cursor()


def homepage():
      print('- '*55,'\n\t\t\t\t\t\tW E L C O M E\n','- '*55)
      print('- '*55,'\n\t\t\t\t\tP R E C I S I O N   F A R M I N G\n','- '*55)
      print('- '*55,'\n\t\t\t\tW H E R E  I N N O V A T I O N  M E E T S  A G R I C U L T U R E\n','- '*55)
      print('\tHello',u_name,', enter your details here\n')
      
      # to input the personal details from the user
      name=input('Name\t\t: ')
      age=int(input('Age\t\t: '))
      crop_farmer=input('The crop you are curently growing : ')
      state=input('Your field location (state) : ')
      city=input('City or sub-locality : ')
      area=int(input('Field size (in Acres) : '))
      income=int(input('Average income per annum: '))
      cur.execute('''insert into user_data
                        values('{}',{},'{}','{}','{}',{},{})'''.format(name,age,crop_farmer,state,city,area,income))
      cn.commit()
      print('Your data is successfully stored!')
      print('- '*55)
      working_menu()
      

def working_menu(): #to work or search on the programme
      while True:
            print('\nWhat would you like to do',u_name,'''?
1. Update my status
2. Search regarding the crop 
3. Get an update on recent programmes
4. Get data of my yield
5. Check my Status
6. EXIT\n''')
            choice=int(input('Enter your choice : '))
            if choice==1:
                  update_status()
            elif choice==2:
                  search_crop_details()
            elif choice==3:
                  program_schemes()
            elif choice==4:
                  yeild_data()
            elif choice==5:
                  check_status()
            elif choice==6:
                  print('THANK YOU',u_name,'for using our PRECISION FARMING program')
                  print('- '*55,'\n\t\t\t\t\t\tT H A N K  Y O U\n','- '*55)
                  sys.exit()
                  break
            else:
                  print('INVALID INPUT\nPLease choose from following')

def update_status():
      global u_name
      user_name=input('Enter you name here (Registered name) : ')
      print('Hey',u_name,'What would you like to update?')
      while True:
            print('''
1. Age
2. Location
3. City
4. Area
5. Income
6. Crop
7. Exit\n''')
            ch=int(input('Enter Your choice : '))
            if ch==1:
                  new_age=int(input('Enter the age to update : '))
                  cur.execute("update user_data set age={} where name='{}'".format(new_age,user_name))
                  cn.commit()
                  print('Record updated')
                  print('- '*55)
                  update_more=input('Do you want to update the data further? (Y/N)')
                  if update_more in 'Yy':
                        update_status()
                  elif update_more in 'Nn' :
                        print('THANK YOU for being updated !')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT')
                        
            elif ch==2:
                  new_location=input('Enter your new Location(STATE) to update : ')
                  cur.execute("update user_data set location='{}' where name='{}'".format(new_location,user_name))
                  cn.commit()
                  print('Record updated')
                  print('- '*55)
                  update_more=input('Do you want to update the data further? (Y/N)')
                  if update_more in 'Yy':
                        update_status()
                  elif update_more in 'Nn' :
                        print('THANK YOU for being updated !')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT')
            elif ch==3:
                  new_city=input('Enter your new city to update : ')
                  cur.execute("update user_data set city='{}' where name='{}'".format(new_city,user_name))
                  print('Record updated')
                  print('- '*55)
                  cn.commit()
                  update_more=input('Do you want to update the data further? (Y/N)')
                  if update_more in 'Yy':
                        update_status()
                  elif update_more in 'Nn' :
                        print('THANK YOU for being updated !')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT')
            elif ch==4:
                  new_area=int(input('Enter your new Area to update in the record : '))
                  cur.execute("update user_data set area={} where name='{}'".format(new_area,user_name))
                  print('Record updated')
                  print('- '*55)
                  cn.commit()
                  update_more=input('Do you want to update the data further? (Y/N)')
                  if update_more in 'Yy':
                        update_status()
                  elif update_more in 'Nn' :
                        print('THANK YOU for being updated !')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT')
            elif ch==5:
                  new_income=int(input('Enter your new Income to update : '))
                  cur.execute("update user_data set income={} where name='{}'".format(new_income,user_name))
                  print('Record updated')
                  print('- '*55)
                  cn.commit()
                  update_more=input('Do you want to update the data further? (Y/N)')
                  if update_more in 'Yy':
                        update_status()
                  elif update_more in 'Nn' :
                        print('THANK YOU for being updated !')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT')
            elif ch==6:
                  new_crop=input('Enter your new crop you are currently growing : ')
                  cur.execute("update user_data set crop='{}' where name='{}'".format(new_crop,user_name))
                  print('Record updated')
                  print('- '*55)
                  cn.commit()
                  update_more=input('Do you want to update the data further? (Y/N)')
                  if update_more in 'Yy':
                        update_status()
                  elif update_more in 'Nn' :
                        print('THANK YOU for being updated !')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('INVALID INPUT')
            elif ch==7:
                  print('THANK YOU for being updated !')
                  print('- '*55)
                  print('LOADING the homepage...')
                  break
            else:
                  print('INVALID INPUT\nPlease choose from following')
                  


def search_crop_details():
      global u_name
      l1=[]
      crop_verify=input('\nVerify the crop you are currently growing : ')
      cur.execute("select crop from crop_details")
      crop=cur.fetchall()
      for i in crop:
           c=i[0]
           l1.append(c)
           
      if crop_verify.upper() in l1:
            print('\nHey since you cultivate',crop_verify,'here are some recommendations ')
            print('for you to search regarding your crop')
            while True:
                  print('''
1. Best time to grow my crop
2. Water requirement for my crop 
3. Soil Conditions for my crop
4. Usage of chemicals/fertilizers I need to do for my crops
5. Weather conditions required for the crop
6. Return Back''')
                  ch=int(input('Enter your choice : '))
                  if ch==1:
                        cur.execute("select sowing_month from crop_details where crop='{}'".format(crop_verify))
                        dt=cur.fetchone()
                        for i in dt:
                              print('You should grow',crop_verify,'in the month of',i)
                              print('- '*55)
                  elif ch==2:
                        cur.execute("select rainfall from crop_details where crop='{}'".format(crop_verify))
                        dt=cur.fetchone()
                        for i in dt:
                              print(i,'rainfal is appropriate for',crop_verify)
                              print('- '*55)
                  elif ch==3:
                        cur.execute("select soil from crop_details where crop='{}'".format(crop_verify))
                        dt=cur.fetchone()
                        for i in dt:
                              print(i,'soil would be suitable for your crop',crop_verify)
                              print('- '*55)
                  elif ch==4:
                        cur.execute("select fertilizer from crop_details where crop='{}'".format(crop_verify))
                        dt=cur.fetchone()
                        for i in dt:
                              print('You should use',i,'for good yeild of crop')
                              print('- '*55)
                  elif ch==5:
                        cur.execute("select weather from crop_details where crop='{}'".format(crop_verify))
                        dt=cur.fetchone()
                        for i in dt:
                              print(i,'climate would be beneficial for',crop_verify)
                              print('- '*55)
                  elif ch==6:
                        print('Thank you',u_name,'for searching through!')
                        print('- '*55)
                        print('LOADING the homepage...')
                        break
                  else:
                        print('\nINVALID CHOICE\nPlease choose from below')
      else:
            print('The crop you are searching for is not present in our records')
            print('This may be because you are searching for a new variety of crop\n')
            print('''SORRY for the inconveinence but, we recommend you to login again as
admin and store the data of the crop for your further reference''')
            space=input('Press SPACEBAR key once and then enter key !')
            if space==' ':
                  user_admin()
            else:
                  print('\t\t\tT H A N K  Y O U\n','- '*55)


def program_schemes():
      global u_name
      while True:
            print('''
Here are some government schemes and programmes for you to enroll into:
1. PM Kisan Samman Nidhi
2. PM Kisan MaanDhan Yojna
3. PM Fasal Bima Yojna
4. Modified interest subvention scheme (MISS)
5. Agriculture Infrastructure Fund(AIF)
6. Market intervention scheme and price support scheme
7. Namo Drone Didi
8. Rashtriya Krishi Vikas Yojna
9. Soil Health Card
10. EXIT\n''')
            ch=int(input('Enter your choice : '))
            if ch==1:
                  print('''\nUnder the scheme PM-KISAN ,financial benefit of Rs. 6000/- per year is
transferred in three equal four-monthly installments into the bank accounts of farmers’ families
across the country, through Direct Benefit Transfer (DBT) mode.''')
                  print('- '*55)
            elif ch==2:
                  print('''\nPradhan Mantri Kisan Maandhan Yojna (PMKMY) is a central sector scheme launched
on 12th September 2019 to provide security to the most vulnerable farmer families. PMKMY is taking care
of the farmers during their old age and provides Rs. 3,000 monthly pension to the enrolled farmers once
they attain 60 years of age, subject to exclusion criteria.''')
                  print('- '*55)
            elif ch==3:
                  print('''\nPMFBY was launched in order to provide a simple and affordable crop insurance
product to ensure comprehensive risk cover for crops to farmers against all non-preventable natural risks
from pre-sowing to post-harvest and to provide adequate claim amount.''')
                  print('- '*55)
            elif ch==4:
                  print('''\nProvides concessional short term agri-loans to the farmers practicing crop
husbandry and other allied activities like animal husbandry, dairying and fisheries. MISS is available
to farmers availing short term crop loans up to Rs.3.00 lakh at an interest rate of 7% per annum for
one year. Additional 3% subvention is also given to the farmers for prompt and timely repayment of loans
thus reducing the effective rate of interest to 4% per annum.''')
                  print('- '*55)
            elif ch==5:
                  print('''\nUnder the scheme, Rs. 1 Lakh Crore will be provided by banks and financial
institutions as loans with interest subvention of 3% per annum and credit guarantee coverage under
CGTMSE for loans up to Rs. 2 Crores for post- harvest management infrastructure and community farming. ''')
                  print('- '*55)
            elif ch==6:
                  print('''\nPrice Support Scheme (PSS) for procurement of pulses, oilseeds and copra and
Market Intervention Scheme (MIS) for procurement of agricultural and horticultural commodities.
The objective of intervention is to protect the growers of these commodities from making distress sale
in the event of a bumper crop during the peak arrival period when the prices tend to fall below economic
levels and cost of production.''')
                  print('- '*55)
            elif ch==7:
                  print('''\nThe scheme aims to provide drones to 15000 selected Women Self Help Group (SHGs)
for providing rental services to farmers for agriculture purpose (application of fertilizers and pesticides).''')
                  print('- '*55)
            elif ch==8:
                  print('''\nThe scheme focuses on creation of pre & post-harvest infrastructure in
agriculture and allied sectors that help in supply of quality inputs, market facilities, etc to farmers. ''')
                  print('- '*55)
            elif ch==9:
                  print('''\nSoil health card provides information to farmers on nutrient status of their
soil along with recommendation on appropriate dosage of nutrients to be applied for improving soil health
and its fertility. ''')
                  print('- '*55)
            elif ch==10:
                  print('THANK YOU for searching regading the government schemes\nHope this would benefit you')
                  print('- '*55)
                  print('LOADING the homepage...')
                  break
            else:
                  print('INVALID CHOICE \nPlease choose from following only : ')


def yeild_data():
      global u_name
      crop_verify=input('\nVerify the crop you are currently growing : ')
      cur.execute("select area from user_data where crop='{}'".format(crop_verify))
      ac=cur.fetchone()
      acre=list(ac)
      print()
      for a in acre:
            print('Your area of land\t: ',a)

      cur.execute("select yeild_per_acre_in_kg from crop_yeild where crop='{}'".format(crop_verify))
      yel=cur.fetchone()
      i=yel[0]
      print('Yeild per acre\t\t: ',yel[0])
            
      total_yeild=a*i
      print('Your total yeild\t: ',total_yeild)
      print('Hey',u_name,',using this data you can easily estimate your amount of profit')
      print('- '*55)
      print('LOADING the homepage...')


def check_status():
      global u_name
      l=[]
      print('Hey',u_name,'Please provide us your regeistered name to check your status\n  ')
      full_name=input('Enter your full name : ')
      cur.execute("select name from user_data where name='{}'".format(full_name))
      dt=cur.fetchall()
      for i in dt:
            nm=i[0]
            l.append(nm)      
      if full_name in l:
            print('Name VERIFIED\n')
            print('\nHey',u_name,'here is your status :')
            cur.execute("Select * from user_data where name='{}'".format(full_name))
            dt=cur.fetchone()
            print('NAME \t: ',dt[0])
            print('AGE \t: ',dt[1])
            print('CROP \t: ',dt[2])
            print('STATE \t: ',dt[3])
            print('CITY \t: ',dt[4])
            print('AREA \t: ',dt[5])
            print('INCOME \t: ',dt[6])
            print('- '*55)
            print('LOADING the homepage...')
      else:                  
            print('Name invalid')
            return
      
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

      cur.execute("insert into crop_yeild values('{}',{})".format(crop,yeild))
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


admin_name=None
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
            
                  
#function for login
def user_login():
      global u_name
      l1=[]
      l2=[]
      u_name=input('Enter username : ')
      pass_word=input('Enter password : ')
      cur.execute("select password from users where password='{}'".format(pass_word))
      pw=cur.fetchall()
      for i in pw:
            c=i[0]
            l1.append(c)
      
      cur.execute("select username from users where username='{}'".format(u_name))
      un=cur.fetchall()
      for i in un:
            u=i[0]
            l2.append(u)
            
                  
      if pass_word in l1 :
            if u_name in l2:
                  print('PASSWORD VERIFIED\n')
                  print('- '*55)
                  working_menu()
            else:
                  print('Password is correct but INVALID Username\nPlease login again\n')
                  return
            
      else:                  
            print('Password invalid\nPlease login again\n')
            return

                   
def user_admin():
      while True:
            print('. '*55,'''
Select your account to LOGIN :
1. USER Account
2. ADMIN Account
3. EXIT
''')
            ch=int(input('Enter your choice : '))
            if ch==1:
                  user_login()
            
            elif ch==2:
                  insert_admin_name_login()
            elif ch==3:
                  print()
                  break
            else:
                  print('INVALID OPTION\nplease choose form following')

u_name=None
def signup_user():
      global u_name
      users=[]
      details={}
      u_name=input("Enter the username : ")
      p_word=input("Enter the password(atleast of 8 characters) : ")
      u=0
      l=0
      d=0
      sp=0
      if len(p_word)>=8:
            for i in p_word:
                  if i.isupper():
                        u+=1
                  elif i.islower():
                        l+=1
                  elif i.isdigit():
                        d+=1
                  elif i in '`-=[]\;,./~!@#$%^&*()_+|}{:>?<"':
                        sp+=1

      if u>=1 and l>=1 and d>=1 and sp>=1:
            print('The password is valid')
            print("Your data is being added in our database")
            cur.execute('''insert into users
                        values('{}','{}')'''.format(u_name,p_word))
            cn.commit()

            print('You have successfully signed up !!')
            homepage()
            
      else:
            print("Password invalid")
            print('Please try again..')
                  


def entry_menu():#for sign in or login only
      print('- '*55,'\n\t\t\t\t\t\tW E L C O M E\n','- '*55)
      while True:
            print('''
CHOOSE FROM FOLLOWING
1. Sign up
2. Login
3. EXIT
''')
            choice=int(input('Enter your choice : '))
            if choice==1:
                  signup_user()
            elif choice==2:
                  user_admin()
            elif choice==3:
                  print('\t\t\t\tT H A N K  Y O U\n\t\t\t\tP R E C I S I O N  F A R M I N G')
                  print('- '*55)
                  break            
entry_menu()





      
