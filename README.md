Adolescent Mental Health: The "Biological Tax" of Social Media
An End-to-End Data Science Investigation into the Physiological Drivers of Depression.

Project Objective

	This project investigates the link between social media usage and clinical depression in a dataset of 1,200 (653 valid) adolescents. 		Moving beyond the simple "screen time" narrative, this study identifies the physiological mechanism—specifically sleep displacement—		that converts high usage into mental health crises.

Key Insights & Discoveries

	The "Silent Strain" Paradox: 
	Discovered that clinical depression is not strongly correlated with perceived addiction. Most depressed 		teens (n=16) reported low 	addiction scores, indicating that physiological damage occurs before psychological awareness.
	
	The Biological Tax: 
	Identified a "Crisis Peak" among males who survive on 5 hours of sleep due to a 7-hour daily social media "Arousal Surplus."
	
	The Democratic Risk: 
	Proved that social interaction level is a neutral factor. High-social and isolated teens "break" at the same rate, confirming the 			risk is physiological (recovery-based), not sociological (loneliness-based).
	
	The Academic Shield: 
	Found zero correlation (0.01) between health and GPA. Teens are "sleepwalking" to maintain a 2.99 GPA baseline 		while their 					internal health deteriorates.

	Age as a "Neutral" Factor:
	proved through the density and scatter plots that Age (13–19) is not a shield.
	The "Digital Distress" pattern is universal. A 14-year-old in the "Danger Zone" is just as vulnerable as an 18-year-old. This makes 		the problem a behavioral one, not a developmental one.

Technical Workflow

	Data Integrity: 
	Cleaned and standardized 653 records using StandardScaler to ensure a fair "apples-to-apples" comparison between sleep, grades, and 		usage hours.

	Feature Synthesis (PCA): 
	Implemented Principal Component Analysis to collapse 7 behavioral variables into 2 distinct "Lifestyle Profiles." Identified that PC2 	(Physiological Recovery) is the primary driver of mental health outcomes.

	Balanced Modeling: 
	Addressed the 2.4% class imbalance using Case-Control Downsampling.

	Risk Quantification: 
	Built a Logistic Regression model that identified a 2.30 predictive weight for the "Recovery Gap," proving that sleep displacement 			increases depression risk.

Results & Validation

	Recall: 
	1.00 (Caught 100% of clinical depression cases).
	
	Accuracy: 
	88% across the total population.
	
	The "High-Risk" Cluster: 
	Identified an additional 12% of the population (n=79) who are currently "Healthy" but possess the exact same "Toxic Fingerprint" as 		the depressed group.

Conclusion
	The study concludes that social media leads to depression by "taxing" the body's recovery systems. To protect adolescent mental 				health, interventions must shift from monitoring "Screen Time" to restoring the Physiological Recovery Gap.
