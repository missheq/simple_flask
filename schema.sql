drop table if exists entries;
create table record (
  id integer primary key autoincrement,
  bid text not null,
  status text not null
);
