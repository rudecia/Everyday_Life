from docx import Document

def cover_letter(industry: str, company: str, role: str, special_quality = ''):
    p0 = 'To Whom it May Concern,'

    p4 = 'Sincerely, \nRudecia'

    if str.lower(role[:1]) in ['a', 'e', 'i', 'o', 'u']:
        role = 'an ' + role
    else:
        role = 'a ' + role

    p1 = f'My name is Rudecia Bernard, and I am a graduate student at the University of Notre Dame studying applied computational mathematics and statistics. Before that, I studied applied mathematics and biology at Brown University. I would truly appreciate the opportunity to work as {role} at {company}.'


    if industry == 'bio':
        p2 = f"I have spent the last three years honing my skills in statistical analysis and machine learning. I was first introduced to this in a clinical research internship at Brigham and Women’s Hospital. While there, I used R to analyze and visualize data sets regarding outcomes for patients with CPPD, a type of arthritis. After that, I started researching with Dr. Neil Sarkar to learn more about the link between lifestyle and the development of cardiovascular disease. While in that role, I organized large databases of NIH patient data using SQL queries, and used the stats and sklearn packages in Python to create predictive models. Both of these experiences affirmed my desire to use my analytical skills to contribute to impactful clinical research."

        p3 = f"I would deeply value the opportunity to work at {company}. Not only would I get to dive into all the AI/ML techniques that fascinate me, but I would also contribute to scientifically rigorous and significant clinical trials. {special_quality} Thank you for reading my application; I appreciate any consideration I may receive. I hope to hear back soon!"

        lines = [p0, p1, p2, p3, p4]


      

    elif industry == 'finance':
        p2 = f" I have spent the last three years honing my skills in statistical analysis and machine learning. I was first introduced to this in a clinical research setting, where I used R to analyze and visualize clinical data sets, but that interest quickly bloomed into a broader pursuit of artificial intelligence and machine learning. I started researching with Dr. Neil Sarkar to learn more about the link between lifestyle and the development of cardiovascular disease. While in that role, I organized large databases of NIH patient data using SQL queries, and used the stats and sklearn packages in Python to create predictive models. Spending the year immersing myself in machine learning confirmed my interest in the subject area; more generally, it revealed my desire to pursue a career in which my mathematical and analytical skills would be pushed to their limits. Being {str.lower(role)} with you would definitely meet that criteria."


        p3 = f"Beyond my technical qualifications, I am someone who seeks to improve and challenge myself whenever possible, so the possibility of working on high-impact projects with {company} really caught my eye. {special_quality} Thank you for reading my application; I appreciate any consideration I may receive from your team."

        lines = [p0, p1, p2, p3, p4]

    file_name = '/Users/rudeciabernard/Desktop/CoverLetters/' + company + '_Cover_Letter.docx'

    doc = Document()

    for line in lines:
        doc.add_paragraph(line)

    doc.save(file_name)


    

 

