
USE SaltRock;

-- Populate Genre (15 records)
INSERT INTO Genre (genre_name) VALUES
('Rock'), ('Pop'), ('Jazz'), ('Classical'), ('Hip-Hop'),
('Electronic'), ('Country'), ('Reggae'), ('Blues'), ('Funk'),
('Metal'), ('R&B'), ('Soul'), ('Punk'), ('Folk');

-- Populate User (5 records)
INSERT INTO User (username, email) VALUES
('alice', 'alice@example.com'),
('bob', 'bob@example.com'),
('carol', 'carol@example.com'),
('dave', 'dave@example.com'),
('eve', 'eve@example.com');

-- Populate Venue (10 records)
INSERT INTO Venue (venue_name, max_fee) VALUES
('The Arena', 5000.00),
('Jazz Club', 2000.00),
('Rock Stadium', 8000.00),
('City Hall', 3000.00),
('Open Air', 4500.00),
('Underground', 1500.00),
('Festival Grounds', 10000.00),
('Acoustic Lounge', 1200.00),
('Grand Theater', 6000.00),
('Blues Bar', 1800.00);

-- Populate Act (24 records)
INSERT INTO Act (act_name, gig_rate, is_solo) VALUES
('The Rockers', 750.00, FALSE),
('Solo Star', 500.00, TRUE),
('Jazz Trio', 600.00, FALSE),
('Classical Quartet', 900.00, FALSE),
('HipHop Crew', 650.00, FALSE),
('Electro Beats', 550.00, FALSE),
('Country Duo', 400.00, FALSE),
('Reggae Vibes', 480.00, FALSE),
('Blues Band', 530.00, FALSE),
('Funk Masters', 720.00, FALSE),
('Metal Heads', 800.00, FALSE),
('R&B Singer', 580.00, TRUE),
('Soulful Voice', 620.00, TRUE),
('Punk Rockers', 700.00, FALSE),
('Folk Tales', 450.00, FALSE),
('Guitar Soloist', 520.00, TRUE),
('Drum Solo', 510.00, TRUE),
('Bass Solo', 500.00, TRUE),
('String Trio', 650.00, FALSE),
('Brass Ensemble', 670.00, FALSE),
('Synth Artist', 530.00, TRUE),
('DJ MixMaster', 560.00, TRUE),
('Pop Duo', 610.00, FALSE),
('Choral Group', 750.00, FALSE);

-- Populate Act_Member (35 records)
-- For simplicity, each act gets at least one member; solo acts get one, bands get multiple
INSERT INTO Act_Member (first_name, last_name, ACT_ID) VALUES
('John', 'Doe', 1), ('Jane', 'Smith', 2), ('Mike', 'Brown', 3),
('Anna', 'Taylor', 3), ('Paul', 'Wilson', 4), ('Sara', 'Lee', 4),
('Luke', 'Martin', 5), ('Emma', 'Clark', 6), ('Chris', 'Lewis', 6),
('Olivia', 'Walker', 7), ('Liam', 'Hall', 7), ('Noah', 'Allen', 8),
('Ava', 'Young', 8), ('Ethan', 'Hernandez', 9), ('Mia', 'King', 9),
('Logan', 'Wright', 10), ('Isabella', 'Lopez', 10), ('Mason', 'Hill', 11),
('Sophia', 'Scott', 11), ('James', 'Green', 12), ('Charlotte', 'Adams', 12),
('Benjamin', 'Baker', 13), ('Amelia', 'Nelson', 14), ('Elijah', 'Carter', 14),
('Harper', 'Mitchell', 15), ('Daniel', 'Perez', 15), ('Evelyn', 'Roberts', 16),
('Michael', 'Turner', 17), ('Abigail', 'Phillips', 17), ('Alexander', 'Campbell', 18),
('Ella', 'Parker', 19), ('Matthew', 'Evans', 19), ('Scarlett', 'Edwards', 20),
('David', 'Collins', 21), ('Victoria', 'Stewart', 21);

-- Populate Song (20 records)
INSERT INTO Song (title, length, year, lyrics, plays, ACT_ID) VALUES
('Rock Anthem', '00:03:50', 2020, 'We will rock you', 1500, 1),
('Pop Hit', '00:03:30', 2021, 'Dancing all night', 2000, 2),
('Jazz Improvisation', '00:05:20', 2019, 'Improvised lines', 800, 3),
('Classical Sonata', '00:07:10', 2018, 'Instrumental', 500, 4),
('HipHop Flow', '00:04:00', 2022, 'Flowing beats', 1200, 5),
('Electronic Beat', '00:04:30', 2021, 'Synth lines', 1100, 6),
('Country Roads', '00:03:45', 2019, 'Take me home', 900, 7),
('Reggae Rhythm', '00:04:15', 2020, 'One love', 1000, 8),
('Blues Express', '00:05:00', 2017, 'Bending notes', 700, 9),
('Funk Groove', '00:04:25', 2018, 'Funky beat', 850, 10),
('Metal Mayhem', '00:03:55', 2022, 'Heavy riffs', 950, 11),
('R&B Smooth', '00:03:40', 2021, 'Smooth vibes', 1050, 12),
('Soul Serenade', '00:04:05', 2020, 'Soulful tune', 1150, 13),
('Punk Anthem', '00:02:50', 2022, 'Fast and loud', 650, 14),
('Folk Ballad', '00:04:10', 2019, 'Storytelling', 600, 15),
('Guitar Solo', '00:03:20', 2021, 'Strumming', 550, 16),
('Drum Solo', '00:02:30', 2020, 'Percussion only', 500, 17),
('Bass Solo', '00:03:00', 2018, 'Bass lines', 480, 18),
('String Harmony', '00:05:30', 2017, 'Strings ensemble', 450, 19),
('Brass Blast', '00:04:45', 2022, 'Brass section', 430, 20);

-- Populate Act_Genre (link acts to genres)
INSERT INTO Act_Genre (ACT_ID, GENRE_ID) VALUES
(1,1),(1,10),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),
(10,10),(11,11),(12,12),(13,13),(14,14),(15,15),(16,2),(17,3),
(18,11),(19,4),(20,5),(21,6),(22,7),(23,2),(24,8);

-- Populate Song_Genre (link songs to genres)
INSERT INTO Song_Genre (SONG_ID, GENRE_ID) VALUES
(1,1),(2,2),(3,3),(4,4),(5,5),(6,6),(7,7),(8,8),(9,9),(10,10),
(11,11),(12,12),(13,13),(14,14),(15,15),(16,2),(17,3),(18,11),
(19,4),(20,6);

-- Populate Gig_Booking (2 records)
INSERT INTO Gig_Booking (ACT_ID, VENUE_ID, start_time, end_time) VALUES
(1,3,'20:00:00','23:00:00'),
(2,2,'18:30:00','20:00:00');
