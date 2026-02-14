import json
import os
import sys
from datetime import datetime

class StateManager:
    def __init__(self, project_root=None):
        if project_root:
            self.project_root = project_root
        else:
            # Auto-detect project root
            # Assuming this script is in brand-strategist-lite/scripts/
            script_dir = os.path.dirname(os.path.abspath(__file__))
            self.project_root = os.path.dirname(os.path.dirname(script_dir))
        
        self.state_file = os.path.join(self.project_root, "project_state.json")
        self.state = self.load_state()

    def load_state(self):
        """Loads state from file or creates a new one if not exists."""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"Error loading state: {e}. creating new state.")
                return self.create_default_state()
        else:
            return self.create_default_state()

    def create_default_state(self):
        """Defines the default structure of the state file."""
        return {
            "last_updated": datetime.now().isoformat(),
            "status": "initialized",
            "inputs": {
                "competitor_urls": [],
                "interviews": [],
                "brand_info": None
            },
            "analysis_outputs": {
                "user_insights_report": None,
                "competitor_analysis_report": None,
                "final_strategy_report": None
            },
            "crawled_data": []
        }

    def save_state(self):
        """Saves current state to file."""
        self.state["last_updated"] = datetime.now().isoformat()
        try:
            with open(self.state_file, 'w', encoding='utf-8') as f:
                json.dump(self.state, f, ensure_ascii=False, indent=2)
            print(f"State saved to {self.state_file}")
        except Exception as e:
            print(f"Error saving state: {e}")

    def add_competitor_url(self, url):
        """Adds a new competitor URL to the list."""
        if url not in self.state["inputs"]["competitor_urls"]:
            self.state["inputs"]["competitor_urls"].append(url)
            self.save_state()
            print(f"Added competitor: {url}")
        else:
            print(f"Competitor already exists: {url}")

    def update_crawled_data(self, file_path):
        """Records a path to a crawled JSON file."""
        # Use relative path for portability
        try:
            rel_path = os.path.relpath(file_path, self.project_root)
        except ValueError:
            rel_path = file_path

        if rel_path not in self.state["crawled_data"]:
             self.state["crawled_data"].append(rel_path)
             self.save_state()

    def check_readiness(self, stage):
        """Checks if data requirements are met for a specific stage."""
        errors = []
        
        # Check Project Root Access (for file checks)
        interviews_dir = os.path.join(self.project_root, "stage_1_user_insights", "interviews")
        analysis_dir = os.path.join(self.project_root, "stage_2_market_analysis")
        strategy_dir = os.path.join(self.project_root, "stage_3_strategy_generation")

        if stage == "competitor_analysis":
            if not self.state["inputs"]["competitor_urls"]:
                errors.append("No competitor URLs configured. Run '/add-competitor' first.")
        
        elif stage == "user_analysis":
            # Check inputs list OR existing files in directory
            has_files = False
            if os.path.exists(interviews_dir) and os.listdir(interviews_dir):
                 # Simple check if directory has files
                 # Filter out gitkeep/ds_store if needed, but basic check is fine
                 if any(f for f in os.listdir(interviews_dir) if not f.startswith('.')):
                     has_files = True
            
            if not has_files and not self.state["inputs"]["interviews"]:
                 errors.append("No user interviews found. Run '/add-interview' first.")
        
        elif stage == "strategy_generation":
             # Needs previous reports
             if not os.path.exists(os.path.join(analysis_dir, "User_Insights_Report.md")):
                 errors.append("Missing 'User_Insights_Report.md'. Run '/brand-user' first.")
             if not os.path.exists(os.path.join(analysis_dir, "Competitor_Analysis.md")):
                 errors.append("Missing 'Competitor_Analysis.md'. Run '/brand-comp' first.")

        elif stage == "all":
            # Check everything for a full run
            e1 = self.check_readiness("user_analysis")
            if not e1: # If user analysis is ready, good. Or we can just run it.
                pass 
            else:
                errors.extend(e1) # If user analysis not ready, we can't run full flow
            
            e2 = self.check_readiness("competitor_analysis")
            if e2:
                errors.extend(e2)

        return errors

if __name__ == "__main__":
    # Simple CLI for testing
    manager = StateManager()
    if len(sys.argv) > 1:
        cmd = sys.argv[1]
        if cmd == "init":
            manager.save_state()
            print("Project state initialized.")
        elif cmd == "add_url" and len(sys.argv) > 2:
            manager.add_competitor_url(sys.argv[2])
        elif cmd == "check" and len(sys.argv) > 2:
            stage = sys.argv[2]
            errors = manager.check_readiness(stage)
            if errors:
                for e in errors:
                    print(f"ERROR: {e}")
                sys.exit(1)
            else:
                print(f"SUCCESS: Ready for {stage}")
                sys.exit(0)
    else:
        print("Current State:")
        print(json.dumps(manager.state, indent=2))
