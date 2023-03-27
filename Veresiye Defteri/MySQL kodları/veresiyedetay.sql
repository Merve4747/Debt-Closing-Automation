Create Table VeresiyeDetay(veresiyedetay_id INT AUTO_INCREMENT,veresiye_id INT,urun_id INT,urun_adet INT,
primary key(veresiyedetay_id),foreign key(veresiye_id) references Veresiye(veresiye_id),
foreign key(urun_id) references Urunler(urun_id));
