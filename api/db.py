import psycopg

conn = psycopg.connect("postgres://postgres:test@localhost:5432/arxiv?sslmode=disable")

if __name__ == "__main__":
    conn.execute('Insert into papers (id, title, abstract, authors, categories) values (%s, %s, %s, %s, %s)', ('123', 'title', 'abstract', 'authors', 'categories'))
    conn.commit()
    res = conn.execute('Select * from papers')
