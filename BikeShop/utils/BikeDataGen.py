from BikeShop.models import Companies, Bikes, Companies_Bikes
from enum import Enum
import random
from datetime import datetime


class Size(Enum):
    S = 1
    M = 2
    L = 3
    XL = 4



def readFile(fileName):


    with open(fileName) as f:
        lines = f.read().splitlines()

    company = None
    for line in lines:

        # try to split first
        split_line = line.split('  ')
        if (split_line[0] == 'company'):
            company = Companies.objects.get(name=split_line[1])

        else:
            split_line = line.split(', ')
            random.seed(datetime.now())
            num_to_Make = random.randint(1, 10)
            for insert in range(1, num_to_Make):
                size = random.randint(1,5)
                print(int(split_line[2]))
                print(int(split_line[3]))
                bike = Bikes.objects.get_or_create(model=split_line[0], type=split_line[1], price=int(split_line[2]), year=int(split_line[3]), thumbnail=split_line[4], size= size)
                Companies_Bikes.objects.update_or_create(company_code= company, bike_id=bike)

            #Bikes.objects.update_or_crea



