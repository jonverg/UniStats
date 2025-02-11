import streamlit as st
from db_operations import db_operations
import streamlit_authenticator as stauth

# options for states
states_options = [
        "Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut",
        "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa",
        "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan",
        "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire",
        "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma",
        "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee",
        "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming",
        "Outside of the US"]

# options for gender
gender_options = ["Male", "Female", "Transgender", "Non-binary", "Prefer not to say"]

# options for international
international_options = ["Yes", "No"]

# options for status
status_options = ["Accepted", "Rejected", "Waitlisted"]

# options for test
test_options = ["SAT", "ACT", "n/a"]

# options for school or major
school_major_activity_options = ["University", "High school", "Major", "Activity"]

# options for year
year_options = [2024,]

# options for filter
filter_options = ["State","Activity"]

# option for add or delete
record_action_options = ["Add an activity record", "Delete an activity record"]
decision_action_options = ["Add a decision record", "Delete a decision record"]

def home_page():
    st.title("UniStats")
    st.image("UniStats.png", width=50)
    st.write("### hello, use this site to search up and post college decisions!")
    st.markdown("""<div style="background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red); height: 1px;"></div>""",unsafe_allow_html=True)

def start_page():
    home_page()
    user_names, user_ids, passwords = db_ops.get_all_users()
    credentials = {"usernames":{}}      
    for user_name,user_id,password in zip(user_names,user_ids,passwords):
            user_dict = {"name": user_id, "password": password}
            credentials["usernames"].update({user_name: user_dict})
    authenticator = stauth.Authenticate(credentials, "hey", "cookie", cookie_expiry_days=30)
    name, authentication_status, username = authenticator.login("main")
    if authentication_status == False:
        st.error("uh-oh! your username or password is incorrect:(", icon="🚨")
        st.warning('''please note that your username is the assigned user id you received when signing up 
             & your password is your last name with first letter in uppercase!''', icon="⚠️")
        register_new_user()
    if authentication_status == None:
        st.warning('''please note that your username is the assigned user id you received when signing up 
             & your password is your last name with first letter in uppercase!''', icon="⚠️")
        register_new_user()
    if authentication_status == True:
        # st.success("succesfully logged in! select from the side menu on the left to conitnue:)")
        select_option = st.sidebar.radio("select page", ["✨✅ view all decision records", "🤓🟩 filter decision records",
                                                         "📊👀 decision stats", 
                                                         "🤌💬 view/add/delete your decision records", "🏆🚶‍♂️ view/add/delete your activity records", 
                                                         "❗➕ add school/major/activity",
                                                         "✏️⚙️ put in/update your basic info", "❤️‍🔥🤍 support UniStats", 
                                                         "➡️📋 export reports","⚠️🔴 community guidelines"])
        if select_option == "✨✅ view all decision records":
            st.write("#### let's take a look at all the admission records ✨✅")
            st.dataframe(db_ops.view_all_decisions1_table())
        if select_option == "🤓🟩 filter decision records":
            st.write("#### let's filter the records and take a look at them  🤓🟩")
            filter_decisions()
        if select_option == "📊👀 decision stats":
            st.write("#### let's take a look at some stats  📊👀")
            view_stats()
        if select_option == "🤌💬 view/add/delete your decision records":
            st.write("#### let's take a look at all your decision records 🤌💬")
            view_decision_records2(username)
            refresh_button = st.button("Refresh page")
            if refresh_button: 
                st.rerun()
            st.markdown("---")
            st.write("#### let's add/delete your decision records  🤌💬")
            user_input_decision_action = st.selectbox("What do you want to do?", [""]+decision_action_options)
            if user_input_decision_action == "Add a decision record":
                post_decision_form(username)
            if user_input_decision_action == "Delete a decision record":
                delete_decision_record_form(username)
        if select_option == "❗➕ add school/major/activity":
            st.write("#### sorry that we don't have all info in the system! let's add a/an school/major/activity ❗➕")
            add_info_form()
        if select_option == "🏆🚶‍♂️ view/add/delete your activity records":
            st.write("#### let's take a look at all your activity records  🏆🚶‍♂️")
            view_activity_records(username)
            refresh_button = st.button("Refresh page")
            if refresh_button: 
                st.rerun()
            st.markdown("---")
            st.write("#### let's add/delete your activity records  🏆🚶‍♂️")
            user_input_record_action = st.selectbox("What do you want to do?", [""]+record_action_options)
            if user_input_record_action == "Add an activity record":
                add_activity_record_form(username)
            if user_input_record_action == "Delete an activity record":
                delete_activity_record_form(username)
        if select_option == "✏️⚙️ put in/update your basic info":
            st.write("#### let's put in/update your info ✏️⚙️")
            st.write("#### your username is:", username, "(this is default and cannot be altered)")
            update_info_form(username)
        if select_option == "❤️‍🔥🤍 support UniStats":
            # st.write("#### let's contact UniStats  ❤️‍🔥🤍")
            # contact_form(user_id)
            # st.write("")
            st.write("#### let's support UniStats (we also don't mind some tips)  ❤️‍🔥🤍")
            st.image("donate_venmo.jpg", caption="yes, this is our venmo.🤑    ", width=300)
        if select_option == "➡️📋 export reports":
            st.write("#### let's export reports  ➡️📋")
            export_reports(username)
        if select_option == "⚠️🔴 community guidelines":
            st.write("#### let's be respectful  ⚠️🔴")
            st.markdown("- be honest and accurate.")
            st.markdown("- don't share sensitive personal information.")
            st.markdown("- avoid irrelevant or inappropriate content.")
            st.write("")
            st.image("corgi.gif", width=200)
        for i in range(30):
            st.sidebar.write(" ")
        authenticator.logout("logout","sidebar")

