import datetime
import time

end_time=datetime.datetime(2020,9,21)
host_path='C:/Windows/System32/drivers/etc/hosts'
block_site=['www.facebook.com']
redirect='127.0.0.1'

while True:
  if datetime.datetime.now()<end_time:
    print('Website BLOCKING'
    with open (host_path,'r') as host_file:
      content=host_file.read()
        for site in block_site:
          if site not in content:
            host_file.write(redirect+""+site+'\n')
          else:
            pass
  else:
     with open(host_path,"r") as host_file:
          content=host_file.readlines()
          host_file.seek(0)
          for line in content:
            if not any(site in line  for site in block_site)
              host_file.write(line)
          host_file.truncate()
    time.sleep(10)          
          
          
          
          
          
