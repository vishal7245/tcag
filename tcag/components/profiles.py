import reflex as rx

def yogesh_agrawal_profile():
    return rx.vstack(
                    rx.heading("Mr. Yogesh Agrawal"),
                    
                    rx.box(
                        rx.heading("Current Position", size="4"),
                        rx.text("Chairman and Managing Director of Genomic Valley Biotech Limited since its inception on 16th May 1994.")
                    ),
                    
                    rx.box(
                        rx.heading("Education", size="4"),
                        rx.unordered_list(
                            rx.list_item("B.Com. (Hons) Graduate (1984) from Delhi University."),
                            rx.list_item("Chartered Accountancy (ICAI) and Cost Accountancy (ICWA) degrees in 1987.")
                        )
                    ),
                    
                    rx.box(
                        rx.heading("Career Milestones", size="4"),
                        rx.ordered_list(
                            rx.list_item(
                                rx.text("Early Career:"),
                                rx.unordered_list(
                                    rx.list_item("Started as an Associated Chartered Accountant at S.S. Kothari and Co., Delhi, an Audit and Consultancy Firm."),
                                    rx.list_item("Trained under Shri N.S. Khanna, Chairman and Managing Director of Hilton Rubbers Limited, as a Management Trainee."),
                                    rx.list_item("Further training by Shri Dharam Veera Ji, the then oldest living ICS, former cabinet secretary of PM Shri Jawaharlal Nehru, Governor of West Bengal, and Chairman of Police Aayog.")
                                )
                            ),
                            rx.list_item(
                                rx.text("Merchant Banking (1989-1993):"),
                                rx.unordered_list(
                                    rx.list_item("Involved in Merchant Banking activities."),
                                    rx.list_item(
                                        "Handled IPOs of various companies such as:",
                                        rx.unordered_list(
                                            rx.list_item("Rishabh Food Products Limited"),
                                            rx.list_item("Kanha Vanspati Limited"),
                                            rx.list_item("Rishabh Agro Products Limited"),
                                            rx.list_item("Ok Play Limited"),
                                            rx.list_item("Bharat Rasayan Limited")
                                        )
                                    )
                                )
                            ),
                            rx.list_item(
                                rx.text("Agro Biotechnology:"),
                                rx.unordered_list(
                                    rx.list_item("Explored new avenues in Agro Biotechnology."),
                                    rx.list_item("Travelled to Europe, USA, Canada, and Israel in search of new technology suitable for Indian conditions."),
                                    rx.list_item("Tied up with Bickel Biotechnology Limited, Israel for technology transfer."),
                                    rx.list_item("Promoted and incorporated Tushar Agri Business Consortium India Limited in May 1994 with co-promoters Shri S.I. Shervani, Geep Industrial Syndicate Limited, and Haryana Government through HSIIDC and HAIC."),
                                    rx.list_item("In 1996-97, became the sole promoter by buying back shares from Mr. Shervani, Geep, HSIIDC, and HAIC."),
                                    rx.list_item("Rebranded the company as Genomic Valley Biotech Limited in 2001, advised by the then Prime Minister Shri Atal Behari Vajpayee.")
                                )
                            )
                        )
                    ),
                    
                    rx.box(
                        rx.heading("Contributions and Associations", size="4"),
                        rx.unordered_list(
                            rx.list_item("Played a significant role in the construction of the Ram Mandir and Ramayan Centre in Mauritius."),
                            rx.list_item("Closely associated with Late Dr. L. M. Singhvi, the longest-serving Indian High Commissioner of the UK and an authority on the Indian Constitution."),
                            rx.list_item("Closely associated with Late Dr. R. C. Lahoti, former Chief Justice of India."),
                            rx.list_item("Supporter and promoter of cultural arts and artists."),
                            rx.list_item("Established the 'Ramayan Ratna Award' and 'Spiritual Voice of the Year Award' under his trust 'Father Camille Bulcke Sri Ram Research Trust'.")
                        )
                    ),
                    
                    rx.box(
                        rx.heading("Current Focus", size="4"),
                        rx.unordered_list(
                            rx.list_item("Striving for a dynamic reorientation of genomics in healthcare."),
                            rx.list_item("Inspired by the vision of transforming India into a global epicenter for genomic research and diagnostics.")
                        )
                    )
                )


