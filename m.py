import datetime
import pytz


uz_time= pytz.timezone('Asia/Tashkent')
current = datetime.datetime.fromtimestamp(1688224457)

uzbekistan=uz_time.localize(current)
