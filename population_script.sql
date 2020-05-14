--Product

INSERT INTO product_producttype(name) VALUES('Tölvuleikir');
INSERT INTO product_producttype(name) VALUES('Leikjatölvur');
INSERT INTO product_producttype(name) VALUES('Aukahlutir');
INSERT INTO product_producttype(name) VALUES('Varahlutir');

INSERT INTO product_productstatus(name) VALUES('Active');
INSERT INTO product_productstatus(name) VALUES('Inactive');
INSERT INTO product_productstatus(name) VALUES('Ordered');
INSERT INTO product_productstatus(name) VALUES('Out of stock');

INSERT INTO product_productagelimit(name) VALUES('Allur aldur');
INSERT INTO product_productagelimit(name) VALUES('3+');
INSERT INTO product_productagelimit(name) VALUES('5+');
INSERT INTO product_productagelimit(name) VALUES('10+');
INSERT INTO product_productagelimit(name) VALUES('18+');

INSERT INTO product_productsubtypes(name) VALUES('Óskilgreint');
INSERT INTO product_productsubtypes(name) VALUES('VR leikir');
INSERT INTO product_productsubtypes(name) VALUES('Óskilgreint');
INSERT INTO product_productsubtypes(name) VALUES('Skotleikir');
INSERT INTO product_productsubtypes(name) VALUES('Hasarleikir');
INSERT INTO product_productsubtypes(name) VALUES('Íþróttaleikir');
INSERT INTO product_productsubtypes(name) VALUES('Kappakstursleikir');
INSERT INTO product_productsubtypes(name) VALUES('Þrautir og heialbraut');
INSERT INTO product_productsubtypes(name) VALUES('Ævintýraleikir');


INSERT INTO product_productmanufacturer(name) VALUES('Sony');
INSERT INTO product_productmanufacturer(name) VALUES('Nitendo');
INSERT INTO product_productmanufacturer(name) VALUES('Microsoft');


INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Microsoft Xbox One Stereo leikjaheyrnartól', 25000, 'Með Microsoft Xbox One Stereo leikjaheyrnartólunum getur þú sokkið þér í heimi tölvuleikja. Höfuðtólið býður upp á steríóhljóð, einstefnu hljóðnema og hentar vel til að spila tölvuleiki, hvort sem það er í einspilun eða í co-op leikjum.', 5, false, 1, 3, 3, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Super Mario Bros', 1999, 'Super Mario Bros er fyrsti Super Mario Bros tölvuleikurinn. Hann kom út árið 1985 á NES (Nintendo Entertainment System).', 5, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Commando', 1299, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 10, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('King kong', 1599, 'King Kong tölvuleikurinn er gerður eftir myndinni um King Kong sem Peter Jackson leikstýrir. Leikurinn var unnin í nánu samstarfi við Peter Jackson og tæknibrellufyrirtækið Weta Ltd. Í leiknum spilaru í fyrstu persónu sem Jack Driscoll en í þriðju persónu sem King Kong sjálfur. Leikurinn gerist aðalega á eyjunni Skull Island sem er þakinn dimmum skógum.  Upplifðu öll helstu atriðin úr myndinni í þessum frábæra leik', 8,  false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Donkey Kong', 999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 5, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Tetris', 2250, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 5, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Paperboy', 1999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Boulder dash 1', 1999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Boulder dash 2', 1999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('1942', 899, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Battle of midway', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Crazy cars', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Ghost busters', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Winter games', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Summer games', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, manufacturer_id, status_id, sub_type_id) VALUES('Super cycle', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 9, false, 1, 1, 1, 1, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, status_id, manufacturer_id, sub_type_id) VALUES('Intel Pentium Gold G5400 3.7GHz 1151 14nm 4MB', 15000, 'Intel Pentium Gold með 2 kjarna og 4 þræði í heild.', 50, false, 1, 4, 1, 10, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, status_id, manufacturer_id, sub_type_id) VALUES('AM4 A10-9700 3.5GHz/3.8GHz', 18500, 'AM4 A10-9700 með Radeon R7 Skjákorti innbyggðu', 50, false, 1, 4, 1, 10, 1);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, status_id, manufacturer_id, sub_type_id) VALUES('Intel Retail Vifta 1150/1155/1156', 2350, 'Intel Stock vifta fyrir 115X 1156/1155/1150', 50, false, 1, 4, 1, 10, 11);
INSERT INTO product_product(name, price, description, quantity, on_sale, age_limit_id, category_id, status_id, manufacturer_id, sub_type_id) ALUES('Noctua NF-P12 redux', 3600, 'Vifta hönnuð með það í huga að vera notuð á kæliturna eða vatnskælingar þar sem aukinn þrýstingur skiptir máli. NF-P12 er ein af þeim viftum sem kom Noctua á kortið og var í miklu uppáhaldi hjá notendum um heim allan.', 50, false, 1, 4, 1, 11, 11);


INSERT INTO product_productimage(image, product_id) VALUES('https://herocity.de/is/wp-content/uploads/2018/08/x_jpa78254-800x800.jpg', 2);
INSERT INTO product_productimage(image, product_id) VALUES('https://upload.wikimedia.org/wikipedia/en/2/26/Commando_flyer.png', 3);
INSERT INTO product_productimage(image, product_id) VALUES('http://myndform.webman.is/thumb.php?file=products/ds_king.kong.jpg&h=400&w=130', 4);
INSERT INTO product_productimage(image, product_id) VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS4zYQ9ruOGrD5eciuPKS6VLeNdzr0Ksy6_isIBU-v83oFpBqk4&usqp=CAU', 5);
INSERT INTO product_productimage(image, product_id) VALUES('https://www.scienceabc.com/wp-content/uploads/2018/12/duck-hunt-game.jpg', 6);
INSERT INTO product_productimage(image, product_id) VALUES('https://mspoweruser.com/wp-content/uploads/2010/12/Tetris1.png', 7);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 8);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 9);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 10);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 11);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 12);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 13);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 14);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 15);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 16);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 17);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 18);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 19);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 20);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 21);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 22);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 23);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 24);

