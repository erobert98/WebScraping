import gspread
# from google.oauth2 import service_account
# import google.auth
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name('./Gspread-ed7c5a1c8359.json', scope)

gc = gspread.authorize(credentials)


# wk = gc.open('Proud Boys - Facebook Search')
wk = gc.open('VoteLocal')
test = wk.get_worksheet(0)

def save_Pageinfo(group, tlikes, date, names, name):
    cell = test.find(group)
    row_number = cell.row
    test.update_cell(row_number, 4, name)
    test.update_cell(row_number, 5, tlikes)
    test.update_cell(row_number, 6, date)
    test.update_cell(row_number, 7, names)

def find_groups():
    values_list = test.col_values(1)
    return values_list


def write_groups(urls):
    L = len(urls)
    print(L)
    cell_list = test.range(f'A1:A{L}')
    print(cell_list)
    item = 0
    while item < L-1:
        for cell in cell_list:
            try:
                cell.value = urls[item]
                item += 1
            except:
                cell.value = 'hmm'
                item += 1
    # Update in batch
    test.update_cells(cell_list)

if __name__ == "__main__":
    # pass
    # write_CSV(store_links, country)
    # check_for_unjoined()
    # mark_as_joined(link, name)
    pass