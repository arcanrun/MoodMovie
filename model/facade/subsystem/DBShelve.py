import shelve
from .interfaces.IDataBase import IDataBase


class DBShelve(IDataBase):
    def add_item(self, item):
        db = shelve.open('shelveDB')
        last_id = len(db.keys()) - 1

        if not last_id == -1:
            db[str(last_id + 1)] = item
        else:
            db['0'] = item

        db.close()

    def get_item(self, id):
        db = shelve.open('shelveDB')
        try:
            return db[str(id)]
        except KeyError:
            return None

    def clear_db(self):
        db = shelve.open('shelveDB')
        db.clear()
        db.close()

    def change_item(self, item, id):
        db = shelve.open('shelveDB')
        db[str(id)] = item
        db.close()

    def has_item(self, sign):
        res = False
        db = shelve.open('shelveDB')
        for k, v in db.items():
            if str(v['id']) == str(sign):
                res = True
                break
        return res

    def has_mark(self, sign):
        res = False
        db = shelve.open('shelveDB')
        for k, v in db.items():
            if str(v['id']) == str(sign):
                if 'your_mark' in v:
                    res = v['your_mark']
                    break
        return res

    def get_all_items(self):
        all_data = []
        db = shelve.open('shelveDB')
        for k, v in db.items():
            all_data.append([k, v])
        all_data.sort(key=lambda x: x[0])
        return all_data

    def delete_item(self, id):
        try:
            db = shelve.open('shelveDB')
            db.pop(str(id))
            return True
        except:
            return False