--Product

INSERT INTO product_producttype(name) VALUES('Tölvuleikir');
INSERT INTO product_producttype(name) VALUES('Leikjatölvur');
INSERT INTO product_producttype(name) VALUES('Aukahlutir');
INSERT INTO product_producttype(name) VALUES('Varahlutir');

INSERT INTO product_productstatus(name) VALUES('Active');
INSERT INTO product_productstatus(name) VALUES('Inactive');
INSERT INTO product_productstatus(name) VALUES('Ordered');
INSERT INTO product_productstatus(name) VALUES('Out of stock');

INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Super Mario Bros', 1999, 'Super Mario Bros er fyrsti Super Mario Bros tölvuleikurinn. Hann kom út árið 1985 á NES (Nintendo Entertainment System).', 1, 1, 12, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Commando', 1299, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('King kong', 1599, 'King Kong tölvuleikurinn er gerður eftir myndinni um King Kong sem Peter Jackson leikstýrir. Leikurinn var unnin í nánu samstarfi við Peter Jackson og tæknibrellufyrirtækið Weta Ltd. Í leiknum spilaru í fyrstu persónu sem Jack Driscoll en í þriðju persónu sem King Kong sjálfur. Leikurinn gerist aðalega á eyjunni Skull Island sem er þakinn dimmum skógum.  Upplifðu öll helstu atriðin úr myndinni í þessum frábæra leik', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Donkey Kong', 999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Duck Hunt',1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Tetris', 2250, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Paperboy', 1999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Boulder dash 1', 1999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Boulder dash 2', 1999, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('1942', 899, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Battle of midway', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Crazy cars', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Ghost busters', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Winter games', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Summer games', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);
INSERT INTO product_product(name, price, description, category_id, status_id, quantity, on_sale) VALUES('Super cycl', 1599, 'Tölvuleikur fyrir alla tölvuleikjaáhugamenn', 1, 1, 5, false);


INSERT INTO product_productimage(image, product_id) VALUES('https://herocity.de/is/wp-content/uploads/2018/08/x_jpa78254-800x800.jpg', 1);
INSERT INTO product_productimage(image, product_id) VALUES('https://upload.wikimedia.org/wikipedia/en/2/26/Commando_flyer.png', 2);
INSERT INTO product_productimage(image, product_id) VALUES('http://myndform.webman.is/thumb.php?file=products/ds_king.kong.jpg&h=400&w=130', 3);
INSERT INTO product_productimage(image, product_id) VALUES('https://encrypted-tbn0.gstatic.com/images?q=tbn%3AANd9GcS4zYQ9ruOGrD5eciuPKS6VLeNdzr0Ksy6_isIBU-v83oFpBqk4&usqp=CAU', 4);
INSERT INTO product_productimage(image, product_id) VALUES('https://www.scienceabc.com/wp-content/uploads/2018/12/duck-hunt-game.jpg', 5);
INSERT INTO product_productimage(image, product_id) VALUES('https://mspoweruser.com/wp-content/uploads/2010/12/Tetris1.png', 6);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 7);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 8);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 9);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 10);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 11);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 12);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 13);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 14);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 15);
INSERT INTO product_productimage(image, product_id) VALUES('https://i.pinimg.com/originals/5e/22/86/5e2286e02a8d3a65558ad3adf7534670.jpg', 16);


INSERT INTO product_searchhistory(search_date, product_id, user_id) VALUES(06-may-2020, 1, 1);
INSERT INTO product_searchhistory(search_date, product_id, user_id) VALUES(06-may-2020, 5, 1);
INSERT INTO product_searchhistory(search_date, product_id, user_id) VALUES(06-may-2020, 3, 1);
INSERT INTO product_searchhistory(search_date, product_id, user_id) VALUES(06-may-2020, 8, 1);
INSERT INTO product_searchhistory(search_date, product_id, user_id) VALUES(06-may-2020, 9, 1);
INSERT INTO product_searchhistory(search_date, product_id, user_id) VALUES(06-may-2020, 10, 1);


