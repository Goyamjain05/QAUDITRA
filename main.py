from agents.ai_agents.coordinator import CoordinatorAgent

def main():
    print("🤖 Launching Q-AUDITRA with Agents...")
    coordinator = CoordinatorAgent()
    coordinator.run_audit()
    print("✅ Audit complete. Check: reports/audit_report.html")

if __name__ == "__main__":
    main()