def filter_decisions():
    # filter_form = st.form("Filter")
    to_filter = st.selectbox("What do you want to filter?",[""]+filter_options)
    if to_filter == "Activity":
        activity_filter = st.selectbox("Filter activity", [""]+db_ops.get_all_activities())
        decision_ids = db_ops.filter_activity(activity_filter)
        if len(activity_filter)!= 0 and decision_ids == False:
            st.warning("no matching records. try other activities.",icon="⚠️")
        elif len(activity_filter)!= 0 and type(decision_ids)!= False:
            st.dataframe(db_ops.specific_decisions_filter_activity(decision_ids))
    elif to_filter == "State":
        state_filter = st.selectbox("Filter state", [""]+states_options)
        decision_ids = db_ops.filter_state(state_filter)
        if len(state_filter)!= 0 and decision_ids == False:
            st.warning("no matching records. try other states.",icon="⚠️")
        elif len(state_filter)!= 0 and type(decision_ids)!= False:
            st.dataframe(db_ops.specific_decisions_filter_state(decision_ids))

def view_stats():
    st.dataframe(db_ops.view_stats())
    st.warning("if gpa is 'None' that means we don't have ",icon="⚠️")

# function to process user input. just in case they don't capitalize the first letter
def capitalize_each_word(text):
    words = text.split()
    capitalized_words = [word.capitalize() for word in words]
    return " ".join(capitalized_words)

def contact_form(user_id):
    contact_form = st.form("Contact us")
    contact_form.write("#### write us something and we will get back to you-")
    user_input_comment = contact_form.text_input("Comment","")
    user_input_email = contact_form.text_input("Email","")
    post_contact = contact_form.form_submit_button("Contact us")
    # maybe a database with all the message store??

def add_info_form():
    user_input_add = st.selectbox("Which one do you want to add?",[""] +school_major_activity_options)
    if user_input_add == "University":
        add_university_form()
    if user_input_add == "High school":
        add_high_school_form()
    if user_input_add == "Major":
        add_major_form()
    if user_input_add == "Activity":
        add_activity_form()

def add_university_form():
    add_form = st.form("Add university")
    add_form.write("#### add an university")
    user_input_add = add_form.text_input("University name","")
    user_input_state = add_form.selectbox('''State''', [""]+ states_options)
    add_button = add_form.form_submit_button("Add university to the system")
    st.warning("please follow the community guidelines.", icon="⚠️")
    if add_button and user_input_add!="" and user_input_state!="":
        user_input_add = capitalize_each_word(user_input_add)
        user_input_info = (user_input_state, user_input_add)
        db_ops.add_university_transactions(user_input_info)
        results = db_ops.check_school()
        if results[0][0] == 2:
            st.error("university is already in the system!", icon="🚨")
        elif results[0][0] == 1:
            st.success("university added! it should be in the system now.", icon="👍")