def romasha_gupta_profile():
    return rx.vstack(
            rx.heading("Ms. Romasha Gupta"),
            
            rx.box(
                rx.heading("Current Position", size="4"),
                rx.text("Project Manager at Genomic Valley Biotech Limited")
            ),
            
            rx.box(
                rx.heading("Education", size="4"),
                rx.text("Postgraduate scientific researcher in bioinformatics")
            ),
            
            rx.box(
                rx.heading("Professional Experience", size="4"),
                rx.text("Over 3.5 years of experience in deep learning and NGS analysis")
            ),
            
            rx.box(
                rx.heading("Career Highlights", size="4"),
                rx.ordered_list(
                    rx.list_item(
                        rx.text("CSIR-IGIB:"),
                        rx.unordered_list(
                            rx.list_item(
                                rx.text("Project: 'Human Physiological/Biomedical Signal Acquisition and ML/AI based analysis for Cognitive Differentiation'"),
                                rx.text("Responsibilities:"),
                                rx.unordered_list(
                                    rx.list_item("Database generation and segregation"),
                                    rx.list_item("Model training for Interstitial Lung Diseases (ILDs)")
                                ),
                                rx.text("Role: Project Assistant-II")
                            ),
                            rx.list_item(
                                rx.text("Project: 'Genomics for Public Health in India'"),
                                rx.text("Tasks:"),
                                rx.unordered_list(
                                    rx.list_item("Data annotation"),
                                    rx.list_item("Genome assembly and annotation")
                                )
                            )
                        )
                    ),
                    rx.list_item(
                        rx.text("T-CAG LifeSciences Pvt. Ltd., New Delhi:"),
                        rx.unordered_list(
                            rx.list_item("Position: Bioinformatics Analyst"),
                            rx.list_item(
                                "Responsibilities:",
                                rx.unordered_list(
                                    rx.list_item("Data analysis and handling client data"),
                                    rx.list_item("NGS analysis, transcriptomic analysis, and metagenomic analysis")
                                )
                            ),
                            rx.list_item("Skills: Proficiency in R, Python, and Linux")
                        )
                    )
                )
            ),
            
            rx.box(
                rx.heading("Scientific Contributions", size="4"),
                rx.text("Co-authored several papers and book chapters in esteemed journals and books:"),
                rx.box(
                    rx.heading("Papers:", size="4"),
                    rx.unordered_list(
                        rx.list_item("Construction of Discrete Model of Human Pluripotency in Predicting Lineage-Specific Outcomes and Targeted Knockdowns of Essential Genes"),
                        rx.list_item("Systems Biology Paradigm for Exploring the Relation between Obesity and Ovarian Cancer with a Focus on Their Genome-Scale Metabolic Models"),
                        rx.list_item("Deciphering the Role of Phosphoglycerate Kinase 1 in Polycystic Ovarian Syndrome using Differential Gene Expression Analysis Approach"),
                        rx.list_item("Realizing the New Reality: Machine Learning Curbing Antimicrobial Resistance in Cutibacterium acnes"),
                        rx.list_item("Precision at its Core: Machine Learning-Infused Metabolomics Model for Preterm Birth Prediction in Human"),
                        rx.list_item("16S rRNA Female Reproductive Microbiome Investigation Reveals Dalfopristin, Clorgyline, and Hydrazine as Potential Therapeutics for the Treatment of Bacterial Vaginosis")
                    )
                ),
                rx.box(
                    rx.heading("Book Chapters:", size="4"),
                    rx.unordered_list(
                        rx.list_item("Introduction to Biomolecular Structure and Biophysics: Basics of Biophysics"),
                        rx.list_item("Plant Metabolomics: A New Era in the Advancement of Agricultural Research"),
                        rx.list_item("Protein Engineering Methods for the Design of Protein Therapeutics"),
                        rx.list_item("Machine Learning for Drug Designing"),
                        rx.list_item("Systems Biology in Understanding the Human Gut Microbiome and Related Diseases Highlighting Metabolic Modeling and Analysis")
                    )
                )
            )
        )
    


def roopak_kumar_profile():
    return rx.vstack(
        rx.heading("Dr. Roopak Kumar"),
        
        rx.box(
            rx.heading("Current Position", size="4"),
            rx.text("Associate Professor at Veena Vadini Ayurved College, Bhopal, Madhya Pradesh (M.P.)")
        ),
        
        rx.box(
            rx.heading("Qualifications", size="4"),
            rx.unordered_list(
                rx.list_item("B.A.M.S (Bachelor of Ayurvedic Medicine and Surgery)"),
                rx.list_item("M.D. (Panchakarma)"),
                rx.list_item("P.G.D.Y.T. (Post Graduate Diploma in Yoga Therapy)"),
                rx.list_item("C.Ch. (Certificate in Child Health)")
            )
        ),
        
        rx.box(
            rx.heading("Experience", size="4"),
            rx.text("Over 17 years of experience in Academics and Research")
        )
    )
    
def shikha_profile():
    return rx.vstack(
        rx.heading("Dr. Shikha"),
        
        rx.box(
            rx.heading("Position", size="4"),
            rx.text("Senior Analyst at T-CAG LifeSciences")
        ),
        
        rx.box(
            rx.heading("Expertise", size="4"),
            rx.text("Extensive experience in Genomics and DNA Sequencing Technologies")
        ),
        
        rx.box(
            rx.heading("Contributions", size="4"),
            rx.text("Successfully contributed to over 50 projects within the company")
        ),
        
        rx.box(
            rx.heading("Role", size="4"),
            rx.text("Plays a vital role in advancing innovative solutions in the field")
        )
    )
