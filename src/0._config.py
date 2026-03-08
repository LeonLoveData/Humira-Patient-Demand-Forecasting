import os
import warnings

warnings.filterwarnings("ignore", category=UserWarning)

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(CURRENT_DIR, "data")
OUTPUT_DIR = os.path.join(CURRENT_DIR, "outputs")

os.makedirs(OUTPUT_DIR, exist_ok=True)

MEDICARE_FILE = os.path.join(DATA_DIR, "Medicare_Part_D_Spending_by_Drug_2023.csv")
MEDICAID_FILE = os.path.join(DATA_DIR, "Medicaid_Spending_by_Drug_2023.csv")

TARGET_DRUG = "HUMIRA"
