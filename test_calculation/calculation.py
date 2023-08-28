import os
class Cal(object):
    def add_num_and_double(self, x, y):
        if type(x) is not int or type(y) is not int:
            raise ValueError
        result = x + y
        result *= 2
        return result

    def save(self, dir_path, file_name):
        if not os.path.exists(dir_path): # True or False
            os.mkdir(dir_path) # 新しいディレクトリを作成
        file_path = os.path.join(dir_path, file_name) # dir_path/file_name
        with open(file_path, 'w') as f:  # ファイルに書き込み
            f.write('test')
