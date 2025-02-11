import mysql.connector
import os
import pandas as pd

class db_operations():

    # constructor with connection path to DB
    def __init__(self):
        # self.connection = mysql.connector.connect(host=os.getenv("MYSQL_HOST"), 
        #                                user=os.getenv("MYSQL_USERNAME"), 
        #                                password=os.getenv("MYSQL_PASSWORD"),
        #                                auth_plugin="mysql_native_password",
        #                                database="RideShare" )
        self.connection = mysql.connector.connect(host="localhost", 
                                       user="root", 
                                       password="CPSC408!",
                                       auth_plugin="mysql_native_password",
                                       database="UniStats" )
        # print(self.connection)
        # print("connection made...")
        self.cur_obj = self.connection.cursor()
        self.login_check = False

    # create students table
    def create_students_table(self):
        query = '''
        CREATE TABLE students(
            student_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            first_name VARCHAR(20) NOT NULL,
            last_name VARCHAR(20) NOT NULL,
            state_id INTEGER,
            FOREIGN KEY (state_id) REFERENCES states(state_id),
            gender VARCHAR(15),
            international BOOLEAN,
            gpa FLOAT,
            test VARCHAR(5),
            test_score INTEGER,
            high_school INTEGER,
            FOREIGN KEY (high_school) REFERENCES schools(school_id)
        );
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("Students Table Created")

    # create states table
    def create_states_table(self):
        query = '''
        CREATE TABLE states(
            state_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            state_abb VARCHAR(3),
            state_name VARCHAR(30)
        )
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("States Table Created")

    
    # create schools table (that inlucde both high schools and universities)
    def create_schoools_table(self):
        query = '''
        CREATE TABLE schools(
            school_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            school_name VARCHAR(50) NOT NULL,
            state_id INTEGER,
            FOREIGN KEY (state_id) REFERENCES states(state_id),
            level VARCHAR(15)
        )
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("Schools Table Created")

    # create schools table (that inlucde both high schools and universities)
    def create_majors_table(self):
        query = '''
        CREATE TABLE majors(
            major_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            major_name VARCHAR(50)
        )
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("Majors Table Created")

    def create_acitivites_table(self):
        query = '''
        CREATE TABLE activities(
            activity_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            activitiy_name VARCHAR(30)
        )
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("Activities Table Created")

    def create_decision_records_table(self):
        query = '''
        CREATE TABLE decision_records(
            decision_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            school_id INTEGER,
            FOREIGN KEY (school_id) REFERENCES schools(school_id),
            major_id INTEGER,
            FOREIGN KEY (major_id) REFERENCES majors(major_id),
            year YEAR,
            status VARCHAR(15),
            comment VARCHAR(50)
        )
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("Decision Records Table Created")

    def create_activity_records_table(self):
        query = '''
        CREATE TABLE activity_records(
            activity_record_id INTEGER NOT NULL PRIMARY KEY AUTO_INCREMENT,
            student_id INTEGER,
            FOREIGN KEY (student_id) REFERENCES students(student_id),
            activity_id INTEGER,
            FOREIGN KEY (activity_id) REFERENCES activities(activity_id),
        )
        '''
        self.cur_obj.execute(query)
        self.connection.commit()
        print("Activity Records Table Created")

    # function to simply execute a DDL or DML query.
    # commits query, returns no results. 
    # best used for insert/update/delete queries with no parameters
    def modify_query(self, query):
        self.cur_obj.execute(query)
        self.connection.commit()

    # function to simply execute a DDL or DML query with parameters
    # commits query, returns no results. 
    # best used for insert/update/delete queries with named placeholders
    def modify_query_params(self, query, dictionary):
        self.cur_obj.execute(query, dictionary)
        self.connection.commit()

    # function to simply execute a DQL query
    # does not commit, returns results
    # best used for select queries with no parameters
    def select_query(self, query):
        result = self.cur_obj.execute(query)
        return self.cur_obj.fetchall()
    
    # function to simply execute a DQL query with parameters
    # does not commit, returns results
    # best used for select queries with named placeholders
    def select_query_params(self, query, dictionary):
        result = self.cur_obj.execute(query, dictionary)
        return self.cur_obj.fetchall()

    # function to return the value of the first row's 
    # first attribute of some select query.
    # best used for querying a single aggregate select 
    # query with no parameters
    def single_record(self, query):
        self.cur_obj.execute(query)
        return self.cur_obj.fetchone()[0]
    
    # function to return the value of the first row's 
    # first attribute of some select query.
    # best used for querying a single aggregate select 
    # query with named placeholders
    def single_record_params(self, query, dictionary):
        self.cur_obj.execute(query, dictionary)
        return self.cur_obj.fetchone()[0]
    
    # function to return a single attribute for all records 
    # from some table.
    # best used for select statements with no parameters
    def single_attribute(self, query):
        self.cur_obj.execute(query)
        results = self.cur_obj.fetchall()
        results = [i[0] for i in results]
        results.remove(None)
        return results
    
    # function to return a single attribute for all records 
    # from some table.
    # best used for select statements with named placeholders
    def single_attribute_params(self, query, dictionary):
        self.cur_obj.execute(query,dictionary)
        results = self.cur_obj.fetchall()
        results = [i[0] for i in results]
        return results
    
    # function for bulk inserting records
    # best used for inserting many records with parameters
    def bulk_insert(self, query, data):
        self.cur_obj.executemany(query, data)
        self.connection.commit()
    
    def get_all_users(self):
        query = '''
        SELECT student_id, last_name
        FROM students
        '''
        results = self.select_query(query)
        user_names = [str(row[0]) for row in results]
        user_ids = [row[0] for row in results]
        passwords = [row[1] for row in results]   
        return user_names, user_ids, passwords
        
    def search_state_id(self, input_state):
        query = '''
        SELECT state_id
        FROM states
        WHERE state_name =%s;'''
        records = (input_state,)
        results = self.select_query_params(query, records)
        return results
    
    def search_state(self, input_state):
        query = '''
        SELECT state_name
        FROM states
        WHERE state_id =%s;'''
        records = (input_state,)
        results = self.select_query_params(query, records)
        return results

    def create_user(self, user_input):
        # insert statement
        query = '''
        INSERT INTO students(first_name, last_name, state_id, gender, international)
        VALUES(%s,%s,%s,%s,%s)
        ''' 
        self.modify_query_params(query, user_input)
        # another query find the user id
        # this will query the largest id - which is also the most current one due to auto increment
        query = '''
        SELECT MAX(student_id) 
        FROM students
        ''' 
        results = self.select_query(query)
        return results[0][0]
    # For create user, might need to:
    #   function to query state_id given the state_name
    #   function to query school_id given the school_name 
    
    def view_all_decisions(self):
        query = '''
        SELECT CONCAT(stu.first_name, ' ', stu.last_name) AS full_name,
            uni.school_name AS university_name, major.major_name AS major, decision.year, decision.status, stu.gpa,
            stu.test, stu.test_score, stu.international, hs.school_name AS high_school_name,
            GROUP_CONCAT(DISTINCT act.activity_name ORDER BY act.activity_name SEPARATOR ', ') AS activities,
            decision.comment AS decision_comments
        FROM students AS stu
        INNER JOIN decision_records AS decision
            ON stu.student_id = decision.student_id
        INNER JOIN majors AS major
            ON decision.major_id = major.major_id
        INNER JOIN schools AS uni
            ON decision.school_id = uni.school_id
        LEFT JOIN schools AS hs
            ON stu.high_school = hs.school_id
        LEFT JOIN activity_records AS actrec
            ON stu.student_id = actrec.student_id
        LEFT JOIN activities AS act
            ON actrec.activity_id = act.activity_id
        GROUP BY stu.first_name, stu.last_name, uni.school_name, major.major_name, decision.year,
                decision.status, stu.gpa, stu.test, stu.test_score, stu.international, hs.school_name,
                decision.comment;
        '''
        results = self.select_query(query)
        df = pd.DataFrame(results)
        df.columns = ['name','university','major','year','status','gpa','test','test score','international','high school', 'activities', 'comment']
        return df
    
    def create_view_all_decisions1(self):
        # query to create view
        query = '''
        CREATE VIEW all_decisions1 AS
        SELECT
            CONCAT(stu.first_name, ' ', stu.last_name) AS full_name,
            uni.school_name AS university_name,
            major.major_name AS major,
            decision.year,
            decision.status,
            states.state_name AS from_state,
            stu.gpa,
            stu.test,
            stu.test_score,
            CASE stu.international
                WHEN 1 THEN 'Yes'
                ELSE 'No'
            END AS international,
            hs.school_name AS high_school_name,
            GROUP_CONCAT(DISTINCT act.activity_name ORDER BY act.activity_name SEPARATOR ', ') AS activities,
            decision.comment AS decision_comments
        FROM students AS stu
        INNER JOIN decision_records AS decision ON stu.student_id = decision.student_id
        INNER JOIN majors AS major ON decision.major_id = major.major_id
        INNER JOIN schools AS uni ON decision.school_id = uni.school_id
        INNER JOIN states ON stu.state_id = states.state_id
        LEFT JOIN schools AS hs ON stu.high_school = hs.school_id
        LEFT JOIN activity_records AS actrec ON stu.student_id = actrec.student_id
        LEFT JOIN activities AS act ON actrec.activity_id = act.activity_id
        GROUP BY
            stu.first_name,
            stu.last_name,
            uni.school_name,
            major.major_name,
            decision.year,
            decision.status,
            states.state_name
            stu.gpa,
            stu.test,
            stu.test_score,
            stu.international,
            hs.school_name,
            decision.comment;
        '''
        self.modify_query(query)
    
    def create_view_all_decisions2(self):
        # query to create view for filtering use
        query = '''
        CREATE VIEW all_decisions AS
        SELECT
            decision.decision_id,
            CONCAT(stu.first_name, ' ', stu.last_name) AS full_name,
            uni.school_name AS university_name,
            major.major_name AS major,
            decision.year,
            decision.status,
            states.state_name AS from_state,
            stu.gpa,
            stu.test,
            stu.test_score,
            CASE stu.international
                WHEN 1 THEN 'Yes'
                ELSE 'No'
            END AS international,
            hs.school_name AS high_school_name,
            GROUP_CONCAT(DISTINCT act.activity_name ORDER BY act.activity_name SEPARATOR ', ') AS activities,
            decision.comment AS decision_comments
        FROM students AS stu
        INNER JOIN decision_records AS decision ON stu.student_id = decision.student_id
        INNER JOIN majors AS major ON decision.major_id = major.major_id
        INNER JOIN schools AS uni ON decision.school_id = uni.school_id
        INNER JOIN states ON stu.state_id = states.state_id
        LEFT JOIN schools AS hs ON stu.high_school = hs.school_id
        LEFT JOIN activity_records AS actrec ON stu.student_id = actrec.student_id
        LEFT JOIN activities AS act ON actrec.activity_id = act.activity_id
        GROUP BY
            decision.decision_id,
            stu.first_name,
            stu.last_name,
            uni.school_name,
            major.major_name,
            decision.year,
            decision.status,
            states.state_name,
            stu.gpa,
            stu.test,
            stu.test_score,
            stu.international,
            hs.school_name,
            decision.comment;
        '''
        self.modify_query(query)
    
    def view_all_decisions1_table(self):
        # query to see this virtual table
        query = '''
        SELECT * FROM
        all_decisions1
        '''
        results = self.select_query(query)
        df = pd.DataFrame(results)
        df.columns = ['name','university','major','year','status', 'from', 'gpa','test','test score','international?','high school', 'activities', 'comment']
        return df

    def add_activity_record(self, user_input):
        # insert statment
        query = '''
        INSERT INTO activity_records(student_id, activity_id)
        VALUES(%s,%s);
        '''
        self.modify_query_params(query,user_input)

    def delete_activity_record(self, user_input):
        # delete statement
        query = '''
        DELETE FROM activity_records 
        WHERE student_id=%s AND activity_id=%s;
        '''
        self.modify_query_params(query,user_input)

    def post_decision(self, user_input):
        # insert statement
        query = '''
        INSERT INTO decision_records(student_id, school_id, major_id, year, status, comment)
        VALUES(%s,%s,%s,%s,%s,%s);
        '''
        self.modify_query_params(query,user_input)

    def add_school(self, user_input):
        # insert statement
        query = '''
        INSERT INTO schools(school_name)
        VALUES(%s);
        '''
        self.modify_query_params(query,user_input)
    
    def add_major(self, user_input):
        # insert statement
        query = '''
        INSERT INTO majors(major_name)
        VALUES(%s);
        '''
        self.modify_query_params(query,user_input)

    def check_major(self, user_input):
        query = '''
        SELECT * 
        FROM majors
        WHERE major_name=%s;
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        if len(results) == 0:
            return False
        else:
            return True
        
    def search_major_id(self, user_input):
        query = '''
        SELECT major_id
        FROM majors
        WHERE major_name =%s;
        '''
        results = self.select_query_params(query, user_input)
        return results
    
    def get_all_colleges(self):
        query = '''
        SELECT school_name 
        FROM schools
        WHERE level='University';
        '''
        results = self.select_query(query)
        college_list = [result[0] for result in results]
        return college_list
    
    def get_all_highschools(self):
        query = '''
        SELECT school_name 
        FROM schools
        WHERE level='High school';
        '''
        results = self.select_query(query)
        highschool_list = [result[0] for result in results]
        return highschool_list
    
    def get_all_majors(self):
        query = '''
        SELECT major_name 
        FROM majors;
        '''
        results = self.select_query(query)
        major_list = [result[0] for result in results]
        return major_list
    
    def get_all_years(self):
        query = '''
        SELECT DISTINCT(year)
        FROM decision_records;
        '''
        results = self.select_query(query)
        year_list = [result[0] for result in results]
        return year_list
    
    def get_all_activities(self):
        query = '''
        SELECT activity_name
        FROM activities;
        '''
        results = self.select_query(query)
        activity_list = [result[0] for result in results]
        return activity_list
    
    def get_user_all_activities(self, user_input):
        query = '''
        SELECT a.activity_name
        FROM activity_records ar LEFT JOIN activities a
        ON a.activity_id = ar.activity_id
        WHERE ar.student_id = %s;
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        user_activity_list = [result[0] for result in results]
        return user_activity_list
    
    def get_user_activities(self, user_input):
        query = '''
        SELECT a.activity_name
        FROM activity_records ar LEFT JOIN activities a
        ON a.activity_id = ar.activity_id
        WHERE ar.student_id = %s;
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        if len(results)==0:
            return False
        elif len(results)!=0:
            df = pd.DataFrame(results)
            df.columns = ['activity']
            return df
        
    
    def get_user_decisions2(self, user_input):
        query = '''
        SELECT s.school_name, m.major_name, d.year, d.status, d.comment FROM decision_records d
        LEFT JOIN schools s on s.school_id = d.school_id
        LEFT JOIN majors m on m.major_id = d.major_id
        WHERE student_id =%s ;
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        if len(results)==0:
            return False
        elif len(results)!=0:
            df = pd.DataFrame(results)
            df.columns = ['university','major','year','status', 'comment']
            return df
        
    def get_user_all_decisions(self, user_input):
        query = '''
        SELECT s.school_name FROM decision_records d
        LEFT JOIN schools s on s.school_id = d.school_id
        LEFT JOIN majors m on m.major_id = d.major_id
        WHERE student_id =%s;
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        user_decision_school_list = [result[0] for result in results]
        return user_decision_school_list
    
    def delete_decision_record(self,user_input):
        # delete statement
        query = '''
        DELETE FROM decision_records
        WHERE student_id=%s AND school_id=%s;
        '''
        self.modify_query_params(query,user_input)
        
    def get_user_decisions(self, user_input):
        query = '''
        SELECT CONCAT(stu.first_name, ' ', stu.last_name) AS full_name,
            uni.school_name AS university_name, major.major_name AS major, decision.status, stu.gpa,
            stu.test, stu.test_score, stu.international, hs.school_name AS high_school_name,
            GROUP_CONCAT(DISTINCT act.activity_name ORDER BY act.activity_name SEPARATOR ', ') AS activities,
            decision.comment AS decision_comments
        FROM students AS stu
        INNER JOIN decision_records AS decision
            ON stu.student_id = decision.student_id
        INNER JOIN majors AS major
            ON decision.major_id = major.major_id
        INNER JOIN schools AS uni
            ON decision.school_id = uni.school_id
        LEFT JOIN schools AS hs
            ON stu.high_school = hs.school_id
        LEFT JOIN activity_records AS actrec
            ON stu.student_id = actrec.student_id
        LEFT JOIN activities AS act
            ON actrec.activity_id = act.activity_id
        WHERE stu.student_id =%s
        GROUP BY stu.first_name, stu.last_name, uni.school_name, major.major_name,
                decision.status, stu.gpa, stu.test, stu.test_score, stu.international, hs.school_name,
                decision.comment;
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        if len(results)==0:
            return False
        elif len(results)!=0:
            df = pd.DataFrame(results)
            df.columns = ['name','university','major','status','gpa','test','test score','international','high school', 'activities', 'comment']
            return df
        
    def check_school(self, user_input):
        query = '''
        SELECT * 
        FROM schools
        WHERE school_name=%s
        '''
        records = (user_input)
        results = self.select_query_params(query, records)
        if len(results) == 0:
            return False
        else:
            return True

    def search_school_id(self, input_school):
        query = '''
        SELECT school_id
        FROM schools
        WHERE school_name =%s;'''
        results = self.select_query_params(query, input_school)
        return results
    
    def search_school(self, input_school):
        query = '''
        SELECT school_name
        FROM schools
        WHERE school_id =%s;'''
        results = self.select_query_params(query, input_school)
        return results
    
    def search_activity_id(self, input_activity):
        query = '''
        SELECT activity_id
        FROM activities
        WHERE activity_name =%s;'''
        results = self.select_query_params(query, input_activity)
        return results
    
    def update_first_name(self, user_input):
        query = '''
        UPDATE students
        SET first_name =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_last_name(self, user_input):
        query = '''
        UPDATE students
        SET last_name =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_state(self, user_input):
        query = '''
        UPDATE students
        SET state_id =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_gender(self, user_input):
        query = '''
        UPDATE students
        SET gender =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_international(self, user_input):
        query = '''
        UPDATE students
        SET international =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_gpa(self, user_input):
        query = '''
        UPDATE students
        SET gpa =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_test(self, user_input):
        query = '''
        UPDATE students
        SET test =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_test_score(self, user_input):
        query = '''
        UPDATE students
        SET test_score =%s
        WHERE student_id = %s;
        '''
        self.modify_query_params(query, user_input)

    def update_highschool(self, user_input):
        query = '''
        UPDATE students
        SET high_school =%s
        WHERE student_id =%s;
        '''
        self.modify_query_params(query, user_input)

    def add_university(self, user_input):
        query = '''
        INSERT INTO schools(school_name, state_id, level)
        VALUES (%s,%s,'University')
        '''
        self.modify_query_params(query, user_input)
    
    def add_high_school(self, user_input):
        query = '''
        INSERT INTO schools(school_name, state_id, level)
        VALUES (%s,%s,'High school')
        '''
        self.modify_query_params(query, user_input)

    def add_major(self, user_input):
        query = '''
        INSERT INTO majors(major_name)
        VALUES (%s)
        '''
        self.modify_query_params(query, user_input)
    
    def add_activity(self, user_input):
        query = '''
        INSERT INTO activities(activity_name)
        VALUES (%s)
        '''
        self.modify_query_params(query, user_input)

    def get_user_info(self, user_input):
        query = '''
        SELECT * 
        FROM students
        WHERE student_id =%s
        '''
        results = self.select_query_params(query, user_input)
        return results[0]

    def add_university_transactions(self, user_input):
        query = '''
        CALL university_check(%s, %s, @if_exist);
        '''
        self.modify_query_params(query, user_input)
        self.connection.commit()
    
    def add_highschool_transactions(self, user_input):
        query = '''
        CALL highschool_check(%s, %s, @if_exist);
        '''
        self.modify_query_params(query, user_input)
        self.connection.commit()

    def check_school(self):
        query = '''
        SELECT @if_exist
        '''
        results = self.select_query(query)
        return results
    
    def add_major_transactions(self, user_input):
        query = '''
        CALL major_check(%s, @if_exist);
        '''
        self.modify_query_params(query, user_input)
        self.connection.commit()

    def check_major(self):
        query = '''
        SELECT @if_exist
        '''
        results = self.select_query(query)
        return results
    
    def add_activity_transactions(self, user_input):
        query = '''
        CALL activity_check(%s, @if_exist);
        '''
        self.modify_query_params(query, user_input)
        self.connection.commit()

    def check_activity(self):
        query = '''
        SELECT @if_exist
        '''
        results = self.select_query(query)
        return results
    
    def specific_decisions_filter_activity(self, decision_input):
        query = '''
        SELECT full_name, university_name, major, year, status, from_state, gpa, test, test_score, international, high_school_name, activities, decision_comments
        FROM all_decisions2
        WHERE decision_id IN''' + decision_input + ";"
        results = self.select_query(query)
        df = pd.DataFrame(results)
        df.columns = ['name','university','major','year','status','from','gpa','test','test score','international','high school', 'activities', 'comment']
        return df
    
    def specific_decisions_filter_state(self, decision_input):
        query = '''
        SELECT full_name, university_name, major, year, status, from_state, gpa, test, test_score, international, high_school_name, activities, decision_comments 
        FROM all_decisions2
        WHERE decision_id IN''' + decision_input + ";"
        results = self.select_query(query)
        df = pd.DataFrame(results)
        df.columns = ['name','university','major','year','status','from','gpa','test','test score','international','high school', 'activities', 'comment']
        return df
    
    def filter_activity(self, user_input):
        query = '''
        SELECT decision_id
        FROM decision_records
        WHERE student_id IN (SELECT student_id
                            FROM activity_records
                            WHERE activity_id IN (SELECT activity_id
                                                  FROM activities
                                                  WHERE activity_name = %s));
        '''
        user_input = (user_input,)
        results = self.select_query_params(query, user_input)
        if len(results) == 0:
            return False
        else:
            decision_ids = '(' + ','.join(str(result[0]) for result in results) + ')'
            return decision_ids
    
    def filter_state(self, user_input):
        query = '''
        SELECT decision_id
        FROM decision_records
        WHERE student_id IN (SELECT student_id
                            FROM students
                            WHERE state_id IN (SELECT state_id
                                                  FROM states
                                                  WHERE state_name = %s
                                                        ));
        '''
        user_input = (user_input,)
        results = self.select_query_params(query, user_input)
        if len(results) == 0:
            return False
        else:
            decision_ids = '(' + ','.join(str(result[0]) for result in results) + ')'
            return decision_ids
        
    def view_stats(self):
        query = '''
        SELECT university_name, status,  COALESCE(ROUND(AVG(gpa),3), 'n/a') AS avg_gpa, COUNT(*) AS student_count
        FROM all_decisions1
        GROUP BY university_name, status
        ORDER BY university_name, status ASC;
        '''
        results = self.select_query(query)
        df = pd.DataFrame(results)
        df.columns = ['university','status','average gpa','student count']
        return df
    
    def open_cursor(self):
        self.cur_obj.cursor()
   
    def close_cursor(self):
        self.cur_obj.close()

    # destructor that closes connection with DB
    def destructor(self):
        self.cur_obj.close()
        self.connection.close()