def add_high_school_form():
    add_form = st.form("Add high school")
    add_form.write("#### add a high school")
    user_input_add = add_form.text_input("High school name","")
    user_input_state = add_form.selectbox('''State''', [""]+ states_options)
    add_button = add_form.form_submit_button("Add high school to the system")
    st.warning("please follow the community guidelines.", icon="⚠️")
    if add_button and user_input_add!="" and user_input_state!="":
        user_input_add = capitalize_each_word(user_input_add)
        user_input_info = (user_input_state, user_input_add)
        db_ops.add_highschool_transactions(user_input_info)
        results = db_ops.check_school()
        if results[0][0] == 2:
            st.error("high school is already in the system!", icon="🚨")
        elif results[0][0] == 1:
            st.success("high school added! it should be in the system now.", icon="👍")

def add_major_form():
    add_form = st.form("Add major")
    add_form.write("#### add a major")
    user_input_add = add_form.text_input("Major name","")
    add_button = add_form.form_submit_button("Add major to the system")
    st.warning("please follow the community guidelines.", icon="⚠️")
    if add_button and user_input_add!="":
        user_input_add = capitalize_each_word(user_input_add)
        user_input_info = (user_input_add,)
        db_ops.add_major_transactions(user_input_info)
        results = db_ops.check_major()
        if results[0][0] == 2:
            st.error("major is already in the system!", icon="🚨")
        elif results[0][0] == 1:
            st.success("major added! it should be in the system now.", icon="👍")

def add_activity_form():
    add_form = st.form("Add activity")
    add_form.write("#### add an activity")
    user_input_add = add_form.text_input("Activity name","")
    add_button = add_form.form_submit_button("Add activity to the system")
    st.warning("please follow the community guidelines.", icon="⚠️")
    if add_button and user_input_add!="":
        user_input_add = capitalize_each_word(user_input_add)
        user_input_info = (user_input_add,)
        db_ops.add_activity_transactions(user_input_info)
        results = db_ops.check_activity()
        if results[0][0] == 2:
            st.error("activity is already in the system!", icon="🚨")
        elif results[0][0] == 1:
            st.success("activity added! it should be in the system now.", icon="👍")

def post_decision_form(user_id):
    decision_form = st.form("My decision")
    decision_form.write("#### add a decision record")
    user_input_id = int(user_id)
    user_input_college = decision_form.selectbox("College",[""]+ db_ops.get_all_colleges())
    # user_input_college = decision_form.text_input("College","")
    user_input_major = decision_form.selectbox("Major",[""]+ db_ops.get_all_majors())
    # user_input_major = decision_form.text_input("Major","")
    user_input_year = decision_form.selectbox("Year",[""]+ year_options)
    user_input_status = decision_form.selectbox("Status",[""]+ status_options)
    user_input_comment = decision_form.text_input("Comment (optional)","")
    post_decision = decision_form.form_submit_button("Add to my decision")
    # decision_form.write("by adding, your decision record will be available to view for others as well.")
    st.warning("if the university or the major is not recorded in the system. use '❗➕ add school/major/activity' on the side menu to add.", icon="⚠️")
    st.warning("please follow the guidelines.", icon="⚠️")
    user_input_college = (user_input_college,)
    user_input_major = (user_input_major,)
    if post_decision and len(user_input_college)>0 and len(user_input_major)>0 and len(str(user_input_year))>0 and len(user_input_status)>0:
        user_input_college_id = db_ops.search_school_id(user_input_college)[0][0]
        user_input_major_id = db_ops.search_major_id(user_input_major)[0][0]
        if len(user_input_comment) == 0:
            user_input_comment = None
        user_input_decision = (user_input_id, user_input_college_id, user_input_major_id, user_input_year, user_input_status, user_input_comment)
        db_ops.post_decision(user_input_decision)
        st.success("decision added! please hit 'Refresh page' for new update.", icon="👍")
        # st.rerun()
    # if post_decision and len(user_input_college)>0 and len(user_input_major)>0 and len(user_input_status)>0:
    #     if len(user_input_comment) == 0:
    #         user_input_comment = None
    #     if db_ops.check_school(user_input_college) == False:
    #         decision_form.error("school not recorded in the system. add it using the side menu.")
    #     if db_ops.check_major(user_input_major) == False:    
    #         decision_form.error("major not recorded in the system. add it using the side menu.")
    #     if db_ops.check_school(user_input_college) == True and db_ops.check_major(user_input_major )== True:
    #         user_input_college_id = db_ops.search_school_id(user_input_college)[0][0]
    #         user_input_major_id = db_ops.search_major(user_input_major)[0][0]
    #         user_input_decision = (user_input_id, user_input_college_id, user_input_major_id, user_input_status, user_input_comment)
    #         db_ops.post_decision(user_input_decision)
    #         # decision_form.success(user_input_decision)
    if post_decision and len(user_input_college)==0:
        st.error("missing info on college.", icon="🚨")
    if post_decision and len(user_input_major)==0:
        st.error("missing info on major.", icon="🚨")
    if post_decision and len(str(user_input_year))==0:
        st.error("missing info on year.", icon="🚨")
    if post_decision and len(user_input_status)==0:
        st.error("missing info on status.", icon="🚨")