INSERT INTO product_searchhistory(search_date, product_id, profile_id) VALUES('06-may-2020', 2, 1);
INSERT INTO product_searchhistory(search_date, product_id, profile_id) VALUES('06-may-2020', 5, 1);
INSERT INTO product_searchhistory(search_date, product_id, profile_id) VALUES('06-may-2020', 3, 1);
INSERT INTO product_searchhistory(search_date, product_id, profile_id) VALUES('06-may-2020', 8, 1);
INSERT INTO product_searchhistory(search_date, product_id, profile_id) VALUES('06-may-2020', 9, 1);
INSERT INTO product_searchhistory(search_date, product_id, profile_id) VALUES('06-may-2020', 10, 1);


-- Auth user

INSERT INTO auth_user(password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES('New12345', '2020-05-12 19:10:25-07', false, 'Ellan', 'Ella', 'Jónsdóttir', 'elinhb15@ru.is', false, true, '2016-06-22 19:10:25-07');

INSERT INTO auth_user(password, last_login, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) VALUES('Other12345', '2020-05-11 11:10:25-07', true, 'Doddi', 'Doddi', 'Hansson', 'doddih@ru.is', false, true, '2020-02-02 09:10:25-07');


-- User

INSERT INTO user_country(name) VALUES('Ísland');

INSERT INTO user_address(address, zip_code, city, user_id, country_id) VALUES('Menntavegur 10', '103', 'Reykjavík', 1, 1);
INSERT INTO user_address(address, zip_code, city, user_id, country_id) VALUES('Nauthólsvegur 3', '105', 'Reykjavík', 2, 1);

INSERT INTO user_card(card_number, valid_month, valid_year, cvc, user_id) VALUES('1234-1234-1234-1234', '01', '23', '123', 1);
INSERT INTO user_card(card_number, valid_month, valid_year, cvc, user_id) VALUES('2345-1234-5678-3456', '04', '21', '321', 2);

INSERT INTO user_profile(user_id) VALUES(1);
INSERT INTO user_profile(user_id) VALUES(2);

INSERT INTO user_userimage(image, user_id) VALUES('', 1);
INSERT INTO user_userimage(image, user_id) VALUES('', 2);


-- Order

INSERT INTO order_orderstatus(name) VALUES('In progress');
INSERT INTO order_orderstatus(name) VALUES('Shipped');
INSERT INTO order_orderstatus(name) VALUES('Delivered');
INSERT INTO order_orderstatus(name) VALUES('Cancelled');

INSERT INTO order_deliverytype(name) VALUES('Delivered');
INSERT INTO order_deliverytype(name) VALUES('Pick up at store');

INSERT INTO order_order(order_date, total_price, delivery_id, order_status_id) VALUES('2020-05-07', 899, 1, 1);
INSERT INTO order_order(order_date, total_price, delivery_id, order_status_id) VALUES('2020-05-07', 4559, 1, 1);
INSERT INTO order_order(order_date, total_price, delivery_id, order_status_id) VALUES('2020-05-08', 3500, 1, 1);
INSERT INTO order_order(order_date, total_price, delivery_id, order_status_id) VALUES('2020-05-08', 1550, 1, 1);
INSERT INTO order_order(order_date, total_price, delivery_id, order_status_id) VALUES('2020-05-09', 33500, 1, 1);
INSERT INTO order_order(order_date, total_price, delivery_id, order_status_id) VALUES('2020-05-09', 15999, 1, 1);

INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(2, 1, 3);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(2, 1, 7);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(2, 1, 8);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(1, 2, 8);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(1, 3, 5);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(1, 4, 4);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(1, 5, 3);
INSERT INTO order_orderedproducts(quantity, order_id, product_id) VALUES(1, 6, 7);

INSERT INTO order_alluserorders(order_id, user_id) VALUES(1, 2);
INSERT INTO order_alluserorders(order_id, user_id) VALUES(2, 2);
INSERT INTO order_alluserorders(order_id, user_id) VALUES(3, 2);

INSERT INTO order_customer(first_name, last_name, address, zip_code, city, mail, card_number, valid_month, valid_year, cvc, country_id, order_id) VALUES('Elín', 'Búadóttir', 'Menntavegur 1', '101', 'Reykjavík', 'elinhb15@ru.is', '1234-1234-4556-9876', '01', '20', '123', 1, 4);
INSERT INTO order_customer(first_name, last_name, address, zip_code, city, mail, card_number, valid_month, valid_year, cvc, country_id, order_id) VALUES('Elín', 'Búadóttir', 'Menntavegur 1', '101', 'Reykjavík', 'elinhb15@ru.is', '1234-1234-4556-9876', '01', '20', '123', 1, 5);
INSERT INTO order_customer(first_name, last_name, address, zip_code, city, mail, card_number, valid_month, valid_year, cvc, country_id, order_id) VALUES('Jón', 'Jónsson', 'Menntavegur 2', '101', 'Reykjavík', 'jonjon@ru.is', '5432-1234-4556-1535', '03', '23', '432', 1, 6);


