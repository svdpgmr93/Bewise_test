from httpx import Client
from src.base import Session
from src.models import Test
from datetime import datetime
from sqlalchemy.exc import IntegrityError
from sqlalchemy import insert

client = Client()
victorina_url = 'https://jservice.io/api/random?count='


def get_tests(tests_count):
    r = client.get(url=f'{victorina_url}+{tests_count}')
    counter = 0
    with Session() as session:
        last_obj = session.query(Test).order_by(Test.id.desc()).first()
        for question in r.json():
            try:
                session.execute(
                    insert(Test),
                    [
                        {
                            'outer_id': question['id'],
                            'question': question['question'],
                            'answer': question['answer'],
                            'create_time': datetime.now(),
                        }
                    ],
                            )
            except IntegrityError:
                counter += 1
                with open('log.txt', 'a') as f:
                    f.write('Duplicate outer id - ' + str(question['id']))
        if type(last_obj) is Test:
            ret_obj = last_obj.to_json()
        else:
            ret_obj = {}
        session.commit()
    if counter:
        get_tests(counter)
    return ret_obj
