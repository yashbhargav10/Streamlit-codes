def main():
	st.title("Hello Streamlit Lovers")
	st.text("Hello World this is a text")
	st.header("This is a header")
	st.subheader("This is a subheader")
	st.title("This is a title")
	

	#Displaying colored text/bootstrap color
	

	st.success("Successful")
	st.warning("This is danger")
	st.info("This is information")
	st.error("This is an error")
	st.exception("This is an exception")


	#Super function
	st.write("## This is a markdown text")
	st.write("This is a text")
	st.write(1+2)

	st.write(dir(st))

	#help info
	st.help(range)

	pass
if __name__=='__main__':
	main()

#reading data
#Load EDA PKGS
import pandas as pd

#display data
df = pd.read_csv("iris.csv")

#Method - 1
#st.dataframe(df)

#Adding a colorstyle from pandas
st.dataframe(df.style.highlight_max(axis = 0))

#Method - 2 : Static table
#st.table(df)

#Method - 3 : using superfunction st.write
st.write(df.head())





#Working with Widgets
#Buttons/Radio/Checkbox/Select

#Working with buttons
name = "Yash"

if st.button("Submit"):
	st.write("Name: {}".format(name.upper()))

if st.button("Submit", key='new02'):
	st.write("Name: {}".format(name.lower()))


#Working with radio buttons
status = st.radio("What is your status", ("Active", "Inactive"))
if status == "Active":
	st.success("You are active")
elif status =="Inactive":
	st.warning("Inactive")

#Working with checkbox
if st.checkbox("Show/Hide"):
	st.text("Showing something")

#Working with beta expander
with st.beta_expander("Python"):
	st.text("Hello Python")
	
#Select/multiple select
my_lang = ["Python", "Julia", "Go", "Rust"]

choice = st.selectbox("Language", my_lang)
st.write("You Selected {}".format(choice))

#Multiple Selection
spoken_lang = ("English","French","Spanish","Twi")
my_spoken_lang = st.multiselect("Spoken lang", spoken_lang, default="English")


#Slider
#Numbers(Int/Float/Dates)
age = st.slider("Age", 1,100,)

#Any Datatype
#Select Slider
color = st.select_slider("Choose Color", options=["Yellow", "red", "blue", "black", "white"], value=("Yellow","red"))




#Text input
fname = st.text_input("Enter Firstname")

#Text input hide password
password = st.text_input("Enter password", type = 'password')
st.title(fname)


#Text area
message = st.text_area("Enter Message", height = 100)
st.write(message)

#number
number = st.number_input("Enter Number", 1.0, 25.0)

#Date input
myappointment = st.date_input("Appointment")

#Time input
mytime = st.time_input("My Time")
