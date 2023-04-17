-- migrate:up
create table papers (
  id VARCHAR(250) not null primary key,
  title text not null,
  authors text not null,
  categories text not null,
  abstract text not null,
  created_at timestamp not null default now(),
  updated_at timestamp not null default now()
);

-- migrate:down
drop table papers;
