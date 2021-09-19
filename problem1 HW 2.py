import argparse
import datetime

parser = argparse.ArgumentParser()


parser.add_argument("--num_d", help="number of days", type=int, default=0, required=False)
parser.add_argument("--num_y", help="number of years", type=int,default=0, required=False)

args = parser.parse_args()


today=datetime.date.today() 
tdelta = datetime.timedelta(days=args.num_d+args.num_y*365)
final_date=today+tdelta

print("current date:", today)
print("given years:",args.num_y)
print("given days:",args.num_d)
print('final date:', final_date)