use bmh204;
Create Table Musteriler(id INT AUTO_INCREMENT ,ad varchar(20),soyad varchar(20),telefon varchar(20),adres varchar(20),primary key(id));


DELIMITER //
CREATE PROCEDURE MusteriEkle(IN gelen_ad VARCHAR(20), IN gelen_soyad varchar(20), IN gelen_telefon varchar(20),gelen_adres varchar(20))
BEGIN
  INSERT INTO Musteriler(ad,soyad,telefon,adres) values(gelen_ad,gelen_soyad,gelen_telefon,gelen_adres);
END//
DELIMITER ;








DELIMITER //
CREATE PROCEDURE MusteriGuncelle(IN gelen_id INT,IN gelen_ad varchar(20), IN gelen_soyad varchar(20), IN gelen_telefon varchar(20),gelen_adres varchar(20))
BEGIN
  update Musteriler
  set ad=gelen_ad,soyad=gelen_soyad,telefon=gelen_telefon where id=gelen_id;
END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE Musterileri_getir()
BEGIN
  select*from Musteriler ;
  END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE Musteri_getir_id(IN gelen_id INT)
BEGIN
  select*from Musteriler where id=gelen_id;
  END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE Musteri_getir_telefon(IN gelen_telefon varchar(20))
BEGIN
  select*from Musteriler where telefon=gelen_telefon;
  END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE MusteriSil(IN gelen_id INT)
BEGIN
  delete from Musteriler 
  Where id=gelen_id;
END//
DELIMITER ;






