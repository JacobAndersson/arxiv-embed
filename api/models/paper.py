import db
from pypika import Query, Table

papersTable = Table("papers")

def insert_paper(paper):
    q = Query.into(papersTable).columns(list(paper.keys())).insert(*paper.values())
    db.conn.execute(q.get_sql())
    db.conn.commit()

def insert_papers(papers):
    paper_columns = list(papers[0].keys())
    paper_values = [list(paper.values()) for paper in papers]

    q = (Query
         .into(papersTable)
         .columns(paper_columns)
         .insert(*paper_values))

    db.conn.execute(q.get_sql())
    db.conn.commit()

def get_full_docs(ids):
    q = Query.from_(papersTable).select("id", "title", "authors", "abstract").where(papersTable.id.isin(ids))
    docs = db.conn.execute(q.get_sql()).fetchall()

    entries = []
    for doc in docs:
        #Ugly. But so is python
        entries.append({
            "id": doc[0],
            "title": doc[1],
            "authors": doc[2],
            "abstract": doc[3],
        })

    return entries