-- Order

INSERT INTO order_orderstatus(name) VALUES('In progress');
INSERT INTO order_orderstatus(name) VALUES('Shipped');
INSERT INTO order_orderstatus(name) VALUES('Delivered');
INSERT INTO order_orderstatus(name) VALUES('Cancelled');

INSERT INTO order_deliverytype(name) VALUES('Delivered');
INSERT INTO order_deliverytype(name) VALUES('Pick up at store');

INSERT INTO order_order(product_quantity, price, order_date, delivery_id, mail_id, order_status_id, product_id_id) VALUES(1, 4999, '2020-05-07', 1, 5, 2, 5);
INSERT INTO order_order(product_quantity, price, order_date, delivery_id, mail_id, order_status_id, product_id_id) VALUES(1, 899, '2020-05-07', 2, 5, 2, 10);
INSERT INTO order_order(product_quantity, price, order_date, delivery_id, mail_id, order_status_id, product_id_id) VALUES(1, 1499, '2020-05-07', 2, 5, 2, 3);
INSERT INTO order_order(product_quantity, price, order_date, delivery_id, mail_id, order_status_id, product_id_id) VALUES(1, 4999, '2020-05-07', 2, 5, 2, 1);
INSERT INTO order_order(product_quantity, price, order_date, delivery_id, mail_id, order_status_id, product_id_id) VALUES(1, 1299, '2020-05-07', 2, 5, 2, 8);

INSERT INTO order_payment(card_number_id, order_id_id) VALUES(1,3);
INSERT INTO order_payment(card_number_id, order_id_id) VALUES(5,4);
INSERT INTO order_payment(card_number_id, order_id_id) VALUES(3,5);
INSERT INTO order_payment(card_number_id, order_id_id) VALUES(4,6);
INSERT INTO order_payment(card_number_id, order_id_id) VALUES(4,7);

-- User

INSERT INTO user_userstatus(name) VALUES('Active');
INSERT INTO user_userstatus(name) VALUES('Inactive');
INSERT INTO user_userstatus(name) VALUES('Blocked');

INSERT INTO user_userrole(name) VALUES('customer');
INSERT INTO user_userrole(name) VALUES('admin');

