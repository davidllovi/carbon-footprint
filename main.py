import os
import calendar
import carbon_functions as caf

rootfolder = "/home/david/Escriptori/mega/100-carbon/location"
folders = os.listdir(rootfolder)
folders.sort()
for year_number in folders:
    datafolder = rootfolder + "/" + year_number
    total_year = 0
    print(f"{year_number}")
    for month in range(1, 13):
        month_name = calendar.month_name[month].upper()
        filepath = f"{datafolder}/{year_number}_{month_name}.json"
        if not os.path.isfile(filepath):
            continue
        list_month = caf.process_file(filepath)
        activities_month_sum = caf.compress_month(list_month)
        total_month = caf.computeCO2(activities_month_sum)
        total_year = total_year + total_month

        km_car = caf.safe_extract(activities_month_sum, 'IN_PASSENGER_VEHICLE')
        km_fly = caf.safe_extract(activities_month_sum, 'FLYING')
        print(f"{month_name.ljust(10, ' ')}: {total_month} kg Car:{km_car} km Fly:{km_fly} km")
    print(f"Total {year_number}: {total_year} kg\n")
