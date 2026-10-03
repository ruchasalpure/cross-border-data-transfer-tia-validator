from crewai import Agent

cross_border_data_transfer_tia_validator = Agent(
    role="Cross Border Data Transfer Tia Validator",
    goal="Deliver high-precision autonomous Cross Border Data Transfer Tia Validator operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
