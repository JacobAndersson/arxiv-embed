# Arxiv embed 
Simple semantic search engine for arxiv papers.  

The semantic similarity is computed between the query and the paper abstract. The embedding model used is [multi-qa-mpnet-base-dot-v1](https://huggingface.co/sentence-transformers/multi-qa-mpnet-base-dot-v1). The abstracts are embedded in advanced and stored in [Milvus](https://milvus.io/).

During retrieval the query is embedded using the same model and the closest 100 documents are retrieved. After that they are re ranked using [ms-marco-MiniLM-L-12-v2](https://huggingface.co/cross-encoder/ms-marco-MiniLM-L-12-v2) model and the top 10 is sent back to the client.

The additional data about the papers are stored in postgres.

## Data
The arxiv dataset can be downloaded on [kaggle](https://www.kaggle.com/datasets/Cornell-University/arxiv?resource=download)


## Setup

To setup backend you need to start with downloading the dataset from kaggle. 

Once this is done you can start the process of setting up the databases
1. Start postgres and milvus ```docker-compose up```
2. Start with running the postgres migrations (They were created using [dbmate](https://github.com/amacneil/dbmate) so recommend using that for running them. They are just plain sql files however so you can really use what you want)
3. Then run `init_milvus.py` script to create the milvus embedding collection
4. No the ingesting can start by running the ```api/ingest.py```. A GPU using highly recommended for this step
5. You are ready!


## Future work
* More data. Current dataset is not fully up to date so scraping arxiv for up to date papers would be needed. Doing that with getting ip blocked however, is a bit trickier.
* Different embedders. [Instructor](https://arxiv.org/abs/2212.09741) in particular looks really interesting
* Speed.
