import pymongo
from url_connection import url


def pull_teachers_info(subject, name, number, type, price):
    document = {
        "Subject" : subject,
        "Name" : name,
        "Phone_number" : number,
        "Type" : type,
        "Price" : price
    }
    document_id = collection.insert_one(document).inserted_id
    print(f'Created a document with id: {document_id}')


with pymongo.MongoClient(url) as client:
    db=client.Private_Lessons
    collection = db.Teachers_Information

    pull_teachers_info("english","Antonio Benitez","+34 666666666","individual","15€")
    pull_teachers_info("english","Penélope Ruiz","+34 653245485","individual","18€")
    pull_teachers_info("english","Sara Johnson","+34 684555365","individual","10€")
    pull_teachers_info("english","Sara Johnson","+34 684555365","collective","6€")
    pull_teachers_info("english","Antonio Benitez","+34 666666666","collective","7€")

    pull_teachers_info("spanish","Antonio Benitez","+34 666666666","individual","15€")
    pull_teachers_info("spanish","Pablo Santos","+34 612345678","individual","17.5€")
    pull_teachers_info("spanish","Severine Johnson","+34 684555365","individual","12€")
    pull_teachers_info("spanish","Antonio Benitez","+34 666666666","collective","7€")
    pull_teachers_info("spanish","Pablo Santos","+34 612345678","collective","10€")

    pull_teachers_info("maths","Pepe Peñalver","+34 648312515","individual","10€")
    pull_teachers_info("maths","Antonia Pacheco","+34 678954255","individual","11.5€")
    pull_teachers_info("maths","Isabel Ortiz","+34 625553112","individual","13€")
    pull_teachers_info("maths","Pepe Peñalver","+34 648312515","collective","6€")
    pull_teachers_info("maths","Isabel Ortiz","+34 625553112","collective","5.5€")

    pull_teachers_info("physics","Antonia Pacheco","+34 678954255","individual","11.5€")
    pull_teachers_info("physics","José Juan Pérez","+34 612333242","individual","10")
    pull_teachers_info("physics","Antonia Pacheco","+34 678954255","collective","6€")

    pull_teachers_info("chemistry","José Juan Pérez","+34 612333242","individual","10")
    pull_teachers_info("chemistry","Antonia Pacheco","+34 678954255","individual","11.5€")
    pull_teachers_info("chemistry","Antonia Pacheco","+34 678954255","collective","6€")




