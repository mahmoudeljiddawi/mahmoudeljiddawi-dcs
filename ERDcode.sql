CREATE TABLE Customer
(
  Client_id INT NOT NULL,
  Name VARCHAR(30) NOT NULL,
  Phone VARCHAR(20) NOT NULL,
  Address VARCHAR(50) NOT NULL,
  PRIMARY KEY (Client_id)
);

CREATE TABLE Employee
(
  Name VARCHAR(30) NOT NULL,
  Emp_id INT NOT NULL,
  PRIMARY KEY (Emp_id)
);

CREATE TABLE Organisation
(
  Name VARCHAR(30) NOT NULL,
  org_id INT NOT NULL,
  contact_mail VARCHAR(50) NOT NULL,
  PRIMARY KEY (org_id)
);

CREATE TABLE Document
(
  Doc_id INT NOT NULL,
  Type VARCHAR(15) NOT NULL,
  Copies INT NOT NULL,
  Status VARCHAR(20) NOT NULL,
  Receipt_date DATE,
  Receipt_number INT,
  Client_id INT NOT NULL,
  org_id INT NOT NULL,
  PRIMARY KEY (Doc_id),
  FOREIGN KEY (Client_id) REFERENCES Customer(Client_id),
  FOREIGN KEY (org_id) REFERENCES Organisation(org_id)
);

CREATE TABLE Traking_history
(
  TrackNumber INT NOT NULL,
  Action_order INT NOT NULL,
  Action_Taken VARCHAR(20) NOT NULL,
  Date DATE NOT NULL,
  Doc_id INT NOT NULL,
  PRIMARY KEY (TrackNumber, Action_order),
  FOREIGN KEY (Doc_id) REFERENCES Document(Doc_id)
);

CREATE TABLE recieve
(
  Doc_id INT NOT NULL,
  Emp_id INT NOT NULL,
  PRIMARY KEY (Doc_id, Emp_id),
  FOREIGN KEY (Doc_id) REFERENCES Document(Doc_id),
  FOREIGN KEY (Emp_id) REFERENCES Employee(Emp_id)
);

CREATE TABLE take_action
(
  Emp_id INT NOT NULL,
  TrackNumber INT NOT NULL,
  Action_order INT NOT NULL,
  PRIMARY KEY (Emp_id, TrackNumber, Action_order),
  FOREIGN KEY (Emp_id) REFERENCES Employee(Emp_id),
  FOREIGN KEY (TrackNumber, Action_order) REFERENCES Traking_history(TrackNumber, Action_order)
);