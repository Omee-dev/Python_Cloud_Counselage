import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from inspect import getsource
# Load the dataset
path = "./Input/Data analyst Data.xlsx"
@st.cache_resource
def load_data():
    # Load your dataset here
    df = pd.read_excel(path)
    return df


st.set_page_config(page_title="CLoud Counselage Intern - Python", page_icon=":snake:", layout="wide", initial_sidebar_state="expanded")
def query_1(df):
    unique_students = df['First Name'].nunique()
    return unique_students

def query_2(df):
    avg_gpa = df['CGPA'].mean()
    return avg_gpa
def query_3(df):
    return df["Year of Graduation"].value_counts()
def query_4(df):
    return df["Experience with python (Months)"].value_counts()
def query_5(df):
    return st.write(f"   Mean    Median    Mode \n",df["Family Income"].unique()[round(sum(df["Family Income"].replace(df["Family Income"].unique(),[0,1,2,3]))/df.shape[0])],sorted(df["Family Income"])[int(df.shape[0]/2)],df["Family Income"].value_counts().keys()[0])
def query_6(df):
    list_of_colleges = df["College Name"].value_counts()[:5]
    st.write(list_of_colleges)
    averages = []
    for i in range(5):
        temp = df["CGPA"].loc[df["College Name"]==list_of_colleges.keys()[i]]
        avg = sum(temp)/temp.shape[0]
        st.write("%s   :: Min:%0.2f Max:%0.2f Avg:%0.2f"%(list_of_colleges.keys()[i],min(temp),max(temp),avg))
        averages.append(avg)
    ax = sns.barplot(x=list_of_colleges.index, y=averages,)
    ax.set_xlabel("College Name")
    ax.set_ylabel("Average CGPA")
    ax.set_title("Average CGPA by Top 5 Colleges")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=-75, ha='left')
    return ax
def query_7(df):
    numeric_quantity = pd.to_numeric(df['Quantity'], errors='coerce')
    Q1 = numeric_quantity.quantile(0.25)
    Q3 = numeric_quantity.quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers = df[(numeric_quantity < lower_bound) | (numeric_quantity > upper_bound)]

    if outliers.empty:
        st.write("No outliers found in 'Quantity' attribute.")
    else:
        st.write("Outliers found in 'Quantity' attribute:")
        st.write(outliers)

    attendee_status_unique = df['Attendee Status'].unique()
    if len(attendee_status_unique) <= 10:
        st.write("Unique values in 'Attendee Status':", attendee_status_unique)

    else:
        st.write("The 'Attendee Status' attribute seems to have many unique values and is likely categorical.")

def query_8(df):
    for i in df["City"].unique():
        city = df["CGPA"].loc[df["City"]==i]
        st.write(f"{i:12} :",sum(city)/len(city))
    
def query_9(df):
    a = df["Family Income"].replace(df["Family Income"].unique(),[8,1,6,3]).corr(df["CGPA"])
    return f"There is a {'very' if abs(a)<0.1 else ''} {'little'if abs(a)<0.3 else ''} {'positive' if a>0 else 'negative'} relation which is of {a}"

def query_10(df):
    return sns.heatmap(df[["CGPA","Family Income","Experience with python (Months)","Expected salary (Lac)"]].replace(df["Family Income"].unique(),[0,1,2,3]).corr(),annot=True,color = "gray")

def query_11(df):
    cross_tab = pd.crosstab(df['Events'], df['College Name'])
    max_attendance_per_college = cross_tab.idxmax(axis=0)

    st.write("Event(s) attracting the most students from specific fields of study:")
    return (max_attendance_per_college)

def query_12(df):
    df["Leadership- skills"].unique()
    df["Leadership- skills"] = df["Leadership- skills"].replace("no ","no")
    student_leaders = df[df["Leadership- skills"]=="yes"]
    student_wo_leaders =df[df["Leadership- skills"]=="no"]
    avg_GPA_leaders = sum(student_leaders["CGPA"])/student_leaders.shape[0]
    avg_GPA_wo_leaders = sum(student_wo_leaders["CGPA"])/student_wo_leaders.shape[0]
    avg_Sal_leaders = sum(student_leaders["Expected salary (Lac)"])/student_leaders.shape[0]
    avg_Sal_wo_leaders = sum(student_wo_leaders["Expected salary (Lac)"])/student_wo_leaders.shape[0]
    #return f"Greater GPA of Leaders?{avg_GPA_leaders>avg_GPA_wo_leaders}",f"Average Difference:{abs(avg_GPA_leaders-avg_GPA_wo_leaders)}\nGreater Sal of Leaders?{avg_Sal_leaders>avg_Sal_wo_leaders} \nAverage Difference:{abs(avg_Sal_leaders-avg_Sal_wo_leaders)}"
    result_df = pd.DataFrame({
            'Metric': ['Greater GPA of Leaders', 'Average Difference (GPA)', 'Greater Salary of Leaders', 'Average Difference (Salary)'],
            'Result': [avg_GPA_leaders > avg_GPA_wo_leaders, abs(avg_GPA_leaders - avg_GPA_wo_leaders), avg_Sal_leaders > avg_Sal_wo_leaders, abs(avg_Sal_leaders - avg_Sal_wo_leaders)]
        })
    return result_df
def query_13(df):
    a = df["Leadership- skills"].replace(["yes","no"],[1,0]).corr(df["Expected salary (Lac)"])
    return f"There is a {'very' if abs(a)<0.1 else ''} {'little'if abs(a)<0.3 else ''} {'positive' if a>0 else 'negative'} relation which is of {a}"
