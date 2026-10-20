# Motorcycle Parts - Revenue & Fee Leakage Audit

Business Forensics: Audited 5,000 wholesale transactions to find profit leakage.

### The Business Problem
Management suspects Warehouse B is overcharging payment processing, eating into net revenue.

### Audit Logic
- Cleaned warehouse names
- Calculated fee_pct = payment_fee / total * 100
- Calculated net_revenue = total - payment_fee
- Flagged leakage if fee_pct > 5%

### Findings
- Total Leakage: R987,500.00
- Warehouse B: 7.07% vs Warehouse A: 2.95% = 140% higher
- Recommendation: Renegotiate Warehouse B contract

### Stack
Python, pandas, Business Audit, AWS S3 Concept
Part of end-to-end case study: SQL -> Python Audit -> Dashboard
