def spreadsheet_encode_column(col_str):
    num = 0
    count = len(col_str) - 1
    for char in col_str:
        num += 26**count * (ord(char) - ord('A') + 1)
        count -= 1
    return num


print(spreadsheet_encode_column("ZZ"))