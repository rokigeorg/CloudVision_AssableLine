drop table if exists Bilder;
create table Bilder (
  id integer primary key autoincrement,
  filename text not null,
  sufix TEXT NOT null,
  pathtopic TEXT,
  rawbits BLOB,
  isCircle integer,
  csvlabels TEXT
);

INSERT INTO Bilder (filename, sufix,pathtopic, isCircle, csvlabels) VALUES ("tname.png", "png","/home/pi/TestDir" "0", "val, val2, val3, val4 ");