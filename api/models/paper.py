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
