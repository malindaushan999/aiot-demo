import pandas as pd
import datetime
import random
import streamlit as st
import numpy as np  # Import numpy for synthetic data generation

# 1. Load or Generate Synthetic Patient Data (Corrected for Regeneration)
def create_patient_data(num_patients=100): #function to create patient data
    np.random.seed(42)  # for reproducibility
    times = [datetime.time(8, 0), datetime.time(12, 0), datetime.time(18, 0)]
    random_indices = np.random.randint(0, 3, num_patients)
    patient_data = pd.DataFrame({
        'patient_id': range(1, num_patients + 1),
        'age': np.random.randint(20, 85, num_patients),
        'medication': np.random.choice(['Aspirin', 'Vitamin D', 'Calcium', 'Lipitor', 'Metformin'], num_patients),
        'prescribed_dosage': np.random.randint(1, 4, num_patients),  # Doses per day
    })
    patient_data['usual_intake_time'] = [times[i] for i in random_indices]
    patient_data['adherence_rate'] = np.random.uniform(0.7, 1.0, num_patients)  # Simulate adherence (70-100%)
    return patient_data


try:
    patient_data = pd.read_csv("synthetic_patient_data.csv")
except FileNotFoundError:
    patient_data = create_patient_data() #create data if file not found
    patient_data.to_csv("synthetic_patient_data.csv", index=False)


# 2. Simulate Pill Dispenser Log based on Patient Data
def generate_simulated_log(patient_data):
    log_data = []
    now = datetime.datetime.now()
    for _, patient in patient_data.iterrows():
        for dose_num in range(patient['prescribed_dosage']):
            base_time = datetime.datetime.combine(now.date(), patient['usual_intake_time']) + datetime.timedelta(hours=random.randint(-1, 1), minutes=random.randint(-30, 30))
            if random.random() < patient['adherence_rate']:  # Simulate adherence
                log_data.append({
                    'patient_id': patient['patient_id'],
                    'medication': patient['medication'],
                    'time': base_time.isoformat()
                })
    df = pd.DataFrame(log_data)
    df.to_csv("pill_dispenser_log.csv", index=False)
    return df


# 3. Reminder Logic (using Patient Data) - Corrected for Streamlit display
def check_medication_reminder(log_file="pill_dispenser_log.csv", patient_data_file="synthetic_patient_data.csv"):
    log = pd.read_csv(log_file)
    patients = pd.read_csv(patient_data_file)
    now = datetime.datetime.now()
    reminders = []
    for _, patient in patients.iterrows():
        for dose_num in range(patient['prescribed_dosage']):
            usual_intake_time = datetime.time.fromisoformat(str(patient['usual_intake_time']))
            expected_time = datetime.datetime.combine(now.date(), usual_intake_time)
            med_taken = False
            for _, row in log.iterrows():
                time_taken = datetime.datetime.fromisoformat(row["time"].replace("Z", "+00:00"))
                if row["patient_id"] == patient["patient_id"] and row["medication"] == patient["medication"] and abs((time_taken - expected_time).total_seconds()) < 3600:
                    med_taken = True
                    break
            if not med_taken:
                reminders.append(f"Reminder: Patient {patient['patient_id']} missed their dose of {patient['medication']} at {patient['usual_intake_time']}.")
    return reminders  # Return the list of reminders

# Streamlit App
st.title("Smart Pill Dispenser Demo")

# Sidebar for controls
st.sidebar.header("Demo Controls")
generate_data = st.sidebar.button("Generate New Data")  # Button to regenerate
if generate_data:
    patient_data = create_patient_data()
    patient_data.to_csv("synthetic_patient_data.csv", index=False)
    log_df = generate_simulated_log(patient_data)
    st.write("New data generated!")
    st.rerun()  # Use st.rerun() instead of st.experimental_rerun()


# Display Patient Data
st.subheader("Patient Data")
st.dataframe(patient_data)

# Display Pill Dispenser Log
st.subheader("Pill Dispenser Log")
try:
    log_df = pd.read_csv("pill_dispenser_log.csv")
    st.dataframe(log_df)
except FileNotFoundError:
    st.write("No log file found. Please generate data.")

# Run Reminders (Corrected placement)
st.subheader("Medication Reminders")

if 'log_df' in locals():
    reminders = check_medication_reminder()  # Call the function and get the reminders
    if reminders:
        for reminder in reminders:
            st.warning(reminder)  # Display the reminders
    else:
        st.success("All medications taken on time.")
else:
    st.write("No log file found. Please generate data.")