def query_14(df):
    return df["Year of Graduation"].loc[df["Year of Graduation"]<=2024].value_counts()
def query_15(df):
    gf=df[df.columns[6]].replace("Others",np.nan).fillna(df[df.columns[7]])
    dgf = gf.dropna()
    value_counts = {}
    for entry in dgf.apply(lambda x:x.replace(" ","").split("|")):
        for item in entry:
            if item in value_counts:
                value_counts[item] += 1
            else:
                value_counts[item] = 1
    max_key = max(value_counts, key=lambda k: value_counts[k])
    return f"{max_key} : {value_counts[max_key]}"

def query_16(df):
    Data_Science = ['Data Visualization using Power BI','Artificial Intelligence', 'Hello ML and DL','IS DATA SCIENCE FOR YOU?','RPA: A Boon or A Bane',]
    index = []
    for event in Data_Science:
        index.append(df.loc[df[df.columns[3]] == event].index)
    t = df[df[df.columns[3]].isin(Data_Science)][df.columns[3]].value_counts()
    t['__Sum of Students__'] = sum(t)
    return t#,f"Sum of Students: {sum(t)}"

def query_17(df,high_CGPA = 8,high_exper = 6,high_salary = 20):
    avg = np.mean(df.loc[df[df.columns[11]].astype(int)>=high_CGPA].loc[df[df.columns[12]].astype(int)>=high_exper][df.columns[14]])
    return f"Average High Salary Expectations: {avg} \nSo is it True that students with higher CGPA and Experience in language tend to have higher expectations of salary?:{avg>=high_salary}"
def query_18(df):
    gf=df[df.columns[6]].replace("Others",np.nan).fillna(df[df.columns[7]])
    giddy = gf.dropna().apply(lambda x:x.replace(" ",""))
    gdf = df.loc[giddy[giddy.str.contains("College")].index][df.columns[5]]
    st.write(f"No. Students know from their Colleges are :{gdf.shape[0]}")
    return gdf.value_counts()[:5]
#def query_10(df):

queries = {
        "Query 1 - How many unique students are included in the dataset?":query_1,
        "Query 2 - What is average GPA of the students?":query_2,
        "Query 3 - What is the distribution of students across different graduation years?":query_3,
        "Query 4 -  What is the distribution of students experience with Python Programming?":query_4,
        "Query 5 - What is the average family income of the students?":query_5,
        "Query 6 - How does GPA vary among different colleges(Show top 5 results)?":query_6,
        "Query 7 - Are there any outliers in the 'attending status' & 'quantity(numbers of courses completed)' attribute?":query_7,
        "Query 8 - What is the average GPA for student from each city?":query_8,
        "Query 9 - Can we identity any relationship between family income and GPA?":query_9,
        "Query 10 - How does the expected salary vary based on factors like 'GPA', 'Family income', 'Experience with python (Months)'?":query_10,
        "Query 11 -Which event tend to attract more students from specific fields of study?":query_11,
        "Query 12 - Do students in leadership positions in their college years tend to have higher GPAs or better expected salary?":query_12,
        "Query 13 - Is there a correlationship positions during their college years tend to have higher GPAs or better expected salary?":query_13,
        "Query 14 - How many students are graduating by the end of 2024?":query_14,
        "Query 15 - Which promotion channel brings in more student participations for the event?":query_15,
        "Query 16 - Find the total number of students who attended the events related to Data Science? (From all Data Science related courses.)":query_16,
        "Query 17 - Those who have high CGPA & More experience in language those who had high expectations for salary? (Avg)":query_17,
        "Query 18 - How students know about the event from their colleges? Which of these top 5 colleges?]":query_18,
        # Add other queries here...
}

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

def footer():
    st.markdown('by[ *__Omee-Dev__*](https://github.com/Omee-dev) ', unsafe_allow_html=True)


# Call the footer function
def main():
    st.title("Student Data Analysis")
    st.subheader("Queries and their Outputs")

    # Load data
    data_load_state = st.text('Loading data...')
    df = load_data()
    if df is not None:
        data_load_state.text("Data loaded successfully!")
        high_CGPA,high_exper,high_salary=8.0,6,20
        # Execute queries
        query_list = list(queries.keys())
        query_selection = st.selectbox("Select a query:", query_list)
        selected_query_function = queries[query_selection]

        if selected_query_function==query_17:
            high_CGPA = st.slider("High CGPA Threshold", min_value=6.0, max_value=10.0, value=8.0, step=0.1)
            high_exper = st.slider("High Experience Threshold", min_value=0, max_value=8, value=6, step=1)
            high_salary = st.slider("High Salary Expectations Threshold", min_value=0, max_value=35, value=20, step=1)

        if st.button("Execute Query"):
        #    selected_query_function = queries[query_selection]
            if selected_query_function==query_17:
                result = selected_query_function(df, high_CGPA,high_exper,high_salary)  
            else:
                result = selected_query_function(df)

            # Display results
            st.subheader("Query Result:")
            if isinstance(result, plt.Axes):
                st.pyplot(result.figure)
            if isinstance(result, str):
                st.text(result)
            else:
                st.write(result)
        if st.button("Get Code"):
          #  selected_query_function = queries[query_selection]
            st.subheader("Code")
            st.code(getsource(selected_query_function),language="python")
        if st.checkbox("Reference Data"):
            st.subheader("Reference Data")
            st.write(df)

    else:
        st.error("Failed to load data. Please check the file path.")
    footer()

if __name__ == "__main__":
    main()