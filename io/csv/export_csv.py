import csv
from django.contrib.auth.models import User

header = ('id', 'username', 'email', 'date_joined')
users = User.objects.all().values_list(*header)
with open('io/csv/users.csv', 'w') as csvfile:
    user_writer = csv.writer(csvfile)
    user_writer.writerow(header)
    for user in users:
        user_writer.writerow(user)
