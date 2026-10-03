# Duties and Responsibilities for Cross-Border Transfer TIA Validator Agent

## Dual-Control Architecture
Maker:
tia-report-generator

Checker:
edpb-measure-checker

## Operational Workflow
1. The Maker (tia-report-generator) analyzes incoming telemetry, context, and requirements.
2. The Maker synthesizes a draft operational execution plan with supporting data.
3. The Checker (edpb-measure-checker) independently verifies all assumptions and constraints.
4. If validation passes, the plan is signed, logged, and committed.
5. All actions are appended to the immutable governance audit trail.
