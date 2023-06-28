import os


class RenameModel:
    def __int__(self):
        pass

    def change_name(self, path, old_name, new_name):
        for filename in os.listdir(path):
            new = filename.replace(old_name, new_name)
            os.rename(os.path.join(path, filename), os.path.join(path, new))
            print(filename)


# if __name__ == "__main__":
#     re = RenameModel()
#     re.change_name('<path>', '<old_name>', '<new_name>')
