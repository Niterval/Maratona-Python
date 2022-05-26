import csv
import gspread

def save_to_csv(jobs):
  file = open('jobs.csv', 'w')
  write = csv.writer(file)
  write.writerow(['title', 'company', 'location', 'how_old', 'link'])

  for job in jobs:
    write.writerow(list(job.values()))


def google_sheet():
  gc = gspread.service_account(filename='credentials.json')
  sh = '1DZGu8GXH9zpJ_BLSJWCbE8RYdbpHuqi64CJoqoyb7Gw'
  content = open('jobs.csv', 'r').read().encode('utf-8')
  gc.import_csv(sh, content)

  return
