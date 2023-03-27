Create Table Urunler(urun_id INT AUTO_INCREMENT,urun_adi varchar(20),aciklama varchar(20) ,urun_fiyati float,primary key(urun_id));



DELIMITER //
CREATE PROCEDURE UrunEkle(IN gelen_urun_adi VARCHAR(20), IN gelen_aciklama varchar(20), IN gelen_urun_fiyati float)
BEGIN
  INSERT INTO Urunler(urun_adi,aciklama,urun_fiyati) values(gelen_urun_adi,gelen_aciklama,gelen_urun_fiyati);
END//
DELIMITER ;




DELIMITER //
CREATE PROCEDURE UrunGuncelle(IN gelen_urun_id INT,IN gelen_urun_adi varchar(20), IN gelen_aciklama varchar(20), IN gelen_urun_fiyati float)
BEGIN
  update Urunler
  set urun_adi=gelen_urun_adi,aciklama=gelen_aciklama,urun_fiyati=gelen_urun_fiyati where urun_id=gelen_urun_id;
END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE Urunleri_getir()
BEGIN
  select*from Urunler ;
  END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE Urun_getir_urun_id(IN gelen_urun_id INT)
BEGIN
  select*from Urunler where urun_id=gelen_urun_id;
  END//
DELIMITER ;


DELIMITER //
CREATE PROCEDURE UrunAra_urun_adi(IN gelen_urun_adi varchar(20))
BEGIN
  select*from Urunler
  where urun_adi LIKE(gelen_urun_adi);
  END//
DELIMITER ;



DELIMITER //
CREATE PROCEDURE UrunSil(IN gelen_urun_id INT)
BEGIN
  delete from Urunler
  Where urun_id=gelen_urun_id;
END//
DELIMITER ;

