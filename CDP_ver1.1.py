import glob
import os
import csv
import pandas as pd
from datetime import datetime
from monthdelta import monthmod

# target_dir = '/Users/nagaokashuuhei/Desktop/R2_data/R*.*'
# #対象のフォルダを絶対パスで指定して変数に代入
#
# folder_list = glob.glob(target_dir)
# #ターゲットのフォルダ内のオブジェクトをすべて抽出
#
# all_file = []
# #この後に処理したいファイルをこのリストに格納していく
# folder_n = 0
# #フォルダを指定した際に、そのフォルダの中のオブジェクトを取得するため、アンカーを設定
#
# while folder_n < len(folder_list):
#     set_file = []
#     os.chdir(folder_list[folder_n])
#     set_file = glob.glob('*.csv')
#     #特定のファイルのみを抽出
#     for file in set_file:
#         all_file.append(folder_list[folder_n]+'/'+file)
#     os.chdir('../')
#     folder_n += 1
all_file_list = []
dob_data_list = []
after_processing_list = []

def get_folders_path(target_dir):
    folders_path = glob.glob(target_dir)
    return folders_path
#対象のフォルダの中のフォルダのパスを取得、リストに入れる

def get_file_path(folders,file_kind,after_pro_list):#フォルダパスを入れる,取得したいフォルダの種類をワイルドカード形式で入れる
    for folder in folders:
        os.chdir(folder)
        files = glob.glob(file_kind)
        for file in files:
            all_file_list.append(folder+'/'+file)
        os.chdir('../')
    return after_pro_list
#対象のフォルダの中のfile_kindの種類のファイルパスをall_file_listに入れていく

def dob_list_gen(file_list,ter_dir,dob_list):
    os.chdir(ter_dir)
    for file in file_list:
        with open(file, 'r', encoding= 'cp932') as f:
            data = csv.reader(f)
            row = list(data)
            del row[0]
            for dob_data in row:
                dob_list.append(dob_data[4])
    return dob_list

def adjust_dob(dob_list,after_list):
    for dob in dob_list:
        before_dob = list(dob)
        before_dob.insert(4,'/')
        before_dob.insert(7,'/')
        before_dob = ''.join(before_dob)
        after_list.append(before_dob)
    return after_list




tg_folder = get_folders_path('/Users/nagaokashuuhei/Desktop/R4_data/R*.*')
data =  get_file_path(tg_folder,'*.csv',all_file_list)
dob_list_gen(all_file_list,'/Users/nagaokashuuhei/Desktop/R4_data',dob_data_list)
print(adjust_dob(dob_data_list,after_processing_list))




#カレントディレクトリから全てのファイルに一度カレントディレクトリから移動してそのファイル内の
#csvファイルを取得。all_fileに追加し、最初の作業ディレクトリに戻る
#その後次のファイルにいくためにfolder_nをカウントアップ
# file_n = 0
# while file_n < len(all_file):
#     with open(all_file[file_n],'r',encoding = 'cp932') as f: #上記でリスト化した処理したいファイルを個別で読み込みする
#         data = csv.reader(f)
#         b_data = []
#         for row in data:
#             b_data.append(row[4])
#         del b_data[0]
#     #all_fileのファイルに対して個別に生年月日を取得して、b_dataリストに代入していく
#
#     after_list = []
#     for x in b_data:
#         b_num = list(x)
#         b_num.insert(4,'/')
#         b_num.insert(7,'/')
#         result = ''.join(b_num)
#         after_list.append(result)
#     #b_dataをYYYY/MM/DDの形式に変換
#
#     find_mon1 = all_file[file_n].find('）')
#     find_mon2 = all_file[file_n][find_mon1:]
#     find_mon3 = find_mon2[4:]
#     get_mon = int(find_mon3.strip('.csv'))
#     #処理中のファイルの月を取得する
#     mon = ''
#
#     if get_mon == 4:
#         mon = '2020/04/30'
#     elif get_mon == 5:
#         mon = '2020/05/31'
#     elif get_mon == 6:
#         mon = '2020/06/30'
#     elif get_mon == 7:
#         mon = '2020/07/31'
#
#     elif get_mon == 8:
#         mon = '2020/08/31'
#
#     elif get_mon == 9:
#         mon = '2020/09/30'
#
#     elif get_mon == 10:
#         mon = '2020/10/31'
#
#     elif get_mon == 11:
#         mon = '2020/11/30'
#
#     elif get_mon == 12:
#         mon = '2020/12/31'
#
#     elif get_mon == 1:
#         mon = '2021/01/31'
#
#     elif get_mon == 2:
#         mon = '2021/02/28'
#
#     elif get_mon == 3:
#         mon = '2021/03/31'
#
#     else:
#         print('none')
#
#     #月毎にアンカーを設置して年代計算のために準備する
#
#     dob = []
#     for x in after_list:
#         dt1 = datetime(int(x[0:4]),int(x[5:7]),int(x[-2:]))
#         dt2 = datetime(int(mon[0:4]),int(mon[5:7]),int(mon[-2:]))
#         dt3 = monthmod(dt1, dt2)
#         dt = dt3[0].months//12#年齢を計算
#         if dt >= 10:
#             dt_a = round(dt,-1)
#             dob.append(dt_a)
#         elif dt >= 90:
#             dt_a = 90
#             dob.append(dt_a)
#         else:
#             dob.append(10)
#
#     #生年月日から経過年数を計算
#
#
#
#
#
#     df = pd.read_csv(all_file[file_n], encoding = 'cp932')
#     df.insert(loc = 5, column = '生年月日/', value = after_list)
#     df.insert(loc = 6, column = '年代', value = dob)
#
#     output = all_file[file_n].find('異')
#     path = all_file[file_n][output:]
#     #●異動者一覧（転入）〜のテキストでそのままcsvとして出力できるようにする
#
#
#
#     df.to_csv('/Users/nagaokashuuhei/Desktop/after_file/' + path)
#
#     file_n += 1
