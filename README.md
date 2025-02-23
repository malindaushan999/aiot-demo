# AIoT - Demo
Demo application for AIoT: The future of smart healthcare

## Overview
This application simulates a smart pill dispenser system using synthetic patient data. It demonstrates data generation, logging, and reminder functionalities using Streamlit for the user interface.

## Features
1. **Synthetic Patient Data Generation**: Generates synthetic patient data including age, medication, prescribed dosage, usual intake time, and adherence rate.
2. **Simulated Pill Dispenser Log**: Simulates pill dispenser logs based on patient data and adherence rates.
3. **Medication Reminders**: Checks the logs and provides reminders for missed doses.

## How to Use
1. **Generate New Data**: Use the "Generate New Data" button in the sidebar to create new synthetic patient data and simulated logs.
2. **View Patient Data**: The patient data is displayed in a table format.
3. **View Pill Dispenser Log**: The simulated pill dispenser log is displayed in a table format.
4. **Medication Reminders**: The application checks for missed doses and displays reminders.

## Files
- `main.py`: The main application script.
- `synthetic_patient_data.csv`: Stores the generated synthetic patient data.
- `pill_dispenser_log.csv`: Stores the simulated pill dispenser log.

## Running the Application
To run the application, use the following command:
```bash
streamlit run main.py
```

## Dependencies
- pandas
- numpy
- streamlit

Install the dependencies using:
```bash
pip install pandas numpy streamlit
```
