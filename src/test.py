from loader import db

print(db.select_all_users())
print(db.select_user_info(id=236993487))
print(db.update_user_phone(id=236993487, phone='new'))
print(db.select_user_info(id=236993487))
print(db.delete_user(id=236993487))
print(db.select_all_users())