def update_info_form(user_id):
    user_input_id = (user_id,)
    user_info = db_ops.get_user_info(user_input_id)
    user_info_state_current = db_ops.search_state(user_info[3])[0][0]
    update_form = st.form("Update info")
    if user_info[4] == None:
        user_info_gender_current = ""
    else:
        user_info_gender_current = user_info[4]
    if user_info[5] == 0:
        user_info_international_current = 'No'
    else:
        user_info_international_current = 'Yes'
    if user_info[7] == None:
        user_info_test_current = ""
    else:
        user_info_test_current = user_info[7]
    if len(db_ops.search_school((user_info[9],)))==0 :
        user_info_highschool_current = ""
    else:
        user_info_highschool_current = db_ops.search_school((user_info[9],))[0][0]
    update_form.write("#### fill out/update info")
    user_input_first_name = update_form.text_input("First name", user_info[1])
    user_input_last_name = update_form.text_input("Last name", user_info[2])
    user_input_state = update_form.selectbox("State", [user_info_state_current]+ states_options)
    user_input_gender = update_form.selectbox("Gender", [user_info_gender_current]+ gender_options)
    user_input_international = update_form.selectbox("Are you an international student?", [user_info_international_current]+ international_options)
    user_input_gpa = update_form.text_input("GPA", user_info[6])
    user_input_test = update_form.selectbox("Test type", [user_info_test_current]+ test_options)
    user_input_test_score = update_form.text_input("Test score", user_info[8])
    user_input_high_school = update_form.selectbox("High school", [user_info_highschool_current]+ db_ops.get_all_highschools())
    submit_form = update_form.form_submit_button("Fill out/Update my info")
    st.warning("please follow the community guidelines.", icon="⚠️")
    st.warning("if the high school is not recorded in the system. use '❗➕ add school/major/activity' on the side menu to add.", icon="⚠️")

    if submit_form and len(user_input_first_name) == 0:
        st.error("first name can't be empty.", icon="⚠️")
    if submit_form and len(user_input_last_name) == 0:
        st.error("last name can't be empty.", icon="⚠️")
    if submit_form and len(user_input_state) == 0:
        st.error("state can't be empty.", icon="⚠️")
    if submit_form and len(user_input_first_name)!=0 and len(user_input_last_name)!=0 and len(user_input_state)!=0:
        if len(user_input_first_name)>0:
            user_info_update = (user_input_first_name, user_id)
            db_ops.update_first_name(user_info_update)
        if len(user_input_last_name)>0:
            user_info_update = (user_input_last_name, user_id)
            db_ops.update_last_name(user_info_update)
        if len(user_input_state)>0:
            user_info_update = (db_ops.search_state_id(user_input_state)[0][0], user_id)
            db_ops.update_state(user_info_update)
        if len(user_input_gender)>0:
            user_info_update = (user_input_gender, user_id)
            db_ops.update_gender(user_info_update)
        if len(user_input_international)>0:
            if user_input_international == 'Yes':
                user_input_international = True
            else:
                user_input_international = False
            user_info_update = (user_input_international, user_id)
            db_ops.update_international(user_info_update)
        if user_input_gpa != None:
            user_info_update = (user_input_gpa, user_id)
            db_ops.update_gpa(user_info_update)
        if len(user_input_test)>0:
            user_info_update = (user_input_test, user_id)
            db_ops.update_test(user_info_update)
        if user_input_test_score != None:
            user_info_update = (user_input_test_score, user_id)
            db_ops.update_test_score(user_info_update)
        if len(user_input_high_school)>0:
            user_input_high_school = (user_input_high_school,)
            user_info_update = (db_ops.search_school_id(user_input_high_school)[0][0], user_id)
            db_ops.update_highschool(user_info_update)
        st.success("account updated.", icon="👍")

