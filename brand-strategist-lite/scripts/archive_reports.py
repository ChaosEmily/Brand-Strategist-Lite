import os
import shutil
from datetime import datetime

def archive_reports():
    # Define source paths
    sources = [
        "stage_2_market_analysis/User_Insights_Report.md",
        "stage_2_market_analysis/Competitor_Analysis.md",
        "stage_3_strategy_generation/Final_Brand_Strategy.md"
    ]
    
    # Check if there are anyway files to archive
    existing_files = [f for f in sources if os.path.exists(f)]
    if not existing_files:
        print("No report files found to archive.")
        return

    # Create archive directory with timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    archive_dir = os.path.join("archive", timestamp)
    
    if not os.path.exists(archive_dir):
        os.makedirs(archive_dir)
        print(f"Created archive directory: {archive_dir}")

    # Move files
    for file_path in existing_files:
        filename = os.path.basename(file_path)
        dest_path = os.path.join(archive_dir, filename)
        shutil.move(file_path, dest_path)
        print(f"Archived: {filename} -> {archive_dir}")

    print("\nArchiving complete.")

if __name__ == "__main__":
    archive_reports()
