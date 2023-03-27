Create Table Veresiye(veresiye_id INT AUTO_INCREMENT,musteri_id INT,veresiye_tarihi Date ,borc_tutari float,odeme_durumu varchar(20),odeme_tarihi Date null ,odeme_tipi varchar(20),Primary key(veresiye_id),foreign key(musteri_id) references Musteriler(musteri_id));

DELIMITER //
CREATE PROCEDURE VeresiyeEkle(IN gelen_musteri_id INT, IN gelen_borc_tutari float,gelen_urun_id_list MEDIUMTEXT,gelen_urun_adet_list MEDIUMTEXT )
BEGIN
  DECLARE veresiye_id INT;
  DECLARE _next TEXT DEFAULT NULL;
DECLARE _nextlen INT DEFAULT NULL;
DECLARE urun_id TEXT DEFAULT NULL;

DECLARE _next1 TEXT DEFAULT NULL;
DECLARE _nextlen1 INT DEFAULT NULL;
DECLARE urun_adet TEXT DEFAULT NULL;
  INSERT INTO Veresiye(musteri_id,veresiye_tarihi,borc_tutari,odeme_durumu,odeme_tarihi,odeme_tipi) values(gelen_musteri_id,curdate(),gelen_borc_tutari,"ödenmedi",null,null);
  SET veresiye_id =  LAST_INSERT_ID();
  

iterator:
LOOP
  IF CHAR_LENGTH(TRIM(gelen_urun_id_list)) = 0 OR gelen_urun_id_list IS NULL THEN
    LEAVE iterator;
    END IF;
 
  SET _next = SUBSTRING_INDEX(gelen_urun_id_list,',',1);
  SET _nextlen = CHAR_LENGTH(_next);
  SET urun_id = TRIM(_next);
   SET _next1 = SUBSTRING_INDEX(gelen_urun_adet_list,',',1);
  SET _nextlen1 = CHAR_LENGTH(_next1);
  SET urun_adet = TRIM(_next1);

INSERT INTO VeresiyeDetay(veresiye_id,urun_id,urun_adet) values(veresiye_id,urun_id,urun_adet);

  SET gelen_urun_id_list = INSERT(gelen_urun_id_list,1,_nextlen + 1,'');
  SET gelen_urun_adet_list = INSERT(gelen_urun_adet_list,1,_nextlen1 + 1,'');
END LOOP;
END//

DELIMITER ;


DELIMITER //
CREATE PROCEDURE VeresiyeGuncelle(IN gelen_veresiye_id INT,gelen_odeme_tipi varchar(20))
BEGIN
  update Veresiye 
  set odeme_tarihi=curdate(),odeme_tipi=gelen_odeme_tipi,odeme_durumu="Ödendi"
  where veresiye_id=gelen_veresiye_id;
END//
DELIMITER ;






DELIMITER //
CREATE PROCEDURE Veresiye_getir(IN gelen_veresiye_id INT)
BEGIN
   select*from Veresiye where veresiye_id=gelen_veresiye_id;
END//
DELIMITER ;

