drop table if exists record;
create table record (
  id integer primary key autoincrement,
  bid text not null,
  status text not null,
  last_time text not null
);
