from database import get_db
from database.models import User
from datetime import datetime
import pytz
tashkent_timezone = pytz.timezone('Asia/Tashkent')

def add_user(tg_id, phone_number, product):
    with next(get_db()) as db:
        new_user = User(tg_id=tg_id, phone_number=phone_number, product=product,
                        payment_date="не оплачено")
        db.add(new_user)
        db.commit()
def payment_status(tg_id, product):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id, product=product,
                                        payment_date="не оплачено").first()
        if user:
            user.payment_date = str(datetime.now(tashkent_timezone))
            db.commit()
def get_phone_db(tg_id):
    with next(get_db()) as db:
        user = db.query(User).filter_by(tg_id=tg_id).first()
        if user:
            return user.phone_number

