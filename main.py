from indeed import search_indeed
from save import save_to_csv, google_sheet

search = 'python'

result_indeed = search_indeed(search)
save_drive_sheet = google_sheet()

save_to_csv(result_indeed)