def register_new_user():
    st.markdown("---")
    # st.markdown(
    #     """
    #     <div style="background-image: linear-gradient(to left, violet, indigo, blue, green, yellow, orange, red); height: 1px;"></div>
    #     """,unsafe_allow_html=True)
    st.write("### not a user?? create an account below.")
    register_form = st.form("Create account")
    user_input_first_name = register_form.text_input("First name", "")
    user_input_last_name = register_form.text_input("Last name", "")
    user_input_state = register_form.selectbox('''State''', [""]+ states_options)
    user_input_gender = register_form.selectbox("Gender", [""]+ gender_options)
    user_input_international = register_form.selectbox("Are you an international student?", [""]+ international_options)
    submit_form = register_form.form_submit_button("Register")
    # fill_gender = False
    if submit_form and len(user_input_first_name)>0 and len(user_input_last_name)>0 and len(user_input_state)>0 and len(user_input_gender)>0 and len(user_input_international)>0:
        # process user input
        user_input_first_name = user_input_first_name[0].upper() + user_input_first_name[1:].lower()
        user_input_last_name = user_input_last_name[0].upper() + user_input_last_name[1:].lower()
        user_input_state_id = db_ops.search_state_id(user_input_state)[0][0]
        # if user_input_gender == "Prefer not to say":
        #     user_input_gender = None
        #     fill_gender = True
        if user_input_international == "No":
            user_input_international_bool = False
        elif user_input_international == "Yes":
            user_input_international_bool = True
        user_input = (user_input_first_name, user_input_last_name, user_input_state_id, user_input_gender, user_input_international_bool)
        user_id = db_ops.create_user(user_input)
        success_message = '''account created successfully! your username is {} 
        and your login password is your last name with the first letter in uppercase! 
        please remember for later on. you can log in above now.'''.format(user_id)
        st.success(success_message, icon="👍")
    if submit_form and len(user_input_first_name)==0:
        st.error("missing info on first name.", icon="🚨")
    if submit_form and len(user_input_last_name)==0:
        st.error("missing info on last name.", icon="🚨")
    if submit_form and len(user_input_state)==0:
        st.error("missing info on state.", icon="🚨")
    if submit_form and len(user_input_gender)==0:
        st.error("missing info on gender.", icon="🚨")
    if submit_form and len(user_input_international)==0:
        st.error("missing info on whether you are an international student.", icon="🚨")

def view_decision_records(user_id):
    user_id = (user_id,)
    if (type(db_ops.get_user_decisions(user_id)))==bool:
        st.warning("you don't have any decision in the record. you can add below.",icon="⚠️")
    else:
        st.dataframe(db_ops.get_user_decisions(user_id))

def view_decision_records2(user_id):
    user_id = (user_id,)
    if (type(db_ops.get_user_decisions2(user_id)))==bool:
        st.warning("you don't have any decision in the record. you can add below.",icon="⚠️")
    else:
        st.dataframe(db_ops.get_user_decisions2(user_id))

def delete_decision_record_form(user_id):
    user_input_id = int(user_id)
    user_id = (user_id,)
    delete_decision_form = st.form("Delete decision")
    delete_decision_form.write("#### delete a decision record")
    user_input_decision = delete_decision_form.selectbox("Decision to delete",[""] +db_ops.get_user_all_decisions(user_id))
    delete_decision_button = delete_decision_form.form_submit_button("Delete from my decision record")
    if delete_decision_button and user_input_decision!="":
        user_input_decision_school_id = db_ops.search_school_id((user_input_decision,))[0][0]
        user_input_decision_record = (user_input_id, user_input_decision_school_id)
        db_ops.delete_decision_record(user_input_decision_record)
        st.success("decision record deleted! please hit 'Refresh page' for new update.", icon="👍")

