import sqlite3

def create():
    conn = sqlite3.connect('survey_test.db') 
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql = '''CREATE TABLE short_survey (
            "name"  VARCHAR,
            "age"   VARCHAR,
            "gender"    VARCHAR,
            "self_emp"  VARCHAR
            )'''

    cursor.execute(sql)

    conn.commit()
    conn.close()

def create1():
    conn = sqlite3.connect('mental_survey.db') 
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")
    
    sql='''CREATE TABLE "mh_survey" (
        "self_empl_flag"	INTEGER,
        "tech_comp_flag"	INTEGER,
        "mh_coverage_flag"	VARCHAR,
        "mh_employer_discussion"	VARCHAR,
        "mh_resources_provided"	VARCHAR,
        "mh_anonimity_flag"	VARCHAR,
        "mh_medical_leave"	VARCHAR,
        "mh_discussion_neg_impact"	VARCHAR,
        "mh_discussion_cowork"	VARCHAR,
        "mh_discussion_supervis"	VARCHAR,
        "mh_conseq_coworkers"	VARCHAR,
        "mh_hurt_on_career"	VARCHAR,
        "mh_neg_view_cowork"	VARCHAR,
        "mh_bad_response_workplace"	VARCHAR,
        "mh_family_hist"	VARCHAR,
        "mh_disorder_past"	VARCHAR,
        "mh_disorder_current"	VARCHAR,
        "mh_diagnos_proffesional"	VARCHAR,
        "mh_sought_proffes_treatm"	INTEGER,
        "mh_eff_treat_impact_on_work"	VARCHAR,
        "mh_not_eff_treat_impact_on_work"	VARCHAR,
        "age"	INTEGER,
        "sex"	REAL,
        "country_live"	VARCHAR,
        "live_us_teritory"	VARCHAR,
        "country_work"	VARCHAR,
        "work_us_teritory"	VARCHAR,
        "work_position"	VARCHAR,
        "remote_flag"	VARCHAR,
    )'''
    cursor.execute(sql)

    conn.commit()
    conn.close()

def create3():
    conn = sqlite3.connect('depression.db') 
    cursor = conn.cursor()
    print("Database created and Successfully Connected to SQLite")

    sql = '''CREATE TABLE short_survey (
            "feel_down"  INTEGER,
            "litte_interest"   INTEGER,
            "bother_sleep"    INTEGER,
            "bother_tired"  INTEGER,
            "bother_apetite"    INTEGER,
            "bother_feelingbad"    INTEGER,
            "bother_concentrate"    INTEGER,
            "bother_moving"    INTEGER,
            "bother_anxiety"    INTEGER,
            "bother_nervous"    INTEGER,
            "bother_worry"    INTEGER,
            "bother_worry_things"    INTEGER,
            "bother_relax"    INTEGER,
            "bother_restless"    INTEGER,
            "bother_annoy"    INTEGER,
            "bother_afraid"    INTEGER
            )'''

    cursor.execute(sql)

    conn.commit()
    conn.close()


def insert_data(name,gender,self_emp):
    try:
        conn = sqlite3.connect('survey_test.db') 
        cursor = conn.cursor()
    
        insert = '''INSERT INTO short_survey(name,gender,self_emp) VALUES(?,?,?);'''

        data_tuple = (name,gender,self_emp)

        cursor.execute(insert, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into short_survey Table\n")
    
        conn.close()
    
    except conn.Error as error:
        print("Failed to insert Python variable into sqlite table\n", error)
    finally:
        if conn:
            conn.close()
            print("The conn connection is closed\n")



def insert_data2(self_empl_flag, tech_comp_flag, mh_coverage_flag, mh_employer_discussion, mh_resources_provided, mh_anonimity_flag, mh_medical_leave, mh_discussion_neg_impact, mh_discussion_cowork, mh_discussion_supervis, mh_conseq_coworkers, mh_hurt_on_career, mh_neg_view_cowork, mh_bad_response_workplace, mh_family_hist, mh_disorder_past, mh_disorder_current, mh_diagnos_proffesional, mh_sought_proffes_treatm, mh_eff_treat_impact_on_work, mh_not_eff_treat_impact_on_work, age, sex, country_live, live_us_teritory, country_work, work_us_teritory, work_position, remote_flag):
    try:
        conn = sqlite3.connect('survey.db') 
        cursor = conn.cursor()
    
        insert = '''INSERT INTO processed(self_empl_flag, tech_comp_flag, mh_coverage_flag, mh_employer_discussion, mh_resources_provided, mh_anonimity_flag, mh_medical_leave, mh_discussion_neg_impact, mh_discussion_cowork, mh_discussion_supervis, mh_conseq_coworkers, mh_hurt_on_career, mh_neg_view_cowork, mh_bad_response_workplace, mh_family_hist, mh_disorder_past, mh_disorder_current, mh_diagnos_proffesional, mh_sought_proffes_treatm, mh_eff_treat_impact_on_work, mh_not_eff_treat_impact_on_work, age, sex, country_live, live_us_teritory, country_work, work_us_teritory, work_position, remote_flag) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

        data_tuple = (self_empl_flag, tech_comp_flag, mh_coverage_flag, mh_employer_discussion, mh_resources_provided, mh_anonimity_flag, mh_medical_leave, mh_discussion_neg_impact, mh_discussion_cowork, mh_discussion_supervis, mh_conseq_coworkers, mh_hurt_on_career, mh_neg_view_cowork, mh_bad_response_workplace, mh_family_hist, mh_disorder_past, mh_disorder_current, mh_diagnos_proffesional, mh_sought_proffes_treatm, mh_eff_treat_impact_on_work, mh_not_eff_treat_impact_on_work, age, sex, country_live, live_us_teritory, country_work, work_us_teritory, work_position, remote_flag)

        cursor.execute(insert, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into processed Table\n")
    
        conn.close()
    
    except conn.Error as error:
        print("Failed to insert Python variable into sqlite table\n", error)
    finally:
        if conn:
            conn.close()
            print("The conn connection is closed\n")

def insert_data3(feel_down,litte_interest,bother_sleep,bother_tired,bother_apetite,bother_feelingbad,bother_concentrate,bother_moving,bother_anxiety,bother_nervous,bother_worry,bother_worry_things,bother_relax,bother_restless,bother_annoy,bother_afraid):
    try:
        conn = sqlite3.connect('depression.db') 
        cursor = conn.cursor()
    
        insert = '''INSERT INTO short_survey(feel_down,litte_interest,bother_sleep,bother_tired,bother_apetite,bother_feelingbad,bother_concentrate,bother_moving,bother_anxiety,bother_nervous,bother_worry,bother_worry_things,bother_relax,bother_restless,bother_annoy,bother_afraid) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?);'''

        data_tuple = (feel_down,litte_interest,bother_sleep,bother_tired,bother_apetite,bother_feelingbad,bother_concentrate,bother_moving,bother_anxiety,bother_nervous,bother_worry,bother_worry_things,bother_relax,bother_restless,bother_annoy,bother_afraid)

        cursor.execute(insert, data_tuple)
        conn.commit()
        print("Python Variables inserted successfully into short_survey Table\n")
    
        conn.close()
    
    except conn.Error as error:
        print("Failed to insert Python variable into sqlite table\n", error)
    finally:
        if conn:
            conn.close()
            print("The conn connection is closed\n")
# insert_data('Nitin','21','Male','No')
# create1()
# create3()