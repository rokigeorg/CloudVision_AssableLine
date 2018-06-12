drop table if exists Images;
drop table if exists ImgMeta;
drop table if exists students;

create table Images (
  id integer primary key autoincrement,
  filename text not null,
  'text' text not null
);

create table ImgMeta (
  id integer primary key autoincrement,
  Imagae_id text not null,
  'isCircle' boolean not null
);

create table students (
  student_id integer primary key autoincrement,
  name text not null,
  city text not null,
  addr text not null,
  pin text not null
);


