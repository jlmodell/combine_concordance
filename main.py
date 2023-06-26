import pandas as pd
import os
from glob import glob

base_path = "~/Desktop"
full_path = None


def get_full_path_from_user():
    global base_path, full_path
    path = input("Enter the path: ")
    while path != "":
        if path[0] == "~":
            full_path = os.path.expanduser(path)
        else:
            full_path = os.path.expanduser(os.path.join(base_path, path))

        print(full_path)

        if os.path.exists(full_path):
            break
        else:
            print("Path does not exist")
            path = input("Enter the path: ")


def combine_all_xlsx_into_single():
    global full_path

    paths = glob(os.path.join(full_path, "*.xlsx"))

    dfs = []

    for path in paths:
        dfs.append(pd.read_excel(path))

    df = pd.concat(dfs, ignore_index=True)

    file_name = full_path.split("/")[-1]

    df.to_excel(os.path.join(full_path, file_name + ".xlsx"), index=False)

    return df


if __name__ == "__main__":
    get_full_path_from_user()
    df = combine_all_xlsx_into_single()

    print(df)