INSERT INTO user_zipcode(postal_code, city) VALUES('101', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('102', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('103', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('104', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('105', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('107', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('108', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('109', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('110', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('111', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('112', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('112', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('116', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('121', 'Reykjavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('170', 'Seltjarnarnes');
INSERT INTO user_zipcode(postal_code, city) VALUES('190', 'Vogar');
INSERT INTO user_zipcode(postal_code, city) VALUES('200', 'Kópavogur');
INSERT INTO user_zipcode(postal_code, city) VALUES('201', 'Kópavogur');
INSERT INTO user_zipcode(postal_code, city) VALUES('202', 'Kópavogur');
INSERT INTO user_zipcode(postal_code, city) VALUES('203', 'Kópavogur');
INSERT INTO user_zipcode(postal_code, city) VALUES('206', 'Kópavogur');
INSERT INTO user_zipcode(postal_code, city) VALUES('210', 'Garðabær');
INSERT INTO user_zipcode(postal_code, city) VALUES('220', 'Hafnarfjörður');
INSERT INTO user_zipcode(postal_code, city) VALUES('221', 'Hafnarfjörður');
INSERT INTO user_zipcode(postal_code, city) VALUES('222', 'Hafnarfjörður');
INSERT INTO user_zipcode(postal_code, city) VALUES('225', 'Garðabær');
INSERT INTO user_zipcode(postal_code, city) VALUES('230', 'Reykjanesbær');
INSERT INTO user_zipcode(postal_code, city) VALUES('240', 'Grindavík');
INSERT INTO user_zipcode(postal_code, city) VALUES('245', 'Sandgerði');
INSERT INTO user_zipcode(postal_code, city) VALUES('250', 'Garður');
INSERT INTO user_zipcode(postal_code, city) VALUES('270', 'Mosfellsbær');
INSERT INTO user_zipcode(postal_code, city) VALUES('271', 'Mosfellsbær');
INSERT INTO user_zipcode(postal_code, city) VALUES('276', 'Kjós');

INSERT INTO user_country(name) VALUES('Ísland');

INSERT INTO user_card(card_number, valid_month, valid_year, cvc) VALUES('1234-1234-1234-1234', '01', '23', '123');
INSERT INTO user_card(card_number, valid_month, valid_year, cvc) VALUES('2345-1234-5678-3456', '04', '21', '321');
INSERT INTO user_card(card_number, valid_month, valid_year, cvc) VALUES('9871-2345-2345-6778', '02', '21', '654');
INSERT INTO user_card(card_number, valid_month, valid_year, cvc) VALUES('3456-2345-3454-5676', '04', '23', '432');
INSERT INTO user_card(card_number, valid_month, valid_year, cvc) VALUES('4567-2345-4567-3456', '01', '22', '565');

INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('elinadmin', 'captain1234', '2', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('asdisadmin', 'captain1234', '2', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('unnaradmin', 'captain1234', '2', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('jonadmin', 'captain1234', '2', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('elin', 'captain1234', '1', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('asdis', 'captain1234', '1', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('unnar', 'captain1234', '1', '1');
INSERT INTO user_user(user_name, password, user_role_id, user_status_id) VALUES('jon', 'captain1234', '1', '1');

INSERT INTO user_customer(first_name, last_name, address, mail, card_number_id, country_id, user_id_id, zip_code_id) VALUES('Elín', 'Búadóttir', 'Menntavegi 1', 'elinhb15@ru.is', 1, 1, 5, 4);
INSERT INTO user_customer(first_name, last_name, address, mail, card_number_id, country_id, user_id_id, zip_code_id) VALUES('Ásdís Karen', 'Waltersdóttir', 'Menntavegi 1', 'asdisw17@ru.is', 2, 1, 5, 4);
INSERT INTO user_customer(first_name, last_name, address, mail, card_number_id, country_id, user_id_id, zip_code_id) VALUES('Unnar', 'Sigurðsson', 'Menntavegi 1', 'unnar17@ru.is', 2, 1, 5, 4);
INSERT INTO user_customer(first_name, last_name, address, mail, card_number_id, country_id, user_id_id, zip_code_id) VALUES('Jón Ágúst', 'Guðmundsson', 'Menntavegi 1', 'jonag15@ru.is', 2, 1, 5, 4);

INSERT INTO user_userimage(image, customer_id) VALUES('https://cdn5.vectorstock.com/i/1000x1000/04/09/user-icon-vector-5770409.jpg', 1);
INSERT INTO user_userimage(image, customer_id) VALUES('https://cdn5.vectorstock.com/i/1000x1000/04/09/user-icon-vector-5770409.jpg', 2);
INSERT INTO user_userimage(image, customer_id) VALUES('https://cdn5.vectorstock.com/i/1000x1000/04/09/user-icon-vector-5770409.jpg', 3);
INSERT INTO user_userimage(image, customer_id) VALUES('https://cdn5.vectorstock.com/i/1000x1000/04/09/user-icon-vector-5770409.jpg', 4);

INSERT INTO user_admin(user_id_id) VALUES(1);
INSERT INTO user_admin(user_id_id) VALUES(2);
INSERT INTO user_admin(user_id_id) VALUES(3);
INSERT INTO user_admin(user_id_id) VALUES(4);

INSERT INTO user_profile(user_id_id) VALUES(5);
INSERT INTO user_profile(user_id_id) VALUES(5);
INSERT INTO user_profile(user_id_id) VALUES(6);
INSERT INTO user_profile(user_id_id) VALUES(7);