# def modify_decision_record_form(user_id):
#     user_input_id = int(user_id)
#     user_id = (user_id,)
#     modify_decision_form = st.form("Modify decision")
#     modify_decision_form.write("#### modify a decision record")
#     user_input_decision = modify_decision_form.selectbox("Decision to modify",[""] +db_ops.get_user_all_decisions(user_id))
#     if len(user_input_decision)!=0:
#         user_input_search_major = (user_id, user_input_decision)
#         st.succes("Here")
#         user_input_major = modify_decision_form.selectbox("Major",[db_ops.get_user_decision_major(user_input_search_major)] +db_ops.get_all_majors())
#     else: 
#         user_input_major = modify_decision_form.selectbox("Major",[""] +db_ops.get_all_majors())
#     user_input_year = modify_decision_form.selectbox("Year",[""] +db_ops.get_all_years())
#     user_input_status = modify_decision_form.selectbox("Status",[""] +status_options)
#     modify_decision_button = modify_decision_form.form_submit_button("Modify my existing decision record")

def view_activity_records(user_id):
    user_id = (user_id,)
    if type(db_ops.get_user_activities(user_id))==bool:
        st.warning("you don't have any activity in the record. you can add below.",icon="⚠️")
    else:
        st.dataframe(db_ops.get_user_activities(user_id)) 

def add_activity_record_form(user_id):
    user_input_id = int(user_id)
    add_activity_form = st.form("Add activity")
    add_activity_form.write("#### add an activity record")
    user_input_activity = add_activity_form.selectbox("Activity to add",[""] +db_ops.get_all_activities())
    # user_input_comment = add_activity_form.text_input("Comment(optional)","")
    add_activity_button = add_activity_form.form_submit_button("Add to my activity record")
    st.warning("if the activity is not recorded in the system. use '❗➕ add school/major/activity' on the side menu to add.", icon="⚠️")
    if add_activity_button and user_input_activity!="":
        user_input_activity_id = db_ops.search_activity_id((user_input_activity,))[0][0]
        # if len(user_input_comment) == 0:
        #     user_input_comment = None
        # user_input_activity_record = (user_input_id, user_input_activity_id, user_input_comment)
        user_input_activity_record = (user_input_id, user_input_activity_id)
        db_ops.add_activity_record(user_input_activity_record)
        st.success("activity record added! please hit 'Refresh page' for new update.", icon="👍")

def delete_activity_record_form(user_id):
    user_input_id = int(user_id)
    user_id = (user_id,)
    delete_activity_form = st.form("Delete activity")
    delete_activity_form.write("#### delete an activity record")
    user_input_activity = delete_activity_form.selectbox("Activity to delete", [""] +db_ops.get_user_all_activities(user_id))
    delete_activity_button = delete_activity_form.form_submit_button("Delete from my activity record")
    if delete_activity_button and user_input_activity!="":
        user_input_activity_id = db_ops.search_activity_id((user_input_activity,))[0][0]
        user_input_activity_record = (user_input_id, user_input_activity_id)
        db_ops.delete_activity_record(user_input_activity_record)
        st.success("activity record deleted! please hit 'Refresh page' for new update.", icon="👍")
        # st.rerun()

report_options = ["All decision records", "My decision records", "My activity records"]

def export_reports(user_id):
    user_input_export = st.selectbox("Report to export", [""] +report_options)
    user_id = (user_id,)
    if user_input_export == "All decision records":
        all_decision_csv = (db_ops.view_all_decisions1_table()).to_csv()
        st.download_button(
            label="Download all decision records",
            data=all_decision_csv,
            file_name='all_decision_records.csv',
            mime='text/csv',
        )
    if user_input_export == "My decision records":
        if (type(db_ops.get_user_decisions2(user_id)))==bool:
            st.warning("you don't have any decision to export.",icon="⚠️")
        else:
            my_decision_csv = (db_ops.get_user_decisions2(user_id)).to_csv()
            st.download_button(
                label="Download my decision records",
                data=my_decision_csv,
                file_name='my_decision_records.csv',
                mime='text/csv',
            )
    if user_input_export == "My activity records":
        if type(db_ops.get_user_activities(user_id))==bool:
            st.warning("you don't have any activity to export.",icon="⚠️")
        else:
            my_activity_csv = (db_ops.get_user_activities(user_id)).to_csv()
            st.download_button(
                label="Download my activity records",
                data=my_activity_csv,
                file_name='my_activity_records.csv',
                mime='text/csv',
            )

def refresh_page():
    st.rerun()

# global variable
db_ops = db_operations()

def main():
    start_page()

if __name__ == "__main__":
    main()