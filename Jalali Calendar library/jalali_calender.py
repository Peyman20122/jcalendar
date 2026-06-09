from hijridate import Hijri, Gregorian
import datetime
import jdatetime
import numpy as np


class jcalender:
    
    def Jalali_Calender(your_year=None, your_month=None):
        shamsi_date = jdatetime.date.today()

        
        if your_year ==None and your_month ==None:
            j_days = jdatetime.date.today().replace(day=1).weekday()
            mont= jdatetime.date.today().month
            year_shamsi = shamsi_date.year
        elif your_year != None and your_month != None:
            mont=your_month
            year_shamsi = your_year
            j_days = jdatetime.date(your_year,mont,1).replace(day=1).weekday() 
    
        days_in_month = jdatetime.j_days_in_month
        lis_months = []
        for i in days_in_month:
            w = []
            for j in range(1,i+1):
                w.append(j)
                lis_months.append(w)
                
        lis_months_choice = lis_months[mont-1]
        days_zero = np.zeros(7).tolist()
        lis_months_co = []
        new_days_zero = []
        
        for i in range(len(days_zero[:j_days])):
            new_days_zero.append(0)
            
        lis_months_co = new_days_zero + lis_months_choice
        new_days_zero_end = []
        lis_week = []
        w=[]
        
        for i in lis_months_co:
            w.append(i)
            if len(w) == 7:
                lis_week.append(w)
                w=[]
        
        k=[]
        for j in lis_months_co:
            if j >= 29:         
                k.append(j)   
                
        days_num_end = 7 - len(w)
        new_days_zero_end = []
        
        for i in range(days_num_end):
            new_days_zero_end.append(0)
            
        list_last_weeks = w + new_days_zero_end
        lis_week.append(list_last_weeks)
        month_names = jdatetime.date.j_months_en
        month_name = month_names[mont-1]
        title = f"{month_name} {year_shamsi}".center(20, ' ')

        print(title)
        week_header = "Sa Su Mo Tu We Th Fr"
        print(week_header)
        for week in lis_week:
            weeks = ' '.join(f'{day:2}' if day!=0 else '  ' for day in week)
            print(weeks)
            
    def Moon_in_Scorpio_Choose_day(days,months,years):
        shamsi_date = jdatetime.date.fromgregorian(day=days,month=months,year=years)
        gregorian_date = Gregorian(years, months, days)
        hijri_date = gregorian_date.to_hijri()
        day_hijri = hijri_date.day
        day_shamsi = shamsi_date.day
        month_shamsi = shamsi_date.month
        day_name_shamsi = shamsi_date.jweekday()
        month_name_shamsi = shamsi_date.jmonth()
        years_sh = shamsi_date.year
        d_sh = day_shamsi +1
        sum_days = day_hijri * 12.2 + d_sh
        division_sum_days = sum_days / 30
        month_shamsi = shamsi_date.month
        col_days = round(division_sum_days + month_shamsi,2)
        if col_days > 12:
            col_days-=12
        if col_days >= 7.60 and col_days <=8.98 :
            return 'Today the moon is in Scorpio.', round(col_days,2) , day_shamsi , month_shamsi , day_name_shamsi , month_name_shamsi,years_sh
        else :
            return 'The moon is not in Scorpio today.', round(col_days,2) , day_shamsi , month_shamsi , day_name_shamsi , month_name_shamsi,years_sh
             
    def Moon_in_Scorpio():
        shamsi_date = jdatetime.date.today()
        day_hijri = Hijri.today().day
        day_shamsi = shamsi_date.day
        month_shamsi = shamsi_date.month
        day_name_shamsi = shamsi_date.jweekday()
        month_name_shamsi = shamsi_date.jmonth()
        years_sh = shamsi_date.year
        d_sh = day_shamsi +1
        sum_days = day_hijri * 12.2 + d_sh
        division_sum_days = sum_days / 30
        month_shamsi = shamsi_date.month
        col_days = round(division_sum_days + month_shamsi,2)
        if col_days > 12:
            col_days-=12
        if col_days >= 7.60 and col_days <=8.98 :
        
            return 'Today the moon is in Scorpio.', round(col_days,2), day_shamsi , month_shamsi , day_name_shamsi , month_name_shamsi,years_sh
        else :
            return 'The moon is not in Scorpio today.', round(col_days,2) , day_shamsi , month_shamsi , day_name_shamsi , month_name_shamsi,years_sh  

    def Mooon_is(months=None,years=None,mons=None):
        tim = []
        for i in range(1,mons):
            st,co,sh,mo,day_name,month_name,years_sh = jcalender.Moon_in_Scorpio_Choose_day(i,months,years)
            if st == 'Today the moon is in Scorpio.':
                lis =[]
                lis = [years_sh,mo,sh]
                tim.append(lis)
        return tim
        
    def Moon_in_Scorpio_Calender(your_year=None, your_month=None,Gregorian_year_1=None,Gregorian_year_2=None):
        shamsi_date = jdatetime.date.today()

        
        if your_year ==None and your_month ==None:
            j_days = jdatetime.date.today().replace(day=1).weekday()
            mont= jdatetime.date.today().month
            year_shamsi = shamsi_date.year
        elif your_year != None and your_month != None:
            mont=your_month
            year_shamsi = your_year
            j_days = jdatetime.date(year_shamsi,mont,1).replace(day=1).weekday() 
    
        days_in_month = jdatetime.j_days_in_month
        
        lis_months = []
        for i in days_in_month:
            w = []
            for j in range(1,i+1):
                w.append(j)
                lis_months.append(w)
                
        lis_months_choice = lis_months[mont-1]
        days_zero = np.zeros(7).tolist()
        lis_months_co = []
        new_days_zero = []
        
        for i in range(len(days_zero[:j_days])):
            new_days_zero.append(0)
            
        lis_months_co = new_days_zero + lis_months_choice
        new_days_zero_end = []
        lis_week = []
        w=[]
        
        for i in lis_months_co:
            w.append(i)
            if len(w) == 7:
                lis_week.append(w)
                w=[]
        
        k=[]
        for j in lis_months_co:
            if j >= 29:         
                k.append(j)   
                
        days_num_end = 7 - len(w)
        new_days_zero_end = []
        
        for i in range(days_num_end):
            new_days_zero_end.append(0)
            
        list_last_weeks = w + new_days_zero_end
        lis_week.append(list_last_weeks)
        month_names = jdatetime.date.j_months_en
        month_name = month_names[mont-1]
        

        g_days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        Gregorian_years = [Gregorian_year_1,Gregorian_year_2]
        
        ad_years = []
        for i in range(1,13):
            t = persian_scripio.Mooon_is(i,Gregorian_years[0],g_days_in_month[i-1])
            ad_years.append(t)
            if i == 12:
                for j in range(1,5):
                    t = persian_scripio.Mooon_is(j,Gregorian_years[1],g_days_in_month[j-1])
                    ad_years.append(t)
                    
        desired_year = ad_years[3:14]
        monthsss = [[] for _ in range(13)]

        for group in desired_year:
            for year,month,day in group :
                monthsss[month].append(day)
                
        for m in range(1,13):
            monthsss[m].sort()

        resualt = [monthsss[m] for m in range(1,13) if monthsss[m]]
        Converted_days = []
        for i in resualt[mont-1]:
            Converted_days.append(str(i))
            
        red = '\033[91m'
        reset = '\033[0m'
        
        Converted_weeks=[]
        for week in lis_week:
            weeks = '  '.join(f'{day:2}' for day in week)
            Converted_weeks.append(weeks)
            
        num = set(Converted_days)
        for i in range(len(Converted_weeks)):
            parts = Converted_weeks[i].split()
            colored_parts = []
            for part in parts:
                if part in num:
                    colored_parts.append(f'{red}{part}{reset}')
                else:
                    colored_parts.append(part)     
            Converted_weeks[i] = '  '.join(f'{day:2}' if day!='0' and day!=reset else '  ' for day in colored_parts)  
            
        title = f"{month_name} {year_shamsi}".center(20, ' ')
        print(title)
        week_header = "Sa  Su  Mo  Tu  We  Th  Fr"
        print(week_header)
        for ke in Converted_weeks:
            print(f'{ke:2}')
               

